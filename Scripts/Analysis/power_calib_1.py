


from utils_p3 import *
import datetime
from scipy.optimize import curve_fit


fig = plt.figure(1, figsize=(16/1.2,5/1.4))
fig.patch.set_facecolor('white')

l_ax = my_sub6(fig,1,1,0,list_rx=[1,1,1],list_sx=[0.30,0.30],list_ry=[1],auto_y=False,auto_x=False)[:,0]

aff_param["ampli"] *=1.2






def aff_list(s, l_v, l1=42, l2=20):
	return aff(s,l=l1)+''.join(map(lambda v: aff(v,l=l2), l_v))

def aff_v_s(txt,v,s=None,talk=False):
	def aff(v,l=20): return str(v)+" "*(l-len(str(v)))
	err = "" if s is None else ("(+-"+aff(s)+" - "+aff(100.*s/v)+"%)")
	print (aff(txt, 42)+aff(v)+err)


print()
print( "#"*50," bash input")

c1,c2 = (0,0,0), (0.8,0,0.1)								# color monitors (plot)
dwell_obj = 1.										# dwell reconstruction target

'''
data_irrad = DataIrrad(	path_csv_data,
	path_csv_dosi,
	lcase_csv,
	use_sqrt_for_meas_sig=True,
	load_hpge_eff=True,
	load_sss_results=True,
	load_ndup=True)
'''

path_csv	= get_param_vari("csv_data", 	str, None)				# get csv with the experiment data (irradiation time, counts...)
case_csv	= get_param_vari("case", 	str, None)				# get the case in the csv
case_csv_res	= get_param_vari("res", 	str, None)				# get the case to compute the residual
csv_dosi	= get_param_vari("csv_dosi", 	str)					# get the path to the csv with the dosimeters data (weight, radius...)
moni		= get_param_vari("moni", 	str)
#if   moni=="v1": i_moni_to_use=0							# get the monitor channel
#elif moni=="v2": i_moni_to_use=1
#else:
#	print "moni choice not valid (v1 or v2)"
#	exit()


print ("#"*50, "data from csv and small calculations")
data_other     = get_csv(path_csv,"data_other",  case_csv)				# get the name of the block with the general data (irradiation plate, hpge...)
data_hpge_name = get_csv_list(path_csv, "hpge", "name", data_other)		# get the list of HPGe names (e.g. L1 for lotus1)
data_hpge_pos  = get_csv_list(path_csv, "hpge", "pos" , data_other)		# get the list of HPGe positions (p0, p1...)
data_hpge_path = get_csv_list(path_csv, "hpge", "path", data_other)		# get the path of the calibration associatd to this HPGe name and position


class HPGe_master:														# small class to manage the EfficiencyCalibration objects:
	def __init__(self):													#   the EfficiencyCalibration object are quite long to generate,
		self.d_hpge_calib   = {} 										#   they are stored in a dict d_hpge_calib accordingly to their name(L1, S1...)
	def get_hpge_calib(self, name,pos):									#   and position (p0,p1...)
		key = (name,pos)
		if key in self.d_hpge_calib: return self.d_hpge_calib[key]
		l_pos_path = list(filter(lambda i: data_hpge_name[i]==name and data_hpge_pos[i]==pos, range(len(data_hpge_name))))
		if len(l_pos_path) == 0 or len(l_pos_path)>1:
			print ("error - get_hpge_calib_path -", len(l_pos_path),"choice(s) from",name,pos)
			exit()
		self.d_hpge_calib[key] = EfficiencyCalibration(data_hpge_path[l_pos_path[0]])
		return self.d_hpge_calib[key]
		
hpge_master = HPGe_master()


l_iso      = np.array(get_csv_list(path_csv,"dosimeters", "iso", case_csv))		# get the list of iso measured
l_mt       = np.array(get_csv_list(path_csv,"dosimeters", "mt", case_csv))		# get the list of mt measured
l_hpge_id   = get_csv_list(path_csv, 	"dosimeters","hpge_id",		case_csv)	# get the list of hpge name used (L1, S1...)
l_hpge_pos  = get_csv_list(path_csv, 	"dosimeters","hpge_pos",	case_csv)	# get the list of hpge position used (p0, p1...)
											# then from the EfficiencyCalibration, get the efficientcy
l_eff_gamma   = np.array(lmap(lambda i: hpge_master.get_hpge_calib(l_hpge_id[i],l_hpge_pos[i]).get_eff_sig(d_spectro[(l_iso[i], l_mt[i])]["keV"])[0], range(len(l_iso))))
l_eff_gamma_s = np.array(lmap(lambda i: hpge_master.get_hpge_calib(l_hpge_id[i],l_hpge_pos[i]).get_eff_sig(d_spectro[(l_iso[i], l_mt[i])]["keV"])[1], range(len(l_iso))))
l_gamma_inten = np.array(lmap(lambda i: d_spectro[(l_iso[i], l_mt[i])]["inten"], range(len(l_iso))))


