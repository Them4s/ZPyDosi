
from utils_p3 import *
import multiprocessing as mp
def aff(v,l=22):
	return str(v)+(l-len(str(v)))*" "

sys.setrecursionlimit(10000)

path_optim = "optim/input.txt"
path_param = "optim/param.txt"
def get_param_optim(param):
	lines = open(path_param).readlines()
	for line in lines:
		if len(line.split())>0 and line.split()[0] == param:
			return line.split()[1]
	return None

path_csv_meas = get_param_optim("csv_meas")
path_csv_dosi = get_param_optim("csv_dosi")
l_case_todo   = get_param_optim("l_case_todo")

time_cst     = float(get_param_optim("time_max_convergence"))
act_max_manu = float(get_param_optim("activity_max"))
cool_min     = float(get_param_optim("cooling_after_irrad"))/60
nb_day_max   = int(get_param_optim("nb_day_allowed"))

l_forbidden_day = get_param_optim("l_forbidden_day")

dose_max_cavity   = float(get_param_optim("dose_max_cavity_roof"))


data = []

l_pos   = []
l_thpge = []


mode_ordre_date    = True 	# False
stop_direct        = False	# False
no_optim_copy	    = False	# False
mode_raz           = False	# False

start_with_plot    = True	# True
aff_as_interpreted = False	# False


ratio_aleat = 0.5 			# 1

l_key_auto = None
#l_key_auto = ["Fe-Pss","Fe-Pfe", "Ni-Pss","Ni-Pcr"]
#l_key_auto = ["Ni-Pni","Ni-Pcr"]
#l_key_auto = ["Ni-Pcr-7"]

rm_time_all = 20/60 * 0

dt_print 	= 10	# 10

conv_critere = 0.999

nb_thread = 16

nb_hpge = 4
dt_manutention = 0/60
delay_hpge_change = 5/60
dt_optim_min = 5/60
nb_per_max = 5

malus = 1e9

h_begin_day = 8
h_end_day   = 19
h_per_day = h_end_day-h_begin_day



#path_csv_file_to_optimize = lines.pop(0)[:-1]
path_csv_file_to_optimize = path_csv_meas

path_csv_file_to_optimize_old = path_csv_file_to_optimize
mode_xlsx = ".xlsx" in path_csv_file_to_optimize
if not mode_xlsx:
	path_csv_file_to_optimize = path_csv_file_to_optimize.replace(".csv","_optim.csv")
else:
	path_csv_file_to_optimize = path_csv_file_to_optimize.replace(".xlsx","_optim.xlsx")




path_save      = get_param_vari("path_save", str, "expected_act_out", aff=False)
name_save      = get_param_vari("name_save", str, "auto_time", aff=False)
if __name__ == "__main__":
	if not no_optim_copy:
		#open(path_csv_file_to_optimize,"w").write("".join(open(path_csv_file_to_optimize_old).readlines()))
		ExcelSheet(path_csv_file_to_optimize_old).save(path_csv_file_to_optimize)
	now = datetime.datetime.now()
	date_in_str_pr_save_img = "optim/"+str(now).split(".")[0].replace("-","_").replace(":","_").replace(" ","_")
	os.mkdir(date_in_str_pr_save_img)


nro_plot = 0

ll_time_and_val_for_plot = []

def do_plot(do_not_block=True):
	global nro_plot, ll_time_and_val_for_plot
	print("do plot")
	if len(ll_time_and_val_for_plot)>0:
		mini = ll_time_and_val_for_plot[0][1][0]
		fig = plt.figure(1, figsize=(8,5))							# object for plot
		fig.patch.set_facecolor('white')
		ax = plt.subplot(1,1,1)
		for i,(l_t_l_v) in enumerate(ll_time_and_val_for_plot):
			l_t, l_v = l_t_l_v
			mini = min(mini, min(l_v))
			c=get_c(i, len(ll_time_and_val_for_plot))
			ax.plot(l_t, l_v, c=c, linewidth=1)
			ax.plot(l_t[-3:], l_v[-3:],"x", c=c, linewidth=1)
		#plt.show()
		#exit()
		ax.set_yscale('log')
		ax.set_ylim([mini*0.98, mini*5])
		ax.set_xlabel(r"$\mathrm{Time~[s]}$",	size=12)
		ax.set_ylabel(r"$\mathrm{Grade~[a.u.]}$",	size=12)
		fig.savefig(date_in_str_pr_save_img+"/conv.png", dpi=200)
		plt.close(fig)
	#bash_command  = "python /Users/axellaureau/data/python/irrad/expected_act15.py"
	bash_command  = ["python3.8"]
	bash_command += ["$petale_analysis/python/irrad/expected_act17.py"]
	bash_command += ["csv_data="+path_csv_file_to_optimize]
	bash_command += ["csv_dosi="+path_csv_dosi]
	bash_command += ["lcase="+l_case_todo]
	bash_command += ["path_save="+date_in_str_pr_save_img]
	bash_command += ["name_save="+str(nro_plot)]
	#bash_command += " no_save="+str(not do_not_block)
	bash_command += ["serv=1",">","log_plot"]
	#process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
	#output, error = process.communicate()
	print(" ".join(bash_command[:-2]))
	bash_command[1] = os.path.expandvars(bash_command[1])
	sub = subprocess.Popen(bash_command, shell=False, stdout=subprocess.DEVNULL) # ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
	if not do_not_block:
		sub.communicate()
	nro_plot += 1
	

