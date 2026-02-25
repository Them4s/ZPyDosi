import os
# from ..Analysis.cnf import read_cnf_file

from ZPyDosi.Common.utils_general import lmap, get_aff_size, tex,  dup, dupx
from ZPyDosi.Common.CsvSeeker import CsvSeeker
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Prints.PrintnSave import aff_s_v, aff_list, aff
from ZPyDosi.Plots.SubPlots import my_sub6, aff_curve
import numpy as np
import matplotlib.pyplot as plt
#from map1loc import *


path_csv = get_param_vari("csv" , str, None)
case_csv = get_param_vari("case", str, None)
aff_old = get_param_vari("aff_old", bool, "True")

#aff_old = False

talk     = get_param_vari("talk",bool,"n")
path_recompute		= get_param_vari("recompute",str,None)	# todo, retrouver a quoi ca servait...

input_csv = CsvSeeker(path_csv)


gene_key = "generic"

path_generic_data	= input_csv.get(gene_key, "path_data", str)
path_src_measurement	= input_csv.get(case_csv, "path_data", str)
path_src_bkgrd		= input_csv.get(case_csv, "path_bkg",  str)
labo_ref		= input_csv.get(case_csv, "labo_ref", str)
#ab			= input_csv.get(case_csv, "a/b", str, None)


print(aff_s_v("path_src_measurement", path_src_measurement))
'''
if ab is not None:
	a,b = map(lambda s:float(s), ab.split("/"))
else:
	if input_csv.get(case_csv, "tab_calib", str, None) is not None:
		def calib(s):
			return input_csv.get_list(case_csv, "tab_calib",s, float)[0]
		x1, y1 = calib("ch1"), calib("nrj1")
		x2, y2 = calib("ch2"), calib("nrj2")
		a = (y2-y1)/(x2-x1)
		b = (y1-a*x1)
	else:
		a,b = 1,0'''
l_param_nrj_calib = input_csv.get(case_csv, "nrj_calib", all_line=True)[1:]
if l_param_nrj_calib[0] == "a*x+b":
	a,b = map(lambda s:float(s), l_param_nrj_calib[1:3])
	print("energy calibration", "a*x+b", a,b)
	def fct_nrj2pos(x):
		return a*x*+b
	def fct_pos2nrj(x):
		return (x-b)/a
elif l_param_nrj_calib[0] == "a*x**2+b*x+c":
	a,b,c = map(lambda s:float(s), l_param_nrj_calib[1:4])
	print("energy calibration", "a*x**2+b*x+c", a,b,c)
	def fct_nrj2pos(x):
		return a*x**2+b*x+c
	
	def fct_pos2nrj(x):
		def fct_pos2nrj_uni(x):
			sqrt_delta = (b**2-4*a*(c-x))**0.5
			rac1, rac2 = (-b+sqrt_delta)/(2*a), (-b-sqrt_delta)/(2*a)
			if rac1<0   and rac2>0: return rac2
			if rac2<0   and rac1>0: return rac1
			if rac2>1e4 and rac1<1e4: return rac1
			if rac1>1e4 and rac2<1e4: return rac2
			print('ERROR - fct_pos2nrj - can not choose between',rac1,'and',rac2)
		if type(x) in [list, np.ndarray]:
			return np.array([fct_pos2nrj_uni(val_x) for val_x in x])
		else:
			return fct_pos2nrj_uni(x)			
else:
	print("energy calibration format error, please use a*x+b or a*x**2+b*x+c")
	exit()


name_src  = "_".join(path_src_measurement.split("/")[-1].split("_")[8:])
mat_src = name_src.replace("_","-").replace(".TKA","").split("-")[0]
#name_hpge = path_src_measurement.split("/")[-1].split("_")[6]

print(aff_s_v("name_src", name_src))
print(aff_s_v("mat_src", mat_src))
#print(aff_s_v("name_hpge", name_hpge))

specific_mat = input_csv.get(case_csv, "looking_for", str, None)
if specific_mat is None:
	try:
		l_path_src_lvl = list(map(lambda s: path_generic_data+"/"+s+"_"+labo_ref,input_csv.get_list(gene_key, "tab_mat2iso",mat_src, str)))
	except:
		l_path_src_lvl = []
