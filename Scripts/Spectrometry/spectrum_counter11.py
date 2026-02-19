from random import gauss
from ..Analysis.cnf import read_cnf_file
import datetime as dtime
import math

import os
from scipy.optimize import curve_fit
from ZPyDosi.Common.utils_general import lmap, get_aff_size, tex, str2time, dup, dupx, activity2float, set_nice_ax
from ZPyDosi.Common.CsvSeeker import CsvSeeker
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Prints.PrintnSave import aff_s_v, aff_s_v_vs
from ZPyDosi.Plots.SubPlots import my_sub6, aff_curve
import numpy as np
import matplotlib.pyplot as plt

print()

print("#"*50)

path_csv = get_param_vari("csv" , str, None)
case_csv = get_param_vari("case", str, None)

do_plot    = get_param_vari("plot", bool, "False")
do_dead_time_corr    = get_param_vari("dead_time_corr", bool, "True")

free_gain = get_param_vari("free_gain_keV", float, "0")
# free_gain = get_param_vari("free_gain_keV", float, "0")
Cumulative_bool= get_param_vari("cumulative_plot", bool, "True")
bkg_sub= get_param_vari("bkg_sub", bool, "False") #Now on False for new substractiomn method
bkg_peak= get_param_vari("bkg_peak", bool, "True") #Now on False for new substractiomn method
plot_only_bkg=get_param_vari("plot_only_bkg", bool, "False") #boolean to subtract or not the bkg
Triche=get_param_vari("Triche", bool, "False") #boolean  use of Zm bkg instead of Ho
print_true_bkg_stat=get_param_vari("print_true_bkg_stat", bool, "False") #boolean  use of Zm bkg instead of Ho
print("#"*50)
if bkg_peak and bkg_sub:
    bkg_sub=False
    print("peak identification mode on => bkg_sub forced to False")

global linearity_warning
linearity_warning = []



input_csv = CsvSeeker(path_csv)

is_peak=False
BKG_WARNING=False
gene_key = "generic"

path_generic_data       = input_csv.get(gene_key, "path_data", str)
path_src_measurement    = input_csv.get(case_csv, "path_data", str)
if "Ho" not in path_src_measurement:
    Triche=False
path_src_bkgrd          = input_csv.get(case_csv, "path_bkg",  str, None)
if path_src_bkgrd is None:
    name_hpge = path_src_measurement.split("/")[-1].split("_")[6]
    path_src_bkgrd          = input_csv.get(case_csv, "path_bkg_"+name_hpge,  str)


bkg_area = 0
bkg_sig  = 0
if Triche:
    print("Triche ON")
    bkg_sub = True
    bkg_peak=False
    factor_triche=18.8454511524465/18.29503560024 #Ratio between eff of Hornli and Zmutt
    path_src_bkgrd          = input_csv.get(case_csv, "path_bkg_Zm",  str)
    bkg_area=27288.766237*factor_triche
    bkg_sig=1194.253538*factor_triche

labo_ref                = input_csv.get(case_csv, "labo_ref", str)
#ab            = input_csv.get(case_csv, "a/b", str, None)

path_generic_data = os.path.expandvars(path_generic_data)

print(aff_s_v("path_generic_data",    path_generic_data))
print(aff_s_v("path_src_measurement", path_src_measurement))
print(aff_s_v("path_src_bkgrd",       path_src_bkgrd))

l_param_nrj_calib = input_csv.get(case_csv, "nrj_calib", default=None, all_line=True)
if l_param_nrj_calib is None:
    name_hpge = path_src_measurement.split("/")[-1].split("_")[6]
    l_param_nrj_calib = input_csv.get(case_csv, "nrj_calib_"+name_hpge, all_line=True)

l_param_nrj_calib = l_param_nrj_calib[1:]

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



name_src  = "_".join(path_src_measurement.split("/")[-1].split("_")[8:]).replace(".TKA","")
mat_src = name_src.replace("_","-").split("-")[0]
name_hpge = path_src_measurement.split("/")[-1].split("_")[6]

print(aff_s_v("name_src", name_src))
print(aff_s_v("name_hpge", name_hpge))
print(aff_s_v("mat_src", mat_src))
print(aff_s_v("labo_ref", labo_ref))



if name_src not in input_csv.get_list(gene_key, "source_description", "name"):
    
    src_descr = None
else:
    def src_param(s):
        #return input_csv.get_list(gene_key, input_csv.get_line_starting_with(name_src, None)[0],s, str)[0]
        return input_csv.get_in_list(gene_key, "source_description", "name", name_src, s, str)
    
    src_descr = {
        "period":      str2time(src_param("period")),
        "sig_period":      str2time(src_param("period_sig")),
        "time":          dtime.datetime(*map(lambda s:int(s), src_param("date").replace("/","_").split("_"))),
        "activity":      activity2float(src_param("activity")),
        "activity_sig_pc":src_param("activity_sig [%]")}

