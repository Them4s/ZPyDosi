
#python ../../../../python/irrad/expected_act.py calib=../../../../hpge/test_tp_fermi/calib_out_2019_02_25_p13_100h

from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Common.utils_general import lmap, get_aff_size, tex, str2time, time2str
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.Plots.SubPlots import my_sub6, my_sub6_finalise
from ZPyDosi.DosiFunctions.Dictionaries import d_spectro, d_matdosi_2_data, d_mt2name, d_mt2tex
from ZPyDosi.DosiFunctions.Functions import get_massic_fraction, get_iso2mass, weight_2_selfshielding_Au_15mm
from ZPyDosi.XSnFlux.Projections import projet_vec_intervals_from_continus
from ZPyDosi.XSnFlux.GetIRDFF import get_irdff_iaea 
from ZPyDosi.Prints.PrintnSave import aff 
from ..Radioprotection.DoseRateCalc import gen_dose_rate_fct
import numpy as np
import matplotlib.pyplot as plt

from data_spectre import *
import datetime, calendar
import datetime
import os

from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
now = datetime.datetime.now()


path_iaea_data = os.path.expandvars("Your path here") # to be modified in the future



print ("#"*50, "get bash args")

path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv      = get_param_vari("lcase", str).split("/")

path_save      = get_param_vari("path_save", str, "expected_act_out")
name_save      = get_param_vari("name_save", str, "auto_time")


no_save  = get_param_vari("no_save", bool, "False")

if True:
	print("WARNING - Fe values are copy-pasted for SS")
	
	for key, v in list(dico_spectrum.items()):
		if key[:3] == "Pfe":
			dico_spectrum["Pss"+key[3:]] = v
	
	for key, v in list(dico_petale_rr.items()):
		if key[:3] == "Pfe":
			dico_petale_rr["Pss"+key[3:]] = v
	

try:
	path_param = "optim/param.txt"
	def get_param_optim(param):
		lines = open(path_param).readlines()
		for line in lines:
			if len(line.split())>0 and line.split()[0] == param:
				return line.split()[1]
		return None
	dose_max_cavity_roof   = float(get_param_optim("dose_max_cavity_roof"))
	dose_max_cavity_door   = float(get_param_optim("dose_max_cavity_door"))
except:
	dose_max_cavity_roof = 0.100
	dose_max_cavity_door = 0.050
	print("WARNING - no optim rep found, max dose rate used of",dose_max_cavity_roof,"mSv/h for the lid and",dose_max_cavity_door,"mSv/h for the cavity")
	
if False:
	move_day = 5
	for line in open(path_csv_data).readlines():
		try :	
			if line.split(",")[0].startswith("exp"):
				print()
			avt = line.split(",")[8]
			y,m,d = avt.split("_")
			new_date = datetime.datetime(int(y),int(m),int(d),0,0,0)+datetime.timedelta(days=move_day)
			def conv(i):
				i=str(i)
				while len(i)<2: i = "0"+i
				return i
			print (avt+ "\t"+conv(new_date.year)+"_"+conv(new_date.month)+"_"+conv(new_date.day))
		except:
			a=1
	exit()
	
	




data_irrad = DataIrrad(	path_csv_data, 
			path_csv_dosi, 
			lcase_csv, 
			use_sqrt_for_meas_sig=True,
			load_hpge_eff=True,
			load_moni=False, 
			remove_data=False)

data_irrad.aff_description()



print ("#"*50)

#path_irdff_iaea = "../../../irdff/iaea_data"
#path_irdff_iaea = "other_data/irdff_iaea_data"

power_per_src_n = 1.32574000e-11

s_txt_meas = 5

y,m = 2019, 9
def t(month,d,h,m,s):
	return datetime.datetime(2019, month, d,h,m,s)
def dt(t1,t2):
	return (t2-t1).total_seconds()


t_begin_fst_week = min(data_irrad.l_irrad_time_start)
t_begin_fst_week = datetime.datetime(t_begin_fst_week.year, t_begin_fst_week.month, t_begin_fst_week.day,0,0,0)
while t_begin_fst_week.weekday()>0:
	t_begin_fst_week = t_begin_fst_week - datetime.timedelta(days=1)
t_end_last_week = max(data_irrad.l_hpge_time_out)
t_end_last_week = datetime.datetime(t_end_last_week.year, t_end_last_week.month, t_end_last_week.day,23,59,59)
while t_end_last_week.weekday()<6:
	t_end_last_week = t_end_last_week + datetime.timedelta(days=1)

if t_end_last_week<t_begin_fst_week+ datetime.timedelta(days=7):
	t_end_last_week = t_begin_fst_week+ datetime.timedelta(days=7)

#print(t_begin_fst_week, t_end_last_week)
#exit()

#t_end_last_week += datetime.timedelta(days=7*15)

nb_week = int((dt(t_begin_fst_week,t_end_last_week)+1.1)/3600/24/7)

print (t_begin_fst_week)
print (t_end_last_week)
print ("nb_week", nb_week)


nb_hpge=4
print ("nb_hpge", nb_hpge)



#print(nb_week)
#exit()

fig = plt.figure(figsize=(17,(1+nb_hpge)*1.3*nb_week))
fig.patch.set_facecolor('white')


tab_ax = my_sub6(fig,1,1,0,list_ry=[1]*nb_week,list_sy=[0.22]*nb_week, list_rx=[1], auto_y=False,auto_x=False, mb=0.01, mh=0.01, mg=0.1, md=0.05)
l_ax = list(reversed(tab_ax[0,:]))
#ax1 = tab_ax[0,0]



l_time_split_ax = []
t0 = t_begin_fst_week
while t0<t_end_last_week:
	l_time_split_ax += [t0]
	t0 += datetime.timedelta(weeks=1)
l_time_split_ax += [t_end_last_week]

print ("l_time_split_ax")
print (l_time_split_ax)


h_matin, h_soir = 7.+55/60, 19.+5/60
#h_matin, h_soir = 0,23
l_jour,  l_nuit =  h_soir-h_matin, 24-(h_soir-h_matin)
f_nuit = 8 

t0 = t_begin_fst_week

def modif_x(x):
	x /= 3600
	if x<h_matin: return x/f_nuit
	v  = h_matin/f_nuit
	x -= h_matin 
	i_jour = 0
	while True:
		if x<l_jour: return v+x/(1 if (i_jour%7)<5 else f_nuit)
		v += l_jour/(1 if (i_jour%7)<5 else f_nuit)
		x -= l_jour
		i_jour += 1
		if x<l_nuit: return v+x/f_nuit
		v += l_nuit/f_nuit
		x -= l_nuit


