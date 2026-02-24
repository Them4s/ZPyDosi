'''
Docstring for Scripts.ModelsnSim.barre
Generate an experiment dependent text bloc to be inserted in the Serpent2 
input of CROCUS for PETALE

'''

from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataInsta.DataInsta import DataInsta
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.DosiFunctions.Dictionaries import d_matdosi_2_data
from ZPyDosi.DosiFunctions.Functions import get_massic_fraction
import numpy as np
from scipy.optimize import curve_fit


def aff(v, l=10, rev=False):
    #v = str(v)+" "
    #return v+" "*(l-len(v)) if not rev else " "*(l-len(v))+v
    if type(v) == int           : v = str(v)
    if type(v) == float         : v = "%.4e"%v
    if type(v) == np.float64 : v = "%.4e"%v
    v = str(v)
    return (v+" ").ljust(l)


print ("#"*50, "get bash args")

path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
case_csv  = get_param_vari("case", str)
ref_mat=case_csv[3:5]

var_red  = get_param_vari("var_reduction", bool, 'false')


air_around = get_param_vari("air_around", bool, 'false')
is_petale = get_param_vari("is_petale", bool, 'false')

print ("#"*50)

data_barre = DataInsta(path_csv_data, case_csv)

data_irrad = DataIrrad(path_csv_data, path_csv_dosi, [case_csv], remove_data=False, load_moni=False)

#data_irrad.aff_description()
# print("\n".join(data_irrad.l_name))
# exit()

