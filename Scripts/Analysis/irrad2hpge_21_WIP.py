
#python ../../../python/irrad/irrad2hpge_4.py csv_dosi=data_dosi.csv csv_exp=meas7.csv case=exp1

'''
Reads the experimental and simulation results, and the preprocessed uncertainties,
Compute the C/E and their covariance.
'''

from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Common.utils_general import aff_param, dupx, dup, get_c, get_aff_size, lmap, tex
from ZPyDosi.Stats.Stats import cov_mult, cov_l_mult, cor_sig_to_cov, cov_to_sig_cor, sig2covdiag, cov_inv
from ZPyDosi.Prints.PrintnSave import aff_s_v, aff_list, aff_decription_s_v_cov, aff_decription_s_v_cov_as_C_over_E, export_csv
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.DosiFunctions.Dictionaries import d_lib, d_mt2tex 
from ZPyDosi.Plots.SubPlots import my_sub6, aff_curve
from ZPyDosi.Plots.MatrixPlots import aff_mat4
import matplotlib.pyplot as plt
import datetime
from scipy.optimize import curve_fit
import scipy
import math
import os
import numpy as np
import time

import shutil
import matplotlib as mpl
mpl.rcParams["text.usetex"] = shutil.which("latex") is not None
#fig = plt.figure(1, figsize=(16/1.2,5/1.4))
# fig = plt.figure(1, figsize=(16*2*1.6,9*1.6))#with activity
# fig = plt.figure(1, figsize=(16*2*1.3,9*1.3))

No_Cov=False # to do C/E and Chi2 without Cov for ilustration

dico_fnames={"expNi_ni_fe"  :"Ni_ni_fe",   "expNi_in1"    :"Ni_in1", "expNi_in2"    :"Ni_in2", "expNi_au"     :"Ni_au","expNi_al"     :"Ni_al","expCr_ni_fe"  :"Cr_ni_fe",   "expCr_in1"    :"Cr_in1", "expCr_in2"    :"Cr_in2", "expCr_au"     :"Cr_au","expCr_al"     :"Cr_al","expFe_ni_fe"  :"Fe_ni_fe",   "expFe_in1"    :"Fe_in1", "expFe_in2"    :"Fe_in2", "expFe_au"     :"Fe_au","expFe_al"     :"Fe_al","expSS_ni_fe"  :"SS_ni_fe",   "expSS_in1"    :"SS_in1", "expSS_in2"    :"SS_in2", "expSS_au"     :"SS_au","expSS_al"     :"SS_al"}

CEA_res={"Cr_in1":[-0.00934572584436333,0.00267993730895877,0,-0.00298527832683637,0.000455430807437374,-0.00977187825815295,0.00259160552341542,-0.0189787152916087,-0.030936165581592],
         "Cr_in2":[0.0243715243493445,0.0367652752822292,0,-0.0122890805760586,-0.0203726706164852,-0.0537385215259754,-0.0719110286426785,-0.0861235023671572,-0.102589379429253],
        #  "Cr_ni_fe":[0.0344685268821874,0.0111918073227757,0,-0.0197533762514187,-0.0305593145551545,-0.0437904961745121,-0.0578339505185821,-0.0761927864586671,-0.0808559687502375], #ni
        #  "Cr_ni_fe_IN":[0.0230540191036215,0.00294257393321873,0,-0.0100559665924157,-0.0134140826675987,-0.0232811868883229,-0.0288261983446252,-0.0413759713315378,-0.04162758765528], #ni
         "Cr_ni_fe":[-0.00660537866582378, 0.00188177330246653, 0 ,0.0660357404416623,0.000844763802378745,-0.0114928500269135,0.0205485116633168,0.0628413221988766,0.144797518249417], #fe56
         "Cr_ni_fe_IN":[0.0109388861693487,0.00447726864328191, 0 ,0.0745705546622593,0.0135872494197034,0.00606755977457474,0.0406693986550761,0.0718161019964478,0.148045196370383], #fe56
        #  "Cr_ni_fe":[-0.0181618127293596,-3.72006878932574E-05,0,0.0651305660842676,-0.00323606465764448,-0.0212346809361101,-0.00207770444172917,0.0055978792880258,-0.0507878696375129], #fe56 without Mn
        #  "Cr_ni_fe_IN":[-0.000821645173764263,0.00255332331979297,0,0.0736581333668074,0.00945446495227587,-0.00384733062436571,0.0175970895597433,0.0140892875001595,-0.0480950480522179], #fe56 without Mn
         "Cr_al":[-0.0298080943714809,-0.0126191145300576,0,-0.0180953815208778,-0.0133708340514005,0.0112318153147413,0.0011137378615409,-0.00819988373177727],
         "Fe_in1":[-0.00309677065184244,-0.0182140839384359,0,0.0328807263239319,0.0237151383303822,0.0284145109469243,0.0209933904355992,-0.0219632114954891,-0.00305793727405212],
         "Fe_au":[0.00886489323121986,0.00392189758541828,0,0.0206358175032035,0.00781193998223562,0.0121414963823772,0.0133639050082905,0.00384418154085497,0.00690263926929213],
         "Fe_in2":[-0.026375409737834,-0.00932433489840201,0,0.0298551055247516,0.0366856483916682,0.0316986381987197,0.0487815065295552,0.037610913077428,0.0203800231401374]}
CEA_sig={"Cr_in1":[0.0290703481552497,0.0295562115858802,0,0.0299323396558536,0.0299035889017618,0.0297763020587175,0.0302095600019647,0.0295055746995122,0.0287985462823433],
         "Cr_in2":[0.00948273682482533,0.00992017741743273,0,0.00968795270167425,0.00980806143269146,0.00962497242534653,0.0123521004182435,0.0101887310022238,0.0103930750593374],
        #  "Cr_ni_fe":[0.00867167857669944,0.00922313608076851,0,0.00839193994294534,0.007954455590397,0.00832276234318192,0.00821555588273087,0.00833906192162578,0.00967112910285067],#fe56
        #  "Cr_ni_fe_IN":[0.00857329473344034,0.00914779625715272,0,0.00847386623000508,0.00809325039667199,0.00850130231267466,0.00847801657961053,0.00865107244514914,0.0100840407792189],#fe56
         "Cr_ni_fe":[0.0144455630447856,0.0151736414233803,0,0.0182067079109433,0.0167894552534757,0.0166946081973933,0.0195910195683758,0.021202447971788,0.0219510509398022],  #ni
         "Cr_ni_fe_IN":[0.0147205693350115,0.0151651472246632,0,0.0183109253220601,0.0169522810692127,0.0169535517404204,0.0199277573676463,0.0213095013554508,0.0228344542329394],  #ni
         "Cr_al":[0.023770167806239,0.0236126001979935,0,0.0196620878564281,0.0192938596815701,0.0260368877033947,0.0285117280279561,0.0390084144845742],
         "Fe_in1":[0.0290044102213872,0.0286619688191014,0,0.0305858978184471,0.0305538206097595,0.0309980933492659,0.0309588235427836,0.0292619149879786,0.0293389850731554],
         "Fe_au":[0.00852210982798841,0.00807007325758824,0,0.00973815624141539,0.0085117747297363,0.00873381236710324,0.00849939518110241,0.00924003460620422,0.00796684681140638],
         "Fe_in2":[0.00835754963525716,0.00863478075102601,0,0.00970209608260571,0.00989939535134201,0.0101836196208442,0.0114063755563283,0.0116603832508663,0.0117206076967452]}
plot_CEA=False
use_CEA_Cr_al=False
do_zoom=True
print()
print("#"*50)

path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv  = get_param_vari("lcase", str).split("/")
save_key  = get_param_vari("save", str, "").replace("/","_")
DT_corr  = get_param_vari("dt_corr", bool, "True")
rr_shape  = get_param_vari("rr_shape", bool, "False")

puiss_max_plot = get_param_vari("puiss_max_plot", float, "110")

Do_load_nuis = get_param_vari("load_nuis",bool,"True") # Key: retro_nuis, addition of argument (true by default)  that define wether or not ndup_nuis are load (retrocompatibility)
Do_load_pos = get_param_vari("load_pos",bool,"True") # addition of argument (true by default)  that define wether or not up_pos are load (retrocompatibility)
which_norm  = get_param_vari("which_norm", str, "None") # Choice of the dosimeter used for normalization, either "None", "Center", "Ref" or "Custom" Note: custom take ref dosimeter 
MC_propagation=get_param_vari("MC_propa",bool,"True")
is_offset_cst=get_param_vari("offset_cst",bool,"True")
do_chi=get_param_vari("do_chi",bool,"True")
load_Factor=get_param_vari("load_Factor",bool,"True")
CoC_mode=get_param_vari("CoC_mode",bool,"False") #C/C comparison mode
Exp_only=get_param_vari("Exp_only",bool,"False") 
No_cov=get_param_vari("No_cov",bool,"False") 


do_remove = False if which_norm in ["Center","Ref","Custom"] else True
# do_remove = True
if Exp_only and len(lcase_csv)>4:
    print("Exp_only mode: do_remove=True and which_norm=None")
    fig = plt.figure(1, figsize=(24,24))
    do_remove=True
    which_norm="None"
    aff_param["ampli"] *=1.5
if Exp_only:
    print("Exp_only mode: do_remove=False and which_norm=None")
    fig = plt.figure(1, figsize=(16,9))
    do_remove=True
    which_norm="None"
    aff_param["ampli"] *=1.5
elif len(lcase_csv)>10:
    fig = plt.figure(1, figsize=(16*4*1.3,9*4*1.3))
    aff_param["ampli"] *=2
else:
    fig = plt.figure(1, figsize=(16*2*1.3,9*1.3))
    aff_param["ampli"] *=2

fig.patch.set_facecolor('white')

l_ax = my_sub6(fig,3,1,0,list_rx=[1,1,1],list_sx=[0.30,0.30],list_ry=[1],auto_y=False,auto_x=False)[:,0] if rr_shape else my_sub6(fig,3,1,0,list_rx=[1,1],list_sx=[0.30,0.30],list_ry=[1],auto_y=False,auto_x=False)[:,0]


data_irrad = DataIrrad  (   path_csv_data,
                            path_csv_dosi,
                            lcase_csv,
                            use_sqrt_for_meas_sig=False,
                            load_hpge_eff=True,
                            load_sss_results=True,
                            #load_sss_spectrum=True,
                            load_ndup=True,
                            load_ndup_nuis=Do_load_nuis,
                            load_up_pos=Do_load_pos,
                            remove_data=do_remove,
                            load_Factor=load_Factor,
                            unique_only=True  )

# print("COUCOU2")
# exit()
print(data_irrad.l_gamma_inten)
# exit()
if not do_remove: #manually reordering the value
    l_ordering = []
    for i in range(data_irrad.nb_dosi):
        mini = 0
        if data_irrad.l_pos_name[i] == "R":  mini = 0.2
        if data_irrad.l_pos_name[i] == "CR": mini = 0.1
        if data_irrad.l_pos_name[i] == "C":  mini = 0.0
        
        if   data_irrad.l_mat[i] == "Fe" and data_irrad.l_aaa[i]=="58"  and data_irrad.l_mt[i]=="102"  : l_ordering+=[-1+mini]
        elif data_irrad.l_mat[i] == "In" and data_irrad.l_aaa[i]=="115" and data_irrad.l_mt[i]=="102"  : l_ordering+=[0+mini]
        elif data_irrad.l_mat[i] == "Au" and data_irrad.l_aaa[i]=="197" and data_irrad.l_mt[i]=="102"  : l_ordering+=[1+mini]
        elif data_irrad.l_mat[i] == "In" and data_irrad.l_aaa[i]=="115" and data_irrad.l_mt[i]=="11004": l_ordering+=[2+mini]
        elif data_irrad.l_mat[i] == "Ni" and data_irrad.l_aaa[i]=="58"  and data_irrad.l_mt[i]=="103"  : l_ordering+=[3+mini]
        elif data_irrad.l_mat[i] == "Fe" and data_irrad.l_aaa[i]=="54"  and data_irrad.l_mt[i]=="103"  : l_ordering+=[4+mini]
        elif data_irrad.l_mat[i] == "Fe" and data_irrad.l_aaa[i]=="56"  and data_irrad.l_mt[i]=="103"  : l_ordering+=[5+mini]
        elif data_irrad.l_mat[i] == "Al" and data_irrad.l_aaa[i]=="27"  and data_irrad.l_mt[i]=="107"  : l_ordering+=[6+mini]
        else:
            print("Warning - DataIrrad - ordering unknown for -",data_irrad.l_mat[i],data_irrad.l_aaa[i],data_irrad.l_mt[i])
            l_ordering+=[7]
    #l_reorder = map(lambda (i,o):i, sorted(enumerate(l_ordering), key=lambda (i,o):o))
    l_reorder = lmap(lambda i_o:i_o[0], sorted(enumerate(l_ordering), key=lambda i_o:i_o[1]))
    for att in [a for a in dir(data_irrad) if not a.startswith('__') and not callable(getattr(data_irrad,a))]:
        val = getattr(data_irrad, att)
        if type(val) == np.ndarray:
            new_val = []
            if val.shape == (data_irrad.nb_dosi,):
                setattr(data_irrad, att, val[l_reorder])
            elif val.shape == (data_irrad.nb_dosi,data_irrad.nb_dosi):
                setattr(data_irrad, att, val[l_reorder,:][:,l_reorder])
            else:
                if len(val)>0:
                    # self._err("_remove_commented, "+att+" shape do not fit: "+str(val.shape))
                    print("_remove_commented, "+att+" shape do not fit: "+str(val.shape))
                    exit()
    