def get_x(d):
	return dt(t0,d)

def add_box(ax, coord, facecolor=None,       alpha=1, linewidth=0, zorder=1, hatch=None, edgecolor=None):
	(x, y), dx, dy = coord
	x1, x2 = modif_x(x), modif_x(x+dx)
	ax.add_collection(PatchCollection([Rectangle((x1, y), x2-x1, dy)], facecolor=facecolor, alpha=alpha, linewidth=linewidth, zorder=zorder, hatch=hatch, edgecolor=edgecolor))

esp = 0.03 
esp2 = 0.16

d_txt_a_aff = {}
def add_txt(ax,x, y, l_txt, ha='center', va='center', size=12):
	global d_txt_a_aff
	if (ax,x,y) not in d_txt_a_aff:
		d_txt_a_aff[(ax,x,y)] = (l_txt,ha,va,size)
	else:
		l_txt_other,ha_other,va_other,size_other = d_txt_a_aff[(ax,x,y)]
		for i in range(len(l_txt_other)):
			if len(l_txt_other[i]) == 0:
				l_txt_other[i] = l_txt[i]
			elif len(l_txt_other[i]) > 0 and len(l_txt[i]) > 0:
				l_txt_other[i] += "/"+l_txt[i]

def print_txt():
	global d_txt_a_aff
	d_shift = {}
	ll_shift = []
	for (ax1,x1,y1)in d_txt_a_aff.keys():
		for (ax2,x2,y2)in d_txt_a_aff.keys():
			if ax1==ax2 and x1!=x2:
				if y1==y2 and x2>x1 and x2-x1<3.0:
					i1, i2 = None, None
					for l_shift in ll_shift:
						if (ax1,x1,y1) in l_shift: i1 = ll_shift.index(l_shift)
						if (ax2,x2,y2) in l_shift: i2 = ll_shift.index(l_shift)
					if i1 is     None and i2 is     None: ll_shift += [[(ax1,x1,y1),(ax2,x2,y2)]]
					if i1 is not None and i2 is     None: ll_shift[i1] += [(ax2,x2,y2)]
					if i1 is     None and i2 is not None: ll_shift[i2] += [(ax1,x1,y1)]
					if i1 is not None and i2 is not None and i2 != i1: 
						i1,i2 = min(i1,i2), max(i1,i2)
						ll_shift[i1] += list(set(ll_shift.pop(i2)))
		
	ll_shift = map(lambda l : sorted(l, key=lambda ax_x_y:ax_x_y[1]) ,ll_shift)
	
	for l_shift in ll_shift:
		n_sub = 2
		if len(l_shift)>2 and min(np.array(lmap(lambda ax_x_y: ax_x_y[1], l_shift))[1:] - np.array(lmap(lambda ax_x_y: ax_x_y[1], l_shift))[:-1])<=1.:
			n_sub = 3
		
		size = 8 if n_sub ==2 else 5
		for i, (ax,x,y) in enumerate(l_shift):
			(l_txt,ha,va,size_old) = d_txt_a_aff[(ax,x,y)]
			d_txt_a_aff.pop((ax,x,y))
			#d_txt_a_aff[(ax,x,y+(0.24 if (i%2)==0 else -0.24))] = (l_txt,ha,va,6) # s_txt_meas-3
			d_txt_a_aff[(ax,x,y-0.5+1./n_sub/2 + 1./n_sub*(i%n_sub))] = (l_txt,ha,va,size) # s_txt_meas-3
	
	

	for (ax,x,y), (l_txt,ha,va,size) in d_txt_a_aff.items():
		offset = len(l_txt)*0.5
		for itxt, txt in enumerate(l_txt):
			#y_tmp=y + (offset-itxt*len(l_txt)/(len(l_txt)-1.+0.5))*esp2*size/s_txt_meas
			y_tmp=y + (offset-itxt*len(l_txt)/(len(l_txt)-1.+0.5))*esp2*size/(9*5/s_txt_meas)
			ax.text(x, y_tmp, txt, ha=ha, va=va, size=size, bbox=dict(alpha=0))
			#dx = tmp.get_bbox_patch().get_window_extent().xmax-tmp.get_bbox_patch().get_window_extent().xmin






'''ax1.set_xlim([
		get_x(l_starting[0][0].replace(hour=0,  minute=0)), 
		get_x(tf.replace(hour=23, minute=59))
		#ax1.get_xlim()[1]
	     ])'''

l_ax[0].text(modif_x(get_x(l_time_split_ax[0])+3600),-0.5,   tex(calendar.month_name[l_time_split_ax[0].month]), ha='left', va='bottom', rotation=90, size=10)




h,d,y,m = 3600, 3600*24, 3600*24*365,60							# time units


def get_sss_res(path, key):
	lines = open(path).readlines()
	while key not in lines[0]: lines.pop(0)
	v,s = map(lambda s:float(s), lines[0].split()[-3:-1])
	return v, v*s

def my_cos(x,a,x0,c):
	return a*np.cos(c*(x-x0))
param_cos = [1.,   4.79003275e+01,   2.98800185e-02]