print(aff_s_v("calibration src mode", src_descr is not None))
print(src_descr)
l_key_truc = input_csv.get_list(gene_key, "tab_mat2peak", mat_src, str)
if l_key_truc is None:
    print("Error - no <"+mat_src+"> in tab_mat2peak")
    exit()
print(l_key_truc)
path_nrj_param = path_generic_data+"/spectrum_plot_out_"+l_key_truc[0]+"_"+labo_ref
print(aff_s_v("path_nrj_param",path_nrj_param))


try:
    lines_nrj_param        = list(filter(lambda s:s[0]!="#", open(path_nrj_param).readlines()[1:]))
except:
    print("ERROR - pb with",path_nrj_param,"have you run the spectrum_plot3.py script to get the peak integration zone?")
    exit()
n_col = 4 if len(lines_nrj_param)<12 else 5



nx,ny = n_col, 1+math.ceil(len(lines_nrj_param)/n_col)

fig = plt.figure(0, figsize=(15.,10.))
print("coucou")
fig.patch.set_facecolor('white')
nx,ny
ax2 = my_sub6(fig, 1+ny, 1, 0, list_rx=[1], list_ry=[1], auto_x=True, auto_y=False)[0,0]

ax2.set_yscale("log")

def get_spectrum(path):
    lines = open(path).readlines()
    t_eff, t_total = map(lambda v:float(v), lines[:2])
    if os.path.isfile(path.replace(".TKA",".CNF")):
        c = read_cnf_file(path.replace(".TKA",".CNF"), 'TRUE')
        dead_time=(c["Real time"]-c["Live time"])/c["Real time"]
    else :
        print("Warning : No CNF file, using TKA")
        dead_time=(t_total-t_eff)/t_total
    dead_time_correction = 1/(1-dead_time)
    print(aff_s_v("dead_time_correction", dead_time_correction), path.replace(".TKA",".CNF"))
    l_v = np.array(lmap(lambda l:float(l),lines[2:]))
    l_s = l_v**0.5
    return l_v*dead_time_correction, l_s*dead_time_correction, l_v, l_s, t_total, dead_time
    # C * t_total/t_eff
    # dt = 1-t_eff/t_tot
    # C * (1-deattime)
    
def find_nrj(l_e,v):
    i = 0
    while l_e[i]<v and i+1<len(l_e):
        i+= 1
    return i
    
def integ(l_v):
    l_v2 = l_v + 0
    l_v2[0] = l_v[0]
    for i in range(len(l_v))[1:]:
        l_v2[i] = l_v2[i-1]+l_v[i]
    return l_v2
l_meas_v, l_meas_s, l_meas_v_not_corr, l_meas_s_not_corr, meas_t, meas_dead_time = get_spectrum(path_src_measurement)                        # data measurment
if path_src_bkgrd is None or path_src_bkgrd=="" :
    l_bkgd_v, l_bkgd_s, bkgd_t = l_meas_v*0, l_meas_s*0, 1.
    l_bkgd_v2, l_bkgd_s2, bkgd_t2 = l_meas_v*0, l_meas_s*0, 1.
elif bkg_peak:
    l_bkgd_v, l_bkgd_s, bkgd_t = l_meas_v*0, l_meas_s*0, 1.
    l_bkgd_v2, l_bkgd_s2, l_bkgd_v_not_corr2, l_bkgd_s_not_corr2, bkgd_t2, bkgd_dead_time2 = get_spectrum(path_src_bkgrd)  # get bkg for peak identification 
    if not(print_true_bkg_stat):l_bkgd_v2, l_bkgd_s2, l_bkgd_v_not_corr2, l_bkgd_s_not_corr2 = map(lambda data:data*meas_t/bkgd_t2, [l_bkgd_v2, l_bkgd_s2, l_bkgd_v_not_corr2, l_bkgd_s_not_corr2])
    if Triche: 
        # l_bkgd_v, l_bkgd_s, l_bkgd_v_not_corr, l_bkgd_s_not_corr = l_bkgd_v*0,l_bkgd_v*0,l_bkgd_v*0,l_bkgd_v*0    # Triche: correction between efficiency of Zmutt and Hornli
        bkg_area*=meas_t/bkgd_t2
        bkg_sig*=meas_t/bkgd_t2
elif (not bkg_sub): # Key word : Background_sub : added the bool to unilateraly disable subtraction.
    l_bkgd_v, l_bkgd_s, bkgd_t = l_meas_v*0, l_meas_s*0, 1.   # set background to the same measurment time
