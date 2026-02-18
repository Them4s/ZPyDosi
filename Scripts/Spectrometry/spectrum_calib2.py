# sudo apt-get remove python-scipy
# sudo python -m pip install scipy

import os, sys
from scipy.optimize import curve_fit
import numpy as np
import scipy 
print(scipy.__version__)

from utils_p5 import *
from scipy.optimize import curve_fit
from random import gauss

print()

print("#"*50)

path_csv = get_param_vari("csv" , str, None)
case_csv = get_param_vari("case", str, None)
sig_src_to_zero = get_param_vari("sig_src_to_zero", bool, "False")
dnrj_out = get_param_vari("dnrj_out", int, "3")



input_csv = CsvSeeker(path_csv)



abs_sig     = get_param_vari("abs_sig", bool, "y")
l_path_in   = get_param_vari("l_in",     str, "spectrum_count_out").split("/")
n_sample    = get_param_vari("n_sample",  int, "2048")

sig_lim_cut = input_csv.get(case_csv, "sigma_cut [%]", float)/100
order       = input_csv.get(case_csv, "fit_order",         int  )
check_cascade = input_csv.get(case_csv, "check_cascade",         bool  )


print(aff_s_v("fit order",order))
print(aff_s_v("sig_lim_cut [%]",sig_lim_cut*100))

l_path_in = lmap(lambda s: "spectrum_count_out/"+s, input_csv.get_list(case_csv, "eff_data","path_list", str))

print("#"*50)

mk_dir("spectrum_calib_out")


if abs_sig == False:
    print("#"*50)
    print("# WARNING - abs_sig is on False, the recommanded value is True")
    print("#           True  -> uses sigma as a real sigma (from statistics)")
    print("#           False -> uses sigma as a relative weight between points...")
    print("#"*50)

fig = plt.figure(2, figsize=(14.,5.7))
fig.patch.set_facecolor('white')
axloc = my_sub6(fig,1,2,0, list_rx=[1], list_ry=[1.,1.], mg=0.25, md=0)
axmat = my_sub6(fig,1,2,1, list_rx=[1], list_ry=[1.], mg=0.14)[0,0]

                                                        ###################
                                                        # usefull functions
def my_fct(l_x, *p):
    v = 0.
    l_x = np.log10(l_x)
    for n in range(len(p)):
        v += p[n]*l_x**n
    return v
'''
def my_fct_log(l_x, *p):
    v = 0.
    #l_x = np.log10(l_x)
    for n in range(len(p)):
        v += p[n]*l_x**n
    return v'''

def my_fct_var(l_x, p, cov):
    sol = []
    l_x = np.log10(l_x)
    for x in l_x:
        S = np.array(list(map(lambda i: x**i, range(len(p)))))
        sol += [S.T.dot(cov.dot(S))]
    return np.array(sol)
                                                        ###########################


class SrcMeas:
    def __init__(self, l_x, l_y, l_s, l_srel_decay, s_src, name):
        self.l_x   = np.array(l_x)
        self.l_y   = np.array(l_y)
        self.l_s   = np.array(l_s)
        self.l_srel_decay   = np.array(l_srel_decay)
        self.s_src = s_src
        self.name  = name

l_meas = []
d_forbid = {}
if check_cascade:
    if not os.path.exists("check_cascade.txt"):
        print("ERROR - check_cascade.txt file does not exist - please run <python $path_python/check_cascade.py>")
        exit()
    for line in open("check_cascade.txt").readlines():
        if "coinc maxi" in line and float(line.split()[16][:-1])>0.4:
            #print(line)
            d_forbid[(line.split()[0], float(line.split()[1]))] = line[:-1]
#exit()
#print(d_forbid)
        
for path_in in l_path_in:
    lines = open(path_in).readlines()
    activity_sig_rel = float(lines.pop(0).split()[-1])/100
    if sig_src_to_zero:
        activity_sig_rel = 0
    print(aff_s_v("path",path_in))
    print(aff_s_v("  activity_sig_rel [%]",activity_sig_rel*100))
    entete = lines.pop(0)
    id_nrj_, id_ratio, id_eff, id_sig = map(lambda name: entete.split().index(name), "nrj ratio eff eff_sig".split())
    l_x, l_y, l_s, l_srel_decay       = map(lambda id_data: list(map(lambda line: float(line.split()[id_data]), lines)), [id_nrj_, id_eff, id_sig, id_ratio+2])
    i=0
    
    while i<len(l_x):
        forbidden = False
        srt_forbid = ""
        for elt_nrj, line in d_forbid.items():
            elt, nrj_forbid = elt_nrj
            if elt in path_in and abs(l_x[i] - nrj_forbid)<1:
                forbidden = True
                srt_forbid = line
        if l_s[i]/l_y[i]>sig_lim_cut or l_y[i]<0 or forbidden:
            print("    pop2",aff(l_x[i]),aff(format(l_y[i], ".4f")),aff(format(l_s[i]/l_y[i], ".4f")), srt_forbid)
            l_x.pop(i)
            l_y.pop(i)
            l_s.pop(i)
            l_srel_decay.pop(i)
        else:
            i += 1
    l_meas += [SrcMeas(l_x, l_y, l_s, l_srel_decay, activity_sig_rel, path_in.split("/")[-1].split("_")[0])]
    

