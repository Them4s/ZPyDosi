from ZPyDosi.Common.utils_general import get_aff_size, tex,time2strdetail
from ZPyDosi.Prints.PrintnSave import aff
from ZPyDosi.Plots.SubPlots import my_sub6
import numpy as np
import datetime
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time 
import xlrd


fig = plt.figure(figsize=(10,12))
fig.patch.set_facecolor('white')
tab = my_sub6(fig,1,1,0,list_ry=[0.5,1,1],list_sy=[0.25,0.25], list_rx=[1], auto_x=False)

#axb      = tab[0,0]
ax_data  = tab[0,2]
ax_res   = tab[0,0]
ax2      = tab[0,1]


t0_plot = 0
#ylims = [1e-4,200]
ylims = [2.2e-4,500]

time_final = 2500*3600
time_final_b = 40*24*3600

#t_max_inter_for_fit = 24*3600

#tmaxi = 300*3600
tmaxi = time_final
time_final = min(time_final,tmaxi)

#t_max_cut = (5*24+11)*3600
#t_max_cut = 400*3600

#fact_inter = 0.239
fact_inter = 0.240
#fact_inter = 0.2325
#fact_lid = 0.006
fact_lid = 0.025
a_def=0.2

add_inter2arret = False
add_arret2inter = True

print_bkg_txt = False

order = 8
#order = 7
parm1, parm2 = None, None

aff_txt = False

parm1 = [1.0287956569799693e-07,6.637770132244113e-07,2.2034583834463852e-07,3.8113241971407034e-06,2.6977207958066966e-06,2.025936134784721e-05,1.5436511686055186e-05,6.480631958444108e-05,0.0001035611482487392,0.0001993118083426514,0.00047599160904421,0.0007727553737838752,0.0025888000212775705,0.0038613181502555436,0.017329844729335225,0.014435498823138444]
parm2 = [5.060441300944927e-09,2.102975109179922e-09,3.862863363155557e-08,1.7298711604086694e-06,7.345804666638942e-07,2.0767405705269492e-05,1.1773371555284363e-05,0.00010175015392391319,7.624930397673175e-05,0.0004512558424831955,0.0021238580413679886,0.004459057827522436,7.178921242999715e-05,13.346090061823569,7.178921243014424e-05,13.346090061824194]

parm1 = [2.2034583834463852e-07,3.8113241971407034e-06,2.6977207958066966e-06,2.025936134784721e-05,1.5436511686055186e-05,6.480631958444108e-05,0.0001035611482487392,0.0001993118083426514,0.00047599160904421,0.0007727553737838752,0.0025888000212775705,0.0038613181502555436,0.017329844729335225,0.014435498823138444]
parm2 = [3.862863363155557e-08,1.7298711604086694e-06,7.345804666638942e-07,2.0767405705269492e-05,1.1773371555284363e-05,0.00010175015392391319,7.624930397673175e-05,0.0004512558424831955,0.0021238580413679886,0.004459057827522436,7.178921242999715e-05,13.346090061823569,7.178921243014424e-05,13.346090061824194]

parm1 = [1.010947062090077e-07,6.548177100852579e-07,2.1595643750431106e-07,3.710600989588316e-06,2.6313866297230167e-06,1.997800514365113e-05,1.5206873929478927e-05,6.400483871640703e-05,0.00010316490973689739,0.00019820019345045194,0.0004744193487656812,0.000769667410877759,0.0025669104945947323,0.0038414067261134475,0.01725288266035062,0.01436942663849082]
parm2 = [2.516953968655509e-08,6.55227969293629e-07,4.5213931599633653e-08,4.051290668526604e-06,8.191329789451315e-07,2.4304100044943538e-05,7.345931414776874e-07,5.880437300547394e-05,7.425444264810675e-06,9.563373664294541e-05,3.2175502033208505e-05,0.00028083629928882107,0.00015024874485750647,0.0009988766005180943,0.0042699428439633555,0.0079619242748327]

