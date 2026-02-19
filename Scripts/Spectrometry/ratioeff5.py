from ZPyDosi.Common.utils_general import lmap, get_aff_size, tex, simple
from ZPyDosi.Common.TabPrinter import TabPrinter
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.Plots.SubPlots import my_sub6, aff_curve
from ZPyDosi.Prints.PrintnSave import save_dict_to_file
from ZPyDosi.Stats.Stats import imoyvar_list
import numpy as np
import matplotlib.pyplot as plt



path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv  = get_param_vari("lcase", str).split("/")

print ("#"*50)
data_irrad = DataIrrad(    path_csv_data,
            path_csv_dosi,
            lcase_csv,
            #use_sqrt_for_meas_sig=True,
            #load_hpge_eff=True,
            #load_sss_results=True,
            #load_ndup=True,
            remove_data=False,
            load_ratio=False
            )
#data_irrad.aff_description()
print ("#"*50)


d_name_iso_mt_2_li = {}
for i, (name, iso, mt) in enumerate(zip(data_irrad.l_name, data_irrad.l_iso, data_irrad.l_mt)):
    if "10" in name:
        if (name, iso, mt) not in d_name_iso_mt_2_li:
            d_name_iso_mt_2_li[(name, iso, mt)] = []
        d_name_iso_mt_2_li[(name, iso, mt)] += [i]

def aff(v, l=20, rev=False):
    v = str(v)+" "
    return v+" "*(l-len(v)) if not rev else " "*(l-len(v))+v
    
#print aff("name")+aff("iso")+aff("mt")+aff("Dt_meas")+aff("t_meas_1")+aff("t_meas_2")+aff("act_1")+aff("act_2")+aff("act_2_at_t1")+aff("diff")

entete = "name hpge_name hpge_pos gamma_nrj iso mt Dt_meas t_meas_1 t_meas_2 act_1 sig_rel1[%] act_2 sig_rel2[%] act_2_at_t1 eff_ratio eff_ratio_sig eff_ratio_sig[%] nb_res"
scribe = TabPrinter(entete.split(), 2)


d_res = {}

for (name, iso, mt), l_i in d_name_iso_mt_2_li.items():
    if len(l_i)>1 :
        l_eff_v, l_eff_s = [], []
        for i in l_i:
            for j in l_i:
                #print(i,j,data_irrad.l_hpge_pos[j], data_irrad.l_hpge_pos[i], data_irrad.l_hpge_id[j], data_irrad.l_hpge_id[i])
                if data_irrad.l_hpge_pos[j] == "pgrd" and data_irrad.l_hpge_pos[i] == "p13" :
                    #print("pass")
                    case=data_irrad.l_hpge_id[j]
                    halflife = data_irrad.l_half_time[i]
                    lambd     = np.log(2)/halflife
                    def act0(i):
                        count_v    = data_irrad.l_counts_v[i]
                        count_s    = data_irrad.l_counts_s[i]
                        dtime      = data_irrad.l_deadtime[i]
                        date       = data_irrad.l_hpge_time[i]
                        time_in    = data_irrad.l_time_in_hpge[i]
                        #v = count_v / (1-dtime)
                        #s = count_s / (1-dtime)
                        v = count_v 
                        s = count_s 
                        a_zero_v = v * lambd / (1-np.exp(-lambd * time_in))
                        a_zero_s = s * lambd / (1-np.exp(-lambd * time_in))
                        return date,time_in, a_zero_v, a_zero_s
                    date_i, t_i, act0_i_v, act0_i_s = act0(i)
                    date_j, t_j, act0_j_v, act0_j_s = act0(j)
                    dt = (date_i-date_j).total_seconds()
                    act0_j2i_v = act0_j_v*np.exp(-lambd*dt)
                    act0_j2i_s = act0_j_s*np.exp(-lambd*dt)


                    if (iso, mt, case) not in d_res:
                        d_res[(iso, mt, case)] = [[],[],[]]
                    if name not in d_res[(iso, mt,case)][2]:
                        d_res[(iso, mt,case)][0] += [act0_j2i_v]
                        d_res[(iso, mt,case)][1] += [act0_j2i_s]
                        d_res[(iso, mt,case)][2] += [name]
                    if (iso, mt, "ref") not in d_res:
                        d_res[(iso, mt, "ref")] = [[],[],[]]
                    if name not in d_res[(iso, mt,"ref")][2]:
                        d_res[(iso, mt,"ref")][0] += [act0_i_v]
                        d_res[(iso, mt,"ref")][1] += [act0_i_s]
                        d_res[(iso, mt,"ref")][2] += [name]


                    # scribe.add("name",              name)
                    # scribe.add("hpge_name",         data_irrad.l_hpge_id [j]+"/"+data_irrad.l_hpge_id [i])
                    # scribe.add("hpge_pos",          data_irrad.l_hpge_pos[j]+"/"+data_irrad.l_hpge_pos[i])
                    # scribe.add("gamma_nrj",         data_irrad.l_gamma_nrj[i])
                    # scribe.add("iso",               iso)
                    # scribe.add("mt",                mt)
                    # scribe.add("Dt_meas",           time2str(dt))
                    # scribe.add("t_meas_1",          time2str(t_i))
                    # scribe.add("t_meas_2",          time2str(t_j))
                    # scribe.add("act_1",             round(act0_i_v, 3))
                    # scribe.add("sig_rel1[%]",       round(act0_i_s/act0_i_v*100, 3))
                    # scribe.add("act_2",             round(act0_j_v, 3))
                    # scribe.add("sig_rel2[%]",       round(act0_j_s/act0_j_v*100, 3))
                    # scribe.add("act_2_at_t1",       round(act0_j2i_v, 3))
                    # scribe.add("eff_ratio",         round(ratio, 3))
                    # scribe.add("eff_ratio_sig",     round(ratio_sig, 3))
                    # scribe.add("eff_ratio_sig[%]",  round(ratio_sig/ratio*100, 3))
                    # scribe.add("nb_res",            round((ratio-1)/ratio_sig, 3))
                    # l_eff_v += [ratio]
                    # l_eff_s += [ratio_sig]
                    # if (iso, mt) not in d_res:
                    #     d_res[(iso, mt)] = [[],[],[]]
                    # d_res[(iso, mt)][0] += [ratio]
                    # d_res[(iso, mt)][1] += [ratio_sig]
                    # d_res[(iso, mt)][2] += [name]