d_xs_irdff_already_process = {}
def fct(idosi, name, mat, iso, mt, weight, volume, pos_barre, pos, power_irrad, t_irrad, t_cooling, t_in_hpge):
	d_rea = d_spectro[(iso,mt)]
	#lines = open(path+".out").readlines()							# step 1: get de atomic density
	'''weight		= get_csv_dosi_data(csv_dosi, name, "weight")
	radius		= get_csv_dosi_data(csv_dosi, name, "diameter [cm]") / 2.
	mat		= name.split("-")[0]
	thickness	= mass_rad_mat_2_ep(weight, radius, mat)
	volume          = (np.pi*radius**2)*thickness'''
	
	at_per_g = 6.022140857e23 / get_iso2mass(iso[:-1])					# at/g
	mass_frac = get_massic_fraction(iso[:-1], d_matdosi_2_data[mat]['compo'])
	at_density = at_per_g * mass_frac * d_matdosi_2_data[mat]["den"]*1e-24			# at/(barn.cm)
	
	ZZZ = iso[-4:-1]
	while ZZZ[0]=="0": ZZZ = ZZZ[1:]
	
	key_spectrum = pos_barre
	rr_v = None
	if pos_barre[0] == "P":
		#_, mat_petale, pos_ds_petale = pos_barre.split("_")
		pos_ds_petale = pos_barre[1:]
		mat_petale = data_irrad.l_compo_plate[idosi].lower()
		key_rr = "P"+"_".join([mat_petale,mat, iso, mt,pos_ds_petale])
		key_spectrum = "P"+"_".join([mat_petale,mat,pos_ds_petale])
		if key_rr in dico_petale_rr:
			rr_v = float(dico_petale_rr[key_rr]["rr_v"])
			rr_v *= volume / dico_petale_rr[key_rr]["vol"]
		#else:
		#	print("pas trouve",key_spectrum, key_rr)
		
	if key_spectrum not in dico_spectrum:
		key_spectrum_replace = "P"+"_".join([mat_petale,"Al",pos_ds_petale])
		print("WARNING - did not found",key_spectrum, "-> using", key_spectrum_replace,"spectrum to reconstruct the rr with its XS")
		key_spectrum = key_spectrum_replace
	
		
	l_fe, l_fv = dico_spectrum[key_spectrum]
	
	'''
	mat mat_dosi_0_4_Al iso 130270  mt 107    rr_v 1.398985e-10   rr_s% 2.51      surf s_petale_dos_0_4_Al z 47.0    rad 1.475     x1 -0.10750000000000001   th 0.05000000000000001    z_correction 1.0003619626320788 vol 0.3417463758483148     den 2.6989 mass 0.9223392937770168
	mat mat_dosi_1_4_Al iso 130270  mt 107    rr_v 9.145790e-11   rr_s% 2.88      surf s_petale_dos_1_4_Al z 47.0    rad 1.475     x1 -2.2975                th 0.04999999999999982    z_correction 1.0003619626320788 vol 0.3417463758483135     den 2.6989 mass 0.9223392937770134
	mat mat_dosi_2_4_Al iso 130270  mt 107    rr_v 6.036415e-11   rr_s% 3.45      surf s_petale_dos_2_4_Al z 47.0    rad 1.475     x1 -4.4875                th 0.05000000000000071    z_correction 1.0003619626320788 vol 0.3417463758483196     den 2.6989 mass 0.9223392937770297
	mat mat_dosi_3_4_Al iso 130270  mt 107    rr_v 4.385879e-11   rr_s% 4.69      surf s_petale_dos_3_4_Al z 47.0    rad 1.475     x1 -6.6775                th 0.05000000000000071    z_correction 1.0003619626320788 vol 0.3417463758483196     den 2.6989 mass 0.9223392937770297
	mat mat_dosi_4_4_Al iso 130270  mt 107    rr_v 3.378063e-11   rr_s% 8.52      surf s_petale_dos_4_4_Al z 47.0    rad 1.475     x1 -8.8675                th 0.05000000000000071    z_correction 1.0003619626320788 vol 0.3417463758483196     den 2.6989 mass 0.9223392937770297
	mat mat_dosi_5_4_Al iso 130270  mt 107    rr_v 2.153021e-11   rr_s% 5.99      surf s_petale_dos_5_4_Al z 47.0    rad 1.475     x1 -11.0575               th 0.05000000000000071    z_correction 1.0003619626320788 vol 0.3417463758483196     den 2.6989 mass 0.9223392937770297
	mat mat_dosi_6_4_Al iso 130270  mt 107    rr_v 1.445448e-11   rr_s% 5.92      surf s_petale_dos_6_4_Al z 47.0    rad 1.475     x1 -13.2475               th 0.05000000000000071    z_correction 1.0003619626320788 vol 0.3417463758483196     den 2.6989 mass 0.9223392937770297
	mat mat_dosi_7_4_Al iso 130270  mt 107    rr_v 1.049769e-11   rr_s% 8.13      surf s_petale_dos_7_4_Al z 47.0    rad 1.475     x1 -15.4375               th 0.05000000000000071    z_correction 1.0003619626320788 vol 0.3417463758483196     den 2.6989 mass 0.9223392937770297
	mat mat_dosi_8_4_Al iso 130270  mt 107    rr_v 7.002774e-12   rr_s% 8.57      surf s_petale_dos_8_4_Al z 47.0    rad 1.475     x1 -17.627499999999998    th 0.04999999999999716    z_correction 1.0003619626320788 vol 0.34174637584829526    den 2.6989 mass 0.9223392937769641
	'''
	
	path_irdff_case = path_iaea_data+"/"+mat+ZZZ+d_mt2name[mt]
	if path_irdff_case not in d_xs_irdff_already_process:
		(l_cor_e, cor), (l_xs_e,l_xs_v,l_xs_s) = get_irdff_iaea(path_irdff_case)
		tmp_proj_xs = projet_vec_intervals_from_continus(l_fe, l_xs_e, l_xs_v)
		d_xs_irdff_already_process[path_irdff_case] = tmp_proj_xs
	tmp_proj_xs = d_xs_irdff_already_process[path_irdff_case]
	
	def dlet(le, log10=False):
		if not log10:
			return np.log(le[1:])-np.log(le[:-1])
		else:
			return np.log10(le[1:])-np.log10(le[:-1])

	def integ(l_e,l_v,quad=False, log10=False):
		l_dlet = dlet(l_e, log10=log10)
		l_integ = l_v*l_dlet
		if quad: l_integ = l_integ**2
		for i in range(len(l_integ))[1:]:
			l_integ[i]+= l_integ[i-1]
		if quad: l_integ = l_integ**0.5
		return l_integ
	#print()
	#print(rr_v)
	txt_shield = ""
	#rr_v = None
	txt_compute_rr = ""
	if rr_v is None:												# then we need to compute it from spectrum
		rr_v_per_at = integ(l_fe, tmp_proj_xs * l_fv)[-1] * volume * my_cos(pos,*param_cos)
		rr_v = rr_v_per_at * at_density
		
		if mat=="Au" and 10e-3<weight<60e-3 and mat not in key_spectrum:
			txt_shield = "sshield Au "+str(weight_2_selfshielding_Au_15mm(weight)) # Au-04 weight 0.03149999999998307
			rr_v *= weight_2_selfshielding_Au_15mm(weight)
		if mat=="In" and int(mt)==102 and mat not in key_spectrum:
			txt_shield = "shield In of 0.142 from sep campaign"
			rr_v *= 0.142
		txt_compute_rr = "compute rr from spectrum"+str((key_spectrum, rr_v, mat, weight))
	#print(key_spectrum, rr_v)
	
	#print("coincoin", rr_v, integ(l_fe, tmp_proj_xs * l_fv)[-1] * volume * my_cos(pos,*param_cos)* at_density)
	
	
	at_per_src		= rr_v											# at/n
	at_per_J		= at_per_src/power_per_src_n					# at/J	
	equilibrium_at_quantity = at_per_J*power_irrad/d_rea["lambda"]				# at/s/(s-1)=at
	#print(equilibrium_at_quantity)
	nrj_irrad = power_irrad * t_irrad
	at_created		= equilibrium_at_quantity*(1-np.exp(-d_rea["lambda"] * t_irrad))# at
	at_put_in_hpge		= at_created * np.exp(-d_rea["lambda"] * t_cooling)		# at
	at_decay_in_hpge	= at_put_in_hpge*(1-np.exp(-d_rea["lambda"] * t_in_hpge))	# gamma
	return at_created, d_rea["lambda"] * at_created, d_rea["lambda"] * at_put_in_hpge, at_decay_in_hpge, txt_compute_rr+txt_shield, d_rea["lambda"]