else:
    print("test")
    l_bkgd_v, l_bkgd_s, l_bkgd_v_not_corr, l_bkgd_s_not_corr, bkgd_t, bkgd_dead_time = get_spectrum(path_src_bkgrd)                    # background measurment
    l_bkgd_v, l_bkgd_s, l_bkgd_v_not_corr, l_bkgd_s_not_corr  = map(lambda data:data*meas_t/bkgd_t, [l_bkgd_v, l_bkgd_s, l_bkgd_v_not_corr, l_bkgd_s_not_corr])    # set background to the same measurment time
    if Triche: 
        l_bkgd_v, l_bkgd_s, l_bkgd_v_not_corr, l_bkgd_s_not_corr = l_bkgd_v*0,l_bkgd_v*0,l_bkgd_v*0,l_bkgd_v*0    # Triche: correction between efficiency of Zmutt and Hornli
        bkg_area*=meas_t/bkgd_t
        bkg_sig*=meas_t/bkgd_t




#l_e = np.array(range(len(l_meas_v))) * a + b                                 # energies in KeV
l_e = fct_pos2nrj(np.array(range(len(l_meas_v))))                            # energies in KeV
if not plot_only_bkg: aff_curve(ax2, dupx(l_e), dup(l_meas_v), dup(l_meas_s),"blue" ,1,0.2, label=tex("raw"))
aff_curve(ax2, dupx(l_e), dup(l_bkgd_v), dup(l_bkgd_s),"green",1,0.2, label=tex("background"))
if not plot_only_bkg: aff_curve(ax2, dupx(l_e), dup(l_meas_v-l_bkgd_v), dup((l_bkgd_s**2+l_meas_s**2)**0.5),"red",1,0.2, label=tex("final"))
ax2.legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)

ax2.set_xlabel(tex(r"Energy [keV]"), size=get_aff_size("s_xylabel"))
ax2.set_ylabel(tex(r"Counts"),    size=get_aff_size("s_xylabel"))
ax2.set_ylim([0.5, ax2.get_ylim()[1]])
old_meas_v=l_meas_v
old_meas_s=l_meas_s
if do_dead_time_corr:
    l_meas_v = l_meas_v-l_bkgd_v
    l_meas_s = (l_bkgd_s**2+l_meas_s**2)**0.5
else : 
    l_meas_v = l_meas_v_not_corr-l_bkgd_v
    l_meas_s = (l_bkgd_s**2+l_meas_s_not_corr**2)**0.5