if len(d_res)==0:
    print("no ratio...")
    exit()
N=50000
M_samp=[]
RNG=np.random.default_rng()
i=-1
dict_samp={}
for key in d_res.keys():
    i+=1
    (iso, mt,case) = key
    act_v = d_res[(iso, mt,case)][0]
    act_s = d_res[(iso, mt,case)][1]
    name    = d_res[(iso, mt,case)][2]
    
    M_samp+=[RNG.normal(act_v,act_s,(N,len(act_v)))]
    dict_samp[(iso, mt,case)]=M_samp[i]
dict_samp_ratio={}
for key in d_res.keys():
    (iso, mt, case) = key
    dict_samp_ratio[(iso, mt, case)]=np.mean(dict_samp[(iso, mt, case)]/dict_samp[(iso, mt, "ref")],axis=1)

i=-1
M_samp=np.zeros((len(d_res.keys()),N))
for key in d_res.keys():
    i+=1
    (iso, mt, case) = key
    M_samp[i]=dict_samp_ratio[(iso, mt, case)]
mean=np.mean(M_samp,axis=1)
cov=np.cov(M_samp)
d_ratio={}

i=-1
for key in d_res.keys():
    i+=1
    (iso, mt, case) = key
    d_ratio["_".join([iso, mt, case])]=mean[i]
    j=-1
    for key2 in d_res.keys():
        j+=1
        (iso2, mt2, case2) = key2
        d_ratio["_".join([iso, mt, case,iso2, mt2, case2])]=cov[i,j]
print(d_ratio)
save_dict_to_file(d=d_ratio,filename="Ratio/"+data_irrad.get_key_for_ratio())


# for key in d_res.keys():
#     (iso, mt) = key
#     ratio_v = d_res[(iso, mt)][0]
#     ratio_s = d_res[(iso, mt)][1]
#     name    = d_res[(iso, mt)][2]
#     def name2nro(name):
#         #print (name)
#         nro, i = "0", len(name)-1
#         while name[i] in "1234567890":
#             nro = name[i]+nro
#             i -= 1
#         return int(nro)
#     l_pos = map(lambda i_n: i_n[0], sorted(list(enumerate(name)), key=lambda i_name: name2nro(i_name[1])))
#     tmp_ratio_v, tmp_ratio_s, tmp_name = [],[],[]
#     for pos in l_pos:
#         tmp_ratio_v += [ratio_v[pos]]
#         tmp_ratio_s += [ratio_s[pos]]
#         tmp_name    += [name   [pos]]
#     d_res[(iso, mt)] = (tmp_ratio_v, tmp_ratio_s, tmp_name)



exit() # a enlever pour faire un joli plot :)