ls, ls2 = 10, 15
txt  = aff("key", l=25)+aff("pos", l=ls)+aff("irrad", l=ls)+aff("power", l=ls)+aff("t_irrad", l=ls)+aff("t_cool", l=ls)+aff("t_hpge", l=ls)
txt += aff("act_irrad",l=ls2)+aff("act_hpge",l=ls2)+aff("decay_hpge",l=ls2)+aff("eff_decay_hpge",l=ls2)+aff("eff",l=24)+"period" # aff("pop out core")+
print (txt)

def act2str(v,unit="Bq", prec=4):
	if prec is not None:
		v = float(('%.'+str(prec-1)+'e')%v)
	if v>1e9: return aff(str(float(int(v/1e9*100))/100), l=7)+"G"+unit 
	if v>1e6: return aff(str(float(int(v/1e6*100))/100), l=7)+" M"+unit
	if v>1e3: return aff(str(float(int(v/1e3*100))/100), l=7)+"  k"+unit
	else:     return aff(str(float(int(v    *100))/100), l=7)+"   "+unit
	
def act2tex(v,unit="Bq", prec=4):
	if prec is not None:
		v = float(('%.'+str(prec-1)+'e')%v)
	def fint(v):
		return v if int(v) != v else int(v)
	if v>1e9: return str(fint(v/1e9))+r"\rm{G"+unit +"}"
	if v>1e6: return str(fint(v/1e6))+r"\rm{M"+unit+"}"
	if v>1e3: return str(fint(v/1e3))+r"\rm{k"+unit+"}"
	else:     return str(fint(v    ))+r"\rm{" +unit+"}"


old_comment = None

d_coord_done = {}
l_starting = []



d_hpge_calib = None
l_hpge_used = []


prev_irrad_name, nro_irrad_name = data_irrad.l_irrad_time_start[0],1




def gen_fct(l_irradiation,time_zero,log=False, fact=1):
	def fct(x):
		#param1 = [1.8367498386316123e-05,0.00012299307547309054,6.392976909445525e-07,1.4060412106102535e-05]
		#param2 = [0.0015857681121517872,0.0015241432672328662,0.00015152240292328896,0.00022814226281985355,1.5825490854051464e-05,4.9989884239010373e-05,1.2575202415384812e-06,6.387857944107609e-06]
		
		param = [0.0018012578836661428,0.002325086566619239,0.0003129105608273616,0.0005380502325996562,7.993956229841799e-05,0.00014659109761208918,7.657444960992908e-06,2.461705194449664e-05,1.524776800760012e-07,2.4614905404731693e-05,1.3769839492151543e-07,2.461689673676992e-05,1.521005552669318e-08,2.463475145343631e-05]
		#param = param1 if not empty else param2
		
		x = np.array(x)
		v = x*0
		for (puiss, duree, begin_of_irradiation) in l_irradiation:		# loop on the irradiations
			t0b = (begin_of_irradiation-time_zero).total_seconds()
			t1b = t0b + duree
			for iparam in range(int(len(param)/2)):				# loop on the fit order
				ai,li = param[2*iparam], param[2*iparam+1]
				for i in range(len(x)):					# 1J decay rate = sum_i a_i*exp(-l_i*t),
					t1b_loc = max(min(t1b,x[i]),t0b)		# so the convolution from t0 to t1 is:
					if x[i]>t0b:
						v[i] += puiss*ai/li * (np.exp(-li*(x[i]-t1b_loc)) - np.exp(-li*(x[i]-t0b)))
		v *= fact
		return v if not log else np.log(v)
	return fct


#gen_fct(l_irradiation,time_zero,log=False)

#fct_learn(l_dtime_precis, *sol)
l_irradiation = []
tmp_case_csv = ""
l_date_test = []
for idosi in range(data_irrad.nb_dosi):
	if tmp_case_csv != data_irrad.l_case_csv[idosi]:
		tmp_case_csv = data_irrad.l_case_csv[idosi]
		power_irrad = float(data_irrad.l_planned_power_and_time[idosi].split("_")[0][:-1])
		print(power_irrad)
		t_irr_e = data_irrad.l_irrad_time_stop[idosi]
		t_irr_b = data_irrad.l_irrad_time_start[idosi]
		duree_irrad_v1 = (t_irr_e-t_irr_b).total_seconds()
		duree_irrad_v2 = str2time(data_irrad.l_planned_power_and_time[idosi].split("_")[1])
		if duree_irrad_v1 != duree_irrad_v2:
			print("ERROR - impossible irradiation time for "+data_irrad.l_case_csv[idosi]+":")
			print(data_irrad.l_planned_power_and_time[idosi],"vs staring at",t_irr_b,"and ending at",t_irr_e)
			exit()
		l_irradiation += [(power_irrad, duree_irrad_v1, t_irr_b)]
		l_date_test += [(t_irr_b-t0).total_seconds(), (t_irr_e-t0).total_seconds()]
#print(l_irradiation)



#lid-top
#0.003333763374473286 299.96130129001546
#0.001451358968346081 0.001708398193379612 0.0031135583636734037 0.0037179257641820726 0.004099256218902062 0.004687108218547294 0.003812933187232498 0.0027594810683189163 0.004653850387677632
#689.0094193165497 585.3436300010161 321.17592901653245 268.9671777833347 243.94669339986714 213.35116523294965 262.2652826303048 362.38697611692726 214.87583757479163

#lid-knee
#0.005765729712068391 173.43858452241966
#0.005079756389211283 0.0058227905091021775 0.006403355880007565 0.006170174672472376 0.005339367343948064 0.0054207425484068695 0.007205518292680757 0.0026934444599903784 0.0077564173127960545
#196.8598340904428 171.7389623474864 156.16811227409377 162.0699661002145 187.28810654570447 184.47657144202415 138.78252186463573 371.27181007607345 128.92550254487497

fct_activity_lid   = gen_dose_rate_fct(l_irradiation,t0, pos="lid_attente")
fct_activity_inter = gen_dose_rate_fct(l_irradiation,t0, pos="BertholdCR_attente")
fct_activity_empty = gen_dose_rate_fct(l_irradiation,t0, pos="BertholdCR_arret")