'''
d_mat_plate = {             # Check SS 
    "Ni":{"den":-8.908, "rgb":"100 100 100",   "compo":"28058g0.0300c 0.6827  28060g0.0300c 0.261   28061g0.0300c 0.0113  28062g0.0300c 0.0359  28064g0.0300c 0.0091"},
    "Fe":{"den":-7.874, "rgb":"100 100 100",   "compo":"26054g0.0300c 0.05845 26056g0.0300c 0.91754 26057g0.0300c 0.02119 26058g0.0300c 0.00282        "}, # (35) (36) (20) (4)
    "SS":{"den":-8.0,   "rgb":"100 100 100",   "compo":"24052g0.0300c -0.14206 24053g0.0300c -0.0152 24050g0.0300c -0.00274 28058g0.0300c -0.087138 \
      28060g0.0300c -0.033565 28062g0.0300c -0.004666 28061g0.0300c -0.002631 \
      12024g0.0300c -0.00008 12025g0.0300c -0.00001 12026g0.0300c -0.00001 \
      25055g0.0300c -0.019 14028g0.0300c -0.0054 14029g0.0300c -0.0003 \
      14030g0.0300c -0.0002 26054g0.0300c -0.03916 26056g0.0300c -0.63204 \
      26057g0.0300c -0.0158"},
    "Cr":{"den":-7.15,  "rgb":"100 100 100",   "compo":"24050g0.0300c 0.04345 24052g0.0300c 0.83789 24053g0.0300c 0.09501 24054g0.0300c 0.02365"},
    }
'''
d_mat_plate = {             # density computed from dimension and mass
    "Ni":{"den":-8.888, "rgb":"100 100 100",   "compo":"6000g0.0300c    -0.0001   14028g0.0300c    -0.000459368   14029g0.0300c    -2.41588E-05   14030g0.0300c    -1.64737E-05   25055g0.0300c    -0.0009   26054g0.0300c    -2.82278E-05   26056g0.0300c    -0.000459508   26057g0.0300c    -1.08018E-05   26058g0.0300c    -1.46272E-06   28058g0.0300c    -0.670626951   28060g0.0300c    -0.267220248   28061g0.0300c    -0.011810834   28062g0.0300c    -0.038276384   28064g0.0300c    -0.010065582"},
    "Fe":{"den":-7.862, "rgb":"100 100 100",   "compo":"5010g0.0300c    -5.50665E-07   5011g0.0300c    -2.44934E-06   6000g0.0300c    -0.00003   7014g0.0300c    -4.98039E-05   7015g0.0300c    -1.96139E-07   13027g0.0300c    -0.00004   14028g0.0300c    -3.67494E-05   14029g0.0300c    -1.9327E-06   14030g0.0300c    -1.31789E-06   16032g0.0300c    -2.55875E-05   16033g0.0300c    -2.07868E-07   16034g0.0300c    -1.20019E-06   16036g0.0300c    -4.41551E-09   19039g0.0300c    -2.78811E-05   19040g0.0300c    -3.57913E-09   19041g0.0300c    -2.1153E-06   23050g0.0300c    -2.44826E-08   23051g0.0300c    -9.97552E-06   24050g0.0300c    -6.6779E-06   24052g0.0300c    -0.000133919   24053g0.0300c    -1.54777E-05   24054g0.0300c    -3.92538E-06   25055g0.0300c    -0.0005   26054g0.0300c    -0.056385577   26056g0.0300c    -0.917875709   26057g0.0300c    -0.021576898   26058g0.0300c    -0.002921816   27059g0.0300c    -0.00002   28058g0.0300c    -0.000107515   28060g0.0300c    -4.28409E-05   28061g0.0300c    -1.89352E-06   28062g0.0300c    -6.13649E-06   28064g0.0300c    -1.61372E-06   29063g0.0300c    -6.85035E-05   29065g0.0300c    -3.14965E-05   33075g0.0300c    -0.00001   41093g0.0300c    -0.00001   42092g0.0300c    -4.17344E-06   42094g0.0300c    -2.68662E-06   42095g0.0300c    -4.69905E-06   42096g0.0300c    -4.99871E-06   42097g0.0300c    -2.90811E-06   42098g0.0300c    -7.46563E-06   42100g0.0300c    -3.06843E-06   50112g0.0300c    -1.8344E-07   50114g0.0300c    -1.2646E-07   50115g0.0300c    -6.56244E-08   50116g0.0300c    -2.83836E-06   50117g0.0300c    -1.5118E-06   50118g0.0300c    -4.8115E-06   50119g0.0300c    -1.71976E-06   50120g0.0300c    -6.58392E-06   50122g0.0300c    -9.50684E-07   50124g0.0300c    -1.20844E-06"}, # (35) (36) (20) (4)
    "Fe_overcoated":{"den":-7.862, "rgb":"100 100 100",   "compo":" 5010g0.0300c    -5.47811E-07     5011g0.0300c    -2.43664E-06     6000g0.0300c    -8.805982E-05    7014g0.0300c    -0.000435953     7015g0.0300c    -1.71689E-06     8016g0.0300c    -0.000741931     8017g0.0300c    -2.99559E-07     8018g0.0300c    -1.67411E-06    13027g0.0300c    -3.97927E-05    14028g0.0300c    -3.6559E-05    14029g0.0300c    -1.92268E-06    14030g0.0300c    -1.31106E-06    16032g0.0300c    -2.54549E-05    16033g0.0300c    -2.06791E-07    16034g0.0300c    -1.19397E-06    16036g0.0300c    -4.39263E-09    19039g0.0300c    -2.77366E-05    19040g0.0300c    -3.56058E-09    19041g0.0300c    -2.10434E-06    23050g0.0300c    -2.43557E-08    23051g0.0300c    -9.92382E-06    24050g0.0300c    -6.64329E-06    24052g0.0300c    -0.000133225    24053g0.0300c    -1.53975E-05    24054g0.0300c    -3.90504E-06    25055g0.0300c    -0.000497409    26054g0.0300c    -0.056318755    26056g0.0300c    -0.916787941    26057g0.0300c    -0.021551327    26058g0.0300c    -0.002918354    27059g0.0300c    -1.98964E-05    28058g0.0300c    -0.000106958    28060g0.0300c    -4.26189E-05    28061g0.0300c    -1.88371E-06    28062g0.0300c    -6.1047E-06    28064g0.0300c    -1.60536E-06    29063g0.0300c    -6.81485E-05    29065g0.0300c    -3.13333E-05    33075g0.0300c    -9.94818E-06    41093g0.0300c    -9.94818E-06    42092g0.0300c    -4.15181E-06    42094g0.0300c    -2.6727E-06    42095g0.0300c    -4.6747E-06    42096g0.0300c    -4.9728E-06    42097g0.0300c    -2.89305E-06    42098g0.0300c    -7.42695E-06    42100g0.0300c    -3.05253E-06    50112g0.0300c    -1.8249E-07    50114g0.0300c    -1.25805E-07    50115g0.0300c    -6.52844E-08    50116g0.0300c    -2.82366E-06    50117g0.0300c    -1.50396E-06    50118g0.0300c    -4.78657E-06    50119g0.0300c    -1.71085E-06    50120g0.0300c    -6.5498E-06    50122g0.0300c    -9.45758E-07    50124g0.0300c    -1.20218E-06"}, # (35) (36) (20) (4)
    "SS":{"den":-7.897, "rgb":"100 100 100",   "compo":"6000g0.0300c    -0.00013   7014g0.0300c    -0.000896469   7015g0.0300c    -3.53051E-06   13027g0.0300c    -0.00004   14028g0.0300c    -0.003858688   14029g0.0300c    -0.000202934   14030g0.0300c    -0.000138379   16032g0.0300c    -7.58149E-05   16033g0.0300c    -6.15906E-07   16034g0.0300c    -3.55612E-06   16036g0.0300c    -1.3083E-08   19039g0.0300c    -0.000204462   19040g0.0300c    -2.6247E-08   19041g0.0300c    -1.55122E-05   22046g0.0300c    -1.58382E-06   22047g0.0300c    -1.45896E-06   22048g0.0300c    -1.4769E-05   22049g0.0300c    -1.10623E-06   22050g0.0300c    -1.08202E-06   24050g0.0300c    -0.007763057   24052g0.0300c    -0.155680814   24053g0.0300c    -0.017992872   24054g0.0300c    -0.004563257   25055g0.0300c    -0.0154   26054g0.0300c    -0.039884175   26056g0.0300c    -0.64925673   26057g0.0300c    -0.015262356   26058g0.0300c    -0.002066738   27059g0.0300c    -0.0004   28058g0.0300c    -0.05725192   28060g0.0300c    -0.022812791   28061g0.0300c    -0.0010083   28062g0.0300c    -0.003267683   28064g0.0300c    -0.000859306   29063g0.0300c    -0.000274014   29065g0.0300c    -0.000125986   41093g0.0300c    -0.00007   42092g0.0300c    -5.56459E-05   42094g0.0300c    -3.58217E-05   42095g0.0300c    -6.2654E-05   42096g0.0300c    -6.66494E-05   42097g0.0300c    -3.87749E-05   42098g0.0300c    -9.95418E-05   42100g0.0300c    -4.09124E-05   50112g0.0300c    -6.42041E-07   50114g0.0300c    -4.4261E-07   50115g0.0300c    -2.29686E-07   50116g0.0300c    -9.93427E-06   50117g0.0300c    -5.29129E-06   50118g0.0300c    -1.68403E-05   50119g0.0300c    -6.01915E-06   50120g0.0300c    -2.30437E-05   50122g0.0300c    -3.3274E-06   50124g0.0300c    -4.22955E-06"},
    "Cr":{"den":-7.178, "rgb":"100 100 100",   "compo":"6000g0.0300c    -0.00004   8016g0.0300c    -0.000189496   8017g0.0300c    -7.651E-08   8018g0.0300c    -4.27584E-07   13027g0.0300c    -0.00001   14028g0.0300c    -9.18735E-06   14029g0.0300c    -4.83175E-07   14030g0.0300c    -3.29473E-07   16032g0.0300c    -9.47686E-06   16033g0.0300c    -7.69882E-08   16034g0.0300c    -4.44515E-07   16036g0.0300c    -1.63537E-09   24050g0.0300c    -0.041720587   24052g0.0300c    -0.836667197   24053g0.0300c    -0.096698142   24054g0.0300c    -0.024524074   26054g0.0300c    -5.64556E-06   26056g0.0300c    -9.19015E-05   26057g0.0300c    -2.16037E-06   26058g0.0300c    -2.92544E-07   28058g0.0300c    -6.71971E-06   28060g0.0300c    -2.67756E-06   28061g0.0300c    -1.18345E-07   28062g0.0300c    -3.83531E-07   28064g0.0300c    -1.00858E-07   29063g0.0300c    -6.85035E-06   29065g0.0300c    -3.14965E-06   74180g0.0300c    -1.17262E-08   74182g0.0300c    -2.62256E-06   74183g0.0300c    -1.42442E-06   74184g0.0300c    -3.06604E-06   74186g0.0300c     -2.87526E-06"},
    }