#l_meas += [SrcMeas([1000], [0.001334], [0.001322*0.003], 0.002)]

#475+563 = 1038
#563+604 = 1167
#569+795 = 1364
#604+795 = 1399 (check)
# https://upload.wikimedia.org/wikipedia/commons/1/12/Cs-134_decay_scheme.svg

nb_pts = sum(map(lambda meas: len(meas.l_x), l_meas))

l_x_tot, l_y_tot, l_s_tot, cov_tot = np.zeros(nb_pts), np.zeros(nb_pts), np.zeros(nb_pts), np.zeros((nb_pts,nb_pts))

pos_pt = 0
for i, meas in enumerate(l_meas):
    l_s_ac_src = (meas.l_s**2+(meas.l_y*meas.s_src)**2)**0.5
    axloc[0,1].errorbar(meas.l_x,meas.l_y*100, yerr=meas.l_s*100,   fmt='.', c=get_c(i,len(l_meas)), zorder=100, alpha=0.6, capthick=2, capsize=3)
    axloc[0,1].errorbar(meas.l_x,meas.l_y*100, yerr=l_s_ac_src*100, fmt='.', c=get_c(i,len(l_meas)), zorder=100, alpha=0.6, capthick=2, capsize=6)
    nb_pts_i = len(meas.l_x)
    print("Y",meas.l_y)
    print("X",meas.l_x)
    l_y_toto ,sub_cov = cov_mult((meas.l_y,          np.diag(meas.l_s**2)),                       # uncorrelated component : peak stat unc
                                 (np.ones(nb_pts_i), np.ones((nb_pts_i,nb_pts_i))*meas.s_src**2)) #   correlated component : src uncertainty
    l_x_tot[pos_pt:pos_pt+nb_pts_i] = meas.l_x
    l_y_tot[pos_pt:pos_pt+nb_pts_i] = meas.l_y
    l_s_tot[pos_pt:pos_pt+nb_pts_i] = meas.l_s
    cov_tot[pos_pt:pos_pt+nb_pts_i, pos_pt:pos_pt+nb_pts_i] = sub_cov
    pos_pt += nb_pts_i

x_min, x_max =  min(l_x_tot),max(l_x_tot)
l_x_fine = np.arange(int(x_min), int(x_max)+1, dnrj_out)
print("X",l_x_tot)
print("Y",l_y_tot)

best_p, covar = curve_fit(my_fct, l_x_tot, l_y_tot, p0=[0]*(order), sigma=cov_tot, absolute_sigma=abs_sig, maxfev=10000)    # do the big fit
sol, sol_sig  = my_fct(l_x_fine, *best_p), my_fct_var(l_x_fine, best_p, covar)**0.5                        # get the fit curve
aff_curve(axloc[0,1], l_x_fine, sol*100, sol_sig*100,"black",1,0.2)                                    # and plot the uncertainty
print("covar",covar)  
for i, meas in enumerate(l_meas):
    l_s_ac_src = (meas.l_s**2+(meas.l_y*meas.s_src)**2)**0.5
    sol_peak  = my_fct(meas.l_x, *best_p)
    axloc[0,0].errorbar(meas.l_x,(meas.l_y/sol_peak-1)*100, yerr=(meas.l_srel_decay)*100,   fmt='.', markersize='0',c=get_c(i,len(l_meas)), zorder=100, alpha=0.5, capthick=2, capsize=4)
    axloc[0,0].errorbar(meas.l_x,(meas.l_y/sol_peak-1)*100, yerr=(meas.l_s/sol_peak)*100,   fmt='.', markersize='0',c=get_c(i,len(l_meas)), zorder=100, alpha=0.5, capthick=2, capsize=4)
    axloc[0,0].errorbar(meas.l_x,(meas.l_y/sol_peak-1)*100, yerr=(l_s_ac_src/sol_peak)*100, fmt='.', markersize='0',c=get_c(i,len(l_meas)), zorder=100, alpha=0.5, capthick=2, capsize=4)
    nro, elt = meas.name, ""
    print (nro)
    while nro[0] not in "0123456789":
        nro, elt = nro[1:], elt+nro[0]
    
    #axloc[0,0].text(meas.l_x[0], ((meas.l_y+l_s_ac_src)/sol_peak-1)*100, tex("^{"+nro+"}"+elt))
    pos = list(meas.l_x).index(min(meas.l_x))
    axloc[0,0].text(meas.l_x[pos], ((meas.l_y+l_s_ac_src)/sol_peak-1)[pos]*100+(1.5 if elt!="Eu" else 1.), tex("^{"+nro+"}"+elt),
            color=get_c(i,len(l_meas)), fontsize=get_aff_size("s_xylabel")*0.75)

    #.text(xlim[0]+(xlim[1]-xlim[0])*0.05,ylim[0]+(ylim[1]-ylim[0])*0.1,
    #            tex(in_1_sig+", "+in_2_sig+s_out), va='top', zorder = 7, fontsize=s)