#print(l_date_test)
#print(fct_activity(l_date_test))


l_data_a_optimiser = []

for idosi in range(data_irrad.nb_dosi):

	if data_irrad.l_irrad_time_start[idosi] != prev_irrad_name:
		prev_irrad_name = data_irrad.l_irrad_time_start[idosi]
		nro_irrad_name += 1
	
	
	power_irrad = float(data_irrad.l_planned_power_and_time[idosi].split("_")[0][:-1])
		
	t_irr_e = data_irrad.l_irrad_time_stop[idosi]
	t_irr_b = t_irr_e - datetime.timedelta(seconds=str2time(data_irrad.l_planned_power_and_time[idosi].split("_")[1]))
	
	comment = nro_irrad_name
	
	if data_irrad.l_hpge_id[idosi] not in l_hpge_used:
		l_hpge_used += [data_irrad.l_hpge_id[idosi]]
	nro_hpge = l_hpge_used.index(data_irrad.l_hpge_id[idosi])+1
	#print nro_hpge
	#exit()
	t_hpge_b = data_irrad.l_hpge_time[idosi]
	t_hpge_e = data_irrad.l_hpge_time_out[idosi]
	
	t_irrad      = (t_irr_e-t_irr_b).total_seconds()
	cooling_time = (t_hpge_b-t_irr_e).total_seconds()
	time_in_hpge = (t_hpge_e-t_hpge_b).total_seconds()
	
	pos = data_irrad.l_pos_reel[idosi]
	
	
	pop1, a1,a2, at_decay_in_hpge, txt_shi, lambda_decay = fct(
									idosi,
									data_irrad.l_name[idosi], 
									data_irrad.l_mat[idosi], 
									data_irrad.l_iso[idosi], 
									data_irrad.l_mt[idosi], 
									data_irrad.l_masse[idosi], 
									data_irrad.l_volume[idosi], 
									data_irrad.l_pos_name[idosi], 
									pos, 
									power_irrad, 
									t_irrad, 
									cooling_time,
									time_in_hpge)
	
	auto_abs = data_irrad.l_auto_abs[idosi]
	
	txt  = 	aff(data_irrad.l_name[idosi], l=25)+aff(pos, l=ls)+aff(comment, l=ls)+aff(str(power_irrad)+"W", l=ls)+aff(time2str(t_irrad), l=ls)+aff(time2str(cooling_time, approx=True), l=ls)+aff(time2str(time_in_hpge, approx=True), l=ls)
	keV = data_irrad.l_gamma_nrj[idosi]
	eff, eff_sig = data_irrad.l_eff_gamma[idosi], data_irrad.l_eff_gamma_s[idosi] 
	inten     = data_irrad.l_gamma_inten[idosi]
	
	val_mesuree = at_decay_in_hpge*eff*inten*auto_abs
	txt += aff(act2str(a1),l=ls2)+aff(act2str(a2),l=ls2)+aff(act2str(at_decay_in_hpge,unit=""),l=ls2)+aff(act2str(val_mesuree,unit=""),l=ls2)
	txt += aff(str(float(int(eff*100000))/1000)+"% at "+str(keV)+"keV",l=24)+aff("T1/2="+time2str(data_irrad.l_half_time[idosi]))
	
	pos_hpge = data_irrad.l_hpge_pos[idosi]
	if pos_hpge=="pgrd": pos_hpge = "grd"
	
	
	date_min  = str(t_irr_e).replace("-","_").replace(" ","_").replace(":","_")
	date_hpge = str(data_irrad.l_hpge_time[idosi]).replace("-","_").replace(" ","_").replace(":","_")
	l_data_a_optimiser +=[ (	data_irrad.l_case_csv[idosi],
					data_irrad.l_name[idosi],
					a1,
					eff*inten*auto_abs,
					lambda_decay,
					date_min,
					pos_hpge,
					data_irrad.l_hpge_id[idosi],
					date_hpge,
					time_in_hpge,
					data_irrad.l_meas_order[idosi])] # t_irrad, power_irrad*t_irrad,
	
	
	txt_irr1 =  tex(str(power_irrad)+r"\,W")
	txt_irr2 =  tex(time2str(t_irrad, tex=True, approx=3))
	txt_irr3 =  tex("i"+str(comment))
	#txt_mes1 =  tex(data_irrad.l_mat[idosi])
	
	#name_dosi_pr_affichage = data_irrad.l_name[idosi].split("-")[0]+"-"+data_irrad.l_name[idosi].split("-")[-1]
	#name_dosi_pr_affichage = data_irrad.l_name[idosi].split("-")[0]+"-"+"-".join(data_irrad.l_name[idosi].split("-")[2:])
	name_dosi_pr_affichage = data_irrad.l_name[idosi]
	
	proche_de_l_irrad = cooling_time < 24*7*3600
	txt_mes1 =  tex(name_dosi_pr_affichage + ("" if proche_de_l_irrad else "^{i"+str(comment)+"}"))
	#txt_mes1 =  tex(name_dosi_pr_affichage + ("" if proche_de_l_irrad else "^{"+data_irrad.l_pos_name_tex[idosi]+"}"))
	
	#txt_mes1 =  tex(data_irrad.l_name[idosi]+"@"+data_irrad.l_pos_name[idosi])
	#print("         "*5, txt_mes1)
	txt_mes2 =  tex(str(time2str(dt(t_hpge_b,t_hpge_e), approx=True, tex=True))+r"\,"+pos_hpge)
	txt_mes3 =  tex(str(pos)+"/i"+str(comment))
	txt_act  =  tex(d_mt2tex[data_irrad.l_mt[idosi]].replace("_{tot}","")+"^{"+data_irrad.l_aaa[idosi]+"}"+act2tex(val_mesuree,unit="", prec=2))
	
	for i in range(nb_week):
		
		if (old_comment is None or old_comment != comment) and l_time_split_ax[i]<t_irr_b<l_time_split_ax[i+1]:
			add_box(l_ax[i],((get_x( t_irr_b), -0.5+esp), dt(t_irr_b,t_irr_e), 1.-2*esp), facecolor=(1,0.75,0.75), alpha=1, linewidth=0, zorder=+1)
			l_ax[i].plot([modif_x(get_x(t_irr_b)),modif_x(get_x(t_irr_e))],[-0.5,+0.5], alpha=0)
			x1, x2 = modif_x(get_x(t_irr_b)), modif_x(get_x(t_irr_e))
			add_txt(l_ax[i], 0.5*(x1+x2),0.,   [txt_irr1, txt_irr2, txt_irr3])
			l_starting += [(t_irr_b,t_irr_e,0)]
			old_comment = comment
		
		if (t_hpge_b, t_hpge_e, nro_hpge) not in l_starting : l_starting += [(t_hpge_b,t_hpge_e,nro_hpge)]
		if nro_hpge>=0:
			if (l_time_split_ax[i]<t_hpge_e and  t_hpge_b<l_time_split_ax[i+1]):
				c = {"Al":(0.9,0.9,0.9), "Fe":(0.7,0.7,0.7), "In":(0.8,0.85,1), "Ni":(1,0.9,0.68), "Au":(1,1,0.7), "Rh":(0.7,0.7,0.7)}[data_irrad.l_mat[idosi]]
				coord = (get_x( t_hpge_b), nro_hpge-0.5+esp), dt(t_hpge_b,t_hpge_e), 1.-2*esp
				if (i,coord) not in d_coord_done: d_coord_done[(i,coord)]  = 0
				else:                             d_coord_done[(i,coord)] += 1
				if d_coord_done[(i,coord)] == 0:
					add_box(l_ax[i], coord, facecolor=c,	   alpha=1, linewidth=0, zorder=+1)
					add_box(l_ax[i], coord, facecolor=(1,1,1), alpha=1, linewidth=0, zorder=-1)
					l_ax[i].plot([modif_x(get_x(t_hpge_b)),modif_x(get_x(t_hpge_e))],[nro_hpge-0.5,nro_hpge+0.5], alpha=0)
					if (l_time_split_ax[i]<t_hpge_b<l_time_split_ax[i+1]):
						x1 = modif_x(get_x(t_hpge_b ))
						x2 = modif_x(get_x(min(t_hpge_e, l_time_split_ax[i+1])))
						
						#add_txt(l_ax[i], x1,nro_hpge, [txt_mes1, txt_mes2, ""], size=s_txt_meas, ha='left')
						add_txt(l_ax[i], 0.5*(x1+x2),nro_hpge, [txt_mes1, txt_mes2, ""], size=s_txt_meas)
				
				if (l_time_split_ax[i]<t_hpge_b<l_time_split_ax[i+1]):
					x1 = modif_x(get_x(t_hpge_b ))
					x2 = modif_x(get_x(min(t_hpge_e, l_time_split_ax[i+1])))
					#add_txt(l_ax[i], x1,nro_hpge, ["", "", txt_act], size=s_txt_meas, ha='left')
					add_txt(l_ax[i], 0.5*(x1+x2),nro_hpge, ["", "", txt_act], size=s_txt_meas)
	print (txt,txt_shi)