if __name__ == "__main__":
	if start_with_plot:
		do_plot(False)

#exit()










lines   = open(path_optim).readlines()
raw = lines.pop(0).replace("-"," ").replace(":"," ").split()[1:]
l_irradiation = []
while len(raw)>0:
	l_irradiation += [(	float(raw.pop(0)), # puiss
				float(raw.pop(0)), # duree
				datetime.datetime(*lmap(lambda i: int(raw.pop(0)), range(6))))] # date
#print (l_irradiation)


id_date = lines.pop(0).split().index("date_min")
date_min = sorted(map(lambda l: l.split()[id_date],filter(lambda l: len(l)>1,lines)))[0]

#print(date_min)
#exit()

s_date    = date_min

d0 = datetime.datetime(*map(lambda s : int(s), s_date.split("_"))).replace(hour=0, minute=0, second=0)
day = d0.replace(hour=0)


fct_activity = gen_dose_rate_fct(l_irradiation,d0, pos="lid_attente")


l_interval_autorise = []

t_hours_autorise = np.zeros(24*nb_day_max)

for d in range(nb_day_max):
	is_a_forbidden_day = str(day).split()[0].replace("-","_") in l_forbidden_day.split("/")
	if not is_a_forbidden_day and day.weekday() < 5:
		i_hour = int((day-d0).total_seconds()/3600)
		t_hours_autorise[i_hour+h_begin_day:i_hour+h_end_day] = np.ones(h_per_day)
	day += datetime.timedelta(days = 1)

do=True


if __name__ == "__main__":
	for i in range(len(t_hours_autorise)):
		if i%24 == 0:
			print()
			print(aff(i),end="")
		print(str(t_hours_autorise[i]),end=" ")


prog_meas = []
l_key = []
l_act = []
l_eff = []
l_lambda_decay = []
l_date_min = []
l_pos_hpge = []
l_id_hpge = []
l_found_id_hpge = []
l_date_hpge = []
l_order_meas_in = []
l_case_in_csv = []
#d_twins = {}
d_ltwins = {}
d_ltwini = {}
def add_twin(d,k1,k2):
	if k1 not in d: d[k1] = []
	if k2 not in d: d[k2] = []
	d[k1] += [k2]
	d[k2] += [k1]

	

for il, l in enumerate(open(path_optim).readlines()[2:]):
	if l == "\n":
		break
	case_in_csv, key, act, eff, lambda_decay, date_min, pos_hpge, id_hpge, date_hpge, time_in_hpge_s, order_in = l.split()
	act, eff, lambda_decay, time_in_hpge_s, order_in = map(lambda s:float(s), [act, eff, lambda_decay, time_in_hpge_s, order_in])
	
	if id_hpge not in l_found_id_hpge:
		l_found_id_hpge += [id_hpge]
	date_in_hpge = (datetime.datetime(*map(lambda s : int(s), date_hpge.split("_")))-d0).total_seconds()/3600
	
	for itmp, tmp_key in enumerate(l_key):
		if mode_ordre_date and False:
			test_date = date_in_hpge == l_date_hpge[itmp]
		else:
			test_date = order_in == l_order_meas_in[itmp]
		if key == tmp_key: # and test_date and l_found_id_hpge.index(id_hpge) == l_id_hpge[itmp] and pos_hpge==l_pos_hpge[itmp]:
			#d_twins[il] = itmp
			#d_twins[itmp] = il
			if test_date and l_found_id_hpge.index(id_hpge) == l_id_hpge[itmp] and pos_hpge==l_pos_hpge[itmp]:
				add_twin(d_ltwins,il, itmp)
			else:
				add_twin(d_ltwini,il, itmp)
			#if __name__ == "__main__":
			#	print("find twin:",il, itmp,key,date_in_hpge, l_date_hpge[itmp],l_found_id_hpge.index(id_hpge),pos_hpge)
	l_case_in_csv += [case_in_csv]
	l_order_meas_in += [order_in]
	l_key += [key]
	l_act += [act]
	l_eff += [eff]
	l_lambda_decay += [lambda_decay]
	l_date_min += [(datetime.datetime(*map(lambda s : int(s), date_min.split("_")))-d0).total_seconds()/3600]
	l_pos_hpge += [pos_hpge]
	l_id_hpge += [l_found_id_hpge.index(id_hpge)]
	l_date_hpge += [date_in_hpge]
	prog_meas += [(time_in_hpge_s)/3600]