d_resu = {"nrj":[], "th_ratio":[], "th_ratio_s":[], "measure":[], "measure_s":[], "measure_s_model":[], "is_sum":[], "sig_mes":[]}
print(lines_nrj_param)
for i_line, line in enumerate(lines_nrj_param):
    e_min1,  e_min2,  e_max1,  e_max2, e_v, e_s, r_v, r_s = map(lambda s:float(s), line.split()[:8])
    shape = line.split()[8]
    ei_min1, ei_min2, ei_max1, ei_max2, ei_v = map(lambda v:find_nrj(l_e,v), [e_min1, e_min2, e_max1, e_max2, e_v])

    if free_gain>0:
        di = find_nrj(l_e, [e_v+free_gain])-find_nrj(l_e, [e_v])    # largeur de la zone a sonder en bins
        maxi = np.amax(l_meas_v[int(ei_v - di):int(ei_v + di)])     # valeur max obtenue
        #exit()
        ei_v_corrected = int(ei_v - di) + list(l_meas_v[int(ei_v - di):int(ei_v + di)]).index(maxi)                 # bin associe a la valeur max
        #print(maxi, ei_v_corrected, ei_v)
        fact_gain = ei_v_corrected / ei_v                           # facteur correctif
        print("free gain correction value:",fact_gain)              # say hello
        l_e /= fact_gain                                            # corrige la liste des energies precedament calculee
        ei_min1, ei_min2, ei_max1, ei_max2, ei_v = map(lambda v:find_nrj(l_e,v), [e_min1, e_min2, e_max1, e_max2, e_v])
                                                                    # corrige les bornes d'integration
        
        #exit()
        #ei_min1, ei_min2, ei_max1, ei_max2, ei_v = map(lambda v:int(v*fact_gain), [ei_min1, ei_min2, ei_max1, ei_max2, ei_v])
    #print(e_min1,  e_min2,  e_max1,  e_max2, e_v)
    #print(ei_min1, ei_min2, ei_max1, ei_max2, ei_v)
    
    #exit()
    if Cumulative_bool :
        ax_i_b, ax_i_m, ax_i_h = my_sub6(fig, 2+ny, nx, 2*nx + i_line, list_rx=[1], list_ry=[1,1,1], auto_x=True, auto_y=False, mg=0.3, md=0.1)[0,:]
        l_plot = [ax_i_b, ax_i_m, ax_i_h]
    else :
        ax_i_m, ax_i_h = my_sub6(fig, 2+ny, nx, 2*nx + i_line, list_rx=[1], list_ry=[1,1], auto_x=True, auto_y=False, mg=0.3, md=0.1)[0,:]
        l_plot = [ax_i_m, ax_i_h]
        
    for ax in l_plot:
        set_nice_ax(ax, x="", y="pow", powmodulo=None)
    
    ax_i_b.set_xlabel(tex(r"Energy [keV]"),    size=get_aff_size("s_xylabel")) if Cumulative_bool else ax_i_m.set_xlabel(tex(r"Energy [keV]"),    size=get_aff_size("s_xylabel"))
    if Cumulative_bool : ax_i_b.set_ylabel(tex(r"Cumulative"),    size=get_aff_size("s_xylabel"))  
    ax_i_m.set_ylabel(tex(r"Counts"),    size=get_aff_size("s_xylabel"))
    ax_i_h.set_ylabel(tex(r"Counts"),    size=get_aff_size("s_xylabel")) 
    
    if Cumulative_bool : ax_i_m.set_xticklabels([])
    ax_i_h.set_xticklabels([])
    
    aff_curve(ax_i_m, dupx(l_e[ei_min1:ei_max2]), dup(l_meas_v[ei_min1:ei_max2]), dup(l_meas_s[ei_min1:ei_max2]),"red",1,0.2)
    aff_curve(ax_i_h, dupx(l_e[ei_min1:ei_max2]), dup(l_meas_v[ei_min1:ei_max2]), dup(l_meas_s[ei_min1:ei_max2]),"red",1,0.2)
    
    def fct_noise_lin (x,a,b): return a*x+b
    def fct_noise_step(x,a):   return 0*x+a
    fct_noise_left  = fct_noise_lin if shape.split('/')[0] == "lin" else fct_noise_step
    fct_noise_right = fct_noise_lin if shape.split('/')[1] == "lin" else fct_noise_step
    
    def fit(ei1, ei2, fct_noise, with_plot=True):
        param, covar = curve_fit(fct_noise, l_e[ei1:ei2], l_meas_v[ei1:ei2], maxfev=1000)
        l_e_zoom = np.arange(l_e[ei1],l_e[ei2],0.1)
        if with_plot :
            ax_i_m.plot(l_e_zoom, fct_noise(l_e_zoom, *param), "green", linewidth=2)
            # ax_i_h.plot(l_e_zoom, fct_noise(l_e_zoom, *param), "green", linewidth=2)
        return param, covar
    param_left, covar_left  = fit(ei_min1, ei_min2, fct_noise_left)
    param_right, covar_right = fit(ei_max1, ei_max2, fct_noise_right)
                                #linearity test using covar on estimated parameter 
    SE_left= np.sqrt(np.diag(covar_left))
    SE_right= np.sqrt(np.diag(covar_right))
    param_lin_left, covar_lin_left = fit(ei_min1, ei_min2, fct_noise_lin, False)
    param_lin_right, covar_lin_right = fit(ei_max1, ei_max2, fct_noise_lin, False)
    SE_lin_left = np.sqrt(np.diag(covar_lin_left))
    SE_lin_right = np.sqrt(np.diag(covar_lin_right))
    is_left_cst = True if abs(param_lin_left[0])<SE_lin_left[0] else False
    is_right_cst = True if abs(param_lin_right[0])<SE_lin_right[0] else False
    
                                 # warning for first nrj param    
    if i_line == 0 :                                 
        if shape.split('/')[0] == "lin" and is_left_cst :
            linearity_warning += "spectrum " 
            linearity_warning += str(case_csv)
            linearity_warning += " left side not that linear \n " 
        if shape.split('/')[1] == "lin" and is_right_cst :
            linearity_warning += "spectrum " 
            linearity_warning += str(case_csv)
            linearity_warning += " right side not that linear \n " 
        if shape.split('/')[0] == "step" and not is_left_cst :
            linearity_warning += "spectrum " 
            linearity_warning += str(case_csv)
            linearity_warning += " left side not that of a step \n "  
        if shape.split('/')[1] == "step" and  not is_right_cst :
            linearity_warning += "spectrum " 
            linearity_warning += str(case_csv)
            linearity_warning += " right side not that of a step \n " 
        else :                   # do not forget to comment this
            linearity_warning += "spectrum test \n"

    tot_bkg=0
    sig_tot_bkg=0
    #Check if back ground is flat
    if bkg_peak:
        if print_true_bkg_stat:
            f_bkg_stat=1/(meas_t/bkgd_t2)
            print("COUCOU",f_bkg_stat)
            # l_bkgd_v2*=f_bkg_stat
        
        def fit(ei1, ei2, fct_noise, with_plot=True):
            param, covar = curve_fit(fct_noise, l_e[ei1:ei2], l_bkgd_v2[ei1:ei2], maxfev=1000)
            l_e_zoom = np.arange(l_e[ei1],l_e[ei2],0.1)
            if with_plot :
                ax_i_m.plot(l_e_zoom, fct_noise(l_e_zoom, *param), "green", linewidth=2)
                # ax_i_h.plot(l_e_zoom, fct_noise(l_e_zoom, *param), "green", linewidth=2)
            return param, covar
        param_left_bkg, covar_left_bkg  = fit(ei_min1, ei_min2, fct_noise_left)
        param_right_bkg, covar_right_bkg = fit(ei_max1, ei_max2, fct_noise_right)
        p_lin,c_lin=curve_fit(fct_noise_lin, np.r_[l_e[ei_min1:ei_min2],l_e[ei_max1:ei_max2]], np.r_[l_bkgd_v2[ei_min1:ei_min2],l_bkgd_v2[ei_max1:ei_max2]], maxfev=1000)
                                    #linearity test using covar on estimated parameter 
        SE_left= np.sqrt(np.diag(covar_left_bkg))
        SE_right= np.sqrt(np.diag(covar_right_bkg))
        param_lin_left_bkg, covar_lin_left_bkg = fit(ei_min1, ei_min2, fct_noise_lin, False)
        param_lin_right_bkg, covar_lin_right_bkg = fit(ei_max1, ei_max2, fct_noise_lin, False)
        SE_lin_left = np.sqrt(np.diag(covar_lin_left_bkg))
        SE_lin_right = np.sqrt(np.diag(covar_lin_right_bkg))
        is_left_cst = True if abs(param_lin_left_bkg[0])<SE_lin_left[0] else False
        is_right_cst = True if abs(param_lin_right_bkg[0])<SE_lin_right[0] else False
        
                                    # warning for first nrj param    
        if i_line == 0 :                                 
            if shape.split('/')[0] == "lin" and is_left_cst :
                linearity_warning += "Background " 
                linearity_warning += str(case_csv)
                linearity_warning += " left side not that linear \n " 
                BKG_WARNING=True
            if shape.split('/')[1] == "lin" and is_right_cst :
                linearity_warning += "Background " 
                linearity_warning += str(case_csv)
                linearity_warning += " right side not that linear \n " 
                BKG_WARNING=True
            if shape.split('/')[0] == "step" and not is_left_cst :
                linearity_warning += "Background " 
                linearity_warning += str(case_csv)
                linearity_warning += " left side not that of a step \n "  
                BKG_WARNING=True
            if shape.split('/')[1] == "step" and  not is_right_cst :
                linearity_warning += "Background " 
                linearity_warning += str(case_csv)
                linearity_warning += " right side not that of a step \n " 
                BKG_WARNING=True
            else :                   # do not forget to comment this
                linearity_warning += "Background test \n"


        sig_bkg_left  = np.std(l_bkgd_v2[ei_min1:ei_min2]-fct_noise_left (l_e[ei_min1:ei_min2], *param_left_bkg )) / (ei_min2-ei_min1)**0.5
        sig_bkg_right = np.std(l_bkgd_v2[ei_max1:ei_max2]-fct_noise_right(l_e[ei_max1:ei_max2], *param_right_bkg)) / (ei_max2-ei_max1)**0.5
        l_e_zoom = l_e[ei_min1:ei_max2]
        noise_left  = fct_noise_left(l_e_zoom,  *param_left_bkg )
        noise_right = fct_noise_right(l_e_zoom, *param_right_bkg)
        door = np.clip((l_e_zoom-e_v)*100, a_min=0, a_max=1)
        print(door)
        print(len(noise_left),len(door))
        # noise = noise_left*(1-door) + noise_right*door
        noise=fct_noise_lin(l_e_zoom,*p_lin)
        l_bkg_v_zoom = l_bkgd_v2[ei_min1:ei_max2]
        tot_bkg = integ(l_bkg_v_zoom-noise)[-1]
        sig_tot_bkg=(sum(l_bkg_v_zoom)+(ei_v-ei_min2)*sig_bkg_left**2+(ei_max1-ei_v)*sig_bkg_right**2)**0.5
        print("counts in bkg = %f +- %f" % (tot_bkg,sig_tot_bkg) )
        if print_true_bkg_stat and i_line==2:
            plt.figure()
            plt.plot(l_e_zoom,l_bkg_v_zoom-noise)
            # plt.yscale("log")
            plt.figure()
            plt.plot(l_e[1000:],l_bkgd_v2[1000:])
            # plt.plot(l_e[ei_min1:ei_v],noise_left[:(ei_v-ei_min1)])
            # plt.plot(l_e[ei_v:ei_max2],noise_left[:(ei_max2-ei_v)])
            plt.plot(l_e[ei_min1:ei_max2],noise)
            # plt.yscale("log")
            plt.figure()
            plt.plot(l_bkgd_v2[1000:])
            plt.show()
            exit()
        if(tot_bkg/sig_tot_bkg)>3:
            linearity_warning += "WARNING A PEAK MAY BE IN THE BACKGROUND INTEGRATION ZONE \n"
            # is_peak=True

    
    #print("#"*10)
    #num_left = len(l_meas_v[ei_min1:ei_min2])
    #num_right = len(l_meas_v[ei_max1:ei_max2])
    #SD_left = np.std(l_meas_v[ei_min1:ei_min2],None,None,None,1)
    #SD_right = np.std(l_meas_v[ei_max1:ei_max2],None,None,None,1)
    #SD_SD_left = SD_left*(gamma((num_left-1)/2)/gamma(num_left/2))*((num_left-1)/2-(gamma(num_left/2)/gamma((num_left-1)/2))**2)**0.5
    #SD_SD_right = SD_right*(gamma((num_right-1)/2)/gamma(num_right/2))*((num_right-1)/2-(gamma(num_right/2)/gamma((num_right-1)/2))**2)**0.5
    #print( np.mean(l_meas_v[ei_min1:ei_min2])**0.5, SD_left, np.mean(l_meas_v[ei_max1:ei_max2])**0.5, SD_right)
    #
    #if i_line == 0 :                                 
    #    if abs(np.mean(l_meas_v[ei_min1:ei_min2])**0.5-SD_left)>SD_SD_left :
    #            linearity_warning += "spectrum " 
    #            linearity_warning += str(case_csv)
    #            linearity_warning += " left side not that Poissonian \n " 
    #    if abs(np.mean(l_meas_v[ei_max1:ei_max2])**0.5-SD_right)>SD_SD_right :
    #            linearity_warning += "spectrum " 
    #            linearity_warning += str(case_csv)
    #            linearity_warning += " right side not that Poissonian \n " 
        
    
    
    sig_left  = np.std(l_meas_v[ei_min1:ei_min2]-fct_noise_left (l_e[ei_min1:ei_min2], *param_left )) / (ei_min2-ei_min1)**0.5
    sig_right = np.std(l_meas_v[ei_max1:ei_max2]-fct_noise_right(l_e[ei_max1:ei_max2], *param_right)) / (ei_max2-ei_max1)**0.5
    #print(sig_left, sig_right)
    #sig_left  = ((sum(l_meas_v[ei_min1:ei_min2]) / (ei_min2-ei_min1))**0.5) / (ei_min2-ei_min1)**0.5
    #sig_right = ((sum(l_meas_v[ei_max1:ei_max2]) / (ei_max2-ei_max1))**0.5) / (ei_max2-ei_max1)**0.5
    #print(sig_left, sig_right)
    sig_zone_integ_g = (ei_v-ei_min2) * sig_left
    sig_zone_integ_d = (ei_max1-ei_v) * sig_right
    sig_zone_integ = (sig_zone_integ_g**2 + sig_zone_integ_d**2)**0.5
    #print(sig_left, sig_right, ei_v-ei_min2, ei_max1-ei_v)
    #print(sig_zone_integ_g, sig_zone_integ_d, sig_zone_integ)
    
    #print(ei_v-ei_min2 , ei_max1-ei_v)
    
    #l_e_zoom = np.arange(l_e[ei_min1],l_e[ei_max2],0.1)
    l_e_zoom = l_e[ei_min1:ei_max2]

    noise_left  = fct_noise_left(l_e_zoom,  *param_left )
    noise_right = fct_noise_right(l_e_zoom, *param_right)
    door = np.clip((l_e_zoom-e_v)*100, a_min=0, a_max=1)
    if Triche:
        p_lin,c_lin=curve_fit(fct_noise_lin, np.r_[l_e[ei_min1:ei_min2],l_e[ei_max1:ei_max2]], np.r_[l_meas_v[ei_min1:ei_min2],l_meas_v[ei_max1:ei_max2]], maxfev=1000)
        noise=fct_noise_lin(l_e_zoom,*p_lin)
    else:
        noise = noise_left*(1-door) + noise_right*door
    ax_i_m.plot(dupx(l_e_zoom), dup(noise), "green",alpha=0.5)
    ax_i_h.plot(dupx(l_e_zoom), dup(noise), "green",alpha=0.5)
    
    l_meas_v_zoom = l_meas_v[ei_min1:ei_max2]
    tot_bkgd_coup= sum(l_bkgd_s[ei_min1:ei_max2]**2)
    tot_simple_coup=sum(old_meas_v[ei_min1:ei_max2])
    if bkg_peak:
        print("tot count in area",sum(old_meas_v[ei_min2:ei_max1]),"+-",sum(old_meas_v[ei_min2:ei_max1])**0.5)
        print("tot bkg in area"  ,sum(l_bkgd_v2[ei_min2:ei_max1]) ,"+-",sum(l_bkgd_v2[ei_min2:ei_max1]) **0.5)
        print("delta Noise left",  np.mean(old_meas_v[ei_min1:ei_min2])*(ei_max1-ei_min2)/2,"+-"   , sum(old_meas_v[ei_min1:ei_min2])**0.5/(ei_min2-ei_min1)*(ei_max1-ei_min2)/2)
        print("delta Noise right", np.mean(old_meas_v[ei_max1:ei_max2])*(ei_max1-ei_min2)/2,"+-"   , sum(old_meas_v[ei_max1:ei_max2])**0.5/(ei_max2-ei_max1)*(ei_max1-ei_min2)/2)
        print("delta bkg Noise left",  np.mean(l_bkgd_v2[ei_min1:ei_min2])*(ei_max1-ei_min2)/2,"+-", sum(l_bkgd_v2[ei_min1:ei_min2] )**0.5/(ei_min2-ei_min1)*(ei_max1-ei_min2)/2)
        print("delta bkg Noise right", np.mean(l_bkgd_v2[ei_max1:ei_max2])*(ei_max1-ei_min2)/2,"+-", sum(l_bkgd_v2[ei_max1:ei_max2] )**0.5/(ei_max2-ei_max1)*(ei_max1-ei_min2)/2)
    zone_gauche_integ = integ((l_meas_v_zoom-noise)[:ei_min2-ei_min1])
    zone_droite_integ = integ((l_meas_v_zoom-noise)[-(ei_max2-ei_max1):])
    sig_model_bdf_left  = max(-min(zone_gauche_integ), max(zone_gauche_integ))
    sig_model_bdf_right = max(-min(zone_droite_integ), max(zone_droite_integ))
    l_meas_v_zoom
    if Cumulative_bool : ax_i_b.plot(dupx(l_e_zoom),dup(integ(l_meas_v_zoom)), "red")
    if Cumulative_bool : ax_i_b.plot(dupx(l_e_zoom),dup(integ(l_meas_v_zoom-noise)), "green")
    
    for ax_i in l_plot:
        ax_i.plot([e_min2,e_min2],ax_i.get_ylim(),c=(0.6,0.6,0.6))
        ax_i.plot([e_max1,e_max1],ax_i.get_ylim(),c=(0.6,0.6,0.6))
    n_min, n_max = map(lambda fct: fct(list(l_meas_v[ei_min1:ei_min2])+list(l_meas_v[ei_max1:ei_max2])), [min,max])            #min/max of the noise
    ax_i_m.set_ylim([max(0,n_min-(n_max-n_min)/4), n_max+(n_max-n_min)/4])
    tot_coups = integ(l_meas_v_zoom-noise)[-1]-tot_bkg*float(is_peak)-bkg_area*float(Triche)
    print("sig : sqrt(cps) =", tot_coups**0.5, "stat_leg =",sig_zone_integ, "pour info, sig model bdg gauche/droite =",sig_model_bdf_left, sig_model_bdf_right, "stat_bkg=",tot_bkgd_coup**0.5,"stat_simple=",tot_simple_coup**0.5)
    print(aff_s_v("energy",e_v,l1=12)+aff_s_v_vs("counts", tot_coups, (tot_coups + sig_zone_integ**2+sig_tot_bkg*float(is_peak)**2+bkg_sig*float(Triche)**2)**0.5,l1=12))
    d_resu["nrj"]        += [e_v]
    d_resu["th_ratio"]   += [r_v]
    d_resu["th_ratio_s"] += [r_s]
    d_resu["measure"]    += [integ(l_meas_v_zoom-noise)[-1]]
    d_resu["measure_s"]  += [integ(l_meas_v_zoom-noise)[-1]**0.5]
    
    