s = 22
s_optim = "l_irradiation_for_activation "#+str(l_irradiation)+"\n"
for pow,duree,date in l_irradiation:
	s_optim += str(pow)+" "+str(duree)+" "+str(date)+" "
s_optim += "\n"
s_optim += aff("case_csv", s)+aff("key", s)+aff("act", s)+aff("eff*inten*auto_abs", s)+aff("lambda_decay", s)+aff("date_min", s)
s_optim += aff("pos_hpge", s)+aff("hpge_id", s)+aff("date_hpge", s)+aff("time_in_hpge", s)+aff("order_meas", s)+"\n"

for (case_csv, key, act, eff, lambda_decay, date_min, pos_hpge, nro_hpge, date_hpge, time_in_hpge, order_meas) in l_data_a_optimiser:
	s_optim += aff(case_csv, s)+aff(key, s)+aff(act, s)+aff(eff, s)+aff(lambda_decay, s)+aff(date_min, s)
	s_optim += aff(pos_hpge, s)+aff(nro_hpge, s)+aff(date_hpge, s)+aff(time_in_hpge, s)+aff(order_meas, s)+"\n"


if os.path.exists("optim"):
	open("optim/input.txt","w").write(s_optim)
else:
	print("WARNING: no optim rep = no generation of the optimisation input <=> pas de bras pas de chocolat")

my_sub6_finalise(tab_ax)

y1,y2 = -0.55, nb_hpge+0.7
for ax in l_ax:
	ax.set_ylim([y1,y2])

for i in range(nb_week):
	l_ax[i].set_xlim((modif_x(get_x(l_time_split_ax[i])), modif_x(get_x(l_time_split_ax[i+1]))))


#ti = l_starting[0][0].replace(hour=0, minute=0)
#tf = sorted(l_starting, key=lambda (d1,d2,a): get_x( d2))[-1][1].replace(hour=0, minute=0)


