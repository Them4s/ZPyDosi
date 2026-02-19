
import os
from ZPyDosi.EfficiencyCalibration.EfficiencyCalibration import EfficiencyCalibration

talk=False
keV_max = 8
eff_min = 0.1 # %


calib = None if not os.path.isfile("calib_out") else EfficiencyCalibration("calib_out")
if calib is None:
	print()
	print("#"*50)
	print("# Warning, no calibration file <calib_out> found, 0.2% used for all energies as an order of magitude")
	print("#"*50)
	
def get_eff(nrj):
	return 0.002 if calib is None else calib.get_eff_sig(nrj)[0]
	

def do_your_job2(path):
	print()
	path_file_with_peak_used = path.replace(path.split("/")[-1], "spectrum_plot_out_"+path.split("/")[-1])
	if os.path.isfile(path_file_with_peak_used):
		l_nrj_used = list(sorted(map(lambda l: float(l.split()[4]), filter(lambda l: l[0]!="#", open(path_file_with_peak_used).readlines()[1:]))))
		print(l_nrj_used)
	else:
		l_nrj_used = []
		print("no",path_file_with_peak_used,"found")

	path_file_coinc = path.replace("lnhb","").replace("nndc","")+"coinc"
	if os.path.isfile(path_file_coinc):
		d_e_2_lc = {}
		lines = open(path_file_coinc).readlines()
		i=0
		while i<len(lines):
			if lines[i].split()[-1][-1] == ",":
				lines[i] += lines.pop(i+1)
			else:
				i += 1
		for line in lines:
			e = line.split()[0]
			l_coin = list(map(lambda ch : float(ch.split()[0]), line.replace(e,"").split(",")))
			#print(e,l_coin)
			d_e_2_lc[float(e)] = l_coin
		def check_coin(e1,e2):
			if e1==e2:
				return False
			'''if e1==e2:
				print(e1)
				exit()'''
			for nrj, lcoin in d_e_2_lc.items():
				if abs(e1-nrj)<0.1:
					for nrj2 in lcoin:
						if abs(e2-nrj2)<keV_max:
							return True
			return False
		#def descr_coin(e1,e2,e3):
		#	r = ""
		#	#if check_coin(e1,e2): r += str(e1)+"/"+str(e2)+" "
		#	#if check_coin(e1,e3): r += str(e1)+"/"+str(e3)+" "
		#	if check_coin(e2,e3): r += str(e2)+"/"+str(e3)+" "
		#	return "" if r == "" else "coinc: "+r
	else:
		print("no",path_file_coinc,"found")
		def descr_coin(e1,e2,e3):
			return ""
	l_nrj = []
	l_inten = []
	if "lnhb" in path:
		data = open(path).readlines()
		while "Energy (keV) ; Ener. unc. (keV) ; Intensity (%) ; Int. unc. (%) ; Type ; Origin ; Lvl. start ; Lvl. end" not in data[0]: data.pop(0)
		data.pop(0)
		while "=========" not in data[0]:
			ev,es,rv,rs = data.pop(0).replace(" ","").split(";")[:4]
			if talk: print("ev",ev,"es",es,"rv",rv,"rs",rs)
			l_nrj += [float(ev)]
			l_inten += [float(rv)]
	elif "nndc" in path:
		for line in open(path).readlines():
			if line[0]!="#":
				e, e_s, r, r_s = line.replace("%","").split()[:4]
				if r_s == "?": print("Warning - no uncertainty on ratio ", e, e_s, r, r_s)
				l_nrj += [float(e)]
				l_inten += [float(r)]
	else:
		print("ERROR - format -",path)
	
	def aff(v, l=11):
		return str(v)+" "*(l-len(str(v)))
	print("#"*50)
	#print("".join(map(lambda v:aff(v), l_nrj)))
	#print("".join(map(lambda v:aff(v), l_inten)))
	out = ""
	for o, e in enumerate(l_nrj):
		for i, e1 in enumerate(l_nrj):
			for j, e2 in list(enumerate(l_nrj))[i+1:]:
				if abs(e-(e1+e2))<keV_max:
					warning = (l_inten[o] < l_inten[i] and l_inten[o] < l_inten[j] and l_inten[o]>eff_min)
					warn = "hey!!!" if warning else ""
					doprint = False
					coincbonus = ("1" if check_coin(e,e1) else " ") + ("2" if check_coin(e,e2) else " ")
					coincbonus = "" if coincbonus == "  " else ("coinc bonus "+coincbonus)
					if check_coin(e1,e2):
						prob_e = l_inten[o]/100 * get_eff(e)
						prob_e1_and_e2 = l_inten[i]/100 * get_eff(e1) * l_inten[j]/100 * get_eff(e2)
						#print(prob_e, l_inten[o])
						ratio_pollution = prob_e1_and_e2/prob_e
						coinc = "coinc maxi: "+format(ratio_pollution*100,".2f")+"%"
					else:
						coinc = ""
					if warning:
						for nrj_used in l_nrj_used:
							if abs(nrj_used-e)<keV_max:
								doprint = True
					if doprint:
						lprint = aff(path.split("/")[-1].split("_")[0])+aff(e)+"= "+aff(e1)+"+ "+aff(e2)+"+ "+aff(format(e-(e1+e2), ".3f"))+" // "
						lprint += aff(format(l_inten[o],".2f")) +"vs "+aff(format(l_inten[i],".2f"))+"+ "+aff(format(l_inten[j],".2f"))+aff(coinc,19)+ coincbonus
						out += lprint + "\n"
						print(lprint)
	return out
print()
out = ""
out += do_your_job2("data_spectrometry/Cs134_nndc")
out += do_your_job2("data_spectrometry/Eu152_nndc")
open("check_cascade.txt","w").write(out)