if linearity_warning :
    print("\n"+"#"*30+" Warning " +"#"*30+   "\n")
    print("".join(linearity_warning))
'''
src_Eu1 = {
    "period":     13.53 * 365 * 86400,
    "sig_period":     0.03 * 365 * 86400,
    "time":         dtime.datetime(*map(lambda s:int(s), "1999/01/13/12/00/00".split("/"))),
    "activity":     45400.,
    #"activity_sig":      0.005,
    "peaks_nrj":     d_resu["nrj"],
    "peaks_ratio":   d_resu["th_ratio"],
    "peaks_ratio_s": d_resu["th_ratio_s"]}
src_Eu2 = {
    "period":     13.53 * 365 * 86400,
    "sig_period":     0.03 * 365 * 86400,
    "time":         dtime.datetime(*map(lambda s:int(s), "1983/02/01/00/00/00".split("/"))),
    "activity":     1.36e-6*37e9,
    #"activity_sig":     0.02,
    "peaks_nrj":     d_resu["nrj"],
    "peaks_ratio":   d_resu["th_ratio"],
    "peaks_ratio_s": d_resu["th_ratio_s"]}

'''

if src_descr is None:
    if do_plot:
        #fig.savefig("spectrum_count.png", bbox_inches=('tight'), dpi=200)
        fig.savefig("spectrum_count_out/"+case_csv+".png", bbox_inches=('tight'), dpi=200)
    plt.show()
    exit()
    