l_ordre = list(map(lambda i_t:i_t[0], sorted(enumerate(l_order_meas_in), key=lambda i_t:i_t[1])))
if mode_ordre_date:
	prog_meas = list(map(lambda d:d, prog_meas))
else:
	prog_meas = list(map(lambda d:5/60, prog_meas))

if __name__ == "__main__":
	print()
	print(d_ltwins)
	print(d_ltwini)
	print()
	#print(l_key[42])
	#print(d_ltwini[42])
	print("l_ordre  ", l_ordre)
	
	
prog_meas = np.array(prog_meas)

l_nro2nronxt = [None for i in range(len(prog_meas))]
for id_nroi, nroi in list(enumerate(l_ordre)):
	for id_nroj, nroj in list(enumerate(l_ordre))[id_nroi+1:]:
		if l_id_hpge[nroi] == l_id_hpge[nroj] and (nroi not in d_ltwins or nroj not in d_ltwins[nroi]):
			l_nro2nronxt[nroi] = nroj
			break

l_nro2nroprv = [None for i in range(len(l_nro2nronxt))]
for i,n in enumerate(l_nro2nronxt):
	if n is not None:
		l_nro2nroprv[n] = i
		if n in d_ltwins:
			for j in d_ltwins[n]:
				l_nro2nroprv[j] = i
				
l_nro2nronxt2 = [None for i in range(len(prog_meas))]
for i,n in enumerate(l_nro2nronxt):
	if (n is not None):
		l_nro2nronxt2[i] = l_nro2nronxt[n]

l_nro2nronxt3 = [None for i in range(len(prog_meas))]
for i,n in enumerate(l_nro2nronxt2):
	if (n is not None):
		l_nro2nronxt3[i] = l_nro2nronxt[n]