done1, done2, done3 = False, False, False
for i in range(nb_week):
	#ax1.text(get_x(ti)+3600,-0.5,   tex(calendar.month_name[ti.month]), ha='left', va='bottom', rotation=90)
	ti = l_time_split_ax[i]
	month  = ti.month
	#while get_x(ti) <= get_x(tf):
	print("week",i)
	
	for d in range(8):
		coord = (get_x(ti)+d*24*3600-(24-h_soir)*3600, y1), (h_matin-h_soir+24)*3600, y2-y1
		add_box(l_ax[i],coord, facecolor=(0.95,0.95,1), alpha=1, linewidth=0, zorder=-2)
	for d in range(7)[-2:]:
		coord = (get_x(ti)+d*24*3600+h_matin*3600, y1), (h_soir-h_matin)*3600, y2-y1
		add_box(l_ax[i], coord, facecolor=(1,1,1), alpha=1,  edgecolor=(0.2,0.2,0.5), zorder=-2, hatch="/", linewidth=0)
		#add_box(l_ax[i], coord, facecolor=(1,1,1), alpha=1,  edgecolor=(0.3,0.3,0.7), zorder=-2)
		#add_box(l_ax[i], coord, facecolor=(0.9,0.9,0.9), alpha=1,  zorder=-2, linewidth=0)

	for d in range(7):
		l_ax[i].plot([modif_x(get_x(ti)+d*24*3600+24*3600)]*2, [y2-0.03, y2],"black") # +13*3600
		D = "Mo Tu We Th Fr Sa Su".split()[d]
		l_ax[i].text(modif_x(get_x(ti)+d*24*3600+13*3600),y2-0.12,   r"$\rm{"+D+"~"+str((ti+datetime.timedelta(days=d)).day)+"}$", ha='center', va='center')
	
	
	
	if l_time_split_ax[i].month != l_time_split_ax[i+1].month:
		t_month = datetime.datetime(l_time_split_ax[i+1].year,l_time_split_ax[i+1].month,1,0,0)
		l_ax[i].plot([modif_x(get_x(t_month)), modif_x(get_x(t_month))], l_ax[i].get_ylim(), c=(0.5,0.5,0.5),  zorder=0)
		l_ax[i].text(modif_x(get_x(t_month)+1*3600),-0.5,   tex(calendar.month_name[t_month.month]), color=(0.5,0.5,0.5), ha='left', va='bottom', rotation=90)
	
		coord = (get_x(t_month), y1), 1.*3600, y2-y1
		#add_box(l_ax[i],coord, facecolor=(0.95,0.95,1), alpha=1,  edgecolor=(0.7,0.7,0.7), zorder=-2)
		add_box(l_ax[i],coord, facecolor=(0.95,0.95,1), alpha=1,  edgecolor=(0.5,0.5,0.5), zorder=-2, hatch="//", linewidth=0)
		#plt.fill_between([get_x(ti),get_x(ti),get_x(ti)+3600,get_x(ti)+3600],[y1,y2,y2,y1], facecolor="none", hatch="//", edgecolor="b", linewidth=0.0,  zorder=0)
	
	l_t_decay = np.arange((ti-t0).total_seconds(), (ti-t0).total_seconds()+7*24*3600, 60*5)
	
	
	#f = act_empt2inter / act_empt2lid
	f = fct_activity_inter([24*3600*7.])/fct_activity_lid([24*3600*7.])
	#print("fct_activity_inter/fct_activity_lid",f)
	
	
	'''
	print(fct_activity_lid([24*3600*7.]))
	print(fct_activity_inter([24*3600*7.]))
	print(fct_activity_empty([24*3600*7.]))
	
	exit()'''
	
	lvl1, lvl2 = dose_max_cavity_door/f, dose_max_cavity_roof
	
	# obj1: lid     = dose_max_cavity_lid  -> lid     curve at -0.5
	# obj2: attente = dose_max_cavity_door -> attente curve at -0.5
	
	
	
	
	l_v_decay_lid   = fct_activity_lid(l_t_decay)
	l_v_decay_inter = fct_activity_inter(l_t_decay)
	l_v_decay_empty = fct_activity_empty(l_t_decay)
	
	a = np.log10(dose_max_cavity_door/f)
	b = np.log10(dose_max_cavity_roof)-a

	l_v_decay_scaled       = (np.log10(l_v_decay_lid  +1e-50) - a)/b - 0.5
	l_v_decay_empty_scaled = (np.log10(l_v_decay_empty+1e-50) - a)/b - 0.5
	l_v_decay_inter_scaled = (np.log10(l_v_decay_inter+1e-50) - a)/b - 0.5
	
	'''
	lvl1, lvl2 = dose_max_cavity_door/f, dose_max_cavity_roof
	
	l_v_decay_lid   = fct_activity_lid(l_t_decay)
	l_v_decay_inter = fct_activity_inter(l_t_decay)
	l_v_decay_empty = fct_activity_empty(l_t_decay)

	l_v_decay_scaled       = (np.log10(l_v_decay_lid  +1e-50) - np.log10(lvl1))/(np.log10(lvl2)-np.log10(lvl1)) - 0.5
	l_v_decay_empty_scaled = (np.log10(l_v_decay_empty+1e-50) - np.log10(lvl1))/(np.log10(lvl2)-np.log10(lvl1)) - 0.5
	l_v_decay_inter_scaled = (np.log10(l_v_decay_inter+1e-50) - np.log10(lvl1))/(np.log10(lvl2)-np.log10(lvl1)) - 0.5
	'''
	
	#print(ti)
	#print(l_t_decay)
	#print(l_v_decay)
	
	c = (0,0.,1.) # (1,0.75,0.75)
	c2 = (0,0.8,0.) # (1,0.75,0.75)
	a2, a2b = 1, 1
	
	c = (1,0,0) # (1,0.75,0.75)
	c2 = c
	a2, a2b = 0.2, 0.3
	aff_all_dose = False
	l_ax[i].plot(lmap(lambda x:modif_x(x), l_t_decay), l_v_decay_scaled,c=c, zorder=-1)
	l_ax[i].plot(lmap(lambda x:modif_x(x), l_t_decay), l_v_decay_scaled,c=c, zorder= 1, alpha=0.2)
	if aff_all_dose:
		l_ax[i].plot(lmap(lambda x:modif_x(x), l_t_decay), l_v_decay_empty_scaled,c=c2, zorder=-1, alpha=a2)
		l_ax[i].plot(lmap(lambda x:modif_x(x), l_t_decay), l_v_decay_empty_scaled,c=c2, zorder= 1, alpha=a2*0.2)
	
		l_ax[i].plot(lmap(lambda x:modif_x(x), l_t_decay), l_v_decay_inter_scaled,c=c2, zorder=-1, alpha=a2)
		l_ax[i].plot(lmap(lambda x:modif_x(x), l_t_decay), l_v_decay_inter_scaled,c=c2, zorder= 1, alpha=a2*0.2)
	
	for j in range(len(l_t_decay)-1):
		if l_v_decay_lid[j] > lvl2 > l_v_decay_lid[j+1]:
			l_ax[i].plot([modif_x(l_t_decay[j])],[ 0.5],"o",c=c, zorder=1, markersize=3)
			if not done1:
				done1 = True
				#l_ax[i].text(modif_x(l_t_decay[j]),  0.5, tex("open lid"), c=c, ha="right", va="top", size=8, rotation=45)
				l_ax[i].text(modif_x(l_t_decay[j]),  0.5, "$\mathrm{lid:"+str(dose_max_cavity_roof*1000)+"\mu Sv/h}$", c=c, ha="right", va="top", size=8, rotation=45)
				print("Open the lid at:" )
				print("  t =",l_t_decay[j]/3600,"h")
				print("  lid     dose rate =",l_v_decay_lid[j],  "mSv/h")
				print("  attente dose rate =",l_v_decay_inter[j],"mSv/h")
				print("  arret   dose rate =",l_v_decay_empty[j],"mSv/h")
		if l_v_decay_lid[j] > lvl1 > l_v_decay_lid[j+1]:
			l_ax[i].plot([modif_x(l_t_decay[j])],[-0.5],"o",c=c, zorder=1, markersize=3)
			if not done2:
				done2 = True
				#l_ax[i].text(modif_x(l_t_decay[j]), -0.5, tex("open door"), c=c, ha="left", va="bottom", size=8, rotation=45)
				#l_ax[i].text(modif_x(l_t_decay[j]), -0.5, tex("open door"), c=c, ha="right", va="top", size=8, rotation=45)
				l_ax[i].text(modif_x(l_t_decay[j]), -0.5, "$\mathrm{cavity:"+str(dose_max_cavity_door*1000)+"\mu Sv/h}$", c=c, ha="left", va="bottom", size=8, rotation=45)
				print("Open the door at:")
				print("  t =",l_t_decay[j]/3600,"h")
				print("  lid     dose rate =",l_v_decay_lid[j],  "mSv/h")
				print("  attente dose rate =",l_v_decay_inter[j],"mSv/h")
				print("  arret   dose rate =",l_v_decay_empty[j],"mSv/h")

		#if l_v_decay[j] > l_v_decay[j+1]:
		if l_v_decay_lid[j] > l_v_decay_lid[j+1] and l_v_decay_scaled[j] < 0 and 10<(l_t_decay[j]/3600)%24<11:
			if not done3:
				done3 = True
				if aff_all_dose:
					l_ax[i].text(modif_x(l_t_decay[j]), l_v_decay_scaled[j]-0.02,
						tex("Dose Rate - lid [a.u.]"), c=c, ha="left", va="bottom", size=6, rotation=-2.5)
					l_ax[i].text(modif_x(l_t_decay[j]), l_v_decay_empty_scaled[j]-0.02,
						tex("Dose Rate - empty [a.u.]"), c=c2, ha="left", va="bottom", size=6, rotation=-2.5, alpha = a2b)
					l_ax[i].text(modif_x(l_t_decay[j]), l_v_decay_inter_scaled[j]-0.02,
						tex("Dose Rate - inter [a.u.]"), c=c2, ha="left", va="bottom", size=6, rotation=-2.5, alpha = a2b)
				else:
					l_ax[i].text(modif_x(l_t_decay[j]), l_v_decay_scaled[j]-0.02,
						tex("Dose Rate [a.u.]"), c=c, ha="left", va="bottom", size=6, rotation=-2.5)
					
	#exit()