water_lvl = data_irrad.l_water_lvl_cm[0]*10		# in mm
CR_north = data_irrad.CR_north_cm[0]*10		# in mm
CR_south = data_irrad.CR_south_cm[0]*10		# in mm
water_lvl_ign = data_irrad.l_water_lvl_cm_ign[0]
if water_lvl_ign is not None:
	water_lvl_ign *= 10				# in mm

print ("#"*50)


def my_fct(x,a,b):
	return a*x+b

l_water_lvl_calibration_mesure    = [798.78666666666, 1000.1020]
l_water_lvl_calibration_deversoir = [800.00,          1000.00  ]
l_water_lvl_calibration_inus      = [798.85,          999.80   ]

best_p_dev, covar_dev = curve_fit(my_fct, l_water_lvl_calibration_deversoir, l_water_lvl_calibration_mesure)
best_p_inu, covar_inu = curve_fit(my_fct, l_water_lvl_calibration_inus,      l_water_lvl_calibration_mesure)

print ("water level correction:")
print ("     list deversoir  ",l_water_lvl_calibration_deversoir)
print ("     list mesure     ",l_water_lvl_calibration_mesure)
print ("     given value:    ", water_lvl)
water_lvl = my_fct(water_lvl, *best_p_dev)
print ("     corrected value:",water_lvl)
if water_lvl_ign is not None:
	water_lvl_ign = my_fct(water_lvl_ign, *best_p_inu)
	print ("     corrected inus: ",water_lvl_ign, "(for info)")