data_irrad.aff_description()



c1,c2 = (0,0,0), (0.8,0,0.1)


# dico_color = {"Al":(0.9,0.9,0.9), "Fe":(0.7,0.7,0.7), "In":(0.8,0.85,1), "Ni":(1,0.9,0.68), "Au":(1,1,0.7)}
dico_color = {"Al":(0.6,0.6,0.6), "Fe":(0.2,0.2,0.2), "In":(0.3,0.3,1), "Ni":(0.8,0.6,0.4), "Au":(0.8,0.8,0.5)}
def get_c_elt(elt):
    if elt in dico_color:
        return dico_color[elt]
    c = np.random.rand(3,)
    dico_color[elt] = c
    return c

def axial_flux_shape(l_x):
    return np.sin(np.pi * l_x/data_irrad.l_water_lvl_cm)
l_unc_due_to_position_axial = abs((axial_flux_shape(data_irrad.l_pos_reel+0.05)-axial_flux_shape(data_irrad.l_pos_reel))/axial_flux_shape(data_irrad.l_pos_reel))
l_unc_due_to_position_radial = np.zeros(len(data_irrad.l_pos_reel))
for i in range(len(data_irrad.l_name)):
    if ("10" in data_irrad.l_name[i]) or ("rc" in data_irrad.l_name[i]): # Check if we are at core center
        l_unc_due_to_position_radial[i] = (1.68/0.65)/100*0.05 # keyword : Position_error. radial uncertainty from experiment, to be adjusted with more truthful result with respect to dosimeter type and postion in PETALE, dimension in cm
l_unc_due_to_position = np.sqrt(np.power(l_unc_due_to_position_axial,2)+np.power(l_unc_due_to_position_radial,2))
print("#"*50)
# print(len(l_unc_due_to_position))
# print(data_irrad.l_pos_reel)
# print(aff_list("unc_due_to_position [%]", l_unc_due_to_position*100))


print("#"*50)





time_ref = data_irrad.l_irrad_time_start[0]
label_already_done = []

l_time_dash_todo = []
class Measure:
    def __init__(self, dwell, t0, l_path, J_per_I, irrad_time_stop, dwell_obj=None, corrected_tka=True): #key : Measure, added the parameter corrected tka to allow the usage of DataIrrad specific function of DT correction.
        if dwell_obj is None: dwell_obj = dwell
        #dwell_obj = 1
        self.t0 = t0
        #dwell = 1
        if corrected_tka and not data_irrad:
            print("Error : \"data_irrad\" variable of \"DataIrrad\" class must be defined in script in order to apply dead time correction. \n Script aborted") 
            exit()
        l_v = []
        t_prev, l_v_prev = None, None
        for path in l_path.split("//"):
        
            if path.endswith(".CNF"):
                print("ERROR - CNF file instead of TKA input file :",path)
                exit()
                
            ye,mo,da,ho,mi,se,voie,dw = path.split("/")[-1].split("_")[:8]
            t =  datetime.datetime(*map(lambda s: int(s), [ye,mo,da,ho,mi,se]))
            if t_prev is not None:
                manque = int((t-t_prev).total_seconds() - len(l_v_prev))
                nb_s = 10
                ave_v, ave_s = sum(l_v_prev[-nb_s:]) / nb_s, (sum(l_v_prev[-nb_s:]))**0.5 / nb_s
                print("# il manque",manque,"secondes, utilisation de la valeur moyenne des 10 dernieres secondes :",ave_v, "+-", ave_s/ave_v*100,"[\%]")
                l_v += [ave_v] * manque
            t_prev = t
            l_v_prev = lmap(lambda v:float(v), open(path).readlines()[2:])
            l_v += l_v_prev
        #print("len(l_v)", len(l_v))
        #exit()
        if corrected_tka : #Key : corrected monitor, correction for dead time, dwell time and voie are expected to be the same for all tka.
            l_v = np.array(data_irrad.linearity_loss_corrected_tka(l_v,id_voie=voie,dwell_time=dw))
            l_v=l_v.tolist()
        while l_v[-1] == 0:
            l_v.pop(len(l_v)-1)
        fact = int(dwell_obj/dwell)
        if fact > 1:
            print("reduce time serie (dwell)")
            new_l_v = []
            while len(l_v)>fact:
                new_l_v += [sum(l_v[:fact])]
                l_v = l_v[fact:]
            dwell = dwell * fact
            l_v = new_l_v
        self.l_v = np.array(l_v)
        self.l_t = np.arange(len(self.l_v))*dwell
        self.l_s = self.l_v**0.5
        if dwell_obj<dwell:
            fact = int(dwell/dwell_obj)
            print ("expand time serie (dwell)", dwell/dwell_obj, fact)
            new_l_v, new_l_s = np.zeros(len(self.l_v)*fact), np.zeros(len(self.l_v)*fact)
            for i in range(len(l_v)):
                for j in range(fact):
                    new_l_v[i*fact+j] = self.l_v[i]/fact
                    new_l_s[i*fact+j] = self.l_s[i]/fact
            dwell = dwell / fact
            self.l_v = new_l_v
            self.l_s = new_l_s
            self.l_t = np.arange(len(self.l_v))*dwell
        pos_maxi = l_v.index(max(self.l_v))
        if self.l_v[pos_maxi+10] == 0: # alors le G2K comptait quand les moni on ete arretes
            self.l_v[pos_maxi-10:pos_maxi+10] = [0] * 20

        self.l_v *= J_per_I
        self.l_s *= J_per_I
        self.l_v /= dwell
        self.l_s /= dwell
        self.dwell = dwell
        self.tot_power=sum(self.l_v*dwell)
        print("total_power: {} Wh".format(self.tot_power/3600))
        maxi = max(self.l_v)
        i_fall = len(self.l_v)-1
        while self.l_v[i_fall] < maxi*0.5: i_fall -= 1
        while self.l_v[i_fall-1] > self.l_v[i_fall]*1.05: i_fall -= 1
        if i_fall == len(self.l_v)-1: i_fall -= 1
        avancement = 1.*self.l_v[i_fall+1]/self.l_v[i_fall]
        self.t_fall = self.l_t[i_fall] + avancement*(self.l_t[i_fall+1]-self.l_t[i_fall]) + self.dwell
        t_stop = (irrad_time_stop-t0).total_seconds()
        
        #print(l_path)
        print("# t0 =", self.t0)
        print("# t_stop - "+str(irrad_time_stop)+" ("+str(t_stop)+" s after begin)")
        print ("# Warning - compensation of the stop-time in the csv and interpreted with the monitor:", t_stop - self.t_fall,"s")
        self.t0 += datetime.timedelta(seconds=(t_stop-self.t_fall))
        print("# after correction t0 =", self.t0)

        cut = 0.9
        s_v, s_d = 0, 0
        maxi = max(self.l_v)
        for v in self.l_v:
            if v>cut*maxi:
                s_v += v*self.dwell
                s_d += self.dwell
        print("# info (not used for analysis): with a cut at "+str(cut*100)+" %, the irradiation time is "+str(s_d)+" s and the average power "+str(s_v/s_d)+" W")
        print()


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
        return lmap(lambda l: list(l)[i0:i1], [self.l_t, self.l_v, self.l_s])
    
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
        dec = (self.t0-time_ref).total_seconds()
        dec = 0
        aff_curve(ax, dupx(self.l_t + dec)/3600.,dup(self.l_v),dup(self.l_s),c,1.,0.3, label=label)
        
        
        #ax.plot([(self.t_fall+dec)/3600., (self.t_fall+dec)/3600.],ax.get_ylim(),c=(0.3,0.3,0.3),dashes=[2,5])
        
        
    def propagate_rr(self, fact, halftime, date_start, hpge_time, time_in_hpge, name, ax=None):
        global label_already_done
        lambd = np.log(2)/halftime
        cp_histo = []
        cp_histo_met_2 = []
        
        l_t = list(self.l_t)
        l_at = []
        
        t_irrad = (date_start-self.t0).total_seconds()
        t_final = (hpge_time-self.t0).total_seconds()+time_in_hpge+60
        
        #l_time_dash_todo.append((date_start-time_ref).total_seconds()/3600.)
        #l_time_dash_todo.append((self.t_fall+(self.t0-time_ref).total_seconds())/3600.)
        l_time_dash_todo.append((date_start-self.t0).total_seconds()/3600.)
        l_time_dash_todo.append((self.t_fall)/3600.)
        
        
        
        l_prod = 1.*self.l_v
        at = 0
        sum_cp_irrad = 0
        for i in range(len(l_t)):
            if l_t[i]>t_irrad:
                sum_cp_irrad += fact*self.l_v[i]*self.dwell
                at += (fact*self.l_v[i] -lambd*at)*self.dwell
            else:
                l_prod[i] = 0
            l_at += [at]
        
        dt = 10
        if True:
            print (aff_s_v("cp_histo at irrad end",at))
        while l_t[-1]<t_final:
            at += -lambd*at* (self.dwell*dt)
            l_at += [at]
            l_t  += [l_t[-1]+(self.dwell*dt)]
        
        t_begin = (hpge_time-self.t0).total_seconds()
        decay, i = 0, 0
        while l_t[i]<t_begin : i += 1
        i0 = i
        while l_t[i]-t_begin < time_in_hpge:
            decay += lambd*l_at[i]*self.dwell*(l_t[i+1]-l_t[i])
            i += 1
        cp_histo = decay
        
        elt = name.split('-')[0]
        c = get_c_elt(elt)
        
        lab = tex(name[:2])
        if lab in label_already_done: lab = None
        else:     label_already_done += [lab]
        
        
        ax.plot((np.array(l_t)+(self.t0-time_ref).total_seconds())/3600.,np.array(l_at)/3600., c=c, linewidth=2, label=lab, zorder = -int(halftime))
        #print("Max_Wh",np.max(np.array(l_at)/3600.))
        ax.fill_between((np.array(l_t[i0:i])+(self.t0-time_ref).total_seconds())/3600., np.array(l_at[i0:i])*0, np.array(l_at[i0:i])/3600., facecolor=c, alpha=0.5,linewidth=0.0, zorder = 0)
        #ax.plot((np.array(l_t))/3600.,np.array(l_at)/3600., c=c, linewidth=2, label=lab, zorder = -int(halftime))
        #ax.fill_between((np.array(l_t[i0:i]))/3600., np.array(l_at[i0:i])*0, np.array(l_at[i0:i])/3600., facecolor=c, alpha=0.5,linewidth=0.0, zorder = 0)
        
        l_t_prod = np.arange(len(l_prod))*self.dwell
        
        cp_histo_met_2 = self.dwell*sum(fact * l_prod * np.exp(-lambd*(t_begin-l_t_prod)) * (1-np.exp(-lambd*time_in_hpge)))
        if True:
            print (aff_s_v("cp_histo",cp_histo))
            print (aff_s_v("cp_histo_met_2",cp_histo_met_2))
            print (aff_s_v("diff [%]",(cp_histo_met_2/cp_histo-1)*100))
            
        #ax.set_xlim([-1, ax.set_xlim()[-1]])
        return cp_histo_met_2