def eval_prog(prog_meas, print_meas=False, give_prog_detail=False):
	note = 0
	l_t_hpge = [0] * nb_hpge
	if print_meas:
		l_txt = [""]*len(l_ordre)
	if give_prog_detail:
		prog_detail = [""]*len(l_ordre)
	d_date_mesure_twin = {}
	d_date_mesure = {}
	l_date_mesure = []
	d_dosi_2_periode ={}
	for inro, nro in enumerate(l_ordre):
		temps_mesure = prog_meas[nro]
		if nro in d_date_mesure_twin:
			date_mesure = d_date_mesure_twin[nro]
		else:
			
			if l_t_hpge[l_id_hpge[nro]]<l_date_min[nro] + cool_min:
				l_t_hpge[l_id_hpge[nro]] = l_date_min[nro] + cool_min
			
			key = l_key[nro]
			
			while act_max_manu < l_act[nro]*np.exp(-l_lambda_decay[nro]*(l_t_hpge[l_id_hpge[nro]]-l_date_min[nro])*3600):
				l_t_hpge[l_id_hpge[nro]] += 5/60
			
			tmp = lmap(lambda irr: abs((irr[2]-d0).total_seconds()/3600-l_date_min[nro]),l_irradiation)
			nro_min_date_min = tmp.index(min(tmp))
			tmp = lmap(lambda irr: abs((irr[2]-d0).total_seconds()/3600-l_t_hpge[l_id_hpge[nro]]),l_irradiation)
			nro_min_date_irr = tmp.index(min(tmp))
			if nro_min_date_irr == nro_min_date_min:
				ajoute = False
				#if dose_max_cavity < fct_activity([l_t_hpge[l_id_hpge[nro]]*3600])[0]:
				#	while dose_max_cavity < fct_activity([l_t_hpge[l_id_hpge[nro]]*3600])[0]:
				#		l_t_hpge[l_id_hpge[nro]] += 5/60
				#		ajoute = True
				#	l_t_hpge[l_id_hpge[nro]] += cool_min
				#	print("pass ajoute 1 decay",key, fct_activity([l_t_hpge[l_id_hpge[nro]]*3600 - cool_min*3600])[0])
				if dose_max_cavity < fct_activity([l_t_hpge[l_id_hpge[nro]]*3600 - cool_min*3600])[0]:
					while dose_max_cavity > fct_activity([l_t_hpge[l_id_hpge[nro]]*3600])[0]:
						#print("-",key)
						l_t_hpge[l_id_hpge[nro]] -= 5/60
					while dose_max_cavity < fct_activity([l_t_hpge[l_id_hpge[nro]]*3600])[0]:
						#print("+",key)
						l_t_hpge[l_id_hpge[nro]] += 5/60
					l_t_hpge[l_id_hpge[nro]] += cool_min
					#print("pass ajoute 2 decay",key, fct_activity([l_t_hpge[l_id_hpge[nro]]*3600 - cool_min*3600])[0])
			
			'''
			ajoute = False
			while dose_max_cavity < fct_activity([l_t_hpge[l_id_hpge[nro]]*3600])[0]:
				tmp = lmap(lambda irr: abs((irr[2]-d0).total_seconds()/3600-l_date_min[nro]),l_irradiation)
				nro_min_date_min = tmp.index(min(tmp))
				tmp = lmap(lambda irr: abs((irr[2]-d0).total_seconds()/3600-l_t_hpge[l_id_hpge[nro]]),l_irradiation)
				nro_min_date_irr = tmp.index(min(tmp))
				if nro_min_date_irr != nro_min_date_min:
					break
				l_t_hpge[l_id_hpge[nro]] += 5/60
				ajoute = True
			if ajoute:
				l_t_hpge[l_id_hpge[nro]] += cool_min
				print("pass ajoute 1 decay",key, fct_activity([l_t_hpge[l_id_hpge[nro]]*3600 - cool_min*3600])[0])
			elif nro_min_date_irr == nro_min_date_min and dose_max_cavity < fct_activity([l_t_hpge[l_id_hpge[nro]]*3600 - cool_min*3600])[0]:
				while dose_max_cavity > fct_activity([l_t_hpge[l_id_hpge[nro]]*3600])[0]:
					l_t_hpge[l_id_hpge[nro]] -= 5/60
				l_t_hpge[l_id_hpge[nro]] += cool_min + 5/60
				print("pass ajoute 2 decay",key, fct_activity([l_t_hpge[l_id_hpge[nro]]*3600 - cool_min*3600])[0])
			
			'''
			'''
			elif nro_min_date_irr == nro_min_date_min and dose_max_cavity < fct_activity([l_t_hpge[l_id_hpge[nro]]*3600 - cool_min*3600])[0]:
				print("pass ajoute decay",key)
				while dose_max_cavity > fct_activity([l_t_hpge[l_id_hpge[nro]]*3600])[0]:
					l_t_hpge[l_id_hpge[nro]] -= 5/60
				l_t_hpge[l_id_hpge[nro]] += cool_min + 5/60
			'''
			ok_global = False
			while not ok_global:
				ok_global = True

				if key in d_dosi_2_periode:
						change = True
						while change:
							change = False
							date_mesure = l_t_hpge[l_id_hpge[nro]]
							for date_other, time_meas_other in d_dosi_2_periode[key]:
								test1 = date_other-1/60<=date_mesure<=date_other+time_meas_other+1/60
								test2 = date_mesure-1/60<=date_other and date_other+time_meas_other-1/60<=date_mesure+temps_mesure
								test3 = date_other-1/60<=date_mesure+temps_mesure<=date_other+time_meas_other+1/60
	
								if test1 or test2 or test3:
									l_t_hpge[l_id_hpge[nro]] += 5/60
									ok_global = False
									change = True
				
				nro_hm = int(l_t_hpge[l_id_hpge[nro]]-1/60)
				nro_hp = int(l_t_hpge[l_id_hpge[nro]]+1/60)
				nro_h = nro_hp if (nro_hp<len(t_hours_autorise) and t_hours_autorise[nro_hp]==1) else nro_hp
				
				while nro_h<len(t_hours_autorise) and t_hours_autorise[nro_h]==0:
					#nro_h += 1
					l_t_hpge[l_id_hpge[nro]] = int(l_t_hpge[l_id_hpge[nro]]+1)
					nro_h = int(l_t_hpge[l_id_hpge[nro]])
					ok_global = False
				
				if nro_hm >= len(t_hours_autorise):
					date_mesure = None
					if print_meas:
						l_txt[nro] += key+" "+str(nro_hp)+" - "
				else:
					date_mesure = l_t_hpge[l_id_hpge[nro]]
				
			if nro in d_ltwins:
				for k2 in d_ltwins[nro]:
					d_date_mesure_twin[k2] = date_mesure
			
			#if do_print:
			#	print("fin", date_mesure)
			
			l_t_hpge[l_id_hpge[nro]] += temps_mesure+delay_hpge_change
			
			
		if date_mesure is not None:
			if key not in d_dosi_2_periode: d_dosi_2_periode[key] = []
			d_dosi_2_periode[key] += [(date_mesure ,temps_mesure)]
			
			act0 = l_act[nro]
			decay_cool = np.exp(-l_lambda_decay[nro]*(date_mesure-l_date_min[nro])*3600)
			hpge_decay = 1/l_lambda_decay[nro] * (1-np.exp(-l_lambda_decay[nro]*temps_mesure*3600))
			count = act0*decay_cool*hpge_decay*l_eff[nro]
			sup_note = 0
			if count<200000:
				sup_note = (20000/(count+1))**2
			else:
				sup_note = (20000/(200000+1))**2 + count/200000
			note += sup_note
			if print_meas and sup_note > 1000:
				print(key, count, sup_note)
			l_date_mesure += [date_mesure]
			d_date_mesure[nro] = (date_mesure,date_mesure+temps_mesure)
			if print_meas or give_prog_detail:
				d_meas = d0+datetime.timedelta(hours = date_mesure)
				d_meas = str(d_meas).replace("-","_").replace(":","_")
				t_meas = str(round(temps_mesure*60))+"m"
				if print_meas:
					l_txt[nro] += aff(l_key[nro])+aff(act0)+aff(date_mesure)+aff(decay_cool)+aff(act0*decay_cool)+aff(count)+d_meas+" "+aff(t_meas)
				if give_prog_detail:
					prog_detail[nro] = d_meas+" "+t_meas
			if (date_mesure + temps_mesure)/24 > nb_day_max:
				if print_meas:
					print("malus "+key+" pas fini...")
					l_txt[nro] += " pas_fini"
				note += malus
			t_halflife = np.log(2)/l_lambda_decay[nro]
			if temps_mesure*3600 > t_halflife * nb_per_max:
				if print_meas:
					print("malus "+key+" de mesure trop longue...")
					l_txt[nro] += " tp_long "+str(temps_mesure*3600 )+" vs "+str(t_halflife * nb_per_max)
				note += malus
			if nro in d_ltwini:
				for nroi in d_ltwini[nro]:
					if nroi in d_date_mesure:
						test1 = (date_mesure < d_date_mesure[nroi][0]) and (date_mesure+temps_mesure > d_date_mesure[nroi][0])
						test2 = (date_mesure < d_date_mesure[nroi][1]) and (date_mesure+temps_mesure > d_date_mesure[nroi][1])
						if test1 or test2:
							if print_meas:
								print("malus "+key+" de jumeaux mal places...")
								l_txt[nro] += " jumeau_pas_ok"
							note += malus
		else:
			if print_meas:
				l_txt[nro] += str(nro)+" is None..."
				print("malus "+key+" de date non definie...")
			note += malus
		
		
		
	l_date_mesure = np.array(sorted(set(l_date_mesure)))
	note *= 1 +0.01*len(list(filter(lambda v:v==True, (l_date_mesure[1:]-l_date_mesure[:-1])<dt_manutention)))

	if print_meas:
			
		txt  = "#"*100 + "\n"
		txt += aff("key")+aff("act")+aff("t_hpge")+aff("decay")+aff("act_hpge")+aff("count")+aff("y_m_d", 11)+aff("h_m_s",8)+aff("t_mesure [m]") + "\n"
		for inro, nro in enumerate(l_ordre):
			if inro>1 and l_date_min[inro] != l_date_min[inro-1]:
				txt += "\n"
			txt += l_txt[inro]+"\n"
			
		txt += str(note)
		print(txt)
	return note if not give_prog_detail else prog_detail
	