src_descr["peaks_nrj"]     =     d_resu["nrj"]
src_descr["peaks_ratio"]   =     d_resu["th_ratio"]
src_descr["peaks_ratio_s"] =     d_resu["th_ratio_s"]

#if   "Eu_1999_01_13_45-4kBq" in path_src_measurement: src_Eu = src_Eu1
#elif "Eu_1983_1-36uCu"       in path_src_measurement: src_Eu = src_Eu2
#else:
#    print("src_name not defined (Eu_1999_01_13_45-4kBq or Eu_1983_1-36uCu)")
#    exit()


ye,mo,da,ho,mi,se = map(lambda s:int(s), path_src_measurement.split("/")[-1].split("_")[:6])

measurement_ref_lotus = {
    "time_start":    dtime.datetime(ye,mo,da,ho,mi,se),
    #"dead_time":    dead_time,
    "time_measurement":meas_t,
    "peaks_nrj":d_resu["nrj"],
    "peaks_measurment":d_resu["measure"],
    "peaks_measurment_s":d_resu["measure_s"]}

def eff_calc(src, measurement, nb_monte_carlo=10000): 
    decay_time = dtime.timedelta.total_seconds(measurement["time_start"]-src["time"])
    lambd,sig_lambd = np.log(2)/src["period"], np.log(2)/src["period"] * (src["sig_period"]/src["period"])
    stat = np.zeros(0)
    s,sig_s = np.zeros(0), np.zeros(0)
    nrj,ratio,sig_ratio = map(lambda l:np.array(l),[src["peaks_nrj"],src["peaks_ratio"],src["peaks_ratio_s"]])
    toto,s,sig_s = map(lambda l:np.array(l),[measurement["peaks_nrj"],measurement["peaks_measurment"],measurement["peaks_measurment_s"]])
    for j in range(nb_monte_carlo):
        s_sample = gauss(s, sig_s)
        ratio_sample = gauss(ratio, sig_ratio)
        lambd_sample = gauss(lambd, sig_lambd)
        bq_sample = src["activity"]                # the activity uncertianty is taken into accout in the fit
        events_sample = bq_sample * np.exp(-lambd_sample*decay_time) * (1/lambd_sample) * ( 1 - np.exp(-lambd_sample*measurement["time_measurement"]) ) * ratio_sample #* (1-measurement["dead_time"])
        eff_sample = s_sample / events_sample
        stat=np.append(stat,eff_sample)
    #print("coucou", np.exp(-lambd_sample*decay_time))
    stat = stat.reshape(nb_monte_carlo, len(nrj))
    eff_stat,sig_eff_stat = np.mean(stat,0), np.std(stat,0)
    return nrj, eff_stat, sig_eff_stat