if len(data_irrad.l_ndup_rr) != len(data_irrad.l_c):
    print ('ERROR - ndup data size do not match...', len(data_irrad.l_ndup_rr), len(data_irrad.l_c))
    exit()
check_rel = (data_irrad.l_ndup_rr-data_irrad.l_c)/data_irrad.l_c
print (aff_list("check vs ndup_rr [%]",check_rel*100))
if np.max(check_rel) > 0.05:
    print('WARNING WARNING WARNING - ndup data value do not match... possibly due to running sss calculation')
    print('data_irrad.l_ndup_rr', data_irrad.l_ndup_rr)
    print('data_irrad.l_c      ', data_irrad.l_c)


d_path2moni = {}
l_cp_histo = []
print ("# propagate")
#t_max = time_ref


for idosi in range(data_irrad.nb_dosi):
    #print(data_irrad.l_monitor_path[idosi])
    ye,mo,da,ho,mi,se,voie,dw = data_irrad.l_monitor_path[idosi].split("//")[0].split("/")[-1].split("_")[:8]
    dwell = float(dw[1:])
    if data_irrad.l_monitor_path[idosi] in d_path2moni:
        moni = d_path2moni[data_irrad.l_monitor_path[idosi]]
    else:
        print ("# load monitor",data_irrad.l_monitor_path[idosi])
        J_per_I = 1./data_irrad.l_monitor_calib[idosi]
        moni = Measure(    dwell,
                datetime.datetime(*map(lambda s: int(s), [ye,mo,da,ho,mi,se])),
                data_irrad.l_monitor_path[idosi],
                J_per_I,
                data_irrad.l_irrad_time_stop[idosi], 
                corrected_tka=DT_corr)
        c = get_c(list(set(data_irrad.l_case_csv)).index(data_irrad.l_case_csv[idosi]),len(list(set(data_irrad.l_case_csv))))
        moni.plot(l_ax[0], c, label=tex(data_irrad.l_case_csv[idosi]))  # , label=r"$\mathrm{monitor~}"+str(i_path_moni+1)+"$"
        d_path2moni[data_irrad.l_monitor_path[idosi]] = moni
        for t in [
                (data_irrad.l_irrad_time_start[idosi]-moni.t0).total_seconds()/3600.,
                moni.t_fall/3600,
                 ]:
            l_ax[0].plot([t,t],[0,puiss_max_plot],c=c, alpha=0.25, zorder=-10) # dashes=[2,5],
            a=1
    #print("propagate_rr",data_irrad.l_name[idosi])
    l_cp_histo += [moni.propagate_rr(    1.,
                        data_irrad.l_half_time[idosi],
                        data_irrad.l_irrad_time_start[idosi],
                        data_irrad.l_hpge_time[idosi],
                        data_irrad.l_time_in_hpge[idosi],
                        data_irrad.l_name[idosi],
                        ax=l_ax[1])]
l_cp_histo = np.array(l_cp_histo)

l_ax[1].set_xlim([-1, l_ax[1].get_xlim()[-1]])
l_ax[0].set_xlim([0, l_ax[0].get_xlim()[-1]])
 


cov_de_zero = np.zeros((data_irrad.nb_dosi, data_irrad.nb_dosi))


l_c,   m_c   = data_irrad.l_c, data_irrad.m_c             # sig2covdiag(data_irrad.l_cs)
l_e,   m_e   = data_irrad.l_counts_v, sig2covdiag(data_irrad.l_counts_s)
for i in range(len(m_e)): #correlation between ND-lib
    for j in range(len(m_e)):
        name1=data_irrad.l_name[i]
        name2=data_irrad.l_name[j]
        if (len(name1.split("-")[1])>3):
            index=0
            while((3+index)<len(name1.split("-")[1]) and name1.split("-")[1][3+index].isnumeric()):
                index+=1
            if(3+index)!=len(name1.split("-")[1]):
                sp=name1.split("-")
                sp[1]=sp[1][:int(3+index)]
                name1="-".join(sp)
                
        if (len(name2.split("-")[1])>3):
            index=0
            while((3+index)<len(name2.split("-")[1]) and name2.split("-")[1][3+index].isnumeric()):
                index+=1
            if(3+index)!=len(name2.split("-")[1]):
                # print(name2)
                # print(name2.split("-"))
                sp=name2.split("-")
                sp[1]=sp[1][:int(3+index)]
                name2="-".join(sp)                
# False they should not be correlated here
        # if(name1==name2):
        #     m_e[i][j]=data_irrad.l_counts_s[i]*data_irrad.l_counts_s[j]
# m_c   = cov_de_zero  # To ignore experimental and dcalculation statistics
# m_e   = cov_de_zero
# f = 1./data_irrad.l_power_per_src_n * (1-data_irrad.l_deadtime)
# f_s= data_irrad.l_power_per_src_n_s/data_irrad.l_power_per_src_n/data_irrad.l_power_per_src_n * (1-data_irrad.l_deadtime)
f = 1./data_irrad.l_power_per_src_n 
f_s= data_irrad.l_power_per_src_n_s/data_irrad.l_power_per_src_n/data_irrad.l_power_per_src_n
cor_f=np.zeros(cov_de_zero.shape)

#correlation matrix for the power scaling, if factors are the same then the simulation must also be statistically speeking
for  i in range(len(data_irrad.l_power_per_src_n )):
    for  j in range(len(data_irrad.l_power_per_src_n )):
        if data_irrad.l_power_per_src_n[i]==data_irrad.l_power_per_src_n[j]: cor_f[i][j]=1
cov_f=cor_sig_to_cov(cor_f,f_s)
#print(data_irrad.l_counts_v)
#print(data_irrad.l_counts_s)
#exit()

m_ndupnuis_rel_cov=data_irrad.m_ndupnuis_rel_cov if Do_load_nuis else cov_de_zero
l_ndupnuis=np.ones(len(l_c)) if Do_load_nuis else np.zeros(len(l_c))

m_uppos_rel_cov=data_irrad.m_uppos_rel_cov if Do_load_pos else cov_de_zero # else -> experimental value for gold
l_uppos=np.ones(len(l_c)) if Do_load_pos else np.zeros(len(l_c))


print(aff_list("1/(J/src*(1-deadtime))",    f*np.ones(len(l_c))))
print(aff_list("propagate_rr 2 HPGe",       l_cp_histo))


l_terms_a_mult = [
                (data_irrad.l_calib_ratio_v,    data_irrad.m_calib_ratio_cov,          "",   None,        (-1,1)),
                (data_irrad.l_eff_gamma,    data_irrad.m_eff_gamma_cov,          "Eff HPGe",   None,        (-1,1)),
                (data_irrad.l_auto_abs,     data_irrad.m_autoabs_cov,            "Autoabs",    None,        (-1,1)),
                (f/np.array(data_irrad.l_factor),       cov_f,                   "Fact",       None,        (-1,1)),
                (np.ones(len(l_c)),         data_irrad.m_ndup_rel_cov,           "ND_{dosi}",  "sig",        (0.,1)),
                (np.ones(len(l_c)),         m_uppos_rel_cov,                     "Position",   "sig",        (-1,1)),
                (np.ones(len(l_c)),         m_ndupnuis_rel_cov,                  "ND_{XS}",    "sig",        (-1,1)),
                (l_cp_histo,                cov_de_zero,                         "",           None,         (-1,1)),
                (data_irrad.l_gamma_inten,  cov_de_zero,                         "",            None,        (-1,1)),
            ]
l_terms_a_mult_C_tot = [
                # (data_irrad.l_calib_ratio_v,    data_irrad.m_calib_ratio_cov,          "",   None,        (-1,1)),
                # (data_irrad.l_eff_gamma,    data_irrad.m_eff_gamma_cov,          "Eff HPGe",   None,        (-1,1)),
                # (data_irrad.l_auto_abs,     data_irrad.m_autoabs_cov,            "Autoabs",    None,        (-1,1)),
                # (f/np.array(data_irrad.l_factor),       cov_f,                   "Fact",       None,        (-1,1)),
                (np.ones(len(l_c)),         data_irrad.m_ndup_rel_cov,           "ND_{dosi}",  "sig",        (0.,1)),
                (np.ones(len(l_c)),         m_uppos_rel_cov,                     "Position",   "sig",        (-1,1)),
                (np.ones(len(l_c)),         m_ndupnuis_rel_cov,                  "ND_{XS}",    "sig",        (-1,1)),
                # (l_cp_histo,                cov_de_zero,                         "",           None,         (-1,1)),
                # (data_irrad.l_gamma_inten,  cov_de_zero,                         "",            None,        (-1,1)),
            ]




# l_terms_a_mult = [
#                 (f/np.array(data_irrad.l_factor),       cov_f,                         "Fact",       "sig",        (-1,1)),
#                 (np.ones(len(l_c)),         data_irrad.m_ndup_rel_cov,           "ND_{dosi}",  "sig",        (0.,1)),
#                 (np.ones(len(l_c)),         m_ndupnuis_rel_cov,                  "ND_{XS}",    "sig",        (-1,1)),
#                 (np.ones(len(l_c)),         m_uppos_rel_cov,                     "Position",   "sig",        (-1,1)),
#                 (l_cp_histo,                cov_de_zero,                         "",           None,         (-1,1)),
#                 (data_irrad.l_eff_gamma,    data_irrad.m_eff_gamma_cov,          "Eff HPGe",   "sig",        (-1,1)),
#                 (data_irrad.l_calib_ratio_v,data_irrad.m_calib_ratio_cov,        "",           None,         (-1,1)),
#                 (data_irrad.l_gamma_inten,  cov_de_zero,                         "",            None,        (-1,1)),
#                 (data_irrad.l_auto_abs,     data_irrad.m_autoabs_cov,            "Autoabs",    "sig",        (-1,1)),
#             ]

l_decay_rate=np.divide(np.log(2),data_irrad.l_half_time)
l_irrad_wait=np.array(lmap(lambda s: (s[0]-s[1]).total_seconds(),zip(data_irrad.l_hpge_time,data_irrad.l_irrad_time_stop)))
l_time_fact=np.subtract(1,np.exp(-l_decay_rate*data_irrad.l_time_in_hpge))/l_decay_rate*np.exp(-l_decay_rate*l_irrad_wait)

l_eff_mult=[
                (data_irrad.l_calib_ratio_v,    data_irrad.m_calib_ratio_cov,    "Eff Ratio",   "sig",        (-1,1)),
                (data_irrad.l_eff_gamma,    data_irrad.m_eff_gamma_cov,          "Eff HPGe",   "sig",        (-1,1)),
            ]

l_tot_eff, m_tot_eff = cov_l_mult(lmap(lambda p: (p[0],p[1]), l_eff_mult))
l_terms_a_mult_act = [
                (data_irrad.l_calib_ratio_v,    data_irrad.m_calib_ratio_cov,          "",   None,        (-1,1)),
                (data_irrad.l_eff_gamma,    data_irrad.m_eff_gamma_cov,          "Eff HPGe",   "sig",        (-1,1)),
                (data_irrad.l_auto_abs,     data_irrad.m_autoabs_cov,            "Autoabs",    "sig",        (-1,1)),
                (data_irrad.l_gamma_inten,  cov_de_zero,                         "",            None,        (-1,1)),
                # (l_cp_histo,                cov_de_zero,                         "",           None,         (-1,1)),
                (l_time_fact,               cov_de_zero,                         "",            None,        (-1,1))
            ]

l_terms_a_mult_RR = [
                (data_irrad.l_calib_ratio_v,    data_irrad.m_calib_ratio_cov,    "Eff Ratio",  None,        (-1,1)),
                (data_irrad.l_eff_gamma,    data_irrad.m_eff_gamma_cov,          "Eff HPGe",   None,        (-1,1)),
                # (l_tot_eff,   m_tot_eff,          "Total Eff.",   "sig",        (-1,1)),
                (data_irrad.l_auto_abs,     data_irrad.m_autoabs_cov,            "",    None,        (-1,1)),
                (data_irrad.l_gamma_inten,  cov_de_zero,                         "",            None,        (-1,1)),
                (l_cp_histo,                cov_de_zero,                         "",           None,         (-1,1)),
                # (l_time_fact,               cov_de_zero,                         "",            None,        (-1,1))
            ]

print(l_time_fact.shape)
#l_c2e, m_c2e = cov_l_mult(map(lambda (v,m,blabla, mode, minimaxi): (v,m), l_terms_a_mult))

