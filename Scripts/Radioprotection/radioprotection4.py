
from ZPyDosi.Common.utils_general import lmap,time2str
from ZPyDosi.Common.ExcelSheet import ExcelSheet
from ZPyDosi.DosiFunctions.Dictionaries import d_spectro
from ZPyDosi.Prints.PrintnSave import aff, aff_t
from ZPyDosi.XSnFlux.Projections import projet_vec_intervals_from_continus
from ZPyDosi.XSnFlux.GetIRDFF import get_irdff_iaea
import numpy as np
import os
from ZPyDosi.DosiFunctions.Functions import get_iso2mass
from ..Analysis.data_spectre import dico_spectrum

path_xsdata    = os.path.expandvars("Path to your XSDATA file")
path_iaea_data = os.path.expandvars("Path to your IRDFF-II Folder")

power_per_src_n = 1.32574000e-11	# J/n
mode_irdff_only =True

#ath_xsdata = "/var/local/lrs_cluster/xsdata/jeff33/sss_jeff33.xsdata"				# get the mass from the xsdata

#path_xsdata = "/Users/axellaureau/data/../serpent/xsdata/jeff33/sss_jeff33.xsdata"	# get the mass from the xsdata

#path_xsdata = "sss_jeff33.xsdata"													# get the mass from the xsdata
#path_xsdata = "/Users/axellaureau/data/tmp/sss_jeff33.xsdata"
#path_iaea_data = "/Users/axellaureau/data/irdff/iaea_data/"

d_iso2mass = {}
warn = False
for iso_complete, mass in map(lambda l: (l.split()[0], float(l.split()[5])),open(path_xsdata).readlines()):
	iso, temp_key = iso_complete[:-4], iso_complete[-4:]
	if not mode_irdff_only or ".34y" == temp_key:
		if iso in d_iso2mass and abs(mass/d_iso2mass[iso]-1)>1e-4:
			print ("warning - "+aff(iso)+aff(d_iso2mass[iso], l=11, rev=True)+"!= "+aff(mass, l=11, rev=True)+"rel diff: "+aff(d_iso2mass[iso]/mass,l=14))
			warn = True
		d_iso2mass[iso] = mass


def get_rr(pos_plaque, iso, masse, d_rea, iso_sss,mat_sss, power_irrad, t_irrad): # massic_den
	
	at_per_g = 6.022140857e23 / get_iso2mass(iso_sss,path_xsdata)					# at/g
	l_iso_e = mat_sss.split()[::2]
	l_iso_f = lmap(lambda v:float(v), mat_sss.split()[1::2])
	pos = l_iso_e.index(iso_sss+".03c") 
	mass_frac =  l_iso_f[pos]*d_iso2mass[l_iso_e[pos][:-4]] / sum(map(lambda i: l_iso_f[i] * d_iso2mass[l_iso_e[i][:-4]],range(len(l_iso_e))))
	#at_density  = at_per_g * mass_frac * massic_den *1e-24					# at/g * g/cm3 * cm2/barn = at/(barn.cm)
	at_massique = at_per_g * mass_frac                 					# at/g
	
	l_fe, l_fv = dico_spectrum[pos_plaque]
	if "_spe" not in iso:
		(l_cor_e, cor), (l_xs_e,l_xs_v,l_xs_s) = get_irdff_iaea(path_iaea_data+iso)
	else:
		lines = open(path_iaea_data+iso.replace("_spe","")+"_xs").readlines()
		while "//" not in lines[0]:
			lines.pop(0)
		lines.pop(0)
		l_xs_e, l_xs_v = [], []
		while "//" not in lines[0]:
			e,v = map(lambda s:float(s), lines.pop(0).split())
			l_xs_e += [e]
			l_xs_v += [v]
		l_xs_e, l_xs_v = map(lambda l:np.array(l), [l_xs_e, l_xs_v])
		#l_xs_e *= 1e-6
		#print l_xs_e
		#exit()
	
	tmp_proj_xs = projet_vec_intervals_from_continus(l_fe, l_xs_e, l_xs_v)
	
	def dlet(le, log10=False):
		if not log10:
			return np.log(le[1:])-np.log(le[:-1])
		else:
			return np.log10(le[1:])-np.log10(le[:-1])

	def integ(l_e,l_v,log10=False):
		l_dlet = dlet(l_e, log10=log10)
		l_integ = l_v*l_dlet
		for i in range(len(l_integ))[1:]:
			l_integ[i]+= l_integ[i-1]
		return l_integ

	#volume = masse/massic_den
	#rr_v_bibi = integ(l_fe, tmp_proj_xs * l_fv)[-1] * volume
	#at_per_src		= rr_v_bibi*at_density							# at/n
	
	#				      barn          n/cm2      cm2/barn g      at/g              
	at_per_src		= integ(l_fe, tmp_proj_xs * l_fv)[-1] * 1e-24 * masse*at_per_g * mass_frac 	# at/n
	
	
	at_per_J		= at_per_src/power_per_src_n						# at/J	
	equilibrium_at_quantity = at_per_J*power_irrad/d_rea["lambda"]					# at/s/(s-1)=at
	#print(equilibrium_at_quantity)
	nrj_irrad = power_irrad * t_irrad
	at_created		= equilibrium_at_quantity*(1-np.exp(-d_rea["lambda"] * t_irrad))	# at
	#at_put_in_hpge		= at_created * np.exp(-d_rea["lambda"] * t_cooling)			# at
	#at_decay_in_hpge	= at_put_in_hpge*(1-np.exp(-d_rea["lambda"] * t_in_hpge))		# gamma
	return d_rea["lambda"] * at_created