else:
	l_path_src_lvl = list(map(lambda s: path_generic_data+"/"+s+"_"+labo_ref,input_csv.get_list(gene_key, "tab_mat2iso",specific_mat, str)))





print(aff_list("data_src_path", l_path_src_lvl))


fig = plt.figure(2, figsize=(15.,12.))
fig.patch.set_facecolor('white')

ax1, ax0, ax2 = my_sub6(fig, 1, 1, 0, list_rx=[1], list_ry=[1,1,1], list_sy=[0.35,0.35], auto_x=True, auto_y=False)[0,:]
#ax1, ax0, ax2 = my_sub6(fig, 1, 1, 0, list_rx=[1], list_ry=[2,0.5,0.5], list_sy=[0.25,0.25], auto_x=True, auto_y=False)[0,:]


def get_spectrum(path):
	lines = open(path).readlines()
	t_eff, t_total = map(lambda v:float(v), lines[:2])
	dead_time_correction = t_total/t_eff
	print(aff_s_v("dead_time_correction", dead_time_correction))
	l_v = np.array(lmap(lambda l:float(l),lines[2:]))
	l_s = l_v**0.5
	return l_v*dead_time_correction, l_s*dead_time_correction, t_total


l_meas_v, l_meas_s, meas_t = get_spectrum(path_src_measurement)						# data measurment
if path_src_bkgrd is None or path_src_bkgrd=="":
	l_bkgd_v, l_bkgd_s, bkgd_t = l_meas_v*0, l_meas_s*0, 1.
else:
	l_bkgd_v, l_bkgd_s, bkgd_t = get_spectrum(path_src_bkgrd)					# background measurment
	l_bkgd_v, l_bkgd_s, bkgd_t = map(lambda data:data*meas_t/bkgd_t, [l_bkgd_v, l_bkgd_s, bkgd_t])	# set background to the same measurment time

ax0.set_ylim([min(l_meas_v-l_bkgd_v), max(l_meas_v)*1.3])
ax1.set_ylim([1e-4, max(l_meas_v)*1.3])
ax2.set_ylim([1, max(l_meas_v)*1.3])

ax1.set_yscale("log")
ax2.set_yscale("log")


#l_e = np.array(range(len(l_meas_v))) * a + b 								# energies in KeV
l_e = fct_pos2nrj(np.array(range(len(l_meas_v))))							# energies in KeV

#print(l_e)
#exit()
l_gamma_e_v,l_gamma_e_s,l_gamma_r_v,l_gamma_r_s, l_gamma_path = [],[],[],[],[]
for path_src_lvl in l_path_src_lvl:
	l_gamma_e_v_tmp,l_gamma_e_s_tmp,l_gamma_r_v_tmp,l_gamma_r_s_tmp, l_gamma_path_tmp = [],[],[],[],[]
	if "lnhb" in labo_ref:
		data = open(path_src_lvl).readlines()
		while "Energy (keV) ; Ener. unc. (keV) ; Intensity (%) ; Int. unc. (%) ; Type ; Origin ; Lvl. start ; Lvl. end" not in data[0]: data.pop(0)
		data.pop(0)
		while "=========" not in data[0]:
			ev,es,rv,rs = data.pop(0).replace(" ","").split(";")[:4]
			if talk: print("ev",ev,"es",es,"rv",rv,"rs",rs)
			l_gamma_e_v_tmp += [float(ev)]
			l_gamma_e_s_tmp += [0. if es=="" else float(es)]
			l_gamma_r_v_tmp += [float(rv)/100]
			l_gamma_r_s_tmp += [0. if rs=="" else float(rs)/100]
			l_gamma_path_tmp += [path_src_lvl]
	elif "nndc" in labo_ref:
		def prec_last_dig(v):
			if "E" not in v:
				return 1./(10**len(v.split(".")[1]))
			else:
				start, expo = v.split("E")
				if "." in start: val = float("1E"+expo) / 10**len(start.split(".")[1])
				else:            val = float("1E"+expo)
				return val
		for line in open(path_src_lvl).readlines():
			if line[0]!="#" and len(line.replace("%","").split())>0:
				#print(line)
				e, e_s, r, r_s = line.replace("%","").split()[:4]
				#if e_s == "?": print("Warning - no uncertainty on energy", e, e_s, r, r_s)
				if r_s == "?": print("Warning - no uncertainty on ratio ", e, e_s, r, r_s)
				e_s = float(e)*0.1 if e_s=="?" else float(e_s)*prec_last_dig(e)
				r_s = float(r)*0.1 if r_s=="?" else float(r_s)*prec_last_dig(r)
				l_gamma_e_v_tmp += [float(e)]
				l_gamma_e_s_tmp += [e_s]
				l_gamma_r_v_tmp += [float(r)/100]
				l_gamma_r_s_tmp += [r_s/100]
				l_gamma_path_tmp += [path_src_lvl]
				
	else:
		print("Error - data format not recognized")
		exit()
	
	l_gamma_e_v  += l_gamma_e_v_tmp 
	l_gamma_e_s  += l_gamma_e_s_tmp 
	l_gamma_r_v  += l_gamma_r_v_tmp 
	l_gamma_r_s  += l_gamma_r_s_tmp 
	l_gamma_path += l_gamma_path_tmp
	c = 0 if len(l_path_src_lvl)==1 else l_path_src_lvl.index(path_src_lvl)/(len(l_path_src_lvl)-1.)/1.5
	
	print(aff_list(path_src_lvl , l_gamma_e_v_tmp, l2=12))
	
	ax1.errorbar(np.array(l_gamma_e_v_tmp),np.array(l_gamma_r_v_tmp)*100, yerr=np.array(l_gamma_r_s_tmp)*100, fmt='o', c=(c,c,c), zorder=100, alpha=1)