l_c2e, m_c2e = cov_l_mult(lmap(lambda p: (p[0],p[1]), l_terms_a_mult)) #multiply everything and propagate the covariances
l_ctot, m_ctot = cov_l_mult(lmap(lambda p: (p[0],p[1]), l_terms_a_mult_C_tot)) #multiply everything and propagate the covariances
l_e2c, m_e2c = cov_inv((l_c2e, m_c2e))
l_e2Act, m_e2Act = cov_inv(cov_l_mult(lmap(lambda p: (p[0],p[1]), l_terms_a_mult_act)))
l_Act, m_Act = cov_mult((l_e, m_e),(l_e2Act, m_e2Act))
l_e2RR, m_e2RR = cov_inv(cov_l_mult(lmap(lambda p: (p[0],p[1]), l_terms_a_mult_RR)))
l_RR, m_RR = cov_mult((l_e, m_e),(l_e2RR, m_e2RR))

print(l_Act.shape,m_Act.shape)


l_terms_a_mult_calc_tot = [
                (l_c,                m_c,        "C",    "sig",            (-1,1)),
                (f/np.array(data_irrad.l_factor),       cov_f,                         "Fact",       "sig",        (-1,1)),
                (np.ones(len(l_c)),         data_irrad.m_ndup_rel_cov,           "ND_{dosi}",  "sig",        (0.,1)),
                (np.ones(len(l_c)),         m_uppos_rel_cov,                     "Position",   "sig",        (-1,1)),
                (np.ones(len(l_c)),         m_ndupnuis_rel_cov,                  "ND_{XS}",    "sig",        (-1,1))
            ]

l_calc_tot,m_calc_tot=cov_l_mult(lmap(lambda p: (p[0],p[1]), l_terms_a_mult_calc_tot))

print()
aff_decription_s_v_cov("C",   (l_c,   m_c  ))
aff_decription_s_v_cov("calc_tot",   (l_calc_tot,   m_calc_tot  ))
aff_decription_s_v_cov("C2E", (l_c2e, m_c2e))
aff_decription_s_v_cov("C*C2E", cov_mult((l_c, m_c),(l_c2e, m_c2e)))
aff_decription_s_v_cov("E*E2C", cov_mult((l_e, m_e),(l_e2c, m_e2c)))
aff_decription_s_v_cov("E2C", (l_e2c, m_e2c))
aff_decription_s_v_cov("E",   (l_e,   m_e  ))
aff_decription_s_v_cov("Ratio",   (data_irrad.l_calib_ratio_v,    data_irrad.m_calib_ratio_cov))
aff_decription_s_v_cov("Act",   (l_Act,   m_Act  ))
aff_decription_s_v_cov("RR_Exp",   (l_RR,   m_RR  ))
# exit()

CMoE_val, CMoE_cov = cov_l_mult([(l_c,   m_c ),(l_c2e, m_c2e), cov_inv((l_e, m_e))])
CMoE_sig, CMoE_cor = cov_to_sig_cor(CMoE_cov)
aff_decription_s_v_cov_as_C_over_E("(C*C2E)/E-1",   (CMoE_val,   CMoE_cov  ))

CoME_val, CoME_cov = cov_mult((l_c,   m_c ), cov_inv(cov_mult((l_e, m_e),(l_e2c, m_e2c))))
CoME_sig, CoME_cor = cov_to_sig_cor(CoME_cov)
aff_decription_s_v_cov_as_C_over_E("C/(E*E2C)-1",   (CoME_val,   CoME_cov  ))

print (aff_list("l_name",                data_irrad.l_name))

print(CMoE_val.dot(CMoE_cov))

if do_chi:
    print("Chi2 before corrections")
    cova = CMoE_cov
    res  = CMoE_val -1
    cova_inv = np.linalg.inv(cova)
    chis = res.T.dot(cova_inv.dot(res))
    prob = np.exp(-chis/2)
    print("Total chi2, exp(-chi2/2)", chis, prob)
    print("\nResult by part")
    groups=[]
    id_start=0
    for i in range(1,len(CMoE_cov)):
        if ((data_irrad.l_iso[i]!=data_irrad.l_iso[i-1]) or (data_irrad.l_case_csv[i]!=data_irrad.l_case_csv[i-1])):
            groups+=[[id_start,i-1]]
            id_start=i
    groups+=[[id_start,i]]
    for group in groups:
        cova = CMoE_cov[group[0]:group[1]+1,group[0]:group[1]+1].copy()
        res  = CMoE_val[group[0]:group[1]+1].copy() -1
        print(cova.shape)
        cova_inv = np.linalg.inv(cova)
        chis = res.T.dot(cova_inv.dot(res))
        prob = np.exp(-chis/2)
        print("exp %s, iso %s,  chi2=%f, exp(-chi2/2)=%e" % (data_irrad.l_case_csv[group[0]],data_irrad.l_iso[group[0]],chis, prob))

        


CMoE_div_val2=np.ones(data_irrad.nb_dosi)
CMoE_div_sig2=np.zeros(data_irrad.nb_dosi)
CMoE_div_ref_index=np.zeros(data_irrad.nb_dosi)
CMoE_div_cor2=np.zeros((data_irrad.nb_dosi, data_irrad.nb_dosi))
CMoE_div_cov=np.zeros((data_irrad.nb_dosi, data_irrad.nb_dosi))
Jacobian_CMoEdiv=np.zeros((data_irrad.nb_dosi, data_irrad.nb_dosi))
sub_cov=np.zeros((data_irrad.nb_dosi, data_irrad.nb_dosi))
l_not_norm=CMoE_val
m_not_norm=CMoE_cov
dico_norm={}
dico_plate={"Ni":"Pni","Cr":"Pcr","Fe":"Pfe","SS":"Pss"}
dico_irrad={
    "begin":{ 
         "therm": "Au",
         "fast" : "Ni"
    },
    "end":{ 
         "therm": {"fe":"fe-","au":"","in":"in-","ni":"ni-","al":"al-"},
         "fast" : {"fe":"fe-","au":"au-","in":"in-","ni":"" ,"al":"al-"}
    }
}
index_val=[]
if which_norm in ["Center","Ref","Custom"]: #normalization process
    if which_norm=="custom" :print("Warning Fe-54/58 not supported yet for Custom")
    if which_norm in ["Center","Ref"]:
        norm_n= "rc" if which_norm=="Center" else "rp"
        for i in range(data_irrad.nb_dosi):
            if norm_n in data_irrad.l_name[i]:
                dico_norm.update({data_irrad.l_name[i]:{"val":CMoE_val[i],"sig":data_irrad.l_counts_s[i]/data_irrad.l_counts_v[i],"index":int(i)}}) #Note for now we consider only experimental uncertainty for reference dosimeters, to avoid double values.
            elif ("10" in data_irrad.l_name[i]) and (data_irrad.l_hpge_id[i]=="Fu") and (data_irrad.l_hpge_pos[i]=="p13") :
                dico_norm.update({data_irrad.l_name[i]:{"val":CMoE_val[i],"sig":data_irrad.l_counts_s[i]/data_irrad.l_counts_v[i],"index":int(i)}})
            elif ("3" in data_irrad.l_name[i]) and ("Au" in data_irrad.l_name[i]):
                dico_norm.update({data_irrad.l_name[i]:{"val":CMoE_val[i],"sig":data_irrad.l_counts_s[i]/data_irrad.l_counts_v[i],"index":int(i)}})
            elif ("3" in data_irrad.l_name[i]) and ("Ni" in data_irrad.l_name[i]):
                dico_norm.update({data_irrad.l_name[i]:{"val":CMoE_val[i],"sig":data_irrad.l_counts_s[i]/data_irrad.l_counts_v[i],"index":int(i)}})
            if "x" in data_irrad.l_order[i]: #list of value to get rid of (value with "x" in order)
                index_val += [i]
        # print(dico_norm)
        for i in range(data_irrad.nb_dosi):
            case_csv=data_irrad.l_case_csv[i].split("_")[1][:2]
            if "-g" in data_irrad.l_name[i] : suffix_2="-g" 
            elif "-i" in data_irrad.l_name[i]: suffix_2="-i" 
            else : suffix_2="" 
            if data_irrad.l_mt[i]=="102": # all used thermal sensitive dosimeters do an (n,g) reactions
                # print("slow",data_irrad.l_name[i])
                suffix_1="3" if ((case_csv=="au") and (norm_n=="rp")) else norm_n
                CMoE_div_val2[i] = dico_norm[dico_irrad["begin"]["therm"]+"-"+dico_plate[data_irrad.l_compo_plate[i]]+"-"+dico_irrad["end"]["therm"][case_csv]+suffix_1+suffix_2]["val"]
                CMoE_div_sig2[i] = dico_norm[dico_irrad["begin"]["therm"]+"-"+dico_plate[data_irrad.l_compo_plate[i]]+"-"+dico_irrad["end"]["therm"][case_csv]+suffix_1+suffix_2]["sig"]
                CMoE_div_ref_index[i] = dico_norm[dico_irrad["begin"]["therm"]+"-"+dico_plate[data_irrad.l_compo_plate[i]]+"-"+dico_irrad["end"]["therm"][case_csv]+suffix_1+suffix_2]["index"]
                for j in range(i,data_irrad.nb_dosi):
                    if (data_irrad.l_mt[j]=="102") and (data_irrad.l_case_csv[i]==data_irrad.l_case_csv[j]): 
                        CMoE_div_cor2[i][j]=1
                        CMoE_div_cor2[j][i]=1
            else:
                if (case_csv!="ni"): suffix_1=norm_n  
                elif (norm_n=="rp"): suffix_1="3"
                else: suffix_1= "10"
                # print("fast",data_irrad.l_name[i])
                CMoE_div_val2[i] = dico_norm[dico_irrad["begin"]["fast"]+"-"+dico_plate[data_irrad.l_compo_plate[i]]+"-"+dico_irrad["end"]["fast"][case_csv]+suffix_1+suffix_2]["val"]
                CMoE_div_sig2[i] = dico_norm[dico_irrad["begin"]["fast"]+"-"+dico_plate[data_irrad.l_compo_plate[i]]+"-"+dico_irrad["end"]["fast"][case_csv]+suffix_1+suffix_2]["sig"]
                CMoE_div_ref_index[i] = dico_norm[dico_irrad["begin"]["fast"]+"-"+dico_plate[data_irrad.l_compo_plate[i]]+"-"+dico_irrad["end"]["fast"][case_csv]+suffix_1+suffix_2]["index"]
                for j in range(i,data_irrad.nb_dosi):
                    if (data_irrad.l_mt[j]!="102") and (data_irrad.l_case_csv[i]==data_irrad.l_case_csv[j]): 
                        CMoE_div_cor2[i][j]=1
                        CMoE_div_cor2[j][i]=1
    elif which_norm in ["Custom"]:
        dico_norm.update({"x":{"val":1.,"sig":1.,"index":int(1)}})
        for i in range(data_irrad.nb_dosi):
            if ("10" not in data_irrad.l_name[i]) and (data_irrad.l_name[i] not in dico_norm):
                dico_norm.update({data_irrad.l_name[i]:{"val":CMoE_val[i],"sig":data_irrad.l_counts_s[i]/data_irrad.l_counts_v[i],"index":int(i)}})
            elif ("10" in data_irrad.l_name[i]) and (data_irrad.l_hpge_id[i]=="Fu") and (data_irrad.l_hpge_pos[i]=="p13") and (data_irrad.l_iso[i] not in ["260580","260540"]) and (data_irrad.l_name[i] not in dico_norm):
                dico_norm.update({data_irrad.l_name[i]:{"val":CMoE_val[i],"sig":data_irrad.l_counts_s[i]/data_irrad.l_counts_v[i],"index":int(i)}})
            if "x" in data_irrad.l_order[i]: #list of value to get rid of (value with "x" in order)
                index_val += [i]
        for i in range(data_irrad.nb_dosi):
            case_csv=data_irrad.l_case_csv[i].split("_")[1]
            CMoE_div_val2[i] = dico_norm[data_irrad.l_order[i]]["val"]
            CMoE_div_sig2[i] = dico_norm[data_irrad.l_order[i]]["sig"]
            CMoE_div_ref_index[i] = dico_norm[data_irrad.l_order[i]]["index"]
            for j in range(i,data_irrad.nb_dosi):
                if (data_irrad.l_order[i]==data_irrad.l_order[j]) and (data_irrad.l_case_csv[i]==data_irrad.l_case_csv[j]): 
                    CMoE_div_cor2[i][j]=1
                    CMoE_div_cor2[j][i]=1
    for i in range(data_irrad.nb_dosi): #calculation of al covariance matrices
        for j in range(data_irrad.nb_dosi): 
            # print(        CMoE_div_ref_index[i])
            # CMoE_div_cov[i][j]=CMoE_cov[CMoE_div_ref_index[i]][CMoE_div_ref_index[j]] #to verify syntax
            # CMoE_div_cov[j][i]=CMoE_cov[CMoE_div_ref_index[i]][CMoE_div_ref_index[j]]
            # sub_cov[i][j]=CMoE_cov[i][CMoE_div_ref_index[j]]
            # sub_cov[j][i]=CMoE_cov[i][CMoE_div_ref_index[j]]
            if j==int(CMoE_div_ref_index[i]) and (i!=j):
                Jacobian_CMoEdiv[i][j]=-CMoE_val[i]/(CMoE_val[j]*CMoE_val[j])
        if not i==int(CMoE_div_ref_index[i]):
            Jacobian_CMoEdiv[i][i]=1/CMoE_val[int(CMoE_div_ref_index[i])]
    CMoE_div_cov2=cor_sig_to_cov(np.array(CMoE_div_cor2),np.array(CMoE_div_sig2))
    if not is_offset_cst:
        CMoE_val2, CMoE_cov2=cov_mult((CMoE_val,CMoE_cov),cov_inv((np.array(CMoE_div_val2),CMoE_div_cov2)))
    else:
        CMoE_val2=np.subtract(CMoE_val,CMoE_div_val2)
    if not MC_propagation: #WIP for uncetainty propagation with CMoE_sig etc.
        # Dz=np.diag(CMoE_val2)
        # Dx=np.diag(CMoE_val)
        # Dy=np.diag(CMoE_div_val2)
        # Sigmax=CMoE_cov
        # Sigmay=CMoE_div_cov #to be calculated form CMoE_cov using the cov(ref,ref2)
        # COVxy=sub_cov #to be calculated form CMoE_cov using the cov(dosi,ref(dosi))
        print("Jacobian matrix of normalization")
        # print(Jacobian_CMoEdiv.tolist())
        CMoE_cov2=np.matmul(Jacobian_CMoEdiv,np.matmul(CMoE_cov,Jacobian_CMoEdiv.T))
        print("normalized data covariance")
        print(CMoE_cov2)
        # CMoE_cov2=Dz.dot((Dx.dot(Sigmax.dot(Dx)) + Dy.dot(Sigmay.dot(Dy)) - 2*Dx.dot(COVxy.dot(Dy))).dot(Dz))
    else:

        if No_Cov:
            CMoE_cov=np.diag(np.diag(CMoE_cov))
        RNG=np.random.default_rng()
        Sample_CMoE=RNG.multivariate_normal(CMoE_val,CMoE_cov,size=80000).T
        if not is_offset_cst:
            CMoE_val_array = np.divide(Sample_CMoE,Sample_CMoE[:][CMoE_div_ref_index.astype(int)])
        else:
            CMoE_val_array = np.subtract(Sample_CMoE,Sample_CMoE[:][CMoE_div_ref_index.astype(int)])
        CMoE_sig2=np.std(CMoE_val_array,axis=1,ddof=1)
        CMoE_cov2=np.cov(CMoE_val_array,ddof=1)
        CMoE_val_sample=np.mean(CMoE_val_array,axis=1)
        print("normalized C/E")
        print(CMoE_cov2)
        print("normalized data covariance")
        print(CMoE_cov2)
        print("SSE")
        print(np.sum(np.square(CMoE_val-CMoE_val_sample)))
    # CMoE_val, CMoE_cov = CMoE_val_sample, CMoE_cov2
    CMoE_val_old, CMoE_cov_old = CMoE_val,CMoE_cov
    CMoE_val, CMoE_cov = CMoE_val2, CMoE_cov2