def pos_ok(pos):
	if l_key_auto is None or len(l_key_auto) == 0:
		return True
	for k in l_key_auto:
		if l_key[pos].startswith(k):
			return True
	return False

def rand():
	return np.random.random()

def rand_pos():
	pos = int(np.random.random() * len(prog_meas))
	return pos if pos_ok(pos) else rand_pos()

def prob(p):
	return np.random.random()<p

def rand_prop():
	if rand()<0.5:
		return 0
	return 1+int(rand()*3) # 0,1,2,3

def mute(prog, specific=None):
	prog = prog*1
	def do_a_mutation(i, vari, propagate):
		prog[i] += vari
		propagated = False
		
		if propagate==-1: l_nro2nro_to_use = l_nro2nroprv
		if propagate== 1: l_nro2nro_to_use = l_nro2nronxt
		if propagate== 2: l_nro2nro_to_use = l_nro2nronxt2
		if propagate== 3: l_nro2nro_to_use = l_nro2nronxt3
		
		if propagate!=0 and (l_nro2nro_to_use[i] is not None) and prog[l_nro2nro_to_use[i]]>vari:
			prog[l_nro2nro_to_use[i]] -= vari
			propagated = True
			
		if prog[i] <= 5/60:
				prog[i] = 5/60
		if i in d_ltwins:
			for k2 in d_ltwins[i]:
				prog[k2] = prog[i]
	
		if propagated and (l_nro2nro_to_use[i]) in d_ltwins:
			for k2 in d_ltwins[l_nro2nro_to_use[i]]:
				prog[k2] = prog[l_nro2nro_to_use[i]]
	
	if specific is not None:
		i, var, prop = specific
		do_a_mutation(i, var, prop)
	else:
		prob_var = rand()
		amp_var  = int(1+rand()*20)
		if rand()<0.25:
			amp_var = 60/5 * (12*rand())
		if rand()<0.25:
			amp_var = 60/5 * (3*24*rand())
		for i in range(len(prog)):
			var = int(rand()*(amp_var*2+2)-amp_var) * dt_optim_min
			if prob(prob_var):
				do_a_mutation(rand_pos(), var, rand_prop())
	return prog