if False:
	#parm1 = [4.879904112059452e-08,6.245630587343926e-09,2.893495664691977e-07,3.4401023124287137e-06,3.108414694680775e-06,2.1567722833541143e-05,1.918117000039467e-05,7.309786929108412e-05,0.00010514580711925888,0.000212908628877374,0.0005007007159544772,0.0008039043985944134,0.0035741953558312057,0.004340561703832964]
	parm1 = [1.4883115377296885e-07,9.695933826981152e-07,3.6880889033187823e-07,7.178514036045216e-06,3.5652716706717004e-06,2.464454283651707e-05,2.1512285661711316e-05,7.959114573149655e-05,0.0001069617300899716,0.0002221131958477992,0.0005077733308577164,0.0008212293058190325,0.0036485628125740525,0.004417728847648495]

	parm2 = []
	for i in range(len(parm1)):
			parm2 += [parm1[i] * (1 if i%2!=0 else fact_inter)]

bounds_min, bounds_max = [1e-10,np.log(2)/(3600*24*60*12)], [1,1]
bounds_min, bounds_max = [1e-10,np.log(2)/(3600*24*60*12)], [10,1]
#bounds_min, bounds_max = [-np.inf,-np.inf], [np.inf,np.inf]
#param [1.8984975404480735e-08,2.6175927230856587e-09,2.904972431060061e-07,2.452412055898363e-06,2.5106281444119076e-09,2.486790777970009e-06,3.240269560772611e-10,2.535306082216637e-06,3.1878720810578945e-06,2.141431926767639e-05,2.0211920651961927e-05,7.482630749882066e-05,0.00010985611443517946,0.00021901249551682832,0.0005344085745815491,0.0008451040012328253,0.004681359842962301,0.004926836028055261]