if No_Cov:
    CMoE_cov=np.diag(np.diag(CMoE_cov))
l_chi2=[]
if is_offset_cst and do_chi:
    l_index=[]
    for i in range(len(CMoE_cov)):
        if CMoE_cov[i,i]**0.5<0.0001 or ("x" in  data_irrad.l_order[i]):
            l_index+=[i]
    print("Chi2 after corrections")
    # print(l_index)
    # print(data_irrad.l_order)
    cova = np.delete(np.delete(CMoE_cov,l_index,axis=0),l_index,axis=1)
    res  = np.delete(CMoE_val,l_index,axis=0)
    L_iso  = np.delete(data_irrad.l_iso,l_index,axis=0)
    L_case  = np.delete(data_irrad.l_case_csv,l_index,axis=0)
    cova_inv = np.linalg.inv(cova)
    chis = res.T.dot(cova_inv.dot(res))
    prob = np.exp(-chis/2)
    print("Total chi2, exp(-chi2/2)", chis, prob)
    print("\nResult by part")
    groups=[]
    id_start=0
    for i in range(1,len(cova)):
        if ((L_iso[i]!=L_iso[i-1]) or (L_case[i]!=L_case[i-1])):
            groups+=[[id_start,i-1]]
            id_start=i
    groups+=[[id_start,i]]
    # print(groups)
    for group in groups:
        l_sub_index=[]
        cova2 = cova[group[0]:group[1]+1,group[0]:group[1]+1].copy()
        res2  = res[group[0]:group[1]+1].copy()
        # print(res2)
        cova_inv = np.linalg.inv(cova2)
        chis = res2.T.dot(cova_inv.dot(res2))
        prob = np.exp(-chis/2)
        unc_chi2=-1
        if False:#Jackknife uncertainty
            l_chi2_j=[]
            # print(CMoE_val_array.shape)
            CMoE_samp=np.delete(CMoE_val_array,l_index,axis=0)
            print(CMoE_samp.shape)
            num=0
            start_time=time.time()
            max_val=len(CMoE_samp[0])
            for i in range(len(CMoE_samp[0])): 
                cov_i=np.cov(np.delete(CMoE_samp,i,axis=1),ddof=1)
                # print(cov_i.shape)
                val_i=np.mean(np.delete(CMoE_samp,i,axis=1),axis=1)
                cova_i=cov_i[group[0]:group[1]+1,group[0]:group[1]+1].copy()
                res_i =val_i[group[0]:group[1]+1].copy()
                cov_inv_i=np.linalg.inv(cova_i)
                l_chi2_j+=[res_i.T.dot(cov_inv_i.dot(res_i))]
                num+=1
                now=time.time()
                print("\r["+"="*int(round(num/max_val*50))+" "*int(50-round(num/max_val*50))+"] "+str(round(num/max_val*100))+"% "+str(round(((max_val-num)*(now-start_time)/num)/60)) +"min left", end='',flush=True)

            cov_i=np.cov(CMoE_samp,ddof=1)
            val_i=np.mean(CMoE_samp,axis=1)
            cova_i=cov_i[group[0]:group[1]+1,group[0]:group[1]+1].copy()
            res_i =val_i[group[0]:group[1]+1].copy()
            cov_inv_i=np.linalg.inv(cova_i)
            chis=res_i.T.dot(cov_inv_i.dot(res_i))
            print("\n",i)
            num=len(l_chi2_j)
            print(num)
            print(len(l_chi2_j))
            print(l_chi2_j[0])
            print(np.mean(l_chi2_j))
            print(res_i)
            p1=np.multiply(np.ones(len(l_chi2_j)),chis*num)
            print(np.mean(p1))
            p2=np.multiply(l_chi2_j,num-1)
            print(np.mean(p2))
            l_chi2_j_star=np.subtract(p1,p2)
            # l_chi2_j_star=np.subtract(num*(chis*np.ones(len(l_chi2_j))),(num-1)*np.array(l_chi2_j))
            print(l_chi2_j_star.shape)
            print(np.mean(l_chi2_j_star))
            chi2_star=np.multiply(np.ones(len(l_chi2_j)),np.mean(l_chi2_j_star))
            print(chi2_star.shape)
            print(chi2_star[0])
            print(np.std(l_chi2_j))
            var_chi2=1/num*(np.var(l_chi2_j_star))
            unc_chi2=(var_chi2*num)**0.5
            # unc_chi2=np.sqrt((num-1)/num*sum((l_chi2_j_star-chi2_star)**2))
        elif False: #bootstrap way
            l_chi2_j=[]
            # print(CMoE_samp.shape)
            num=0
            start_time=time.time()
            max_val=4000
            for i in range(max_val): 
                Sample_CMoE=RNG.multivariate_normal(CMoE_val_old,CMoE_cov_old,size=80000).T
                CMoE_val_array = np.subtract(Sample_CMoE,Sample_CMoE[:][CMoE_div_ref_index.astype(int)])
                CMoE_samp=np.delete(CMoE_val_array,l_index,axis=0)
                cov_i=np.cov(CMoE_samp,ddof=1)
                val_i=np.mean(CMoE_samp,axis=1)
                cova_i=cov_i[group[0]:group[1]+1,group[0]:group[1]+1].copy()
                res_i =val_i[group[0]:group[1]+1].copy()
                cov_inv_i=np.linalg.inv(cova_i)
                l_chi2_j+=[res_i.T.dot(cov_inv_i.dot(res_i))]
                num+=1
                now=time.time()
                print("\r["+"="*int(round(num/max_val*50))+" "*int(50-round(num/max_val*50))+"] "+str(round(num/max_val*100))+"% "+str(round(((max_val-num)*(now-start_time)/num)/60)) +"min left", end='',flush=True)
            print()
            print(len(l_chi2_j))
            chis=np.mean(l_chi2_j)
            unc_chi2=np.std(l_chi2_j)
            # unc_chi2=np.sqrt((num-1)/num*sum((l_chi2_j_star-chi2_star)**2))

        # print(chi2_star)
        print("exp %s, iso %s, nb dosi %d ,  chi2=%f+-%f, exp(-chi2/2)=%e" % (L_case[group[0]],L_iso[group[0]],len(res2),chis,unc_chi2, prob))
        #saving reduced chi2
        l_chi2+=[r'\chi^2_{\nu}='+str(round(chis/len(res2),1))]*(len(res2)+1)
        # l_chi2+=[r'\chi^2='+str(round(chis,1-int(np.floor(np.log10(chis)))))]*(len(res2)+1)
print(len(l_chi2))
# exit()
# print(CMoE_div_cor2)
if not do_remove: # effective getting rid of the value with"x" 
    CMoE_val=np.delete(CMoE_val,index_val) 
    CMoE_cov=np.delete(np.delete(CMoE_cov,index_val,axis=1),index_val,axis=0)
    if CoC_mode: #exfiltrate m_c
        relunc_c=np.delete(cov_to_sig_cor(m_c)[0]/l_c,index_val)
        relunc_c_all=cov_to_sig_cor(m_c)[0]/l_c



l_terms_a_aff = list(filter(lambda p: p[3] is not None, l_terms_a_mult))+[
                    # (l_c2e,              m_c2e,      "C2E",  "sig",            (-1,1)),
                    # (l_ctot,              m_ctot,      "All",  "sig",            (-1,1)),
                    (l_c,                m_c,        "C",    "sig",            (-1,1)),
                    (l_e,                m_e,        "E",    "sig",            (-1,1)),
                    # (l_Act,              m_Act,     "Activity" ,"val and sig"+" already minus 1",            (-1,1)),
                    (l_not_norm,         m_not_norm,     "C/E-1" ,"val and sig",            (-1,1)),
                    (CMoE_val,           CMoE_cov,   "Renormalized C/E-1","val and sig"+" already minus 1"*int(is_offset_cst),    (-1,1))
                ]

l_terms_a_aff_Exp = list(filter(lambda p: p[3] is not None, l_terms_a_mult_RR))+[
                    # (l_e,                m_e,        "E",    "sig",            (-1,1)),
                    (l_Act,              m_Act,     "Activity" ,"val and sig"+" already minus 1",            (-1,1)),
                    (l_RR,              m_RR,     "Reaction rates" ,"val and sig"+" already minus 1",            (-1,1)),
                ]