def save_res_in_csv(prog_res, path_out):

	print("saving results in", path_out)
	'''lines = open(path_out).readlines()
	if   ";" in lines[0]: sep = ";"
	elif "," in lines[0]: sep = ","
	else:
		print("error, csv separator not recognized... -> <",lines[0][:-1],">")
		exit()'''
	prog_detail = eval_prog(prog_res, give_prog_detail=True)

	
	sheet = ExcelSheet(path_out)

	prev_case = ""
	i = 0
	
	for nro,case in enumerate(l_case_in_csv):
		if case != prev_case:
			i = 0
			while sheet.get(i,0) != case:         i += 1
			while sheet.get(i,0) != "dosimeters": i += 1
			def found_j(s):
				j = 0
				while sheet.get(i,j) != s and j<1000: j += 1
				if j == 1000:
					print("Error - found_j - <"+s+"> not in line...",)
				return j
			#id_y_m_d,id_h_m_s,id_t_mesure = map(lambda s: lines[i].split(sep).index(s), ["y_m_d","h_m_s","time_in_hpge"])
			id_y_m_d,id_h_m_s,id_t_mesure = map(lambda s: found_j(s), ["y_m_d","h_m_s","time_in_hpge"])
			i += 1
			prev_case = case
		#new_line_words = lines[i].split(",")
		sheet.set(i,id_y_m_d, prog_detail[nro].split()[0])
		sheet.set(i,id_h_m_s, prog_detail[nro].split()[1].split(".")[0])
		sheet.set(i,id_t_mesure, prog_detail[nro].split()[2])
		#lines[i] = sep.join(new_line_words)
		i += 1
	sheet.save(path_out)
	#open(path_out,"w").write("".join(lines))
	#print("...done")
	#print("".join(lines))
	#exit()



def gen_serie(seed, shared_prog, shared_eval,nb_try, small_var, stop, id_pos, id_prop, id_sens):
	#path_pid_file = "optim/pid/"+str(os.getpid())+"_genseries"
	#open(path_pid_file, "w").write("hello")
	#exit()
	np.random.seed(seed)
	tmp_best_prog = np.array(shared_prog) * 1.
	tmp_best_eval = shared_eval.value
	last_get_grade = tmp_best_eval
	i = 0
	def get():
		global last_get_grade, tmp_best_eval
		#print("get",seed)
		for i in range(len(shared_prog)):
			tmp_best_prog[i] = shared_prog[i]
		tmp_best_eval  = shared_eval.value
		last_get_grade = shared_eval.value
	def send():
		#if prob(0.1):
		#	return
		#print("send",seed)
		for i in range(len(shared_prog)):
			shared_prog[i] = tmp_best_prog[i]
		shared_eval.value = tmp_best_eval
	get()
	#print("->",seed, id_pos)
	
	while stop.value == 0 :
		#if tmp_best_eval  < shared_eval.value*1.00:
		#	print("send", tmp_best_eval)
		#	send()
		if tmp_best_eval  > shared_eval.value:
			#print("get", tmp_best_eval)
			get()
		vari_jour = 24-h_per_day+1
		if id_pos<0:
			if prob(0.75):
				if prob(0.75):
					vari = dt_optim_min
				else:
					vari = dt_optim_min * 2**(1+int(rand()*10))
			else:
				if prob(0.75):
					vari = vari_jour
					if prob(0.25): vari += (24*2)
				else:
					vari = 24
			if prob(0.5): vari = -vari
			pos = rand_pos()
			prop = rand_prop()
		else:
			pos  = id_pos
			prop = id_prop
			vari = 5/60*id_sens
			id_pos += 1
			#print(id_pos)
			if id_pos >= len(tmp_best_prog):
				id_pos = 0
		good = True
		i = 0
		lock = False
		while good:
			prog_challenger  = mute(tmp_best_prog*1., (pos ,vari, prop))
			grade_challenger = eval_prog(prog_challenger)
			nb_try.value += 1
			if grade_challenger < tmp_best_eval:
				if not lock:
					vari *= 2
					#if seed==0:
					#	print(seed, "*+2", vari, tmp_best_eval, grade_challenger, prog_challenger[pos], pos)
			else:
				if 5/60 < abs(vari):
					vari /= -2
					lock = True
					#if seed==0:
					#	print(seed, "/-2", vari, tmp_best_eval, grade_challenger, prog_challenger[pos], pos)
				else:
					#if seed==0:
					#	print("goooood", tmp_best_eval, grade_challenger, prog_challenger[pos], pos)
					good = False
			if good:
				tmp_best_eval = grade_challenger
				tmp_best_prog = prog_challenger
			i += 1
		if tmp_best_eval  < shared_eval.value*1.00:
			#print("send", tmp_best_eval)
			send()
		'''
		while good:
			prog_challenger  = mute(tmp_best_prog*1., (pos ,vari, prop))
			grade_challenger = eval_prog(prog_challenger)
			nb_try.value += 1
			if grade_challenger < tmp_best_eval:
				tmp_best_eval = grade_challenger
				tmp_best_prog = prog_challenger
				vari *= 4
			else:
				if 5/60 < abs(vari) < vari_jour:
					vari /= 4
				else:
					good = False
			i += 1
		'''
		#if i>1:
		#print(len(tmp_best_prog))
		#print(" "*50,tmp_best_prog[61], i, vari)
		#exit()
	#os.remove(path_pid_file)