aff_curve(axloc[0, 0], l_x_fine, sol/sol-1, sol_sig/sol*100,"black",1,0.2)




print(aff_s_v("best_p =","["+",".join(map(lambda v:str(v),best_p))+"]"))

#print(covar)

axloc[0, 0].set_ylim((-5, 5))


res  = l_y_tot - my_fct(l_x_tot, *best_p)
chi2 = (res.T).dot(np.linalg.inv(cov_tot).dot(res))
print("chi2", chi2)
l_chi2_samp = []
for i in range(2048):
    loc_p = np.random.multivariate_normal(best_p, covar)
    l_y_best_fit = my_fct(l_x_tot, *best_p)
    l_y_samp_fit = my_fct(l_x_tot, *loc_p)
    res = l_y_samp_fit - l_y_best_fit
    l_chi2_samp += [(res.T).dot(np.linalg.inv(cov_tot).dot(res))]
print(aff_s_v("moy/var (old)",imoyvar_list(l_chi2_samp)))


l_chi2_samp = []                    # new
for i in range(2048):
    l_y_best_fit = my_fct(l_x_tot, *best_p)
    l_y_samp_fit = np.random.multivariate_normal(l_y_best_fit, cov_tot)
    ires = l_y_samp_fit - l_y_best_fit
    l_chi2_samp += [(ires.T).dot(np.linalg.inv(cov_tot).dot(ires))]


tmp = np.array(sorted(l_chi2_samp)+[1e100])
fract_chi2 = list(tmp<chi2).index(False) / (len(tmp)-1)*100
print("assuming that the fit val&cov is the Truth, an eff. sampling at the same nrj show that this chi2 contains",fract_chi2,"% of values...")
print(aff_s_v("moy/var",imoyvar_list(l_chi2_samp)))

#e_msh_cov = l_x_fine*1.
e_msh_cov = np.arange(int(x_min), int(x_max)+1, dnrj_out)

print("sampling")
l_etalo = []
for i in range(n_sample):
    loc_p = np.random.multivariate_normal(best_p, covar)
    sol = my_fct(e_msh_cov, *loc_p)
    #sol *= gauss(1,0.005)
    l_etalo += [sol]
    #if i<512 or True:
    #    axloc[0,1].plot(e_msh_cov, sol*100,c="black", alpha = 0.01)
    #    axloc[0,0].plot(e_msh_cov, (sol-sol_ref)/sol_ref*100,c="black", alpha = 0.01)

print("covar calc")
#cov, cor, cov_s, cor_s = icovar_jkk(l_etalo, l_w=None, do_cor=True, do_jackknife=True, fast_jackknife=True, blabla=False, nb_jkk=128, fast=True)
#print("maxcor",cor_s.max())
cov, cor = icovar_jkk(l_etalo, l_w=None, do_cor=True, do_jackknife=False, fast_jackknife=True, blabla=False, nb_jkk=128, fast=True)
print("ok")