for i in range(len(parm1)//2):
	parm1[2*i  ] = max(bounds_min[0], min(bounds_max[0], parm1[2*i  ]))
	parm1[2*i+1] = max(bounds_min[1], min(bounds_max[1], parm1[2*i+1]))
	parm2[2*i  ] = max(bounds_min[0], min(bounds_max[0], parm2[2*i  ]))
	parm2[2*i+1] = max(bounds_min[1], min(bounds_max[1], parm2[2*i+1]))

'''
	a                        lambda                   T1/2
	1.8984975404480735e-08   2.6175927230856587e-09   264803295.96227357
	2.904972431060061e-07    2.452412055898363e-06    282638.954939419
	2.5106281444119076e-09   2.486790777970009e-06    278731.60327776667
	3.240269560772611e-10    2.535306082216637e-06    273397.8297223669
	3.1878720810578945e-06   2.141431926767639e-05    32368.39667400536
	2.0211920651961927e-05   7.482630749882066e-05    9263.415551687754
	0.00010985611443517946   0.00021901249551682832   3164.875040231144
	0.0005344085745815491    0.0008451040012328253    820.191573520883
	0.004681359842962301     0.004926836028055261     140.6880960951215

'''

do_bounds = False
print("bounds", bounds_min, bounds_max)
#exit()
xlog = False


l_fact_inter = [fact_inter]
#bkg_arret = [0.0184,0.0183,0.0185,0.0186,0.0190,0.0187,0.0186,0.0188,0.0191,0.0192,0.0197,0.0195,0.0190,0.0189]
#bkg_inter = [0.0035,0.0040,0.0040,0.0049,0.0044,0.0044]
#bkg_arret, bkg_inter = map(lambda l: sum(l)/len(l), [bkg_arret, bkg_inter])
bkg_arret = 0.01845
bkg_inter = 0.0037
bkg_inter = 0.0033
print("bkg_arret, bkg_inter", bkg_arret, bkg_inter)



data_top_inter = [
			(13, 45, 0,19.2e-3),
			(14,  4, 0,12.0e-3),
			(14, 19, 0,15.9e-3),
			(14, 36, 0,14.1e-3),
			(14, 54, 0,11.9e-3),
			(15,  7, 0,11.5e-3),
			(16, 30,25,4.31e-3),
			(17, 34,25,2.04e-3),
			(1*24+10, 40,25, 0.3e-3),]
			
data_top_arret = [
			(15, 21, 0, 8.2e-3),
			(15, 24, 0, 7.8e-3),]

data_knee_inter = [
			(13, 45, 0, 67.2e-3),
			(14,  4, 0, 40.9e-3),
			(14, 19, 0, 32.7e-3),
			(14, 36, 0, 23.4e-3),
			(14, 54, 0, 15.5e-3),
			(15,  7, 0, 13.3e-3),
			(16, 31,10, 8.1e-3 ),
			(17, 30,25, 2.04e-3),
			(1*24+10, 40,25, 0.5e-3),]
			
data_knee_arret = [
			(15, 21, 0, 11.6e-3),]

data_Bdw_inter = [
			(13, 50, 0, 1.9102),
			(14,  7, 0, 1.1775),
			(14, 25, 0, 0.7882),
			(14, 39, 0, 0.6245),
			(15,  0, 0, 0.4697),
			(15, 10, 0, 0.4083),
			(15, 27, 0, 1.5260),
			(16, 35, 1, 0.186),
			(16, 41, 3, 1.048),
			(17, 37,52, 0.121),
			(17, 44,15, 0.694),
			(18, 27, 0, 0.4335),
			(1*24+10, 21, 0, 0.0580),
			(1*24+10, 38, 0, 0.0104),
			(1*24+12, 48, 0, 0.0099),
			(1*24+14, 36, 0, 0.0082),
			(1*24+15, 12, 0, 0.0469),
			(2*24+12,  0, 0, 0.0282),
			(2*24+14, 22, 0, 0.0047),
			(2*24+16, 37, 0, 0.0044),
			(2*24+18, 26, 0, 0.0253),]

data_Bcr_inter = []
data_Bcr_arret = []
data_Bcr_x     = []


d0 = datetime.datetime(2020,5,13,0,0,0)
data_Bcr_inter = []

wb = xlrd.open_workbook("dose_rate_data.xlsx")
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows): #[:100]:
	year = sheet.cell_value(i, 0)
	if type(year) == float:
		ye,mo,da,ho,mi,se,dose,state = map(lambda j:sheet.cell_value(i, j), range(8))
		if state == "": state = "x"
		h_eq = (datetime.datetime(*map(lambda s:int(s),[ye,mo,da,ho,0,0]))-d0).total_seconds()/3600
		if h_eq*3600 < tmaxi:
			if h_eq < 5000:
				if state=="inter":
					data_Bcr_inter += [(h_eq, int(mi), int(se), float(dose))]
				elif state=="arret":
					data_Bcr_arret += [(h_eq, int(mi), int(se), float(dose))]
				elif state=="x":
					data_Bcr_x += [(h_eq, int(mi), int(se), float(dose))]
				else:
					print("ERROR - unrecognized state:", state)
					exit()
			else:
				data_Bcr_x += [(h_eq, int(mi), int(se), float(dose))]

l_irradiation = []

for i in range(sheet.nrows):
	year = sheet.cell_value(i, 10)
	if type(year) == float:
		ye,mo,da,ho,mi,se,power_W,Wh = map(lambda j:sheet.cell_value(i, 10+j), range(8))
		#ye,mo,da,ho,mi,se,power_W,Wh = l[:-1].split(";")[10:10+8]
		power_W, Wh = float(power_W), float(Wh)
		duree_h = Wh/power_W
		time_end_irrad = (datetime.datetime(*map(lambda s:int(s),[ye,mo,da,ho,mi,se]))-d0).total_seconds()
		if time_end_irrad<tmaxi:
			l_irradiation += [(float(power_W), duree_h*3600, time_end_irrad-duree_h*3600)]


red = (1,0,0)
blue = (0,0,1)
data = {}
#l_data_to_fit = None
def to_t(l):
	return list(map(lambda t: t[0]*3600+t[1]*60.+t[2], l))