fig = plt.figure(figsize=(11,5))
fig.patch.set_facecolor('white')
nb_plt = len(d_res.keys())
tab_ax = my_sub6(fig,1,1,0,list_ry=[1]*nb_plt, list_rx=[1], auto_y=False,auto_x=False)
l_ax = list(reversed(tab_ax[0,:]))


for ikey, key in enumerate(d_res.keys()):
    l_eff, l_eff_sig, l_name = map(lambda l: np.array(l), d_res[key])
    #nb_dosi = 3
    #l_eff, l_eff_sig, l_name = l_eff[:nb_dosi], l_eff_sig[:nb_dosi], l_name[:nb_dosi]
    moy,sig = imoyvar_list(l_eff)
    sig_ori = sig
    if len(l_eff)>2:
        sig /= (len(l_eff)-1)**0.5
    
    l_test = np.arange(moy*0.9, moy*1.1, moy/100000.)
    sampled_guess = l_test
    cov = np.diag(l_eff_sig**2)
    covl_inv = np.linalg.inv(cov)
    l_chi2 = lmap(lambda g: (l_eff-g).T.dot(covl_inv.dot(l_eff-g)), sampled_guess)
    l_w = np.exp(-np.array(l_chi2)/2)
    
    moy2,sig2 = imoyvar_list(sampled_guess, l_w)
    def approx(v):
        return round(v, 5)
        #return int(v*10000)/10000.
    print (str(key))
    print ("    on the measurments disp val,sig,sig_res[%] = "+str((approx(moy),approx(sig_ori), approx(sig_ori/moy*100))))
    print ("    on the measurments disp val,sig,sig_res[%] = "+str((approx(moy),approx(sig), approx(sig/moy*100))))
    print ("    and using uncertainties val,sig,sig_res[%] = "+str((approx(moy2),approx(sig2),approx(sig2/moy2*100))))
    print ("    residuals: "+"\n               ".join(map(lambda v:str(v), (l_eff-moy2)/(sig2**2+l_eff_sig**2)**0.5)))
    
    for d in range(len(l_eff)):
        l_ax[ikey].errorbar([d], [l_eff[d]], [l_eff_sig[d]], c=(0,0,0),linewidth=2)
        on = moy2<l_eff[d]
        l_ax[ikey].text(d,l_eff[d]+(1 if on else -1)*l_eff_sig[d],r"$"+str(simple(l_eff_sig[d]/l_eff[d]*100,2))+r"\%$",va="bottom" if on else "top",ha="left",size=get_aff_size("s_tick")*0.8)
    
    l_ax[ikey].set_xlim([-1.1, len(l_eff)-0.5])
    aff_curve(l_ax[ikey], l_ax[ikey].get_xlim(), [moy2, moy2], [sig2,sig2], (0,0,1), 1,0.3, dashes=[5,2])
    l_ax[ikey].plot(l_ax[ikey].get_xlim(), [moy2*1.01, moy2*1.01], c=(0,0,1), dashes=[2,5])
    l_ax[ikey].plot(l_ax[ikey].get_xlim(), [moy2*0.99, moy2*0.99], c=(0,0,1), dashes=[2,5])
    l_ax[ikey].text(-1,moy2,     r"$\mu$",va="bottom",ha="left",size=get_aff_size("s_tick"), color=(0,0,1))
    l_ax[ikey].text(-1,moy2*1.01,r"$\mu+1\%$",va="bottom",ha="left",size=get_aff_size("s_tick"), color=(0,0,1))
    l_ax[ikey].text(-1,moy2*0.99,r"$\mu-1\%$",va="bottom",ha="left",size=get_aff_size("s_tick"), color=(0,0,1))
    
    #aff_curve(ax, lx,ly,sly,c,a1,a2
    
    if 0.9<moy2<1.1:
        l_ax[ikey].plot(l_ax[ikey].get_xlim(), [1, 1], c=(0,0,0), dashes=[5,2])
    
    l_ax[ikey].set_xticks(range(len(l_eff)))
    l_ax[ikey].set_xticklabels(map(lambda n:tex(n), l_name), size=get_aff_size("s_tick"))
    # , rotation=(0 if len(l_name)<4 else 45))
    
    l_ax[ikey].set_ylabel(tex(r"Eff. ratio"),    size=get_aff_size("s_xylabel"))
    l_ax[ikey].set_xlabel(tex(r"Dosimeter"),    size=get_aff_size("s_xylabel"))


fig.savefig("ratioeff_all.png", bbox_inches=('tight'), dpi=200)
plt.show()