l_gamma_e_v,l_gamma_e_s,l_gamma_r_v,l_gamma_r_s = map(lambda l:np.array(l), [l_gamma_e_v,l_gamma_e_s,l_gamma_r_v,l_gamma_r_s])


aff_curve(ax0, dupx(l_e), dup(l_meas_v), dup(l_meas_s),"blue" ,1,0.2, label=tex("Raw"))
aff_curve(ax0, dupx(l_e), dup(l_bkgd_v), dup(l_bkgd_s),"green",1,0.2, label=tex("Background"))
aff_curve(ax0, dupx(l_e), dup(l_meas_v-l_bkgd_v), dup((l_bkgd_s**2+l_meas_s**2)**0.5),"red",1,0.2, label=tex("Signal"))
#ax1.legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)

aff_curve(ax2, dupx(l_e), dup(l_meas_v), dup(l_meas_s),"blue" ,1,0.2, label=tex("Raw"))
aff_curve(ax2, dupx(l_e), dup(l_bkgd_v), dup(l_bkgd_s),"green",1,0.2, label=tex("Background"))
aff_curve(ax2, dupx(l_e), dup(l_meas_v-l_bkgd_v), dup((l_bkgd_s**2+l_meas_s**2)**0.5),"red",1,0.2, label=tex("Signal"))
ax2.legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)

aussi_bas = False
if aussi_bas:
	aff_curve(ax1, dupx(l_e), dup(l_meas_v), dup(l_meas_s),"blue" ,1,0.2, label=tex("Raw"))
	aff_curve(ax1, dupx(l_e), dup(l_bkgd_v), dup(l_bkgd_s),"green",1,0.2, label=tex("Background"))
	aff_curve(ax1, dupx(l_e), dup(l_meas_v-l_bkgd_v), dup((l_bkgd_s**2+l_meas_s**2)**0.5),"red",1,0.2, label=tex("Signal"))
	ax1.plot([-1], [1], "o", c=(0,0,0), label=tex(r"P_{\gamma} [\%]"))
	ax1.legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=2)
else:
	aff_curve(ax1, dupx(l_e), dup(l_meas_v-l_bkgd_v), dup((l_bkgd_s**2+l_meas_s**2)**0.5),"red",1,0.2)



ax1.set_xlim((0,l_e[-1]))
#print(l_e)
#exit()

for i in range(len(l_gamma_e_v)):
	ax1.plot([l_gamma_e_v[i],l_gamma_e_v[i]], ax1.get_ylim(), alpha=0.2,c='black')