# fall 2019 - exp 1
# my_fct(955.05, *best_p_dev) -> 954.8563788333317 (val ds l'input)
# my_fct(954.4,  *best_p_inu) -> 954.619461391721  (val de check)


txt_surf_rm_barre = ""
l_surf   = []
l_trans  = []
l_cell   = []
l_dosis  = []
l_dosi   = []
l_det1   = []
l_det2   = []
l_defmat = []
l_defidet= []

i_s = 0
i_c = 0
i_d = 0


def nro_s():
	global i_s
	i_s += 1
	return str(i_s-1)

def nro_c():
	global i_c
	i_c += 1
	return str(i_c-1)
	
def nro_d():
	global i_d
	i_d += 1
	return str(i_d-1)

def add_in_l(l,s):
	if s not in l:
		l.append(s)


def fct_C(h1, h2, l_remhn_dosi):
	global l_surf, l_cell, l_dosi,l_dosis, txt_surf_rm_barre,l_det1,l_det2, l_defmat
	id_C = list(data_barre.l_name).index("C")
	large_barre = data_barre.l_width[id_C]
	large_hole  = data_barre.l_hole_width[id_C]
	e_barre     = data_barre.l_thickness[id_C]
	e_cut	    = data_barre.l_hole_thickness[id_C]
	centrage    = data_barre.l_centrage[id_C]
	
	r = large_hole/2.
	l_s = ["s_barre_"+nro_s(), "s_barre_"+nro_s(), "s_barre_"+nro_s()]
	l_surf += ["surf "+aff(l_s[0],l=15)+"cylx   "+aff(0)+aff(h1+r)+aff(r)+aff(-e_barre/2+centrage)+aff(-e_barre/2+e_cut+centrage)]
	l_surf += ["surf "+aff(l_s[1],l=15)+"cylx   "+aff(0)+aff(h2-r)+aff(r)+aff(-e_barre/2+centrage)+aff(-e_barre/2+e_cut+centrage)]
	l_surf += ["surf "+aff(l_s[2],l=15)+"cuboid "+aff(-e_barre/2+centrage)+aff(-e_barre/2+e_cut+centrage)+aff(-r)+aff(r)+aff(h1+r)+aff(h2-r)]
	for (r_dosi, e_dosi, m_dosi,h_dosi, n_dosi) in l_remhn_dosi:
		nro_dosi = n_dosi # nro_d()
		name_s = "s_dosim_"+nro_dosi
		l_s += [name_s ]
		l_dosis += ["surf "+aff(name_s,l=25)+"cylx   "+aff(0)+aff(h_dosi)+aff(r_dosi)+aff(-e_barre/2+e_cut-e_dosi+centrage)+aff(-e_barre/2+e_cut+centrage)]
		if air_around:
			rad_air = r_dosi+0.2
			l_dosis += ["surf "+aff(name_s+"_air",l=25)+"cylx   "+aff(0)+aff(h_dosi)+aff(rad_air)+aff(-e_barre/2+e_cut-e_dosi+centrage)+aff(-e_barre/2+e_cut+centrage)]
		if not var_red:
			l_dosi  += ["cell "+aff("c_dosim_"+nro_dosi,l=25)+"u_core imp 3 mat_dosi_"+m_dosi+" -"+name_s] #    +s0+":-"+s1+":-"+s2
		else:
			l_dosi  += ["cell "+aff("c_dosim_"+nro_dosi,l=25)+"u_core imp 3 mat_dosi_"+n_dosi+" -"+name_s] #    +s0+":-"+s1+":-"+s2
		if air_around:
			bord = "" if rad_air < large_hole/2 else ("-"+l_s[2])
			l_dosi  += ["cell "+aff("c_dosim_"+nro_dosi+"_air",l=25)+"u_core Air "+name_s+" -"+name_s+"_air "+bord] #    +s0+":-"+s1+":-"+s2
		print ("      "+str(d_matdosi_2_data[m_dosi]["iso"]))
		print ("      "+str(d_matdosi_2_data[m_dosi]["compo"]))
		for iso,l_mt in d_matdosi_2_data[m_dosi]["iso"]:
			mat_iso = "mat_reac_"+m_dosi+"_"+str(iso)
			frac_masse_iso = get_massic_fraction(str(iso)[:-1], d_matdosi_2_data[m_dosi]["compo"], data_irrad.path_xsdata)
			if not var_red:
				add_in_l(l_defmat,aff("mat "+mat_iso, l=25)+" -"+aff(frac_masse_iso*d_matdosi_2_data[m_dosi]["den"],l=20)+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+str(iso)[:-1]+".34y 1")
				
				
				#idet  mat_dosi_Au      791970  12102
				
			#add_in_l(l_defmat,aff("mat "+mat_iso, l=25)+" -"+str(d_matdosi_2_data[m_dosi]["den"])+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+d_matdosi_2_data[m_dosi]["compo"].replace("g0.0300c",".34y"))
			for mt in l_mt:
				if not var_red:
					l_det1  += ["det "+aff("dos_"+n_dosi+"_"+str(iso)+"_"+str(mt)+"_rr")+" dtl "+aff(name_s,l=15)+ "dr "+str(mt)+" "+mat_iso]
				else:
					add_in_l(l_defidet,"   idet  "+aff("mat_dosi_"+n_dosi)+aff(iso)+aff(mt))
				#l_det1  += ["det "+aff("dos_"+n_dosi+"_"+str(iso)+"_"+str(mt)+"_rr")+" dc "+aff("c_dosim_"+nro_dosi,l=15)+ "dr "+str(mt)+" "+mat_iso]
		
		if not var_red:
			l_det2  += ["det "+aff("dos_"+n_dosi+"_spectrum")+"de e_mesh dt -3 dtl "+aff(name_s,l=15)]
		#l_det2  += ["det "+aff("dos_"+n_dosi+"_spectrum")+"de e_mesh dt -3 dc "+aff("c_dosim_"+nro_dosi,l=15)]
		
		if not var_red:
			add_in_l(l_defmat,aff("mat mat_dosi_"+m_dosi, l=25)+" -"+aff(d_matdosi_2_data[m_dosi]["den"],l=20)+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+d_matdosi_2_data[m_dosi]["compo"])
		else:
			add_in_l(l_defmat,aff("mat mat_dosi_"+n_dosi, l=25)+" -"+aff(d_matdosi_2_data[m_dosi]["den"],l=20)+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+d_matdosi_2_data[m_dosi]["compo"])
		
		#add_in_l(l_defmat,"mat mat_reac_"+m_dosi+" -"+str(d_matdosi_2_data[m_dosi]["den"])+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+d_matdosi_2_data[m_dosi]["compo"].replace("g0.0300c",".34y"))
	
	def add_air(s):
		return s+("" if not air_around else "_air")
	l_cell += ["cell "+aff("c_barre_"+nro_c(),l=25)+"u_core H2O (-"+":-".join(l_s[:3]) + ") -40 "+" ".join(map(lambda s:add_air(s), l_s[3:]))] #    +s0+":-"+s1+":-"+s2
	#if air_around:
	#	l_cell += ["cell "+aff("c_barre_"+nro_c(),l=15)+"0 Air (-"+":-".join(l_s[:3]) + ")  40 "+" ".join(l_s[3:])] #    +s0+":-"+s1+":-"+s2
	l_cell += ["cell "+aff("c_barre_"+nro_c(),l=25)+"u_core Air (-"+":-".join(l_s[:3]) + ")  40 "+" ".join(map(lambda s:add_air(s), l_s[3:]))] #    +s0+":-"+s1+":-"+s2
	txt_surf_rm_barre += " ".join(l_s[:3])+" " #s0+" "+s1+" "+s2
	