ax_data.plot([0],[0], c=(0,0,0), label=tex("Fit + Bkg"))
for s,l,sy,c in [
				("Berthold~-~attente", 	data_Bcr_inter,		"o", (0,0,1)),
				("Berthold~-~arret"  , 	data_Bcr_arret,		"o", (1,0,0)),
				(""  , 	data_Bcr_x,		"x", (0.3,0,0.3)),
				#("Berthold~cavity~door", 	data_Bdw_inter,		"o", (0,  0.5,  0  )),
				("Lid~-~top",  				data_top_inter,		"o", (0,  0.7,0  )),
				("Lid~-~knee", 				data_knee_inter,	"o", (0,  0.25,  0  )),
				]:
	l_t = np.array(to_t(l))
	l_v = np.array(list(map(lambda t: t[3], l)))
	ax_data.plot(l_t/3600-t0_plot, l_v, sy, c=c, markersize=3, alpha=0.5, label= "" if s=="" else tex(s))




ax_data.set_yscale('log')
ax_data.set_ylim(ylims)

def old_fct(x, l_irradiation):								# legacy correlation from "Cinetique CROCUS" xlx file
	param = 18.81
	v = x*0.
	#x = x/3600
	for (puiss, duree, t0b) in l_irradiation:
		t1b = t0b + duree
		for i in range(len(x)):
			if x[i]>t1b:
				v[i] = param*puiss*((x[i]-t1b)**(-0.2)-(-t0b+x[i])**(-0.2))+0.1
	return v

f_num = 3600
f_num = 1

def gen_fct(l_irradiation, log=False):									# generate dose rate function associated to an irradiation profile
	def fct(x,*param):
		param = abs(np.array(param))
		v = x*0
		x = x/f_num
		for (puiss, duree, t0b) in l_irradiation:
			duree, t0b = duree/f_num, t0b/f_num
			t1b = t0b + duree
			if x[-1]>t0b:
				i_pos_debut = list(x>t0b).index(True)
				i_pos_fin   = list(x>t1b).index(True)
				for i_param in range(int(len(param)/2)):									# loop on the fit order
					ai,li = param[2*i_param], param[2*i_param+1]
					#for ix in range(len(x)):											# 1J decay rate = sum_i a_i*exp(-l_i*t),
					#	t1b_loc = max(min(t1b,x[ix]),t0b)							# so the convolution from t0 to t1 is:
					#	if x[ix]>t0b:
					#		v[ix] += puiss*ai/li * (np.exp(-li*(x[ix]-t1b_loc)) - np.exp(-li*(x[ix]-t0b)))
					
					v[i_pos_debut:i_pos_fin] += puiss*ai/li * (1 - np.exp(-li*(x[i_pos_debut:i_pos_fin]-t0b)))
					v[i_pos_fin:]            += puiss*ai/li * (np.exp(-li*(x[i_pos_fin:]-t1b)) - np.exp(-li*(x[i_pos_fin:]-t0b)))
				
		return v if not log else np.log(v)
	return fct

'''
def gen_fct(l_irradiation, log=False):									# generate dose rate function associated to an irradiation profile
	def fct(x,*param):
		param = abs(np.array(param))
		v = x*0
		x = x/f_num
		for (puiss, duree, t0b) in l_irradiation:
			duree, t0b = duree/f_num, t0b/f_num
			t1b = t0b + duree
			for i in range(int(len(param)/2)):									# loop on the fit order
				ai,li = param[2*i], param[2*i+1]
				for i in range(len(x)):											# 1J decay rate = sum_i a_i*exp(-l_i*t),
					t1b_loc = max(min(t1b,x[i]),t0b)							# so the convolution from t0 to t1 is:
					if x[i]>t0b:
						v[i] += puiss*ai/li * (np.exp(-li*(x[i]-t1b_loc)) - np.exp(-li*(x[i]-t0b)))
		return v if not log else np.log(v)
	return fct
'''