l_plot_tmp, l_ie, l_lim_left, l_lim_right = [], [], [], []

s1 = 14
txt_out = ""
print()
txt_out = "".join(map(lambda s:aff(s,s1), "e_min1 e_min2 e_max1 e_max2 e_v e_s r_v r_s shape".split()))
print(txt_out)
txt_out += "\n"

def app(v):return "%.5e" % v


if path_recompute is None:
	path_save = path_generic_data+"/spectrum_plot_out_"+mat_src+"_"+labo_ref
	if os.path.isfile(path_save):
		path_recompute = path_save
		print("saved plot parameters found:",path_save)
	else:
		print("no saved parameters found at:",path_save)

if path_recompute is not None:
	for line in open(path_recompute).readlines()[1:]:
		if line[0]!="#":
			e_min1,e_min2,e_max1,e_max2 = map(lambda v:float(v), line.split()[:4])
			s_gamma_e_v, s_gamma_e_s, s_gamma_r_v, s_gamma_r_s = 0, 0, 0, 0
			for ie in range(len(l_gamma_e_v)):
				if e_min2<l_gamma_e_v[ie]<e_max1:
					s_gamma_e_v += l_gamma_e_v[ie]*l_gamma_r_v[ie]
					s_gamma_e_s += (l_gamma_e_s[ie]*l_gamma_r_v[ie])**2
					s_gamma_r_v += l_gamma_r_v[ie]
					s_gamma_r_s += l_gamma_r_s[ie]**2
					#print(l_gamma_r_v[ie])
					if aff_old:
						ax2.plot([l_gamma_e_v[ie],l_gamma_e_v[ie]],ax2.get_ylim(), "black", alpha=0.25)
					
			#l_plot_tmp.append(ax1.plot([e,e], ax1.get_ylim(), alpha=0.4,c='blue',dashes=[5,3])[0])
			
			ymin,ymax = ax2.get_ylim()
			if aff_old:
				ax2.fill_between([e_min1,e_min2], [ymin,ymin], [ymax,ymax], facecolor="blue", alpha=0.2,linewidth=0.0, zorder = 0)
				ax2.fill_between([e_max1,e_max2], [ymin,ymin], [ymax,ymax], facecolor="red",  alpha=0.2,linewidth=0.0, zorder = 0)
			
			if s_gamma_r_v == 0:
				print("Warning - no peak found in the reconstruction for",line.split()[4])
			else:
				gamma_e_v = s_gamma_e_v	/ s_gamma_r_v
				gamma_e_s = s_gamma_e_s**0.5
				gamma_r_v = s_gamma_r_v
				gamma_r_s = s_gamma_r_s**0.5
				gamma_r_v = s_gamma_r_v
				txt1 = "".join(map(lambda v:aff(app(v),s1), [e_min1,e_min2,e_max1,e_max2]))
				txt3 = "".join(map(lambda v: aff(app(v),s1), [gamma_e_v, gamma_e_s, gamma_r_v, gamma_r_s])) + aff(line.split()[-1])
				print(txt1+txt3)
				txt_out += txt1+txt3+"\n"
				
	#print txt_out
	open("spectrum_plot_out","w").write(txt_out)
	#exit()
	print()