def fct_CR(nro, name, l_remhn_dosi):
	global l_surf, l_cell, l_dosi,l_dosis,l_det1,l_det2, l_defmat, l_trans
	print (name)
	id_name = list(data_barre.l_name).index(name)
	large_barre = data_barre.l_width[id_name]
	e_barre     = data_barre.l_thickness[id_name]
	centrage    = data_barre.l_centrage[id_name]
	l_s = []
	for (r_dosi, e_dosi, m_dosi,h_dosi, n_dosi) in l_remhn_dosi:
		nro_dosi = n_dosi
		name_s = "s_dosim_"+nro_dosi
		l_s += [name_s]
		p1,p2 = -e_barre/2-e_dosi+centrage, -e_barre/2+centrage
		p1,p2 = e_barre/2+centrage, e_barre/2+e_dosi+centrage
		l_dosis += ["surf "+aff(name_s,l=25)+"cylx   "+aff(0)+aff(h_dosi)+aff(r_dosi)+aff(p1)+aff(p2)]
		if not var_red:
			l_dosis += ["surf "+aff(name_s+"_det",l=20)+"cylx   "+aff(0)+aff(h_dosi)+aff(r_dosi)+aff(p1)+aff(p2)]
		if not var_red:
			l_dosi  += ["cell "+aff("c_dosim_"+nro_dosi,l=25)+str(20+nro+1)+" imp "+("4" if name=="CR" else "5")+" mat_dosi_"+m_dosi+" -"+name_s] #    +s0+":-"+s1+":-"+s2
		else:
			l_dosi  += ["cell "+aff("c_dosim_"+nro_dosi,l=25)+str(20+nro+1)+" imp "+("4" if name=="CR" else "5")+" mat_dosi_"+n_dosi+" -"+name_s] #    +s0+":-"+s1+":-"+s2
		print ("      "+str(d_matdosi_2_data[m_dosi]["iso"]))
		print ("      "+str(d_matdosi_2_data[m_dosi]["compo"]))
		for iso,l_mt in d_matdosi_2_data[m_dosi]["iso"]:
			mat_iso = "mat_reac_"+m_dosi+"_"+str(iso)
			frac_masse_iso = get_massic_fraction(str(iso)[:-1], d_matdosi_2_data[m_dosi]["compo"],data_irrad.path_xsdata)
			if not var_red:
				add_in_l(l_defmat,aff("mat "+mat_iso, l=25)+" -"+aff(frac_masse_iso*d_matdosi_2_data[m_dosi]["den"],l=20)+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+str(iso)[:-1]+".34y 1")
			for mt in l_mt:
				if not var_red:
					l_det1  += ["det "+aff("dos_"+n_dosi+"_"+str(iso)+"_"+str(mt)+"_rr")+" dtl "+aff(name_s+"_det",l=15)+ "dr "+str(mt)+" "+mat_iso]
				else:
					add_in_l(l_defidet,"   idet  "+aff("mat_dosi_"+n_dosi)+aff(iso)+aff(mt))
				#l_det1  += ["det "+aff("dos_"+n_dosi+"_"+str(iso)+"_"+str(mt)+"_rr")+" dc "+aff("c_dosim_"+nro_dosi,l=15)+ "dr "+str(mt)+" "+mat_iso]
		
		if not var_red:
			l_det2  += ["det "+aff("dos_"+n_dosi+"_spectrum")+"de e_mesh dt -3 dtl "+aff(name_s+"_det",l=15)]
		
		if not var_red:
			l_trans += ["trans S "+aff(name_s, l=20)+" rot 0 0 0 0 0 1 45"]
		else:
			l_trans += ["strans "+aff(name_s, l=20)+" 0 0 0 0 0 45"]
			
		
		if   name == "R":  det = str(7.5*2.917)
		elif name == "CR": det = str(5.5*2.917)
		else: 
			print ("error -",name,"not in [CR R]")
			
		if not var_red:
			l_trans += ["trans S "+aff(name_s+"_det", l=20)+" -"+det+" "+det+" 0"]
			l_trans += ["trans S "+aff(name_s+"_det", l=20)+" rot 0 0 0 0 0 1 45"]
		if False:
			l_cell += ["cell c_toto_test_collision_dosim_"+nro_dosi+" u_core Cd -"+name_s+"_det"]
		name_s+"_det"
		if not var_red:
			add_in_l(l_defmat,aff("mat mat_dosi_"+m_dosi, l=25)+" -"+aff(d_matdosi_2_data[m_dosi]["den"],l=20)+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+d_matdosi_2_data[m_dosi]["compo"])
		else:
			add_in_l(l_defmat,aff("mat mat_dosi_"+n_dosi, l=25)+" -"+aff(d_matdosi_2_data[m_dosi]["den"],l=20)+" rgb "+d_matdosi_2_data[m_dosi]["rgb"]+" "+d_matdosi_2_data[m_dosi]["compo"])

	
	#l_cell += ["cell "+aff("c_barre_"+nro_c(),l=15)+"0 H2O (-"+":-".join(l_s[:3]) + ") "+" ".join(l_s[3:])] #    +s0+":-"+s1+":-"+s2
	l_cell += ["cell "+aff(200+(nro+1)*10+0,l=15)+str(20+nro+1)+" fill=20 -172 "+" ".join(l_s)+((" s_barre_"+name) if (len(l_remhn_dosi)>0 or True) else "")]
	l_cell += ["cell "+aff(200+(nro+1)*10+1,l=15)+str(20+nro+1)+" Al6060 172 -173"]
	l_cell += ["cell "+aff(200+(nro+1)*10+2,l=15)+str(20+nro+1)+" fill=3 173"]
	