print (aff_list("l_eff_gamma",l_eff_gamma))
print (aff_list("l_eff_gamma_s",l_eff_gamma_s))
print (aff_list("l_eff_gamma_s [%]",l_eff_gamma_s/l_eff_gamma*100))
print (aff_list("l_gamma_inten",l_gamma_inten))


irrad_time	= datetime.datetime(*map(lambda s:int(s), (get_csv(path_csv,"date", case_csv)+"_"+get_csv(path_csv,"time_start_irrad", case_csv)).split("_")))
l_name		= get_csv_list(path_csv, "dosimeters","name", case_csv)
l_name_sss	= get_csv_list(path_csv, "dosimeters","name_sss", case_csv)
#l_w        = np.array(map(lambda s:float(s), get_csv_list("weight")))
#l_pos      = np.array(map(lambda s:float(s), get_csv_list("pos")))
#l_h        = l_pos + radius + h_barre_min

l_w        = np.array(lmap(lambda name: float(get_csv_dosi_data(csv_dosi, name, "weight")), l_name))
#l_diam   = np.array(map(lambda name: get_csv_dosi_data(csv_dosi, name, "diameter [cm]"), l_name))

l_h        = get_csv_list(path_csv, "dosimeters","pos_reel [cm]", case_csv, data_type=float)


l_hpge_date = get_csv_list(path_csv, "dosimeters","y_m_d", case_csv)
l_hpge_hour = get_csv_list(path_csv, "dosimeters","h_m_s", case_csv)
l_hpge_time = lmap(lambda i: datetime.datetime(*map(lambda s:int(s), (l_hpge_date[i]+"_"+l_hpge_hour[i]).split("_"))), range(len(l_hpge_date)))
l_time_in_hpge = lmap(lambda s: float(s[:-1]) * {"s":1, "m":60, "h":3600, "d":3600*24}[s[-1]],get_csv_list(path_csv, "dosimeters","time_in_hpge", case_csv))
l_measure   = get_csv_list(path_csv, "dosimeters","counts", case_csv, data_type=float)
l_measure_s = get_csv_list(path_csv, "dosimeters","counts_sig", case_csv, data_type=float)

if case_csv_res is not None:
	l_measure_res      = get_csv_list(path_csv, "dosimeters","counts", case_csv_res, data_type=float)
	l_measure_res_s    = get_csv_list(path_csv, "dosimeters","counts_sig", case_csv_res, data_type=float)
	l_hpge_date_res    = get_csv_list(path_csv, "dosimeters","y_m_d",  case_csv_res)
	l_hpge_hour_res    = get_csv_list(path_csv, "dosimeters","h_m_s", case_csv_res)
	l_hpge_time_res    = lmap(lambda i: datetime.datetime(*map(lambda s:int(s), (l_hpge_date_res[i]+"_"+l_hpge_hour_res[i]).split("_"))), range(len(l_hpge_date_res)))
	l_time_in_hpge_res = lmap(lambda s: float(s[:-1]) * {"s":1, "m":60, "h":3600, "d":3600*24}[s[-1]],get_csv_list(path_csv, "dosimeters","time_in_hpge", case_csv_res))
#else:
#	l_meas_res, l_m_res, l_ms_res = None, None, None



dir_moni        = get_csv(path_csv, "monitor_path", case_csv)
calc        	= get_csv(path_csv,	"sss_path",			case_csv)



aff_v_s("dir_moni", dir_moni)
aff_v_s("calc", calc)
aff_v_s("irrad_time", irrad_time)


print (aff_list("l_name",	l_name))
print (aff_list("l_w",		l_w))
print (aff_list("l_h",		l_h))
print (aff_list("l_hpge_time",	l_hpge_time))

print (aff_list("l_measure",l_measure))
print (aff_list("l_measure_s",l_measure_s))
print (aff_list("l_measure_s [%]",l_measure_s/l_measure*100))
print (aff_list("l_time_in_hpge",l_time_in_hpge))





den_at_dosi = 5.90079E-02
den_dosi = 19.3
#J_per_I = 1./2771.92150091								# J / I
J_per_I = 1.										# J / I

half_time = 2.69517*3600*24


l_m = l_measure
l_ms = l_measure_s
	

time_ref = irrad_time




def act_begin(meas, meass, Dt):
	lambd = np.log(2)/half_time
	return lambd*meas / (1-np.exp(-lambd*Dt)), lambd*meass / (1-np.exp(-lambd*Dt))
	