def my_super_fit(l_irradiation,order, x,y, param_guess=None, force_lambda=None):					# fitting to many parameter at the same time do not converge...
	print("start to fit")
	t0 = time.time()
	lim_t = 24
	
	sol = None 																	# then this function do an iteration, adding more and more exponentials
	my_fct = gen_fct(l_irradiation)
	my_fct_log = gen_fct(l_irradiation, log=True)
	if param_guess is None or len(param_guess) != order*2:
		for o in range(order):														# loop on the order (e.g. order 3->3exponentials so 6 params)
			if sol is None:
				sol = [y[0],1/3600.*f_num]
			else:
				sol = list(sol)+list(sol[-2:]) 											# the guess is the previous exponential with smaller values
			print(o, sol)
			bounds = [bounds_min*(o+1)]+[bounds_max*(o+1)]
			try:
				#print(bounds)
				sol, cov_sol = curve_fit(my_fct_log, x, np.log(y), p0=sol, maxfev=2500, bounds=bounds)	# here the calculation is done
				sol = abs(sol)
			except:
				sol = np.zeros(2*(o+1))
			print("#"*50,'fit',o, (((my_fct_log(x, *sol)-np.log(y))**2).sum())**0.5)
	else:
		#print([bounds_min*order]+[bounds_max*order])
		sol, cov_sol = curve_fit(my_fct_log, x, np.log(y), p0=param_guess, maxfev=2500, bounds=([bounds_min*order]+[bounds_max*order]))
		#sol, cov_sol = curve_fit(my_fct_log, x, np.log(y), p0=param_guess, maxfev=2500)
		sol = abs(np.array(sol))
		print("#"*50,'fit',(((my_fct_log(x, *sol)-np.log(y))**2).sum())**0.5)
	print("ok in",time.time()-t0,"s")
	sol = np.array(sorted([[sol[2*o], sol[2*o+1]] for o in range(order)], key=lambda i_j:i_j[1])).reshape(2*order)
	print("parm =", "["+",".join(map(lambda v:str(v), sol))+"]")
	print(aff("a",25)+aff("lambda",25)+aff("T1/2",25))
	for o in range(order):
		print (aff(sol[2*o],25) + aff(sol[2*o+1],25) + aff(np.log(2)/sol[2*o+1],25))						# and print the results!
	return my_fct, sol, cov_sol


#l_dtime_precis     = np.arange(0,time_final,120.)
#print(len(l_dtime_precis))
l_dtime_precis     = np.arange(0,time_final,3600)								# binnin ofr plot, with a focus around the irradiations
l_sup = []
for (puiss, duree, t0b) in l_irradiation:
	duree, t0b = duree/f_num, t0b/f_num
	t1b = t0b + duree
	l_sup += list(np.arange(t0b, t1b+3600, 60))
	l_sup += list(np.arange(t0b, t0b+100, 5))
	l_sup += list(np.arange(t1b-10, t1b+100, 5))
	l_sup += list(np.arange(t1b+100, t1b+3600*3, 500))
	l_sup += list(np.arange(t1b+3600*3, t1b+3600*10, 1000))
#print(len(l_dtime_precis),len(l_sup))
l_dtime_precis = np.array(sorted(list(l_dtime_precis)+l_sup))
#print(len(l_dtime_precis))
#exit()

l_dtime_precis_log = np.logspace(np.log10(1.),int(np.log10(time_final_b))+1,100)

l_dtime_precis_b   = np.arange(0,time_final_b,30.)	# a precise time array for plot


def ifilter(x,y, tmax):
	x,y = list(x), list(y)
	i = 0
	while i<len(x):
		if x[i] > tmax:
			x.pop(i)
			y.pop(i)
		else:
			i += 1
	return np.array(x),np.array(y)



l_t_inter = np.array(to_t(data_Bcr_inter))
l_v_inter = np.array(list(map(lambda t: t[3], data_Bcr_inter))) - bkg_inter

l_t_arret = np.array(to_t(data_Bcr_arret))
l_v_arret = np.array(list(map(lambda t: t[3], data_Bcr_arret))) - bkg_arret

#l_t_inter, l_v_inter, l_t_arret, l_v_arret = lmap(lambda l:np.array(l), l_data_to_fit)

l_t_inter_begin, l_v_inter_begin = ifilter(l_t_inter, l_v_inter, 24*3600)
l_t_arret_begin, l_v_arret_begin = ifilter(l_t_arret, l_v_arret, 24*3600)