sol, sol_sig  = my_fct(e_msh_cov, *best_p), my_fct_var(e_msh_cov, best_p, covar)**0.5                        # get the fit curve
open("spectrum_calib_out/calib.txt","w").write(
    "raw_data_e "+" ".join(map(lambda v:aff(v, 23),l_x_tot))+"\n"+
    "raw_data_v "+" ".join(map(lambda v:aff(v, 23),l_y_tot))+"\n"+
    "raw_data_s "+" ".join(map(lambda v:aff(v, 23),l_s_tot))+"\n"+
    "nrj        "+" ".join(map(lambda v:aff(v, 23),e_msh_cov))+"\n"+
    "eff        "+" ".join(map(lambda v:aff(v, 23),sol))+"\n"+
    "stdv       "+" ".join(map(lambda v:aff(v, 23),sol_sig))+"\n"+
    "stdv_rel   "+" ".join(map(lambda v:aff(v, 23),sol_sig/sol))+"\n"+
    "corr   \n"+"\n".join(map(lambda l: " ".join(map(lambda v:aff(v, 23),l)), list(cor)))#+"\n"+
    )


aff_mat4(e_msh_cov, e_msh_cov, cor, axmat, "vertical", None, "Energy [keV]", "Energy [keV]",
        minimaxi=(-1,1.002), logz=False, logx=False, logy=False, smooth=None, pad=0.05, pcol=True, head_top=True, midblanc=True)

axloc[0,0].set_xlim([e_msh_cov[0]-20, e_msh_cov[-1]+20])
axmat.set_xlim([e_msh_cov[0], e_msh_cov[-1]])
axmat.set_ylim([e_msh_cov[-1],e_msh_cov[0]])


axmat.set_xlabel(tex(r"Energy\,[keV]"), size=get_aff_size("s_xylabel"))
axmat.set_ylabel(tex(r"Energy\,[keV]"), size=get_aff_size("s_xylabel"))

axloc[0,1].set_ylabel(tex(r"Efficiency\,[\%]"), size=get_aff_size("s_xylabel"))
#axloc[0,0].set_ylabel(tex(r"\nicefrac{\mathrm{eff.}}{\mathrm{eff.}}\,[\sigma]"), size=get_aff_size("s_xylabel"))
axloc[0,0].set_ylabel(tex(r"Residual\,[\%]"), size=get_aff_size("s_xylabel"))
axloc[0,0].set_xlabel(tex(r"Energy\,[keV]"), size=get_aff_size("s_xylabel"))


axloc[0,1].set_ylim([0,axloc[0,1].get_ylim()[-1]])
axloc[0,1].set_xticklabels([])








do_ref = False

if do_ref:                                                            # plot the geni2000 results
    if False:
        #eff = EfficiencyCalibration("calib_out_2019_02_25_p13_100h")
        eff = EfficiencyCalibration("calib_L1_p13_2019_03_01_100h")
        sol_ref_nrj, sol_ref, sol_ref_sig = eff.nrj, eff.eff, eff.eff_sig
        sol_ref     = projet_vec_interpol(tab_x, np.log(sol_ref_nrj), sol_ref)
        sol_ref_sig = projet_vec_interpol(tab_x, np.log(sol_ref_nrj), sol_ref_sig)
        
        aff_curve(axloc[0,2], np.exp(tab_x),  sol_ref*100,            sol_ref_sig,"black",1,0.2)
        aff_curve(axloc[0,1], np.exp(tab_x), (sol_ref/sol-1)*100, sol_ref_sig/sol*100,"black",1,0.2)
        
    else:
        eff = EfficiencyCalibrationG2K("toto")
        #sol_ref = eff.get_eff(np.exp(l_x_fine))
        #sol_ref_sig = sol_ref*0
        axloc[0,0].errorbar(eff.raw_data_e,(eff.raw_data_v/my_fct(eff.raw_data_e, *best_p)-1)*100, yerr=eff.raw_data_v, fmt='o', c="red", zorder=100, alpha=0.6)
        axloc[0,1].errorbar(eff.raw_data_e,eff.raw_data_v*100, yerr=eff.raw_data_v*0, fmt='o', c="red", zorder=100, alpha=0.6)
        #axref[0,0].errorbar(np.log(eff.raw_data_e),eff.raw_data_v, yerr=eff.raw_data_v*0, fmt='o', c="red", zorder=100, alpha=0.6)
        #aff_curve(axref[0,0], tab_x,         sol_ref, sol_ref_sig,"black",1,0.2)
    #aff_curve(axloc[0,2], np.exp(tab_x), sol_ref*100, sol_ref_sig*100,"black",1,0.2)
    #aff_curve(axloc[0,1], np.exp(tab_x), (sol_ref/sol-1)*100, sol_ref_sig/sol*100,"black",1,0.2)


fig.savefig("spectrum_calib_out/calib.png", bbox_inches=('tight'), dpi=200)


plt.show()