def residual_counts(act1, act1s, d1, d2, Dt2):
	lambd = np.log(2)/half_time
	t12 = (d2-d1).total_seconds()
	act2, act2s = act1*np.exp(-lambd*t12),  act1s*np.exp(-lambd*t12)
	return act2/lambd*(1-np.exp(-lambd*Dt2)), act2s/lambd*(1-np.exp(-lambd*Dt2))

if case_csv_res is not None:
	print ("remove residual")
	for i in range(len(l_hpge_date)):	
		date,     time_meas	 = l_hpge_time[i],     l_time_in_hpge[i]
		date_res, time_meas_res  = l_hpge_time_res[i], l_time_in_hpge_res[i]
		act_res, acts_res = act_begin(l_measure_res[i], l_measure_res_s[i], time_meas_res)
		act,     acts     = act_begin(l_measure[i],     l_measure_s[i],     time_meas)
		res_supression, res_supression_s = residual_counts(act_res, acts_res, date_res, date, time_meas)
		l_measure[i] -= res_supression
		l_measure_s[i] = (l_measure_s[i]**2+res_supression_s**2)**0.5
		act_new, act_news     = act_begin(l_measure[i], l_measure_s[i],     time_meas)
		print ("    ",time_meas_res, act_res,acts_res,"|", time_meas, act,acts, "|", act_new, act_news)


if True:
	if False:
		def autop(m):
			return 1-0.0081*(m*1e3)
	else:	
		l_e  = np.array( [0]+[0.0005,0.001,0.002,0.004,0.008,0.016,0.032,0.064,0.128,0.256])
		l_na = np.array( [1]+[4.95E-07,1.02E-06,2.11E-06,4.12E-06,8.70E-06,1.65E-05,3.33E-05,6.29E-05,1.22E-04,2.32E-04])
		l_a  = np.array( [1]+[4.81E-07,9.69E-07,1.96E-06,3.81E-06,7.02E-06,1.33E-05,2.37E-05,3.93E-05,6.78E-05,1.13E-04])
		l_s  = np.zeros(len(l_a))+1
		l_s[0] = 0.01
		def my_fct(x, a, b, c):
			return a*np.exp(b*x) + c
		def my_fct(x, a, b,c,d):
			return a*np.exp(-b*x)+c*x+d
			#return 1-a*np.exp(-b*x)-c*np.exp(-d*x)
		popt, ipcov =  curve_fit(my_fct, l_e, l_a/l_na, sigma=l_s)
		if False:
			fig2 = plt.figure(2, figsize=(16,5))
			ax = plt.subplot(1,1,1)
			ax.plot(l_e, l_a/l_na,"o")
			l_e2=np.arange(0,l_e[-1],l_e[-1]/1000)
			ax.plot(l_e2, my_fct(l_e2,*popt))
			ax.set_xscale('log')
			#ax.set_yscale('log')
			plt.show()
			exit()
		def autop(m):
			return my_fct(m,*popt)
		
	print ("WARNING - autop correction is used (for plotting & cos fitting), e.g. for",l_w[0],"g -> ",autop(l_w[0]))
	l_w_eff = l_w*autop(l_w)
	print (aff_list("l_w_eff", l_w_eff))
else:
	l_w_eff = l_w

def autoabs(wgt):
	ep = wgt/den_dosi /(np.pi*0.75**2)
	#return 1-ep*0.08/0.01
	return 1-ep*1.8730100366 # +- 0.0162282 
	
	#return 1-ep*(1-0.98165842)/0.01 # 0.98165842 +-0.0027002  
	#exit()
	#return 1-ep*(1-0.98165842)/0.01	# 0.98165842 +-0.0027002
	# w2, eff2 = 0.040, 0.00249713
	# w1, eff1 = 0.010, 0.00250135
	# l1, l2 = map(lambda w: w / 19.3 / (np.pi*0.75**2), [w1,w2])
	# auto_abs = eff2/eff1
	# print "auto_abs per cm",(1-auto_abs) / (l2-l1)




l_abs_gamma_Au = autoabs(l_w)

#fact_gamma_Au = l_eff_gamma*l_gamma_inten
print (aff_list("l_abs_gamma_Au",l_abs_gamma_Au))