def job(key, e, v):
	global l_plot_tmp, l_ie, l_lim_left, l_lim_right, txt_out
	#print key,e,v
	if key == "z" or key == "w":
		tmp = abs(l_gamma_e_v - e)
		tmp_min = tmp.min()
		ie = list(tmp).index(tmp_min)
		l_ie += [ie]
		l_plot_tmp.append(ax1.plot([l_gamma_e_v[ie],l_gamma_e_v[ie]], ax1.get_ylim(), c='red')[0])
		l_plot_tmp.append(ax1.errorbar(l_gamma_e_v[ie],l_gamma_r_v[ie]*100, yerr=l_gamma_r_s[ie]*100, fmt='o', c="red", zorder=100, alpha=1))
	elif key == "a" or key == "q":
		l_lim_left.append(e)
		l_plot_tmp.append(ax1.plot([e,e], ax1.get_ylim(), alpha=0.4,c='blue',dashes=[5,3])[0])
		l_plot_tmp.append(ax0.plot([e,e], ax1.get_ylim(), alpha=0.4,c='blue',dashes=[5,3])[0])
		l_plot_tmp.append(ax2.plot([e,e], ax1.get_ylim(), alpha=0.4,c='blue',dashes=[5,3])[0])
	elif key == "e":
		l_lim_right.append(e)
		l_plot_tmp.append(ax1.plot([e,e], ax1.get_ylim(), alpha=0.4,c='red',dashes=[5,3])[0])
		l_plot_tmp.append(ax0.plot([e,e], ax1.get_ylim(), alpha=0.4,c='red',dashes=[5,3])[0])
		l_plot_tmp.append(ax2.plot([e,e], ax1.get_ylim(), alpha=0.4,c='red',dashes=[5,3])[0])
	elif key == "r":
		l_ie, l_lim_left, l_lim_right = [], [], []
		while len(l_plot_tmp)>0: l_plot_tmp.pop(0).remove()
	elif key == "enter":
		if len(l_lim_left)<2 or len(l_lim_right)<2 or len(l_ie)<1:
			l_ie, l_lim_left, l_lim_right = [], [], []
			while len(l_plot_tmp)>0: l_plot_tmp.pop(0).remove()
		else:
			txt1 = "".join(map(lambda v:aff(app(v),s1), [min(l_lim_left),max(l_lim_left),min(l_lim_right),max(l_lim_right)]))
			
			s_gamma_e_v, s_gamma_e_s, s_gamma_r_v, s_gamma_r_s = 0, 0, 0, 0
			for ie in l_ie:
				s_gamma_e_v += l_gamma_e_v[ie]*l_gamma_r_v[ie]
				s_gamma_e_s += (l_gamma_e_s[ie]*l_gamma_r_v[ie])**2
				s_gamma_r_v += l_gamma_r_v[ie]
				s_gamma_r_s += l_gamma_r_s[ie]**2
			gamma_e_v = s_gamma_e_v	/ s_gamma_r_v
			gamma_e_s = s_gamma_e_s**0.5
			gamma_r_v = s_gamma_r_v
			gamma_r_s = s_gamma_r_s**0.5
			gamma_r_v = s_gamma_r_v
			#txt2 = "".join(map(lambda ie: "".join(map(lambda t:aff(app(t[ie]),s1), [l_gamma_e_v, l_gamma_e_s, l_gamma_r_v, l_gamma_r_s])), l_ie))
			txt3 = "".join(map(lambda v: aff(app(v),s1), [gamma_e_v, gamma_e_s, gamma_r_v, gamma_r_s]))+aff("step/step")
			print(txt1+txt3)
			txt_out += txt1+txt3+"\n"
			l_ie, l_lim_left, l_lim_right = [], [], []
			while len(l_plot_tmp)>0: l_plot_tmp.pop(0).remove()



def on_ylims_change(axes):
	ax0.set_ylim((-axes.get_ylim()[1]/20.,axes.get_ylim()[1]))

ax2.callbacks.connect('ylim_changed', on_ylims_change)
				
				
def onclick(event):
	ix, iy = event.xdata, event.ydata
	#print event.key
	#print 'x = %d, y = %d'%(ix, iy)
	job(event.key, ix, iy)
	
cid = fig.canvas.mpl_connect('button_press_event', onclick)



for ax in [ax0, ax1, ax2]:
	ax.set_xlabel(tex(r"Energy [keV]"), size=get_aff_size("s_xylabel"))
	ax.set_ylabel(tex(r"Counts"),       size=get_aff_size("s_xylabel"))

#ax0.set_ylim([min(l_meas_v-l_bkgd_v), max(l_meas_v)*1.3])
#ax1.set_ylim([1e-4, max(l_meas_v)*1.3])
#ax2.set_ylim([1, max(l_meas_v)*1.3])

#ax1.set_yscale("log")
#ax2.set_yscale("log")


plt.show()

open("spectrum_plot_out","w").write(txt_out)
print()
print("#"*50)
print("# Output saved in spectrum_plot_out. If you want it to be the new ref then write in a terminal:")
print("# mv spectrum_plot_out "+path_generic_data+"/spectrum_plot_out_"+mat_src+"_"+labo_ref)
print("#"*50)
print()