if False : #Act
    aff_act=[(l_Act,              m_Act,     "Activity" ,"val and sig",            (-1,1))]
    figa=plt.figure()
    l_ax2 = my_sub6(figa,2,1,1,list_rx=[1]*len(aff_act),list_sx=[0.34]*(len(aff_act)-1),list_ry=[0.8,0.3, 0.14],auto_y=False,auto_x=False,mh=-0.22)
    for imat, (v,cov,blabla, mode, minimaxi) in enumerate(aff_act):
        l_cut_ND=[]
        lx = np.arange(len(cov))
        sig, cor = cov_to_sig_cor(cov)
        mini,maxi = minimaxi
        if maxi == 1: maxi = 1.001
        aff_mat4(lx, lx, cor, l_ax2[imat][0], "horizontal", blabla, "", "", pad=0.01,
            xlim=None, ylim=None,
            logz=None, logx=False, logy=False, minimaxi=(mini,maxi), midblanc=True if mini==-1 else False, midgreen=False, minblanc=True if blabla=="ND_{dosi}" else False, nb_leg=4,
            maxblanc=False, centered=False, smooth=None, pcol=False,head_top=True, maskout=False, simple_scale=False)
        do_minus= False # to avoid the -1 if already normalized
        ymin_val=min([min(v-1*int(do_minus))*100,-10])
        ymax_val=max([max(v-1*int(do_minus))*100+5,10])
        ymin_val2= math.floor(ymin_val/10)*10 if (ymin_val-math.floor(ymin_val/10)*10)<5 else math.floor(ymin_val/10)*10+5
        ymax_val2= math.ceil(ymax_val/10)*10 if (math.ceil(ymax_val/10)*10-ymax_val)<5 else math.ceil(ymax_val/10)*10-5
        # ymax_val2+=5
        ylim, pos =[ymin_val2, ymax_val2], np.arange(ymin_val2,ymax_val2,10).tolist()     #Key: graph_lim , Modification of the graph ylim as some In-i C/E are not visible
        if len(pos)<3 : pos=np.arange(ymin_val2,ymax_val2,5).tolist()
        l_iref=[]
        l_cut_ND += [-(lx[0]+lx[1])/2]
        id_cea_Cr_al=0
        for idosi in range(len(v)): #replaced data_irrad.nb_dosi by len(v) to allow reduced size C/E
            lw=2 if len(lcase_csv)<10 else 1.5
            key_cea=data_irrad.l_case_csv[idosi][3:]
            l_ax2[imat][1].errorbar([lx[idosi]], [(v[idosi]-1*int(do_minus))*100], [sig[idosi]*100],c=get_c_elt(data_irrad.l_mat[idosi]),linewidth=lw, alpha=1)
            if idosi < (len(v)-1):
                if (data_irrad.l_aaa[idosi] != data_irrad.l_aaa[idosi+1]):
                    l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                    l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                    l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                    # l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                if (data_irrad.l_NDlib[idosi] != data_irrad.l_NDlib[idosi+1]):
                    l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                    l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                    l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                    l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                if (data_irrad.l_compo_plate[idosi] != data_irrad.l_compo_plate[idosi+1]) and (data_irrad.l_compo_plate[idosi+1]!="Ni"):
                    l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1],linewidth=1)
                    l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1],linewidth=1)
                    l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1],linewidth=1)
        if l_iref:
            for iref in l_iref:
                l_ax2[imat][1].plot([lx[iref]],[0],marker="x",c=get_c_elt(data_irrad.l_mat[iref]))
        l_cut_ND += [lx[idosi]+(lx[0]+lx[1])/2]
        #aff_err_predic(ax, lx,(sig/v)*100,slx,sly,c,a1,a2)
        l_ax2[imat][1].set_ylabel(tex(r"Difference [\%]"), size=get_aff_size("s_xylabel"))
        l_ax2[imat][2].set_ylim([0, 1])
        #ylim, pos =[-50, 50], [-40, -20, 0, 20, 40]
        #ylim, pos =[-30, 30], [-20, -10, 0, 10, 20]
        #ylim, pos =[-25, 25],  np.arange(-20, 21, 10)
        #ylim, pos =[-20, 20], [-15, -10, -5, 0, 5, 10, 15]
        # ylim, pos =[-15, 15], [-10, -5,  0, 5,  10]
        # l_ax2[imat][1].set_ylim(ylim)
        # l_ax2[imat][1].set_yticks(pos)
        #if True:
        #    l_ax2[imat][1].set_ylim([-50, 50])
        #    l_pos = [-40, -20, 0, 20, 40]
        #else:
        #    l_ax2[imat][1].set_ylim([-15, 15])
        #    l_pos = [-10,-5, 0, 5, 10]
        # l_ax2[imat][1].plot(l_ax2[imat][0].get_xlim(),[0,0], c="gray",dashes=[5,3], zorder=-10)
    plt.show()
# kick correction factor matrix if fully correlated
if False:l_terms_a_aff=l_terms_a_aff[1:]
# if np.equal(np.ones(cov_f.shape),cov_to_sig_cor(l_terms_a_aff[0][1])[1]).all():l_terms_a_aff=l_terms_a_aff[1:]

do_minus= not is_offset_cst # to avoid the -1 if already normalized
ymin_val=min([min(CMoE_val-1*int(do_minus))*100,-10])
ymax_val=max([max(CMoE_val-1*int(do_minus))*100,10])
print(ymin_val,ymax_val)

ylim_avt = l_ax[0].get_ylim()



#for t in l_time_dash_todo:
#    l_ax[0].plot([t,t],l_ax[0].get_ylim(),c=(0.7,0.7,0.7), zorder=-10) # dashes=[2,5],
    
    
    
    

    
    
    
l_ax[0].set_ylim(ylim_avt)
    
#l_ax[0].plot([0,0],l_ax[0].get_ylim(),c=(0.3,0.3,0.3),dashes=[2,5])

l_ax[0].set_xlabel(r"$\mathrm{Time~[h]}$", size=get_aff_size("s_leg")*0.8)
#l_ax[0].set_ylabel(r"$\mathrm{Counts~[s^{-1}]}$", size=get_aff_size("s_xylabel"))
l_ax[0].set_ylabel(r"$\mathrm{Power~[W]}$", size=get_aff_size("s_leg")*0.8)
l_ax[0].tick_params(axis='both', which='both', labelsize=get_aff_size("s_leg")*0.8)
l_ax[0].set_title(r"$\mathrm{Fission~chamber~monitors}$", fontsize=get_aff_size("s_leg")*0.8)
l_ax[0].legend(loc='best', fontsize=get_aff_size("s_leg")*0.7, ncol=2)

l_ax[1].set_xlabel(r"$\mathrm{Time~[h]}$", size=get_aff_size("s_leg")*0.8)
l_ax[1].set_ylabel(r"$\mathrm{Cumulated~energy~[Wh]}$", size=get_aff_size("s_leg")*0.8)
l_ax[1].tick_params(axis='both', which='both', labelsize=get_aff_size("s_leg")*0.8)
l_ax[1].set_title(r"$\mathrm{Integral~weighted~by~element~decay}$", fontsize=get_aff_size("s_leg")*0.8)
l_ax[1].legend(loc='best', fontsize=get_aff_size("s_leg")*0.7, ncol=2)

if rr_shape: l_ax[2].set_xlabel(r"$\mathrm{Position~[cm]}$", size=get_aff_size("s_leg")*0.8)
if rr_shape: l_ax[2].set_ylabel(r"$\mathrm{Reaction~rate~[a.u.]}$", size=get_aff_size("s_leg")*0.8)
if rr_shape: l_ax[2].tick_params(axis='both', which='both', labelsize=get_aff_size("s_leg")*0.8)
if rr_shape: l_ax[2].set_title(r"$\mathrm{Reaction~rate~shape}$", fontsize=get_aff_size("s_leg")*0.8)
#l_ax[2].legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)

#l_ax[1].set_xscale('log')
#l_ax[1].set_yscale('log')


l_ax[0].set_ylim([0, puiss_max_plot])
l_ax[1].set_ylim([0,l_ax[1].get_ylim()[1]])