class Measure:
	def __init__(self, dwell, t0, path):
		self.t0 = t0
		l_v = map(lambda v:float(v), open(path).readlines()[2:])
		while l_v[-1] == 0:
			l_v.pop(len(l_v)-1)
		fact = int(dwell_obj/dwell)
		if fact > 1:
			new_l_v = []
			while len(l_v)>fact:
				new_l_v += [sum(l_v[:fact])]
				l_v = l_v[fact:]
			dwell = dwell_obj
			l_v = new_l_v
		self.l_v = np.array(l_v)
		self.l_t = np.arange(len(self.l_v))*dwell
		self.l_s = self.l_v**0.5
		self.l_v *= J_per_I
		self.l_s *= J_per_I
		self.dwell = dwell
	
	def assimile(self, other, data_gap, ax=None):
		if (self.t0-other.t0).total_seconds() > 0:
			return other.assimile(self, data_gap)
		t_fin = (self.t0-time_ref).total_seconds() + self.l_t[-1]
		t_nxt = (other.t0-time_ref).total_seconds()
		inter_lt, inter_lv, inter_ls = data_gap.sub(t_fin+self.dwell, t_nxt-self.dwell)
		tmp_len_avt = len(self.l_v)
		s_ta, s_0a, s_1a = self.comp_factor(data_gap)
		s_tb, s_0b, s_1b = other.comp_factor(data_gap)
		s_t, s_0, s_1 = s_ta+s_tb, s_0a+s_0b, s_1a+s_1b
		fact = 1.* s_0 / s_1
		inter_lv, inter_ls = map(lambda l: list(np.array(l)*fact), [inter_lv, inter_ls])
		self.l_v = np.array(list(self.l_v)+inter_lv+list(other.l_v))
		self.l_s = np.array(list(self.l_s)+inter_ls+list(other.l_s))
		self.l_t = np.arange(len(self.l_v))*self.dwell
		
		if ax is not None:
			aff_curve(ax, dupx((np.arange(len(inter_lv))+ tmp_len_avt)*self.dwell + (self.t0-time_ref).total_seconds())/3600.,
				dup(inter_lv),dup(inter_ls),"black",1.,0.3)
		
	def sub(self, t0, t1):
		i0, i1 = 0, 0
		my_t = (self.t0-time_ref).total_seconds()
		#print t0, t1
		while my_t+self.l_t[i0] <  t0: i0 += 1
		while my_t+self.l_t[i1] <= t1: i1 += 1
		return map(lambda l: list(l)[i0:i1], [self.l_t, self.l_v, self.l_s])
	
	def comp_factor(self, other, reverse=False):
		if (self.t0-other.t0).total_seconds() > 0:
			return other.comp_factor(self, reverse=not reverse)
		add_t0, add_t1 = (self.t0-time_ref).total_seconds(), (other.t0-time_ref).total_seconds() 
		i0, i1 = 0, 0
		while self.l_t[i0] + add_t0 < other.l_t[0] + add_t1:
			i0 += 1
		s_0,s_1,s_t = 0,0,0
		while len(self.l_t) > i0 and len(other.l_t) > i1 : #and  (other.l_t[i0] + add_t0) < (other.l_t[i1] + add_t1):
			s_0 += self.l_v[i0]
			s_1 += other.l_v[i1]
			s_t += self.dwell
			i0, i1 = i0+1, i1+1

		if reverse:
			s_0, s_1 = s_1, s_0
		return s_t, s_0, s_1
		
	def plot(self, ax, c, label=None):
		#aff_curve(ax, dupx(self.l_t + (self.t0-time_ref).total_seconds()),dup(self.l_v)/2700.,dup(self.l_s)/2700.,c,1.,0.3, label=label)
		aff_curve(ax, dupx(self.l_t + (self.t0-time_ref).total_seconds())/3600.,dup(self.l_v),dup(self.l_s),c,1.,0.3, label=label)

	#def propagate_rr(self, fact, t_half, date_start, l_date_meas, ax=None): #date_meas_max
	def propagate_rr(self, fact, t_half, date_start, l_hpge_time, l_time_in_hpge, l_name, ax=None): #date_meas_max

		lambd = np.log(2)/t_half
		l_t = list(self.l_t)
		l_at = []
		t_irrad = (date_start-self.t0).total_seconds()
		
		#t_final = (date_meas_max-self.t0).total_seconds()
		t_final = t_irrad
		#for date, time_meas, name in l_date_meas:
		#	t_final = max(t_final, (date-self.t0).total_seconds()+time_meas+60)
		for i in range(len(l_hpge_time)):
			t_final = max(t_final, (l_hpge_time[i]-self.t0).total_seconds()+l_time_in_hpge[i]+60)
		
		l_prod = 1.*self.l_v
		
		at = 0
		for i in range(len(l_t)):
			if l_t[i]>t_irrad:
				at += (fact*self.l_v[i] -lambd*at)*self.dwell
			else:
				l_prod[i] = 0
			l_at += [at]
		while l_t[-1]<t_final:
			#at += (fact*self.l_v[i] -lambd*at)*self.dwell
			at += -lambd*at*self.dwell
			l_at += [at]
			l_t  += [l_t[-1]+self.dwell]
		l_cp_histo = []
		l_cp_histo_met_2 = []
		#for date, time_meas, name in l_date_meas:
		for j in range(len(l_hpge_time)):
			t_begin = (l_hpge_time[j]-self.t0).total_seconds()
			decay, i = 0, 0
			while l_t[i]<t_begin : i += 1
			i0 = i
			while l_t[i]-t_begin < l_time_in_hpge[j]:
				decay += lambd*l_at[i]*self.dwell
				i += 1
			l_cp_histo += [decay]
			ax.fill_between((np.array(l_t[i0:i])+(self.t0-time_ref).total_seconds())/3600., np.array(l_at[i0:i])*0, l_at[i0:i], facecolor=(0.5,0.5,0.5), alpha=0.3,linewidth=0.0, zorder = 0)
		
			l_t_prod = np.arange(len(l_prod))
			l_cp_histo_met_2 += [sum(fact * l_prod * np.exp(-lambd*(t_begin-l_t_prod)) * (1-np.exp(-lambd*l_time_in_hpge[j])))]
			
		l_cp_histo_met_2 = np.array(l_cp_histo_met_2)
		l_cp_histo       = np.array(l_cp_histo)
		if ax is not None:
			ax.plot((np.array(l_t)+(self.t0-time_ref).total_seconds())/3600.,l_at, c="black", linewidth=2)
		return l_cp_histo_met_2