nrj,eff_green, sig_eff_green= eff_calc(src_descr, measurement_ref_lotus)

def aff(v, l=19, rev=False):
    v = str(v)+" "
    return v+" "*(l-len(v)) if not rev else " "*(l-len(v))+v
def simple(v):return "%.5e" % v

resu = "src_acivity_sig [%] "+src_descr["activity_sig_pc"]+"\n"
resu += aff("nrj")+aff("ratio",l=15)+aff("sig")+aff("sig_rel")+aff("coups")+aff("sig")+aff("sig_rel")+aff("is_sum",l=8)+aff("eff")+aff("eff_sig")+aff("sig_rel")+aff("sig_model")+"\n"
for i in range(len(d_resu["nrj"])):
    resu += aff(d_resu["nrj"][i])+aff(d_resu["th_ratio"][i],l=15)+aff(d_resu["th_ratio_s"][i])+aff(simple(d_resu["th_ratio_s"][i]/d_resu["th_ratio"][i]))
    resu += aff(d_resu["measure"][i])+aff(d_resu["measure_s"][i])+aff(simple(d_resu["measure_s"][i]/d_resu["measure"][i]))
    #resu += aff(d_resu["is_sum"][i],l=8)+aff(eff_green[i])+aff(sig_eff_green[i])+aff(sig_eff_green[i]/eff_green[i])+aff(d_resu["measure_s_model"][i])+"\n"
    resu += aff(0,l=8)+aff(simple(eff_green[i]))+aff(simple(sig_eff_green[i]))+aff(simple(sig_eff_green[i]/eff_green[i]))+aff(0)+"\n"
print()
print(resu)
#if out is not None: 


open("spectrum_count_out/"+case_csv,"w").write(resu)

#print()
#print("l_x = ",list(nrj))
#print("l_y = ",list(eff_green))
#print("l_s = ",list(sig_eff_green))


fig.savefig("spectrum_count_out/"+case_csv+".png", bbox_inches=('tight'), dpi=200)
print()
print("#"*50)
print("# Output saved in spectrum_count_out/"+case_csv)
print("#"*50)
print()





plt.show()










#bq_sample = gauss(src["activity"], src["activity"]*src["activity_sig"] * (1 if with_src_unc else 0))