if add_inter2arret:
	l_t_arret = np.concatenate((l_t_inter_begin, 			l_t_arret))
	l_v_arret = np.concatenate((l_v_inter_begin/fact_inter,	l_v_arret))

if add_arret2inter:
	l_t_inter = np.concatenate((l_t_arret_begin, 			l_t_inter))
	l_v_inter = np.concatenate((l_v_arret_begin*fact_inter,	l_v_inter))


fct_learn, sol_arret, cov_arret = my_super_fit(l_irradiation, order, l_t_arret, l_v_arret, parm1)				# compute the fitted function and solution

fct_learn, sol_inter, cov_inter = my_super_fit(l_irradiation, order, l_t_inter, l_v_inter, parm2)				# compute the fitted function and solution

print(sol_inter)
print(sol_arret)


for l_irr,axe,alpha in [								# plot the irradiation gate on the graph
		(l_irradiation,      ax_data,	1.),
	   ]:
	for (puiss, duree, t0b) in l_irr:
		t1b = t0b + duree
		ax_data.plot([t0b/3600-t0_plot,t0b/3600-t0_plot], [0,puiss],     c=(0,0,0), alpha=alpha)
		ax_data.plot([t0b/3600-t0_plot,t1b/3600-t0_plot], [puiss,puiss], c=(0,0,0), alpha=alpha)
		ax_data.plot([t1b/3600-t0_plot,t1b/3600-t0_plot], [puiss,0],     c=(0,0,0), alpha=alpha)
		if aff_txt:
			ax_data.text(t0b/3600-t0_plot, puiss,tex(format(puiss,'.1f')+"W, "+time2strdetail(t1b-t0b)),va="top",ha="right",rotation=90)
		
		ax_data.add_artist(Rectangle(xy=(t0b/3600-t0_plot,0), width=(t1b-t0b)/3600, height=puiss, color=(0,0,0), alpha=0.2, zorder=-1))



for a in [ax_data]:
	a.plot(l_dtime_precis/3600-t0_plot, fct_learn(l_dtime_precis, *sol_inter), c=blue, zorder=-1,alpha=a_def)
	a.plot(l_dtime_precis/3600-t0_plot, fct_learn(l_dtime_precis, *sol_arret), c=red, zorder=-1,alpha=a_def)
	
	a.plot(l_dtime_precis/3600-t0_plot, fct_learn(l_dtime_precis, *sol_arret)+bkg_arret, c=red, zorder=-1)
	a.plot(l_dtime_precis/3600-t0_plot, fct_learn(l_dtime_precis, *sol_inter)+bkg_inter, c=blue, zorder=-1)
	a.plot(l_dtime_precis/3600-t0_plot, fct_learn(l_dtime_precis, *sol_inter)*fact_lid, c=(0,0,0), zorder=-1)
	
	
	
	#a.plot(l_dtime_precis/3600-t0_plot, old_fct(l_dtime_precis, l_irradiation), c=(0.2,0.6,0.2), zorder=-2, label=tex("Old correlation"))#, dashes=[5,2]


ax_res.plot(l_t_arret/3600-t0_plot, ((fct_learn(l_t_arret, *sol_arret)+bkg_arret)/(l_v_arret+bkg_arret)-1)*100, "o", c=red, markersize=3, alpha=0.5, )
ax_res.plot(l_t_inter/3600-t0_plot, ((fct_learn(l_t_inter, *sol_inter)+bkg_inter)/(l_v_inter+bkg_inter)-1)*100, "o", c=blue,markersize=3, alpha=0.5, )


ax_data.legend(loc="best")


#										# plot an the example of irradiation
#axb.plot(l_dtime_precis_b/3600, gen_fct(l_irradiation_test)(l_dtime_precis_b, *sol), c=color,alpha=alpha_test)
#print(gen_fct(l_irradiation_test, time_zero_b)(l_dtime_precis_b, *sol))