mode_vr = True
if not mode_vr:
	print (aff_list("l_calcul (raw)", np.array(lmap(lambda name : get_sss_out(calc+"_det0.m", "DETdos_"+name+"_791970_102_rr ")[-2] , l_name_sss))))

	print (aff_s_v("den_at_dosi",den_at_dosi))
	#l_c  = den_at_dosi * np.array(map(lambda name : get_sss_out(calc+"_det0.m", "DETdos"+name+"_rr_jeff ")[-2] , l_name_sss))
	#l_cs = np.array(map(lambda name : get_sss_out(calc+"_det0.m", "DETdos"+name+"_rr_jeff ")[-1] , l_name_sss))
	l_c  = den_at_dosi * np.array(lmap(lambda name : get_sss_out(calc+"_det0.m", "DETdos_"+name+"_791970_102_rr ")[-2] , l_name_sss))
	l_cs = np.array(lmap(lambda name : get_sss_out(calc+"_det0.m", "DETdos_"+name+"_791970_102_rr ")[-1] , l_name_sss))
	l_cs *= l_c
else:
	l_c =


if False: # MCNP (Oscari) value
	print ("WARNING: l_c values overloaded!!")
	#l_c  = np.array([1.07205100483455E-06	,1.44008433455611E-06	,1.47434136618048E-06	,1.25511339393653E-06	,0.000000597		,2.67504048823368E-07])
	#l_cs = np.array([1.60807650725181E-09	,1.87210963492295E-09	,1.91664377603462E-09	,1.63164741211748E-09	,1.07452213861487E-09	,7.75761741587767E-10])

	#l_c  = den_at_dosi*np.array([1.7431320374999997e-05   ,2.3853193244999995e-05   ,2.4923074049999997e-05   ,2.134117692e-05       ,1.0421215874999999e-05   ,5.138528535e-06        ]) # MCNP ENDF
	#l_cs =             np.array([0.0061  		 ,0.0054		   ,0.0054		     ,0.0056		       ,0.0078  		 ,0.0114		   ]) # MCNP ENDF
	
	#l_c  = den_at_dosi*np.array([1.7794243215e-05	 ,2.4109409205e-05	   ,2.5130366099999998e-05   ,2.1871799775000002e-05   ,1.0645927425e-05	 ,5.212611179999999e-06    ]) # MCNP JEFF
	#l_cs =             np.array([0.0061  		 ,0.0053		   ,0.0051		     ,0.0055		       ,0.0079  		 ,0.0116		   ]) # MCNP JEFF
	
	l_c  = den_at_dosi*np.array([1.8016366725e-05	 ,2.4190584075000002e-05   ,2.5501401449999998e-05   ,2.1984279974999996e-05   ,1.070572608e-05 	 ,5.375981204999999e-06    ]) # MCNP JEFF-IRDFF
	l_cs =             np.array([0.0061  		 ,0.0053		   ,0.0052		     ,0.0056		       ,0.0079  		 ,0.0122		   ]) # MCNP JEFF-IRDFF

	l_cs *= l_c
	
	
	# etal        2635.972811830101   (+-15.993150364805787   - 0.6067266814372823  %) MCNP JEFF-IRDFF	(ref)
	# etal        2567.7822852025056  (+-15.636024573614431   - 0.6089310867093747  %) MCNP ENDF            -2.6 %
	# etal        2609.7015297563985  (+-15.750797195035005   - 0.6035478393004298  %) MCNP JEFF            -1.0 %
	# etal        2617.3005776513337  (+-15.686840206001284   - 0.599351879564328   %) SSS  JEFF-IRDFF      -0.7 %
	# 0.0025450390826177328   
	# 0.0025415301617870297

	# etal        2617.269129472117   (+-15.655660461235808   - 0.598167772849307   %) exp 1 # Exp 1 - ref1
	# etal        2627.773957504891   (+-15.93001435417703    - 0.6062170723886315  %) exp 2 # Exp 2 - water lvl
	# etal        2618.98311133       (+-15.3368217991        - 0.58560216493       %) exp 4 # Exp 4 - high T 
	# etal        2606.5641456998815  (+-14.997041582934438   - 0.5753567050201107  %) exp 6 # Exp 6 - ref2

	# etal        2689.25371415919    (+-16.18441666708142    - 0.6018181394291228  %) exp 1 # Exp 1 v2 - 
	# etal        2691.235590881609   (+-15.484242232072795   - 0.5753581100270894  %) exp 4 # Exp 4 v2 - high T
	# etal        2644.6669818110563  (+-14.877429991398031   - 0.5625445507399964  %) exp 7 # Exp 1 v2 - high P
	