#prog_meas[61]= 14
#print(l_key[61])
#print(prog_meas[61])
#exit()


def combin_prog(l1,l2):
	l1,l2 = np.array(l1), np.array(l2)
	ll_combin = []
	l_combin = []
	in_comb = False
	optim_prog = l1 if eval_prog(l1) < eval_prog(l2) else l2
	optim_grad = eval_prog(optim_prog)
	for id_hpge in set(l_id_hpge):
		for iordre, ordre in enumerate(l_ordre):
			if l_id_hpge[ordre] == id_hpge:
				if abs(l1[ordre]-l2[ordre])<1/60:
					if in_comb:
						ll_combin += [l_combin]
						l_combin = []
						in_comb = False
				else:
					in_comb = True
					l_combin += [ordre]
	for l_combin in ll_combin:
		def add(i=0):
			if i == len(comb):
				return
			if comb[i] == 0:
				comb[i] = 1
			else:
				comb[i] = 0
				add(i+1)
		if 1<len(l_combin)<11:
			comb = [0]*len(l_combin)
			l_todo = []
			for i in range(2**len(l_combin)-2):
				add()
				l_todo += [tuple(comb)]
			def comb2prog(comb):
				tmp_prog = optim_prog * 1.
				for ipos, pos in enumerate(l_combin):
					tmp_prog[pos] = l1[pos] if comb[ipos] == 0 else l2[pos]
					if pos in d_ltwins:
						for pos2 in d_ltwins[pos]:
							tmp_prog[pos2] = tmp_prog[pos]
				return tmp_prog
			def comb2grade(comb):
				return eval_prog(comb2prog(comb))
			l_comb_grade = pool.map(eval_prog, map(lambda comb: comb2prog(comb), l_todo))
			best_comb_pos = l_comb_grade.index(min(l_comb_grade))
			tmp_prog = comb2prog(l_todo[best_comb_pos])
			tmp_grad = eval_prog(tmp_prog)
			if tmp_grad < optim_grad:
				optim_prog = tmp_prog
				optim_grad = tmp_grad
	return optim_prog

aff_inter = False
def compute_a_local_optimim(prog_initial, talk=True, tmax = time_cst):
	global ll_time_and_val_for_plot
	prog_initial = prog_initial * 1
	shared_prog    = mp.Array("d", prog_initial * 1.)
	shared_grad    = mp.Value("d", eval_prog(shared_prog))
	last_best_grade = shared_grad.value
	
	shared_nb_try  = mp.Value("d", 0)
	shared_stoooop = mp.Value("d", 0)
	
	l_p = []
	for i in range(nb_thread):
		if rand()<ratio_aleat:
			id_pos, id_sens, id_prop  = -1, None, None
		else:
			id_sens = -1 if rand()<0.5 else 1
			id_pos  =  int(len(shared_prog)*rand())
			id_prop =  0 if i>(nb_thread/2) else 1
			#print(id_sens, id_pos, id_prop) # 105
			#id_pos = 105
			#id_sens = 1
			#id_prop = 0
		p = mp.Process(target=gen_serie, args=(i, shared_prog, shared_grad,shared_nb_try, False, shared_stoooop, id_pos, id_prop, id_sens))
		p.start()
		l_p += [p]
	
	time_since_best = time.time()
	time_begining = time.time()
	iter = 0
	l_last_grad = []
	l_time_for_plot = []
	l_val_for_plot  = []
	dt = 1.
	t0 = time.time()
	while True:
		time.sleep(dt)
		l_time_for_plot += [time.time()-t0]
		l_val_for_plot  += [shared_grad.value]
		#print("pass")
		if os.path.isfile("optim/stop"):
			print("                                   stop file")
			shared_stoooop.value = 1
			return None
		new_prog = np.array(shared_prog)
		new_res  = eval_prog(shared_prog, print_meas=aff_inter)
		if talk and iter%dt_print == 0:
			print("->",shared_grad.value)
		if shared_grad.value < last_best_grade:
			last_best_grade = shared_grad.value
			time_since_best  = time.time()

		if tmax > 0:
			stop = time.time() - time_begining > time_cst
		else:
			stop = False
			l_last_grad += [shared_grad.value]
			if len(l_last_grad)>30:
				val = l_last_grad.pop(0)
				if val*conv_critere<shared_grad.value:
					stop = True
		if stop:
			shared_stoooop.value = 1
			while len(l_p)>0:
				l_p.pop(0).join()
			if talk:
				ll_time_and_val_for_plot += [[l_time_for_plot, l_val_for_plot]]
			new_prog = np.array(shared_prog)
			new_res  = eval_prog(shared_prog, print_meas=aff_inter)
			return new_prog
		iter += 1
	