for i, (pow,duree,date) in enumerate(l_irradiation):
	print(i+1,"- dose rate attente/arret:", fct_activity_inter([(date-t0).total_seconds()]), fct_activity_empty([(date-t0).total_seconds()]))

l_d_done = []
for d in data_irrad.l_irrad_time_stop:

	if d not in l_d_done:
		l_d_done += [d]
		
		#print(d, end="\t")
		d2 = d+datetime.timedelta(minutes=0)
		while fct_activity_lid([(d2-t0).total_seconds()])[0]>dose_max_cavity_roof:
			d2 += datetime.timedelta(minutes=5)

		print(d,"   ",d2,"   ",fct_activity_lid([(d2-t0).total_seconds()])[0])

#exit()

#	fct_activity_inter

#coord = (get_x(tf)+18*3600, y1), (24-18)*3600, y2-y1 ???
#ax1.add_collection(PatchCollection([Rectangle(*coord)], facecolor=(0.21,0,0.71), alpha=0.07, linewidth=0, zorder=-2)) ???
	

for starting,ending,pos in l_starting:
	i_plot = lmap(lambda i: l_time_split_ax[i]<starting<l_time_split_ax[i+1], range(len(l_time_split_ax))).index(True)
	l_ax[i_plot].plot([modif_x(get_x(starting)), modif_x(get_x(starting))], [l_ax[i_plot].get_ylim()[0], pos-0.5+esp], c=(0.85,0.85,0.85),alpha=1, zorder=-1,  linewidth=1) # dashes=[3,3],
for iax, ax in enumerate(l_ax):
	l_sub_starting = list(filter(lambda start_end_pos: l_time_split_ax[iax]<start_end_pos[0]<l_time_split_ax[iax+1], l_starting))
	l_sub_start = lmap(lambda start_end_pos: start_end_pos[0], l_sub_starting)
	l_sub_start = list(set(l_sub_start))
	#exit()
	l_label_x_txt = lmap(lambda start: (modif_x(get_x(start)), tex(":".join(str(start).split()[-1].split(":")[:2])))    ,l_sub_start)
	l_label_x_txt = sorted(l_label_x_txt, key = lambda x_txt: x_txt[0])
	l_label_x   = lmap(lambda x_txt : x_txt[0], l_label_x_txt)
	l_label_txt = lmap(lambda x_txt : x_txt[1], l_label_x_txt)
	for i in range(len(l_label_x))[1:]:
		j = i-1
		#while l_label_txt[j] == "": j-=1
		if float(l_label_x[i])-float(l_label_x[j]) < 30/60:
			l_label_txt[i] = ""
	ax.set_xticks(l_label_x)
	ax.set_xticklabels(l_label_txt, rotation=45, ha='right')
	ax.tick_params(axis='both', which='both', labelsize=get_aff_size("s_tick")*0.6)
	
	#ax.set_yticks     ([0,1,2,3,4])
	#ax.set_yticklabels([r"$\rm{CROCUS}$", r"$\rm{HPGe_1}$", r"$\rm{HPGe_2}$", r"$\rm{HPGe_3}$", r"$\rm{HPGe_4}$"])
	
	
	ax.set_yticks     (range(nb_hpge+1))
	#ax.set_yticklabels([r"$\rm{CROCUS}$"]+lmap(lambda i: r"$\rm{HPGe_{"+str(i+1)+"}}$",range(nb_hpge)))
	ax.set_yticklabels([r"$\rm{CROCUS}$", r"$\rm{Furggen}$", r"$\rm{Homtruc}$",r"$\rm{Liotruc}$", r"$\rm{Zmtruc}$"])

	
	#ax1.plot([get_x(starting), get_x(starting)], [ax1.get_ylim()[0], pos-0.5+esp], c=(0.5,0.5,0.5), zorder=0, dashes=[5,3])	


	
for iax, ax in enumerate(l_ax):
	ax.tick_params(axis='x',which='both',bottom=True, top=False)   


	ax.set_ylabel(tex(r"Week\,"+str(l_time_split_ax[iax].isocalendar()[1])),rotation=90)
	ax.yaxis.set_label_position("right")
	#ax.yaxis.tick_right()
	
print ("print txt")
print_txt()

print ("save")
#fig.savefig("expected_act_out.pdf", bbox_inches=('tight'), dpi=200) #
if name_save == "auto_time":
	name_save = str(now).split(".")[0].replace("-","_").replace(":","_").replace(" ","_")

if not os.path.exists(path_save):
	os.makedirs(path_save)

if not no_save:
	#fig.savefig(path_save+"/"+name_save+".png", bbox_inches=('tight'), dpi=250) #
	fig.savefig(path_save+"/"+name_save+".pdf", bbox_inches=('tight'), dpi=250) #
#fig.savefig("expected_act_out.png", bbox_inches=('tight'), dpi=200) #
#plt.show()