def Mega_plot(l_terms_a_aff=l_terms_a_aff):
    if Exp_only and len(lcase_csv)>4:
        l_ax2 = my_sub6(fig,2,1,1,list_rx=[0.3]*(len(l_terms_a_aff)-2)+[2,2],list_sx=[0.34]*(len(l_terms_a_aff)-3)+[0.6,0.4],list_ry=[0.8,0.3, 0.14],auto_y=False,auto_x=False,mh=-0.22)
    elif Exp_only:
        l_ax2 = my_sub6(fig,2,1,1,list_rx=[0.8]*(len(l_terms_a_aff)-2)+[1,1],list_sx=[0.34]*(len(l_terms_a_aff)-3)+[0.6,0.4],list_ry=[0.8,0.3, 0.14],auto_y=False,auto_x=False,mh=-0.22)
    elif len(lcase_csv)>10:
        l_ax2 = my_sub6(fig,2,1,1,list_rx=[1]*(len(l_terms_a_aff)-1)+[2],list_sx=[0.34]*(len(l_terms_a_aff)-2)+[0.4],list_ry=[0.8,0.3, 0.14],auto_y=False,auto_x=False,mh=-0.22)
    else:
        l_ax2 = my_sub6(fig,2,1,1,list_rx=[1]*len(l_terms_a_aff),list_sx=[0.34]*(len(l_terms_a_aff)-1),list_ry=[0.8,0.3, 0.14],auto_y=False,auto_x=False,mh=-0.22)
    for imat, (v,cov,blabla, mode, minimaxi) in enumerate(l_terms_a_aff):
        if (not do_remove) and (len(v)!=data_irrad.nb_dosi): data_irrad._remove_commented(True) # Will eventually do the job as long as the reduced array are  last in l_terms_a_aff
        l_cut_ND=[]
        lx = np.arange(len(cov))
        sig, cor = cov_to_sig_cor(cov)
        mini,maxi = minimaxi
        if maxi == 1: maxi = 1.001
        aff_mat4(lx, lx, cor, l_ax2[imat][0], "horizontal", blabla, "", "", pad=0.01,
            xlim=None, ylim=None,
            logz=None, logx=False, logy=False, minimaxi=(mini,maxi), midblanc=True if mini==-1 else False, midgreen=False, minblanc=True if blabla=="ND_{dosi}" else False, nb_leg=4,
            maxblanc=False, centered=False, smooth=None, pcol=False,head_top=True, maskout=False, simple_scale=False)
        # l_ax2[imat][2].set_title(blabla)
        if blabla=="ND_{dosi}": blabla=r"ND$_{dosi}$"
        if blabla=="ND_{XS}": blabla=r"ND$_{XS}$"
        l_ax2[imat][2].set_title(blabla, size=get_aff_size("s_xylabel")-8,y=1.0,pad=-6)
        if mode == 'sig':
            if max((sig/v)*100)>1:
                l_ax2[imat][1].set_ylim([0,10])
                ylim=[0,10]
                l_pos = [2,4,6,8,10]
            else:
                l_ax2[imat][1].set_ylim([0,1])
                ylim=[0,1]
                l_pos = [0.2,0.4,0.6,0.8,1]
            for idosi in range(data_irrad.nb_dosi):
                l_ax2[imat][1].plot([idosi], [(sig[idosi]/v[idosi])*100],'o', c=get_c_elt(data_irrad.l_mat[idosi]))
                #l_ax2[imat][2].plot([idosi], [v[idosi]],'o', c=get_c_elt(data_irrad.l_mat[idosi]))
                if idosi < (len(v)-1):
                    if (data_irrad.l_aaa[idosi] != data_irrad.l_aaa[idosi+1]):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                        # l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                    if (data_irrad.l_NDlib[idosi] != data_irrad.l_NDlib[idosi+1]):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                        l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                    if (data_irrad.l_compo_plate[idosi] != data_irrad.l_compo_plate[idosi+1]) and (data_irrad.l_compo_plate[idosi+1]!="Ni"):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1],linewidth=1)
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1],linewidth=1)
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1],linewidth=1)
            l_ax2[imat][1].set_ylabel(tex(r"\sigma_{rel} [\%]"), size=get_aff_size("s_xylabel")-8)
            if max((sig/v)*100)>1:
                l_ax2[imat][1].set_ylim([0,10])
                l_pos = [2,4,6,8,10]
            else:
                l_ax2[imat][1].set_ylim([0,1])
                l_pos = [0.2,0.4,0.6,0.8,1]
            l_ax2[imat][1].set_yticks(l_pos)
            #l_ax2[imat][1].set_xticklabels(map(lambda p: nice_nb(p, mode_exp=False, log=logz),l_pos))
            l_ax2[imat][2].axis('off')
            l_ax2[imat][2].set_ylim([0, 1])
            
        elif "Activity" in blabla or "Reaction rates" in blabla:
            do_minus= False # to avoid the -1 if already normalized
            ymin_val=min([min(v-1*int(do_minus)),-10])
            ymax_val=max([max(v-1*int(do_minus))+5,10])
            ymin_val2= math.floor(ymin_val/10)*10 if (ymin_val-math.floor(ymin_val/10)*10)<5 else math.floor(ymin_val/10)*10+5
            ymax_val2= math.ceil(ymax_val/10)*10 if (math.ceil(ymax_val/10)*10-ymax_val)<5 else math.ceil(ymax_val/10)*10-5
            # ymax_val2+=5
            ylim, pos =[ymin_val2, ymax_val2], np.arange(ymin_val2,ymax_val2,10).tolist()     #Key: graph_lim , Modification of the graph ylim as some In-i C/E are not visible
            if len(pos)<3 : pos=np.arange(ymin_val2,ymax_val2,5).tolist()
            l_iref=[]
            l_cut_ND += [-(lx[0]+lx[1])/2]
            id_cea_Cr_al=0
            ax3=l_ax2[imat][1].twinx()
            for idosi in range(len(v)): #replaced data_irrad.nb_dosi by len(v) to allow reduced size C/E
                lw=2 if len(lcase_csv)<10 else 1.5
                key_cea=data_irrad.l_case_csv[idosi][3:]
                if sig[idosi]<0.01: l_iref+=[idosi]
                if use_CEA_Cr_al and (idosi >= 9)and (idosi<17): #very special temporary case for al dosi with Cr
                    l_ax2[imat][1].errorbar([lx[idosi]], [[CEA_res["Cr_al"][idosi-9]]], [sig[idosi]],c=get_c_elt(data_irrad.l_mat[idosi]),linewidth=lw, alpha=1-0.8*float(CoC_mode))
                    id_cea_Cr_al+=1
                    print(idosi)
                else:
                    ax3.plot([idosi], [(sig[idosi]/v[idosi])*100],'o', c=get_c_elt(data_irrad.l_mat[idosi]),alpha=0.5)
                    l_ax2[imat][1].errorbar([lx[idosi]], [(v[idosi]-1*int(do_minus))], [sig[idosi]],c=get_c_elt(data_irrad.l_mat[idosi]),marker="x",markersize=8,linewidth=4, alpha=1-0.8*float(CoC_mode))
                if CoC_mode and False:
                    l_ax2[imat][1].errorbar([lx[idosi]], [(v[idosi]-1*int(do_minus))], [relunc_c[idosi]],c=get_c_elt(data_irrad.l_mat[idosi]),linewidth=lw, alpha=1)
                # key_cea=lcase_csv[1][3:]
                if (plot_CEA) and (key_cea in CEA_res.keys()) and  (idosi<9):
                    # print(idosi)
                    l_ax2[imat][1].errorbar([lx[idosi]+0.4], [CEA_res[key_cea][idosi]], [CEA_sig[key_cea][idosi]],c="g",marker=".",alpha=0.8)
                if (plot_CEA) and (key_cea in CEA_res.keys()) and (idosi>8)and (idosi<18):
                    l_ax2[imat][1].errorbar([lx[idosi]+0.4], [CEA_res[key_cea][idosi-9]], [CEA_sig[key_cea][idosi-9]],c="g",marker=".",alpha=0.8)
                if (plot_CEA) and (key_cea in CEA_res.keys()) and (idosi >= 18)and (idosi<27) and (key_cea+"_IN" in CEA_res.keys()):
                    l_ax2[imat][1].errorbar([lx[idosi]+0.4], [CEA_res[key_cea+"_IN"][idosi-18]], [CEA_sig[key_cea+"_IN"][idosi-18]],c="g",marker=".",alpha=0.8)
                if idosi < (len(v)-1):
                    if (data_irrad.l_aaa[idosi] != data_irrad.l_aaa[idosi+1]):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                        # l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                    if (data_irrad.l_NDlib[idosi] != data_irrad.l_NDlib[idosi+1]):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                        l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                    if (data_irrad.l_compo_plate[idosi] != data_irrad.l_compo_plate[idosi+1]) and (data_irrad.l_compo_plate[idosi+1]!="Ni"):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1],linewidth=1)
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1],linewidth=1)
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1],linewidth=1)
            if l_iref:
                for iref in l_iref:
                    l_ax2[imat][1].plot([lx[iref]],[0],marker="x",c=get_c_elt(data_irrad.l_mat[iref]))
            l_cut_ND += [lx[idosi]+(lx[0]+lx[1])/2]
            #aff_err_predic(ax, lx,(sig/v),slx,sly,c,a1,a2)
            ax3.set_ylabel(tex(r"\sigma_{rel} [\%]"), size=get_aff_size("s_xylabel"))
            if max((sig/v)*100)>1:
                ax3.set_ylim([0,4])
                l_pos = [1,2,3,4]
            else:
                ax3.set_ylim([0,1])
                l_pos = [0.2,0.4,0.6,0.8,1]
            ax3.set_yticks(l_pos)
            ax3.tick_params(labelsize=get_aff_size("s_xylabel")-8)
            if "Activity" in blabla:
                l_ax2[imat][1].set_ylabel(tex("Activity [Bq]"), size=get_aff_size("s_xylabel")-8)
            else:
                l_ax2[imat][1].set_ylabel(tex("RR [at/s]"), size=get_aff_size("s_xylabel")-8)
            l_ax2[imat][2].set_ylim([0, 1])
            #ylim, pos =[-50, 50], [-40, -20, 0, 20, 40]
            #ylim, pos =[-30, 30], [-20, -10, 0, 10, 20]
            #ylim, pos =[-25, 25],  np.arange(-20, 21, 10)
            #ylim, pos =[-20, 20], [-15, -10, -5, 0, 5, 10, 15]
            # ylim, pos =[-15, 15], [-10, -5,  0, 5,  10]
            # l_ax2[imat][1].set_ylim(ylim)
            l_ax2[imat][1].set_yscale("log")
            # l_ax2[imat][1].yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator())
            #if True:
            #    l_ax2[imat][1].set_ylim([-50, 50])
            #    l_pos = [-40, -20, 0, 20, 40]
            #else:
            #    l_ax2[imat][1].set_ylim([-15, 15])
            #    l_pos = [-10,-5, 0, 5, 10]
            # l_ax2[imat][1].plot(l_ax2[imat][0].get_xlim(),[0,0], c="gray",dashes=[5,3], zorder=-10)
        elif "val and sig" in mode:
            do_minus= not (( "already" in mode ) and (is_offset_cst)) # to avoid the -1 if already normalized
            ymin_val=min([min(v-1*int(do_minus))*100,-10])
            ymax_val=max([max(v-1*int(do_minus))*100+5,10])
            ymin_val2= math.floor(ymin_val/10)*10 if (ymin_val-math.floor(ymin_val/10)*10)<5 else math.floor(ymin_val/10)*10+5
            ymax_val2= math.ceil(ymax_val/10)*10 if (math.ceil(ymax_val/10)*10-ymax_val)<5 else math.ceil(ymax_val/10)*10-5
            # ymax_val2+=5
            ylim, pos =[ymin_val2, ymax_val2], np.arange(ymin_val2,ymax_val2,10).tolist()     #Key: graph_lim , Modification of the graph ylim as some In-i C/E are not visible
            if len(pos)<3 : pos=np.arange(ymin_val2,ymax_val2,5).tolist()
            l_iref=[]
            l_cut_ND += [-(lx[0]+lx[1])/2]
            id_cea_Cr_al=0
            for idosi in range(len(v)): #replaced data_irrad.nb_dosi by len(v) to allow reduced size C/E
                lw=5 if len(lcase_csv)<10 else 1.5
                key_cea=data_irrad.l_case_csv[idosi][3:]
                if sig[idosi]*100<0.01: l_iref+=[idosi]
                if use_CEA_Cr_al and (idosi >= 9)and (idosi<17): #very special temporary case for al dosi with Cr
                    l_ax2[imat][1].errorbar([lx[idosi]], [[CEA_res["Cr_al"][idosi-9]*100]], [sig[idosi]*100],c=get_c_elt(data_irrad.l_mat[idosi]),linewidth=lw, alpha=1-0.8*float(CoC_mode))
                    id_cea_Cr_al+=1
                    print(idosi)
                else:
                    l_ax2[imat][1].errorbar([lx[idosi]], [(v[idosi]-1*int(do_minus))*100], [sig[idosi]*100],c=get_c_elt(data_irrad.l_mat[idosi]),linewidth=lw, alpha=1-0.8*float(CoC_mode))
                if CoC_mode:
                    if "Renormalized" in blabla:
                        l_ax2[imat][1].errorbar([lx[idosi]], [(v[idosi]-1*int(do_minus))*100], [relunc_c[idosi]*100],c=get_c_elt(data_irrad.l_mat[idosi]),linewidth=lw, alpha=1)
                    else:
                        l_ax2[imat][1].errorbar([lx[idosi]], [(v[idosi]-1*int(do_minus))*100], [relunc_c_all[idosi]*100],c=get_c_elt(data_irrad.l_mat[idosi]),linewidth=lw, alpha=1)
                # key_cea=lcase_csv[1][3:]
                if (plot_CEA) and (key_cea in CEA_res.keys()) and  (idosi<9):
                    # print(idosi)
                    l_ax2[imat][1].errorbar([lx[idosi]+0.4], [CEA_res[key_cea][idosi]*100], [CEA_sig[key_cea][idosi]*100],c="g",marker=".",alpha=0.8)
                if (plot_CEA) and (key_cea in CEA_res.keys()) and (idosi>8)and (idosi<18):
                    l_ax2[imat][1].errorbar([lx[idosi]+0.4], [CEA_res[key_cea][idosi-9]*100], [CEA_sig[key_cea][idosi-9]*100],c="g",marker=".",alpha=0.8)
                if (plot_CEA) and (key_cea in CEA_res.keys()) and (idosi >= 18)and (idosi<27) and (key_cea+"_IN" in CEA_res.keys()):
                    l_ax2[imat][1].errorbar([lx[idosi]+0.4], [CEA_res[key_cea+"_IN"][idosi-18]*100], [CEA_sig[key_cea+"_IN"][idosi-18]*100],c="g",marker=".",alpha=0.8)
                if idosi < (len(v)-1):
                    if (data_irrad.l_aaa[idosi] != data_irrad.l_aaa[idosi+1]):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                        # l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                    if (data_irrad.l_NDlib[idosi] != data_irrad.l_NDlib[idosi+1]):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1])
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1])
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1])
                        l_cut_ND +=[(lx[idosi]+lx[idosi+1])/2]
                    if (data_irrad.l_compo_plate[idosi] != data_irrad.l_compo_plate[idosi+1]) and (data_irrad.l_compo_plate[idosi+1]!="Ni"):
                        l_ax2[imat][1].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=ylim[0],ymax=ylim[1],linewidth=1)
                        l_ax2[imat][0].vlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",ymin=[-1],ymax=[len(v)+1],linewidth=1)
                        l_ax2[imat][0].hlines((lx[idosi]+lx[idosi+1])/2,linestyle="--",color="k",xmin=[-1],xmax=[len(v)+1],linewidth=1)
            if l_iref:
                for iref in l_iref:
                    l_ax2[imat][1].plot([lx[iref]],[0],marker="x",c=get_c_elt(data_irrad.l_mat[iref]))
            l_cut_ND += [lx[idosi]+(lx[0]+lx[1])/2]
            #aff_err_predic(ax, lx,(sig/v)*100,slx,sly,c,a1,a2)
            l_ax2[imat][1].set_ylabel(tex(r"Difference [\%]"), size=get_aff_size("s_xylabel")-8)
            l_ax2[imat][2].set_ylim([0, 1])
            #ylim, pos =[-50, 50], [-40, -20, 0, 20, 40]
            #ylim, pos =[-30, 30], [-20, -10, 0, 10, 20]
            #ylim, pos =[-25, 25],  np.arange(-20, 21, 10)
            #ylim, pos =[-20, 20], [-15, -10, -5, 0, 5, 10, 15]
            # ylim, pos =[-15, 15], [-10, -5,  0, 5,  10]
            l_ax2[imat][1].set_ylim(ylim)
            l_ax2[imat][1].set_yticks(pos)
            #if True:
            #    l_ax2[imat][1].set_ylim([-50, 50])
            #    l_pos = [-40, -20, 0, 20, 40]
            #else:
            #    l_ax2[imat][1].set_ylim([-15, 15])
            #    l_pos = [-10,-5, 0, 5, 10]
            l_ax2[imat][1].plot(l_ax2[imat][0].get_xlim(),[0,0], c="gray",dashes=[5,3], zorder=-10)
        
        if True:
            if False:
                l_name = []
                for i in range(data_irrad.nb_dosi):
                    key    = data_irrad.l_name[i].split("-")[1]
                    mat    = data_irrad.l_mat[i]
                    aaa    = data_irrad.l_aaa[i]
                    mt_tex = d_mt2tex[data_irrad.l_mt[i]]
                    #l_name += [tex("^{"+aaa+"}_{"+mt_tex+'}'+mat+"^{"+key+"}")]
                    l_name += [tex(mt_tex+"^{"+aaa+"}"+mat+"^{"+key+"}")]
            
                if len(l_name)<6:
                    l_ax2[imat][0].set_yticks(lx)
                    l_ax2[imat][0].set_xticks(lx)
                    l_ax2[imat][0].set_xticklabels(map(lambda n:n, l_name), size=get_aff_size("s_tick")*0.5, rotation=(0 if len(l_name)<4 else 45))
                    l_ax2[imat][0].set_yticklabels(map(lambda n:n, l_name), size=get_aff_size("s_tick")*0.5)
            
                else:
                    l_ax2[imat][0].set_xticks(lx[::2])
                    l_ax2[imat][0].set_yticks(lx[1::2])
                    #l_namesx = map(lambda (i,name): "" if (i%2==0) else name, enumerate(l_name))
                    #l_namesy = map(lambda (i,name): "" if (i%2==1) else name, enumerate(l_name))
                    l_namesy = l_name[::2]
                    l_namesx = l_name[1::2]
                    l_ax2[imat][0].set_yticklabels(map(lambda n:n, l_namesx), size=get_aff_size("s_tick")*0.5)
                    l_ax2[imat][0].set_xticklabels(map(lambda n:n, l_namesy), size=get_aff_size("s_tick")*0.5, rotation=80)
            else:
                def aff(i0, i1, l, pos, fct_txt, fct_c, aff_if_alone=True, is_long=False,centring="center",large_txt=False, larger=False):
                    l_cut = []
                    size = get_aff_size("s_tick")*0.65
                    if "chi" in l[0] or large_txt: size*=0.8
                    if larger: size=get_aff_size("s_tick")
                    dec = 0.3
                    i0_save = i0
                    for i in np.arange(i0,i1):
                        if l[i] != l[i0]:
                            #print i0, i, i0-dec,i-1+dec
                            if (not is_long) or (i-i0>5):
                                if centring =="left":
                                    posi=i0
                                    tpos="left"
                                elif centring=="right":
                                    posi=i-0.5
                                    tpos="right"
                                else:
                                    posi=0.5*(i0+i)-0.5
                                    tpos="center"
                                l_ax2[imat][2].text(posi,pos-0.02, tex(fct_txt(i0)), va="bottom", ha=tpos, size=size)
                                l_ax2[imat][2].plot([i0-dec,i-1+dec],[pos,pos],c=fct_c(i0))
                            l_cut += [(i0,i)]
                            i0 = i
                    if i0!=i0_save or aff_if_alone:
                        if centring =="left":
                            posi=i0-1
                            tpos="left"
                        elif centring=="right":
                            posi=i-0.5
                            tpos="right"
                        else:
                            posi=0.5*(i0+i)-0.5
                            tpos="center"
                        if (not is_long) or (i-i0>5):
                            l_ax2[imat][2].text(posi+1,pos-0.02, tex(fct_txt(i0)), va="bottom", ha=tpos, size=size)
                            l_ax2[imat][2].plot([i0-dec,i+1-1+dec],[pos,pos],c=fct_c(i0))
                        l_cut += [(i0,i+1)]
                    else:
                        l_cut += [(i0,i+1)]
                    return l_cut
                
                
                l_cut = aff(0, data_irrad.nb_dosi, data_irrad.l_mat_with_iso, 0.33, lambda i: data_irrad.l_mat_with_iso[i],  lambda i:get_c_elt(data_irrad.l_mat[i]), larger=False)
                l_cut_new = []
                for i0,i1 in l_cut:
                    mt2tex = {102:r'\gamma', 12102:r'\gamma', 103: r'p',107: r'\alpha', 4: r"n'",11004:r"n'"}
                    l_cut_new += aff(i0,i1, data_irrad.l_mt, 0.05,  lambda i: mt2tex[int(data_irrad.l_mt[i])],  lambda i:(0,0,0), larger=False)
                l_cut_new2 = []
                # for i0,i1 in l_cut_new:
                #     l_cut_new2 += aff(i0,i1, data_irrad.l_aaa, 0.05, lambda i: data_irrad.l_aaa[i],  lambda i:(0,0,0), False)
                for (i1,i2) in l_cut_new2[1:]:
                    c, dec = (0,0,0), 0.06 * data_irrad.nb_dosi / 43
                    #print data_irrad.nb_dosi
                    #exit()
                    l_ax2[imat][1].plot([i1-0.5,i1-0.5],l_ax2[imat][1].get_ylim(), linewidth=0.5, c=c)
                    l_ax2[imat][0].plot([i1-0.5,i1-0.5],l_ax2[imat][0].get_ylim(), linewidth=0.5, c=c)
                    l_ax2[imat][0].plot(l_ax2[imat][0].get_ylim(),[i1-0.5-dec,i1-0.5-dec], linewidth=0.5, c=c)
                dummy=[]
                l_lib=[]
                for lib in data_irrad.l_NDlib:
                    if True:
                        if lib in d_lib:
                            l_lib+=[d_lib[lib]]
                        else:
                            l_lib+=[lib]
                    else:
                        l_lib+=[lib]
                l_lib2=[]
                for lib in data_irrad.l_compo_plate_full_name:
                    if True:
                        l_lib2+=[lib]
                pdown=0
                if len(np.unique(l_lib2))>1:
                    pdown=1
                if len(l_lib2) <80: 
                    if not Exp_only: dummy += aff(0,len(l_lib2), l_lib2, -0.5, lambda i: l_lib2[i],  lambda i:(0,0,0), False, True,centring="center", large_txt=True)
                if not Exp_only: dummy += aff(0,len(l_lib), l_lib, -0.4 - 0.6*int(pdown), lambda i: l_lib[i],  lambda i:(0,0,0), False, True,centring="left")
                # if len(l_lib2) <80: dummy += aff(0,len(l_lib2), l_lib2, -0.3, lambda i: l_lib2[i],  lambda i:(0,0,0), False, True,centring="center", large_txt=True)
                if not Exp_only: dummy += aff(0,len(data_irrad.l_Activ_Energy), data_irrad.l_Activ_Energy, -2.1, lambda i: data_irrad.l_Activ_Energy[i],  lambda i:(0,0,0), True, True,centring="right")
                if len(l_chi2)==len(v) and not Exp_only:
                    print("TEST")
                    if len(l_chi2) <80:dummy += aff(0,len(l_chi2), l_chi2, -0.7, lambda i: l_chi2[i],  lambda i:(0,0,0), True, True,centring="left")
                #l_ax2[imat][2].patch.set_visible(False)
                l_ax2[imat][2].axis('off')
                
                l_ax2[imat][0].set_xticks([])
                l_ax2[imat][0].set_yticks([])
                l_ax2[imat][1].set_xticks([])
                l_ax2[imat][2].set_xticks([])
            

        l_ax2[imat][1].set_xlim(l_ax2[imat][0].get_xlim())
        l_ax2[imat][2].set_xlim(l_ax2[imat][0].get_xlim())
        #l_ax2[imat][1].set_ylabel(r"$\sigma_{rel}~[\%]$")
        if No_cov:l_ax2[imat][0].remove()
    