for i in range(len(prog_meas)):
	prog_meas[i] = max(5./60, prog_meas[i]-rm_time_all)


best = (prog_meas * 1, eval_prog(prog_meas, print_meas=(__name__ == "__main__")))

if False:
	dt, dj = 5/60, 24-h_per_day+1
	idx = 0
	print("modif a la main pr test")
	print(eval_prog(prog_meas, print_meas=False))
	while l_key[idx] != "Ni-Pcr-4": # or l_id_hpge[idx] != 0:
		idx += 1
	print(idx)
	print(prog_meas[idx], prog_meas[idx], prog_meas[idx]*60)
	prog_meas = mute(np.array(prog_meas), (idx ,dt*(12*3), 0)) # dt_optim_min * 2**(1+int(rand()*10))
	print(eval_prog(prog_meas, print_meas=False))
	
	print(prog_meas[idx], prog_meas[idx], prog_meas[idx]*60)
	
	save_res_in_csv(np.array(prog_meas), path_csv_file_to_optimize)
	do_plot(False)
	
	exit()

if stop_direct:
	exit()
nb = 5000000

last_grade_printed = best[1]
last_grade_print_time = time.time()

#exit()



if __name__ == "__main__":

	print("ckeck pos ok")
	for i in range(10):
		print("ok", l_key[rand_pos()]) # l_key[l_nro2nronxt3[rand_pos()]]
		
	#do_plot(False)
	pool = mp.Pool(mp.cpu_count())
	l_final = []
	l_tps = []
	
	
	best_of_the_best  = prog_meas * 1.
	
	time_start_calc = time.time()
	time_last_conve = time.time()
	
	
	eval_prog(best_of_the_best)
	save_res_in_csv(np.array(best_of_the_best), path_csv_file_to_optimize)
	do_plot(False)
	if aff_as_interpreted:
		exit()
	
	while True:
		print("#"*100)
		old_res = eval_prog(best_of_the_best)
		if mode_raz :
			new_local_optimum = compute_a_local_optimim(prog_meas*0+5/60)
		else:
			new_local_optimum = compute_a_local_optimim(prog_meas*1.)
			#new_local_optimum = compute_a_local_optimim(best_of_the_best*1.)
		if new_local_optimum is None:
			#pool.close()
			#pool.join()
			#os.remove(path_pid_file)
			#exit()
			break
		print()
		print("find     ",eval_prog(new_local_optimum, print_meas=False),"(",eval_prog(new_local_optimum)-old_res,")")
		#print(best_of_the_best)
		old = eval_prog(new_local_optimum)
		ll_time_and_val_for_plot[-1][0] += [ll_time_and_val_for_plot[-1][0][-1]]
		ll_time_and_val_for_plot[-1][1] += [old_res]
		
		best_of_the_best = combin_prog(best_of_the_best, new_local_optimum*1)
		
		print("combined ",eval_prog(best_of_the_best),"(",eval_prog(best_of_the_best)-old_res,")")
		
		old2 = eval_prog(best_of_the_best)
		
		ll_time_and_val_for_plot[-1][0] += [ll_time_and_val_for_plot[-1][0][-1]]
		ll_time_and_val_for_plot[-1][1] += [old2]
		
		best_of_the_best = compute_a_local_optimim(best_of_the_best, talk=False, tmax=time_cst/4)
		if best_of_the_best is None:
			break
		
		ll_time_and_val_for_plot[-1][0] += [ll_time_and_val_for_plot[-1][0][-1]]
		ll_time_and_val_for_plot[-1][1] += [eval_prog(best_of_the_best)]
		
		print("optimized",eval_prog(best_of_the_best),"(",eval_prog(best_of_the_best)-old_res,")")
		save_res_in_csv(np.array(best_of_the_best), path_csv_file_to_optimize)
		if eval_prog(best_of_the_best)<old_res:
			do_plot()
		print()
		
	pool.close()
	pool.join()
	
	
	#os.remove(path_pid_file)