#nro_cr = 0
l_nb_dosi_par_barre = []
l_barrename_nb_nro = []
for i_barre_name, barre_name in enumerate(data_barre.l_name):
    if not barre_name.startswith("P"):
        print ("generation input for rod", barre_name)
        nb_dosi_barre = 0
        l_dosi_place = []
        for i in range(len(data_barre.l_pos_hole[i_barre_name])//2):
            l_dosi_in_hole = []
            p_hole_1, p_hole_2 = data_barre.l_pos_hole[i_barre_name][i*2], data_barre.l_pos_hole[i_barre_name][i*2+1]
            for i_dosi, pos_dosi in enumerate(data_irrad.l_pos_reel):
                if data_irrad.l_pos_name[i_dosi] == barre_name and p_hole_1 < pos_dosi < p_hole_2:
                    if data_irrad.l_name[i_dosi] in l_dosi_place:
                        print ("WARNING - found twice -",data_irrad.l_name[i_dosi])
                        pass
                    else:
                        l_dosi_in_hole += [i_dosi]
                        l_dosi_place += [data_irrad.l_name[i_dosi]]
            print ("   hole",i,"dosi:"," ".join(map(lambda i:data_irrad.l_name[i], l_dosi_in_hole)))
            if barre_name == "C":
                fct_C(p_hole_1, p_hole_2,
                    map(lambda i: (data_irrad.l_radius[i], data_irrad.l_thickness[i], data_irrad.l_mat[i], data_irrad.l_pos_reel[i]+0*data_irrad.l_radius[i], data_irrad.l_name[i]), l_dosi_in_hole))
            else:
                fct_CR(i_barre_name,barre_name, lmap(lambda i: (data_irrad.l_radius[i], data_irrad.l_thickness[i], data_irrad.l_mat[i], data_irrad.l_pos_reel[i]+0*data_irrad.l_radius[i], data_irrad.l_name[i]), l_dosi_in_hole))
                #nro_cr += 1
            nb_dosi_barre += len(l_dosi_in_hole)
        l_nb_dosi_par_barre += [nb_dosi_barre]
        l_barrename_nb_nro += [(barre_name,nb_dosi_barre,i_barre_name)]
	
if "C" in data_barre.l_name:
	id_C = list(data_barre.l_name).index("C")
	large_barre = data_barre.l_width[id_C]
	e_barre     = data_barre.l_thickness[id_C]
	centrage    = data_barre.l_centrage[id_C]
	h_barre_min, h_barre_max = data_barre.l_h_min[id_C], data_barre.l_h_max[id_C]
	l_surf += ["surf "+aff("s_barre",l=15)+"cuboid "+aff(-e_barre/2+centrage)+aff(e_barre/2+centrage)+aff(-large_barre/2)+aff(large_barre/2)+aff(h_barre_min)+aff(h_barre_max)]
	if l_dosi:
		l_cell += ["cell "+aff("c_barre",l=15)+"u_core  plexi -s_barre "+txt_surf_rm_barre]
	else:
		l_cell += ["cell "+aff("c_barre",l=15)+"u_core  H2O -s_barre "+txt_surf_rm_barre]
	
	print ("WARNING - add in the '2.4 Fuel zones/UO2 fuel zone' decription:")
	print ("          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% --- 2.4 Fuel zones")
	print ("          cell   15   u_core  fill=10   (-60:-61:-62:-63) -6 23 s_barre                        % UO2 fuel zone")


i, warning_done = 1, False
for name_barre in ["CR","R"]:
	if name_barre in data_barre.l_name:
		id_barre = list(data_barre.l_name).index(name_barre)
		width 	 = data_barre.l_width[id_barre]
		thickness= data_barre.l_thickness[id_barre]
		h_barre_min, h_barre_max = data_barre.l_h_min[id_barre], data_barre.l_h_max[id_barre]
		barrename_nb_nro = l_barrename_nb_nro[list(data_barre.l_name).index(name_barre)]
		centrage    = data_barre.l_centrage[id_barre]
		if barrename_nb_nro[1] or True:
			l_surf += ["surf "+aff("s_barre_"+name_barre,l=15)+"cuboid "+aff(-thickness/2+centrage)+aff(thickness/2+centrage)+aff(-width/2)+aff(width/2)+aff(h_barre_min)+aff(h_barre_max)]
			l_cell += ["cell "+aff("c_barre_"+name_barre,l=15)+str(20+barrename_nb_nro[2]+1)+" plexi -s_barre_"+name_barre]
		i += 1
		if not warning_done:
			print("WARNING - add in the '%  u = 15: Umetal fuel lattice with 176 fuel pins and 2 CR'")
			print("          17 17 16 16 16 XX 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 ")
			print("          17 17 17 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17")
			print("          17 17 17 XX 16 16 16 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17")
			print("          17 17 17 17 17 16 16 16 16 16 16 16 16 16 16 16 17 17 17 17 17 17")
			print("          17 17 17 17 17 17 17 17 16 16 16 16 16 16 17 17 17 17 17 17 17 17")
			print("          17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17")
			warning_done = True
		if not var_red:
			l_trans += ["trans S "+aff("s_barre_"+name_barre, 20)+" rot 0 0 0 0 0 1 45"]
		else:
			l_trans += ["strans "+aff("s_barre_"+name_barre, 20)+" 0 0 0 0 0 45"]
			
	
print ("#"*50)
print ("surf   40  pz "+str(water_lvl/10.))
print ()
print ("trans   20n     0  0   "+str(CR_north/10. +0.0))                                       
print ()
print ("trans   20s     0  0   "+str(CR_south/10. +0.0))
print ()
print ("\n".join(l_surf))
print ()
print ("\n".join(l_cell))
print ()
print ("\n".join(l_dosis))
print ()
print ("\n".join(l_trans))
print ()
print ("\n".join(l_dosi))
print ()
print ("\n".join(l_defmat))
print ()
print ("mat mat_petale " + str(d_mat_plate[ref_mat]["den"])+" dmax 0.1 rgb 100 100 100 \n       "+str(d_mat_plate[ref_mat]["compo"]))
print()

if not var_red:
	print ("\n".join(l_det1)) # .replace("_rr","_rr_jeff")
	print ()
	#print( "\n".join(l_det1).replace("mat_Au","mat_Au_irdff"))
	#print
	print ("\n".join(l_det2))
	print ()
else:
	if is_petale:
		l_defidet=[]
		for dosi_name,iso,mt in zip(data_irrad.l_name,data_irrad.l_iso,data_irrad.l_mt):
			add_in_l(l_defidet,"   idet  "+aff("mat_dosi_"+dosi_name)+aff(iso)+aff(mt))
	print ("set mat_matrix_rr")
	print ("\n".join(l_defidet))
print ("#"*50)
fnew=open("input","w")
with open("input_ref","r") as file:
	for line in file.readlines():
		fnew.write(line)
		if "--- 1.4 Water level in cm (max is 100 cm)" in line:
			fnew.write("surf   40  pz "+str(water_lvl/10.))
			fnew.write("\n")
			fnew.write("trans   20n     0  0   "+str(CR_north/10. +0.0))                                       
			fnew.write("\n")
			fnew.write("trans   20s     0  0   "+str(CR_south/10. +0.0))
			fnew.write("\n")
			fnew.write("\n".join(l_surf))
			fnew.write("\n")
			fnew.write("\n".join(l_cell))
			fnew.write("\n")
			fnew.write("\n".join(l_dosis))
			fnew.write("\n")
			fnew.write("\n".join(l_trans))
			fnew.write("\n")
			fnew.write("\n".join(l_dosi))
			fnew.write("\n")
			fnew.write("\n".join(l_defmat))
			fnew.write("\n")
			fnew.write("mat mat_petale " + str(d_mat_plate[ref_mat]["den"])+" dmax 0.1 rgb 100 100 100 \n       "+str(d_mat_plate[ref_mat]["compo"]))
			l_defidet=[]
			for dosi_name,iso,mt in zip(data_irrad.l_name,data_irrad.l_iso,data_irrad.l_mt):
				add_in_l(l_defidet,"   idet  "+aff("mat_dosi_"+dosi_name)+aff(iso)+aff(mt))
			if l_defidet:
				fnew.write("set mat_matrix_rr")
				fnew.write("\n".join(l_defidet))
fnew.close()
print("input file autogenerated from input_ref")