i = 0

print (aff_list("l_calcul (sss*den_at)", l_c))
print (aff_list("l_calcul_s [%]",l_cs/l_c*100))


while i < len(l_c):
	if l_c[i]==None: 
		m = l_m[i]
		def rm(l,i):
			l = list(l)
			v=l.pop(i)
			return v,np.array(l)
		m, l_m = rm(l_m,i)
		ms, l_ms = rm(l_ms,i)
		l_c = rm(l_c,i)[1]
		l_cs = rm(l_cs,i)[1]
		l_w = rm(l_w,i)[1]
		l_w_eff = rm(l_w_eff,i)[1]
		l_cp_histo = rm(l_cp_histo,i)[1]
		l_h = rm(l_h,i)[1]
		print (l_name[i],"not found in the calculation, measurment removed", m)
	else:
		i += 1
power_per_src_n, power_per_src_n_s= get_sss_res(calc+"_res.m", "TOT_POWER")




l_path_moni = sorted(filter(lambda s:s[-4:]==".TKA", os.listdir(dir_moni)))
l_path_moni = l_path_moni[-2:]


#l_moni = [None,None]
d_moni = {}
for i_path_moni, path_moni in enumerate(l_path_moni):
	ye,mo,da,ho,mi,se,v = path_moni.split("_")[:7]
	#i_moni = 0 if v=="v1" else 1
	c = c1 if v=="v1" else c2
	if v not in d_moni:
		tmp = Measure(1.,datetime.datetime(*map(lambda s: int(s), [ye,mo,da,ho,mi,se])), dir_moni+"/"+path_moni)
		d_moni[v] = tmp
		tmp.plot(l_ax[0], c, label=r"$\mathrm{monitor~}"+str(i_path_moni+1)+"$")
	else:
		print ("Error - please update the assimilation procedure for monitors")
		exit()
		#print "assimilate",i_moni, path_moni
		#tmp = Measure(1.,datetime.datetime(*map(lambda s: int(s), [ye,mo,da,ho,mi,se])), dir_moni+"/"+path_moni)
		#d_moni[moni].assimile(tmp, l_moni[(i_moni+1)%2], ax=l_ax[0])
		#tmp.plot(l_ax[0], c)
	#print y,mo,d,h,mi,s,v

#l_ax[0].set_ylim([0,42000])

ye,mo,da,ho,mi,se,v = path_moni.split("_")[:7]


# CHOIX MONITEUR
if moni not in d_moni:
	print ("Error - asked monitor: "+moni+"  - list of available monitors: ", " ".join(d_moni.keys()))
	exit()
l_cp_histo = d_moni[moni].propagate_rr(1., half_time, irrad_time, l_hpge_time, l_time_in_hpge, l_name, ax=l_ax[1]) # datetime.datetime(2019, 04, 01, 12, 00, 00), 




def calc_etal(c_i, cp_histo_i, fact_gamma_Au, abs_gamma_Au_i, m_i, talk=False):
	if talk: print ("#"*50, "calculation explanation 1/2: sss rr to count in hpge")
	#if talk: print "calc way"
	if talk: aff_v_s("power per src neutron", power_per_src_n)
	if talk: aff_v_s("rr/nsrc"				  ,c_i)
	if talk: aff_v_s("rr/nsrc / (J/nsrc)      = rr/J"	  ,c_i/power_per_src_n)
	if talk: aff_v_s("(rr/J) * (evtHPGemes*J) = rr evtHPGeMeas" ,c_i/power_per_src_n * (cp_histo_i*fact_gamma_Au*abs_gamma_Au_i))
	if talk: print ("# note: the formula is: c_i/power_per_src_n * (cp_histo_i*fact_gamma_Au*abs_gamma_Au_i)")
	if talk: print ("#       where cp_histo_i is the propagated (sum+decay) monitor history without the calibration factor")
	if talk: print ("#       -> then the ratio with the measurment is directly the calibration factor")
	if talk: print ("#"*50, "calculation explanation 2/2: exp count in hpge")
	if talk: aff_v_s("RealevtHPGe", m_i)
	if talk: print ("#"*50,"(end)")
	return c_i/power_per_src_n * (cp_histo_i*fact_gamma_Au*abs_gamma_Au_i) / m_i