for i,(isol, icov, c) in enumerate([	(sol_arret, cov_arret, (1,0,0)),
										(sol_inter, cov_inter, (0,0,1))]):
	print(isol)
											# plot the deacy rate associated to 1 Joule in 1 second
	ax2.plot(l_dtime_precis_log/3600, gen_fct([(1.,1, 0)])(l_dtime_precis_log, *isol), c=c)
	
	#print("sample")
	#for j in range(16):
	#	isol_j = np.random.multivariate_normal(isol, icov)
	#	ax2.plot(l_dtime_precis_log/3600, gen_fct([(1.,1, 0)])(l_dtime_precis_log, *isol_j), c=c, alpha=0.5)
	#print("ok")
	
	for o in range(order):
		ax2.plot(l_dtime_precis_log/3600, isol[2*o]/f_num*np.exp(-isol[2*o+1]*l_dtime_precis_log/f_num), "-",c=c, alpha=0.2) # , dashes=[2,6]
		
		cst = format(isol[2*o]/f_num, '.2e').replace("e-","~10^{-").replace("e+","~10^{")+"}"
		lam = format(isol[2*o+1]/f_num, '.2e').replace("e-","~10^{-").replace("e+","~10^{")+"}"
		
		ax2.text(3.5 if i==0 else 65,5e-3 / (2.**o),tex(cst+"\exp("+lam+" . t)"+("+"if o<order-1 else "")), va="top",ha="left",c=c, size=8)
	
	


#for h,m,s in l_alter:
#	t = h+m/60+s/3600
#	ax_data.plot([t,t], ylims, c=(0,0,0),zorder=-1)
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_ylim([3e-9, 3e-2])


ax_data.set_xlim([0.6, ax_data.get_xlim()[-1]])
if xlog:
	ax_data.set_xscale('log')

for x,txt in [
	(60,      "min"),
	(3600,    "hour"),
	(3600*24, "day"),
	#(3600*24*2, "day"),
	#(3600*24*3, "day"),
	#(3600*24*4, "day"),
	#(3600*24*5, "day"),
	#(3600*24*6, "day"),
	(3600*24*7, "week"),
	(3600*24*30, "month"),
	 ]:
	ax2.text(x/3600,2e-2,tex(txt), va="top",ha="right",rotation=90, alpha=0.5)
	ax2.plot([x/3600,x/3600], ax2.get_ylim(), c=(0,0,0), alpha=0.5, linewidth=0.5)



ax_data.plot(ax_data.get_xlim(), [bkg_arret,bkg_arret], c=red, alpha=a_def)
ax_data.plot(ax_data.get_xlim(), [bkg_inter,bkg_inter], c=blue,alpha=a_def)

if print_bkg_txt:
	ax_data.text(0.62,bkg_arret*1.05,tex(str(int(bkg_arret*10000)/10)+"~10^{-3}"), va="bottom",ha="left",c=red)
	ax_data.text(0.62,bkg_inter*1.05,tex(str(int(bkg_inter*10000)/10)+"~10^{-3}"), va="bottom",ha="left",c=blue)

#ax2.set_xlim([1e-2, 1*24*7*1.1])
ax2.set_xlim([1e-2, time_final_b/3600])
#ax_data.set_ylim((0,ax_data.get_ylim()[-1]))

ax2.set_xlabel(tex(r"Time [hour]"), size=get_aff_size("s_xylabel"))			# axes names
ax2.set_ylabel(tex(r"Dose rate [mSv/h/J]"), size=get_aff_size("s_xylabel"))
ax_data.set_xlabel(tex(r"Time [hour]"), size=get_aff_size("s_xylabel"))			# axes names
ax_data.set_ylabel(tex(r"Dose rate [mSv/h]"), size=get_aff_size("s_xylabel"))


xlimsave = ax_data.get_xlim()
ax_res.plot(xlimsave, [0,0], c="black",dashes=[8,4], zorder=-1)

print("save zoom")
ax_data.set_xlim([10.5,35])
ax_res.set_xlim([10.5,35])
fig.savefig("berthold_out_zoom.png", bbox_inches=('tight'), dpi=250) #

print("save classic")
ax_data.set_xlim(xlimsave)
ax_res.set_xlim(xlimsave)
fig.savefig("berthold_out.png", bbox_inches=('tight'), dpi=250) #


plt.show()