#my_sub6_finalise(l_ax2)

if Exp_only:
    Mega_plot(l_terms_a_aff_Exp)
    save_key+="Exp" if save_key=="" else "_Exp" 
    # plt.tight_layout(pad=15)
    plt.subplots_adjust(wspace=0.4,hspace=2.4)
else:
    Mega_plot()

if CoC_mode:
    save_key+="CoC" if save_key=="" else "_CoC" 

#add to csv file
print (aff_list("l_name",                data_irrad.l_name))
aff_decription_s_v_cov("Corrected C/E-1",   (CMoE_val,   CMoE_cov  ))


if not os.path.exists("irra2hpge_out"):
    os.mkdir("irra2hpge_out")

print ("export csv")
export_csv("irra2hpge_out/irrad2hpge.csv")

# plt.show()
print ("export jpg")
if save_key != "":
    save_key = "_"+save_key
fig.savefig("irra2hpge_out/irrad2hpge"+save_key+".png", bbox_inches=('tight'), dpi=400)


if save_key != "": export_csv("irra2hpge_out/irrad2hpge"+save_key+".csv")

LTC=False
if LTC:
    #Linear Trends Calculations. Quite useless :P
    v=CMoE_val
    cov=CMoE_cov

    rng=np.random.default_rng()
    Samples=rng.multivariate_normal(v,cov,size=2**16)
    print(Samples.shape)
    A=[]
    B=[]
    def flin(X,a,b):
        return np.multiply(X,a)+b
    print("start calc")
    for s in Samples:
        coef,sig =curve_fit(flin,range(1,10),s)
        A+=[coef[0]]
        B+=[coef[1]]
    fig2,axs=plt.subplots(1,2)
    # plt.subplot(121)
    axs[0].hist(A,bins=20)
    axs[0].set_title("Slope")
    ax2=axs[0].twinx()
    ax2.hist(A,bins=41,cumulative=True,histtype="step",color="r")
    # plt.subplot(122)
    axs[1].hist(B,bins=20)
    axs[1].set_title("Ordinate")
    ax3=axs[1].twinx()
    ax3.hist(B,bins=41,cumulative=True,histtype="step",color="r")
    def statistic(x):
        return scipy.stats.normaltest(x)[0]
    # A=np.array(A)
    # res=scipy.stats.monte_carlo_test((A-np.mean(A))/np.std(A),lambda size:rng.normal(0,1,size=size),statistic)
    print(f"MC calculation: Slope = {np.mean(A)} $\pm$ {np.std(A)}")
    res=scipy.stats.linregress(range(1,10),v)
    print(f"Without Covariances: Slope = {res.slope} $\pm$ {res.stderr}, p-value = {res.pvalue}")
    # print(f"Slope = {np.mean(A)} $\pm$ {np.std(A)}, MC_test={res.pvalue}, Normal_test{scipy.stats.normaltest((A-np.mean(A))/np.std(A))[1]}")

if False:
    rng=np.random.default_rng()
    def statistic(x):
        return scipy.stats.normaltest(x)[0]
    res=scipy.stats.monte_carlo_test((CMoE_val-np.mean(CMoE_val))/np.std(CMoE_val),lambda size:rng.normal(0,1,size=size),statistic)
    print(f"Normality test p-value = {res.pvalue}")

if CoC_mode:
        from PIL import Image 
        im=Image.open("irra2hpge_out/irrad2hpge"+save_key+".png")
        width,height=im.size
        print(im.size)
        left=width-1.5*1548-10
        right=width-1
        bottom=height-int(15/26*2563)-1
        top=height-2563-24
        im2=im.crop((left,top,right,bottom))
        im2.save("irra2hpge_out/irrad2hpge"+save_key+"_zoom.png")
else:
    if do_zoom and not Exp_only:
        from PIL import Image 
        im=Image.open("irra2hpge_out/irrad2hpge"+save_key+".png")
        width,height=im.size
        print(im.size)
        left=width-1.5*1548-10
        right=width-1
        bottom=height-1
        top=height-2563+40
        im2=im.crop((left,top,right,bottom))
        im2.save("irra2hpge_out/irrad2hpge"+save_key+"_zoom.png")
    # else:
        # plt.show()
    if not Exp_only:
        from PIL import Image 
        im=Image.open("irra2hpge_out/irrad2hpge"+save_key+".png")
        width,height=im.size
        print(im.size)
        left=width-2*1548+17
        right=width-1548-10
        # right=width-1
        bottom=height-1
        top=height-2563-100
        im2=im.crop((left,top,right,bottom))
        im2.save("irra2hpge_out/irrad2hpge"+save_key+"_paper_zoom.png")
# else:
# plt.show()