def nb_unit(n):
	if n<1e3: return int(n*10)/10.
	if n<1e6:  return str(int(n/1e3*10)/10.)+"kBq"
	if n<1e9:  return str(int(n/1e6*10)/10.)+"MBq"
	if n<1e12: return str(int(n/1e9*10)/10.)+"GBq"
	if n<1e15: return str(int(n/1e12*10)/10.)+"TBq"
	if n<1e18: return str(int(n/1e15*10)/10.)+"PBq"
	return int(n*10)/10.
compo_fe = "26054.03c 0.05845 26056.03c 0.91754 26057.03c 0.02119 26058.03c 0.00282"
compo_ni = "28058.03c 0.68077 28060.03c 0.26223 28061.03c 0.01140 28062.03c 0.03635 28064.03c 0.00926"
print ("comment    | rea               | prod       | pow W | Irad h               | cool h  | activity  | T_1/2                | keV        | f_cool | act_manut  | dose manut1 | dose manut2 | activity per plate")

#wb = xlrd.open_workbook("input_radioprotection.xlsx")
#sheet = wb.sheet_by_index(0)

input = ExcelSheet("input_radioprotection.xlsx")
#print(input.sheet.max_row)
#exit()
i = 1
while input.get(i, 0) is not None:
	name, petale_compo, power, irrad_time, irrad_cool, reaction, prod_elt, masse, f_dose1, f_dose2, iso, mt, iso_sss, sss_descr = map(lambda j: input.get(i, j), range(14))
	irrad_time, irrad_cool, masse = map(lambda s: eval(str(s)), [irrad_time, irrad_cool, masse])
	
	
	
	iso, mt = map(lambda s: int(s), [iso, mt])
	if type(iso_sss) == float: iso_sss = int(iso_sss)
	iso_sss = str(iso_sss)
	spectro_data = d_spectro[(str(int(iso)),str(int(mt)))]
	fcool = np.exp(-spectro_data["lambda"] * irrad_cool)
	res = np.array(lmap(lambda pos:get_rr("P"+petale_compo+"_Al_"+str(pos), reaction, masse, spectro_data, iso_sss, sss_descr, power, irrad_time), np.arange(1,10)))
	print(aff(name,10), "|", aff(reaction,17), "|", aff(prod_elt,10), "|", aff(power,5), "|", aff(irrad_time/3600, 20),"|", aff(irrad_cool/3600,8),end="")
	print("|", aff(nb_unit(sum(res)), 9), "|", aff(time2str(spectro_data["halftime"]), 20), "|", aff(spectro_data["keV"], 10),"|", aff(format(fcool,"0.4f"),7),end="")
	print("|", aff(nb_unit(sum(res)*fcool)), "|", aff("" if f_dose1=="x" else format(sum(res)*fcool*f_dose1,".3f"), 11), "|", aff("" if f_dose2=="x" else format(sum(res)*fcool*f_dose2,".3f"), 12),end="")
	print( "| per plate in % ->",aff_t(map(lambda v: format(v,"0.1f"), res/sum(res)*100), 5))

	i += 1

# http://www.radprocalculator.com/Gamma.aspx
# https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc=24NA&unc=nds	https://nucleonica.com/Application/ReducedDecaySchemes/Na24_TXT.htm
# https://fr.wikipedia.org/wiki/Produit_d%27activation