n_sample = int(1e5)

aff_v_s("n_sample for chi2 minimisation", n_sample)


for i in range(len(l_eff_gamma)):
	if l_eff_gamma[i] != l_eff_gamma[0] or l_gamma_inten[i] != l_gamma_inten[0]:
		print ('Error in the uncertainty propagation, please implement the correlation in the efficiency')
		exit()
nd_unc = 0.0101
#nd_unc = 0

sampled_fact_gamma_Au = map(lambda i: gauss(l_eff_gamma[0], l_eff_gamma_s[0])*l_gamma_inten[0], range(n_sample))
sampled_nd_unc_Au     = map(lambda i: gauss(1., nd_unc), range(n_sample))					# from IRDFF unc. propagation
#sampled_fact_gamma_Au = map(lambda i: gauss(eff_gamma_Au, 0.1*eff_gamma_Au)*I_gamma_Au, range(n_sample))


l_sampled_etal = np.zeros((len(l_c),n_sample))

for i in range(len(l_c)):
	for n in range(n_sample):
		etal = calc_etal(
			gauss(l_c[i], l_cs[i]) *sampled_nd_unc_Au[n],
			l_cp_histo[i],
			sampled_fact_gamma_Au[n],
			#gauss(l_eff_gamma[0], 0.1*l_eff_gamma[0]),
			l_abs_gamma_Au[i],
			gauss(l_m[i], l_ms[i]),
			talk=(i==0 and n==0))
		l_sampled_etal[i,n] = etal
	s1 = l_cs[i]/l_c[i]
	s2 = l_ms[i]/l_m[i]
	s3 = l_eff_gamma_s[0]/l_eff_gamma[0]
	if i == 3:
		print ("coucou", s1,s2,s3,0.0101, (s1**2+s2**2+s3**2+nd_unc**2)**0.5)
	aff_v_s("etal",*imoyvar_list(l_sampled_etal[i]))




cov, cor = icovar(l_sampled_etal.T, talk=False)
for i_l, l in enumerate(list(cor)):
	print (aff_list("correlation_matrix:" if i_l==0 else "",l))
print (aff_list("np.diag(correlation_matrix)**0.5",np.diag(cov)**0.5))


#exit()

l_etal_guess = np.array(map(lambda i: imoyvar_list(l_sampled_etal[i])[0], range(len(l_sampled_etal))))
etal_guess, etal_guess_sig = imoyvar_list(l_etal_guess)
etal_guess_sig += etal_guess*0.05



aff_v_s("etal_guess for sampling in 5*sig",		etal_guess, etal_guess_sig)

sampled_guess = map(lambda i: etal_guess+10*etal_guess_sig*(rand()*2-1), range(n_sample))
n = 4
cov = cov[:n, :n]
l_etal_guess = l_etal_guess[:n]

covl_inv = np.linalg.inv(cov)
l_chi2 = map(lambda g: (l_etal_guess-g).T.dot(covl_inv.dot(l_etal_guess-g)), sampled_guess)  
aff_v_s("min(l_chi2)", min(l_chi2))

print ((l_etal_guess-sampled_guess[0]),covl_inv)
print (l_etal_guess,sampled_guess[0])


l_w           = np.exp(-np.array(l_chi2)/2)

print ("#"*50, "CALIBRATION FACTOR:")

aff_v_s("etal", *imoyvar_list(sampled_guess, l_w))




if False:
	rr_per_src = 2.12966e-05 * den_at_dosi
	nrj_per_src = 1.32614e-11
	nrj_released = 10.*3600
	
	rr_per_nrj = rr_per_src/nrj_per_src
	at_created = rr_per_nrj*nrj_released
	at_decay_in_HPGe = at_created * (1-np.exp(-30*60 * np.log(2)/(2.69517*3600*24)))
	at_meas_in_HPGe = 0.00263655004271*at_decay_in_HPGe
	
	
	print()
	print ("rr_per_src      ", rr_per_src)
	print ("rr_per_nrj      ", rr_per_nrj)
	print ("at_created      ", at_created)
	print ("at_decay_in_HPGe", at_decay_in_HPGe)
	
	print ("at_meas_in_HPGe ", at_meas_in_HPGe	)



l_m, l_ms, l_c, l_cs = map(lambda l:l/(l_w_eff/max(l_w_eff)),[l_m, l_ms, l_c, l_cs])			# effective weight correction


l_ax[2].errorbar(l_h, l_m/l_cp_histo, yerr=l_ms/l_cp_histo, c=c1,linewidth=2, fmt='rx', label=r"$\mathrm{measurement}$")
fac = sum((l_m/l_cp_histo)[:4])/sum(l_c[:4])
l_c *= fac
l_cs *= fac


l_ax[2].errorbar(l_h, l_c, yerr=l_cs, c=c2,linewidth=2, fmt='rx', label=r"$\mathrm{calculation}$")

def my_fct(x,a,x0,c):
	return a*np.cos(c*(x-x0))
if True:
	r = -1
	best_p, covar = curve_fit(my_fct, l_h[:r], (l_m/l_cp_histo)[:r], p0=[(l_m/l_cp_histo)[0], 50, np.pi/100], sigma=(l_ms/l_cp_histo)[:r], absolute_sigma=True, maxfev=10000)
else:
	best_p, covar = curve_fit(my_fct, l_h, (l_m/l_cp_histo), p0=[(l_m/l_cp_histo)[0], 50, np.pi/100], sigma=(l_ms/l_cp_histo), absolute_sigma=True, maxfev=10000)
print ("fit param: a*np.cos(c*(x-x0)): a="+str(best_p[0])+" x0="+str(best_p[1])+" c="+str(best_p[2]))


#l_ax[2][0,1].plot(np.arange(0,100,0.1), my_fct(np.arange(0,100,0.1), * best_p),"black")
l_ax[2].plot(np.arange(0,100,0.1), my_fct(np.arange(0,100,0.1), * best_p),"black", linewidth=2)
#l_ax[2].plot(np.arange(0,100,0.1), my_fct(np.arange(0,100,0.1), * [0.01, 50, np.pi/100]),"black")

#l_ax[2][0,1].set_ylim([0,l_ax[2][0,1].get_ylim()[1]])
#l_ax[2][0,1].set_xlim([0,100])
l_ax[2].set_ylim([0,l_ax[2].get_ylim()[1]])
l_ax[2].set_xlim([0,100])

def aff_res(ax, lx, ly1, ly1s, ly2, ly2s, c):
	delta  = ly2-ly1
	deltas = (ly1s**2+ly2s**2)**0.5
	ax.plot(lx,delta/deltas,"x",c=c,alpha=0.4, ms=4, mew=1.5)
	
def aff_res_finalise(ax):
	ax.plot(ax.get_xlim(), [1, 1], "--", c="black", zorder = 6)
	ax.plot(ax.get_xlim(), [-1,-1],"--", c="black", zorder = 6)
	ax.plot(ax.get_xlim(), [2, 2], "--", c="black",alpha=0.4, zorder = 6)
	ax.plot(ax.get_xlim(), [-2,-2],"--", c="black",alpha=0.4, zorder = 6)



l_ax[0].set_xlabel(r"$\mathrm{Time~[h]}$", size=get_aff_size("s_xylabel"))
l_ax[0].set_ylabel(r"$\mathrm{Counts~[s^{-1}]}$", size=get_aff_size("s_xylabel"))
l_ax[0].tick_params(axis='both', which='both', labelsize=get_aff_size("s_tick"))
l_ax[0].set_title(r"$\mathrm{Fission~chamber~monitors}$", fontsize=get_aff_size("s_leg"))
l_ax[0].legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)

l_ax[1].set_xlabel(r"$\mathrm{Time~[h]}$", size=get_aff_size("s_xylabel"))
l_ax[1].set_ylabel(r"$\mathrm{Cumulated~counts~[counts]}$", size=get_aff_size("s_xylabel"))
l_ax[1].tick_params(axis='both', which='both', labelsize=get_aff_size("s_tick"))
l_ax[1].set_title(r"$\mathrm{Integral~weighted~by~Au~decay}$", fontsize=get_aff_size("s_leg")*0.8)
#l_ax[0].legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)

l_ax[2].set_xlabel(r"$\mathrm{Position~[cm]}$", size=get_aff_size("s_xylabel"))
l_ax[2].set_ylabel(r"$\mathrm{Reaction~rate~[a.u.]}$", size=get_aff_size("s_xylabel"))
l_ax[2].tick_params(axis='both', which='both', labelsize=get_aff_size("s_tick"))
l_ax[2].set_title(r"$\mathrm{Reaction~rate~shape}$", fontsize=get_aff_size("s_leg"))
l_ax[2].legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)

fig.savefig("propag6.jpg", bbox_inches=('tight'), dpi=200)
plt.show()


