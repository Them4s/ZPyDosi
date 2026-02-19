

'''
Compute and save the uncertainties due to core cross-sections using multiple data from a set of perturbed simulations
'''


import os
from ZPyDosi.Common.utils_general import lmap, get_aff_size, get_c, tex, dup, dup_piquet,set_nice_ax
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.Prints.PrintnSave import aff_list, aff_mat
from ZPyDosi.Plots.SubPlots import my_sub6, my_sub6_finalise, get_lim
from ZPyDosi.Plots.MatrixPlots import aff_mat4
from ZPyDosi.Stats.Stats import icovar_jkk, imoyvar, cov_to_sig_cor
from ZPyDosi.XSnFlux.Aggregate import aggregate_spectrum
from ZPyDosi.XSnFlux.GetIRDFF import get_irdff_iaea
from ZPyDosi.XSnFlux.Projections import projet_vec_intervals_from_continus
import numpy as np
import matplotlib.pyplot as plt



print ("#"*50)
path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
Big_dosi  = get_param_vari("Big_dosi", bool,"True")
lcase_csv  = get_param_vari("lcase", str).split("/")
gr_order = get_param_vari("gr_order", int,2) # to gain ram by decreasing the spectral resolution by 2**gr_order
do_rm=get_param_vari("do_rm",bool,"False") #To remove commented detectors
redo=get_param_vari("redo",bool,"False") 

data = DataIrrad(path_csv_data, path_csv_dosi, lcase_csv, load_ndup_nuis_tosuppress=True, load_sss_results=False, load_sss_spectrum=False,group_order=gr_order, remove_data=do_rm)
print ("#"*50)

path_ex = "ndupnuis_out/out_"+(data.get_key_for_ndup_nuis())

if (not redo) and os.path.isfile(path_ex):
    print("nducup_nuis data already exist")
    exit()
nb_rand = 66 # todo : chzercher le nombre de calcul utilisable
N_samp=2**15

nb_dosi = data.nb_dosi

d_pathidnro2pathpos = {}
d_pathpos2id = {}
id = 0

if Big_dosi:
    l_pos_dosi=[name.replace("_3","_1").replace("_5","_1") for name in data.l_pos_name]
else:
    l_pos_dosi=data.l_pos_name


#ll_vtot = [[] for i in range(nb_rand)]
l_path_todo = []
l_pathpos = []
for idosi in range(nb_dosi):
    path = data.l_sss_path_nuis[idosi]
    lpos  = data.l_sss_pos_nuis[idosi]
    if path not in l_path_todo:
        l_path_todo += [path]
        for ipos, pos in enumerate(lpos.split("/")):
            #if (path, pos) not in d_pathpos2id:
            d_pathidnro2pathpos[(path, ipos, id)] = (path, pos)  #not used
            d_pathpos2id[(path, pos)] = id  #not used
            l_pathpos += [(path, pos)]
            id += 1

d_pathpos2pathidnro = {v: k for k, v in d_pathidnro2pathpos.items()}
d_id2pathpos = {v: k for k, v in d_pathpos2id.items()}

#print(d_pathidnro2pathpos)
#print(d_pathpos2pathidnro)
#print(l_path_todo)
#print(d_id2pathpos)
#print(d_pathpos2id)
#print(l_pathpos)
#exit()

#d_nro2pos = {0:"all", 1:"C", 2:"CR", 3:"R"}
#d_pos2nro = {v: k for k, v in d_nro2pos.items()}
#d_pos_2_ll_v = {"all":[], "C":[], "CR":[], "R":[]}



ll_vtot   = []
ll_srel   = []
irand=0
while all([os.path.isfile(path_todo + str(irand+1)+"/input_mat_sss_2_of/perspectra") for path_todo in l_path_todo]):
    irand+=1
    l_vtot = []
    l_srel = []
    for path_todo in l_path_todo:
        #path = "calc_sss/ndup_b8/rand"+str(irand)+"/rand_mat_sss_2_of/perspectra"
        path = path_todo + str(irand)+"/input_mat_sss_2_of/perspectra"
        # print(path)
        dim = lmap(lambda s:int(s),open(path).readlines()[0].split())    # get data shape
        nb_pos, nb_per, nb_nrj = dim
        specdata       = np.array(lmap(lambda s:float(s), " ".join(open(path       ).readlines()[1:]).split())).reshape(dim)[:,0,:]
        specdata_sig   = np.array(lmap(lambda s:float(s), " ".join(open(path+"_sig").readlines()[1:]).split())).reshape(dim)[:,0,:]
        if gr_order!=0:
            specdata    =aggregate_spectrum(specdata    ,gr_order)
            specdata_sig=aggregate_spectrum(specdata_sig,gr_order,True)
            nb_nrj=int(nb_nrj/2**gr_order)

        for ipos in range(nb_pos):
            l_v, l_s  = specdata[ipos, :], specdata_sig[ipos, :]
            #d_pos_2_ll_v[d_nro2pos[ipos]] += [l_v]
            l_vtot += list(l_v)
            l_srel += list(l_s / l_v)
#    print(l_vtot)
#    exit()
    ll_vtot += [l_vtot]
    ll_srel += [l_srel]
ll_srel = np.array(ll_srel)
l_vtot_ave = np.mean(ll_vtot, axis=0)
l_srel_ave = np.mean(ll_srel, axis=0)
#print(ll_srel)
#print(l_srel_ave)
#exit()
print("Coucou")
E1,E2 = 1e-10, 20.
l_nrj_piquet = 10**(((np.log10(E2)-np.log10(E1)) * np.array(range(nb_nrj+1))*1./(nb_nrj  )) + np.log10(E1))
l_nrj        = (l_nrj_piquet[1:] + l_nrj_piquet[:-1])/2

d_pos_2_cov = {}
d_pos_2_cov_sig = {}
d_pos_2_std = {}
d_pos_2_ave = {}
d_pos_2_stat = {}
cov_tot,cov_tot_sig = icovar_jkk(ll_vtot, l_w=None, do_cor=False, do_jackknife=True, fast_jackknife=False, blabla=False, nb_jkk=None, fast=False)
# print(cov_tot.shape,cov_tot_sig.shape)
# exit()
moy, std = imoyvar(ll_vtot)

print("coucou 1.5")
if False:
    f_leg=1.5
    fig = plt.figure(1, figsize=(7,5))
    fig.patch.set_facecolor('white')
    ax = plt.subplot(1,1,1)
    ax.set_xscale("log")
    #ax.set_yscale("log")
    tout = False
    if not tout:
        n0, n = 16, 2
    else:
        n0, n = 0, 32
    ll_vtot = ll_vtot[n0:n0+n]
    ll_srel = ll_srel[n0:n0+n]
    l_vtot_ave = np.mean(ll_vtot, axis=0)
    l_srel_ave = np.mean(ll_srel, axis=0)
    for i in range(len(ll_vtot)):
        if tout:
            ri = i/(len(ll_vtot)-1)
            d = [2+4*ri, 6*ri]
        else:
            d = {0:[1,0], 1:[6,4], 2:[2,2]}[i]
        l_vtot, l_srel = ll_vtot[i], ll_srel[i]
        #print(len(l_nrj_piquet))
        #print(len(l_vtot))
        #exit()
        for j in range(nb_pos)[1:]:
            c = get_c(j-1,nb_pos-1)
            lv = (l_vtot/(l_vtot_ave+1e-15))[j*len(l_v):(j+1)*len(l_v)]
            ls = l_srel[j*len(l_v):(j+1)*len(l_v)] * lv
            lv = (lv-1)*100
            ls *=100
            ax.plot(dup(l_nrj_piquet)[1:-1], dup(lv), c=c, dashes=d)
            ax.fill_between( dup(l_nrj_piquet)[1:-1], dup(lv-ls), dup(lv+ls), facecolor=c, alpha=0.2 )
            if i == 0:
                ax.plot([],[],c=c, label=tex({1:"Core center", 2:"Control rod", 3:"Reflector", }[j]))
        ax.plot([],[],c=(0,0,0), dashes=d, label=tex("Sample "+str(i)))
    if not tout:
        ax.legend(loc='best', ncol=2, fontsize=get_aff_size("s_leg")*0.7*f_leg)                                 # print the legend
    ax.set_ylim([-10,10])
    ax.set_xlim(ax.get_xlim())
    ax.plot(ax.get_xlim(), [0,0], c=(0,0,0), lw=0.75)
    ax.set_ylabel(tex("\phi variation [\%]"), size=get_aff_size("s_xylabel")*f_leg)
    ax.tick_params(axis='both', which='both', labelsize=get_aff_size("s_tick")*f_leg)
    set_nice_ax(ax,x="MeV")
    fig.savefig("ndupnuis_out/inter.png", bbox_inches=('tight'), dpi=300)
    plt.show()
    exit()


#for path_todo in l_path_todo:
for ipathposi, pathposi in enumerate(l_pathpos):
    #for ipos in range(nb_pos):
    #    keyi = d_nro2pos[ipos]
    #    for jpos in range(nb_pos):
    for ipathposj, pathposj in enumerate(l_pathpos):
            #keyj = d_nro2pos[jpos]
            keyi, keyj =  pathposi,  pathposj
            ipos, jpos = ipathposi, ipathposj
            d_pos_2_cov[(keyi, keyj)]     = cov_tot    [nb_nrj*ipos: nb_nrj*(ipos+1), nb_nrj*jpos: nb_nrj*(jpos+1)]
            d_pos_2_cov_sig[(keyi, keyj)] = cov_tot_sig[nb_nrj*ipos: nb_nrj*(ipos+1), nb_nrj*jpos: nb_nrj*(jpos+1)]
            if ipos==jpos:
                d_pos_2_std[keyi        ] = std[nb_nrj*ipos: nb_nrj*(ipos+1)]
                d_pos_2_ave[keyi        ] = moy[nb_nrj*ipos: nb_nrj*(ipos+1)]
    d_pos_2_stat[keyi] = l_srel_ave[nb_nrj*ipos: nb_nrj*(ipos+1)]


fig2 = plt.figure(0, figsize=(6,6))
fig2.patch.set_facecolor('white')
axmatsup = plt.subplot(1,1,1)
#fig = plt.figure(1, figsize=(10,12))
fig = plt.figure(1, figsize=(9,12))
fig.patch.set_facecolor('white')
axmat = plt.subplot(2,2,1)
axmat2 = plt.subplot(2,2,3)
l_ax = my_sub6(fig,1,2,1,list_rx=[1],list_ry=[1,1,1,1,1],list_sy=[0.1,0.1,0.1,0.1],auto_y=False, list_idx_none=[(0,1),(0,2),(0,3),(0,4)])

tmp3 = l_ax[0,-3]
tmp2 = l_ax[0,-2]
l_ax[0,-2] = tmp3
l_ax[0,-3] = tmp2

def dlet(le, log10=False):
    if not log10:
        return np.log(le[1:])-np.log(le[:-1])
    else:
        return np.log10(le[1:])-np.log10(le[:-1])


def integ(l_e,l_v,quad=False, log10=False):
    l_dlet = dlet(l_e, log10=log10)
    l_integ = l_v*l_dlet
    if quad: l_integ = l_integ**2
    for i in range(len(l_integ))[1:]:
        l_integ[i]+= l_integ[i-1]
    if quad: l_integ = l_integ**0.5
    return l_integ

#ll_ce   = []
#lll_cor = []
#ll_xe   = []
#ll_xv   = []
#ll_xs   = []
#ll_fv, ll_fs = [],[]

#lll_fc_bin = []
ll_fv_bin  = []
ll_fs_bin  = []
ll_xv_c0   = []
ll_xe_c0   = []
#l_srel_ave_dosi = []
l_fe_bin = list(l_nrj_piquet)
lll_cov = np.zeros(((len(l_fe_bin)-1) * nb_dosi, (len(l_fe_bin)-1) * nb_dosi))
lll_cov_sig = np.zeros(((len(l_fe_bin)-1) * nb_dosi, (len(l_fe_bin)-1) * nb_dosi))



print("coucou2")

for idosi in range(data.nb_dosi):
    idata_irdff = get_irdff_iaea(os.path.expandvars("$petale_analysis/data/iaea_data/"+data.l_key_irdff_iaea[idosi]), e_min = None)
    # get_irdff_iaea -> (l_cor_e, cor), (l_xs_e,l_xs_v,l_xs_s)
    #ll_ce   += [list(l_nrj_piquet)]                            # ori : [idata_irdff[0][0]] irdff cov nrj (bin)     new : phi cov nrj (bin)
    #lll_fc_bin += [list(d_pos_2_cov[l_pos_dosi[idosi]])]   # ori : [idata_irdff[0][1]] irdff cov val (bin)     new : phi cov val (bin)
    #ll_xe      += [list(l_nrj_piquet)]                         # ori : [idata_irdff[1][0]] irdff xs  nrj (c0)      new : phi ave nrj (bin)
    ll_fv_bin  += [list(d_pos_2_ave[(data.l_sss_path_nuis[idosi], l_pos_dosi[idosi])])]   # ori : [idata_irdff[1][1]] irdff xs  val (c0)      new : phi ave val (bin)
    ll_fs_bin  += [list(d_pos_2_std[(data.l_sss_path_nuis[idosi], l_pos_dosi[idosi])])]   # ori : [idata_irdff[1][1]] irdff xs  val (c0)      new : phi ave val (bin)
    #ll_xs      += [list(d_pos_2_std[l_pos_dosi[idosi]])]  # ori : [idata_irdff[1][2]] irdff xs  sig (c0)      new : phi ave sig (bin)
    #print(idosi, l_pos_dosi[idosi], len(idata_irdff[0][0]), len(idata_irdff[0][1]), len(idata_irdff[1][0]), len(idata_irdff[1][1]))
    
    ll_xv_c0 += [idata_irdff[1][1]] # ori : list(data.ll_fv) dosi phi val (bin)  new : irdff xs  (c0)
    ll_xe_c0 += [idata_irdff[1][0]] # ori : list(data.l_fe)  dosi phi nrj (bin)  new : irdff nrj (c0)
    #print("a", len(ll_xe_c0[-1]), len(ll_xv_c0[-1]), data.l_key_irdff_iaea[idosi])
    #ll_fs += # ori : list(data.ll_fs) dosi phi sig
    pos1 = (len(l_fe_bin)-1)* idosi
    pos2 = (len(l_fe_bin)-1)*(idosi+1)
    lll_cov    [nb_nrj*idosi: nb_nrj*(idosi+1), nb_nrj*idosi: nb_nrj*(idosi+1)] = d_pos_2_cov[((data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]), (data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]))]
    lll_cov_sig[nb_nrj*idosi: nb_nrj*(idosi+1), nb_nrj*idosi: nb_nrj*(idosi+1)] = d_pos_2_cov_sig[((data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]), (data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]))]
    for jdosi in range(data.nb_dosi)[idosi+1:]:
        lll_cov    [nb_nrj*idosi: nb_nrj*(idosi+1), nb_nrj*jdosi: nb_nrj*(jdosi+1)] = d_pos_2_cov[((data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]), (data.l_sss_path_nuis[jdosi], l_pos_dosi[jdosi]))]
        lll_cov_sig[nb_nrj*idosi: nb_nrj*(idosi+1), nb_nrj*jdosi: nb_nrj*(jdosi+1)] = d_pos_2_cov_sig[((data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]), (data.l_sss_path_nuis[jdosi], l_pos_dosi[jdosi]))]
        lll_cov    [nb_nrj*jdosi: nb_nrj*(jdosi+1), nb_nrj*idosi: nb_nrj*(idosi+1)] = d_pos_2_cov[((data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]), (data.l_sss_path_nuis[jdosi], l_pos_dosi[jdosi]))].T
        lll_cov_sig[nb_nrj*jdosi: nb_nrj*(jdosi+1), nb_nrj*idosi: nb_nrj*(idosi+1)] = d_pos_2_cov_sig[((data.l_sss_path_nuis[idosi], l_pos_dosi[idosi]), (data.l_sss_path_nuis[jdosi], l_pos_dosi[jdosi]))].T

    #l_srel_ave_dosi += list(l_srel_ave[nb_nrj*idosi: nb_nrj*(idosi+1)])

print("coucou3")

'''
for k in range(len(data.l_key_irdff_iaea)): # trunk irdff data to flux energy boundaries
    #print(ll_fe[k][0])
    #print(" ",ll_ce[k][0])
    while ll_xe_c0[k][0] < l_fe_bin[0]:
        ll_xe_c0[k] = ll_xe_c0[k][1:]
        ll_xv_c0[k] = ll_xv_c0[k][1:]
    while ll_xe_c0[k][-1] > l_fe_bin[-1]:
        ll_xe_c0[k] = ll_xe_c0[k][:-1]
        ll_xv_c0[k] = ll_xv_c0[k][:-1]
    print(len(ll_xe_c0[k]), len(ll_xv_c0[k]))'''

#ll_xv_proj_f = lmap(lambda i: projet_vec_intervals_from_continus(l_fe, ll_xe[i], ll_xv[i]), range(len(ll_ce)))     # old for irdff uncertainty propagation
#ll_xs_proj_f = lmap(lambda i: projet_vec_intervals_from_continus(l_fe, ll_xe[i], ll_xs[i]), range(len(ll_ce)))
ll_xv_bin = lmap(lambda i: projet_vec_intervals_from_continus(l_fe_bin, ll_xe_c0[i], ll_xv_c0[i]), range(len(ll_xv_c0)))


#ll_xv_proj_c = lmap(lambda i: projet_vec_intervals_from_continus(ll_ce[i], ll_xe[i], ll_xv[i]), range(len(ll_ce)))
#ll_xs_proj_c = lmap(lambda i: projet_vec_intervals_from_continus(ll_ce[i], ll_xe[i], ll_xs[i]), range(len(ll_ce)))
#ll_xv_proj_c = lmap(lambda i: projet_vec_intervals_from_integrated(ll_ce[i], ll_xe[i], ll_xv[i]), range(len(ll_ce)))
#ll_xs_proj_c = lmap(lambda i: projet_vec_intervals_from_integrated(ll_ce[i], ll_xe[i], ll_xs[i]), range(len(ll_ce)))


#ll_rv_proj_c = lmap(lambda i: projet_vec_intervals_from_integrated(np.log(ll_ce[i]), np.log(l_fe), ll_fv[i]*ll_xv_proj_f[i]*data.l_at_den[i]),range(len(ll_fv)))
#ll_rs_proj_c = lmap(lambda i: projet_vec_intervals_from_integrated(np.log(ll_ce[i]), np.log(l_fe), ll_fs[i]*ll_xv_proj_f[i]*data.l_at_den[i]),range(len(ll_fv)))

#ll_rv_bin = lmap(lambda i: projet_vec_intervals_from_integrated(np.log(l_fe_bin), np.log(l_fe_bin), ll_fv_bin[i]*ll_xv_bin[i]*data.l_at_den[i]),range(len(ll_xv_bin)))
ll_rv_bin = lmap(lambda i: ll_fv_bin[i] * ll_xv_bin[i] * data.l_at_den[i], range(len(ll_xv_bin))) # TODO : voir si utile de faire le calcul du RR sur maillage c0 de irdff puis repasser en bin ensuite

#ll_fv_proj_c = lmap(lambda i: ll_rv_proj_c[i]/(ll_xv_proj_c[i]*data.l_at_den[i]+1e-15),range(len(ll_rv_proj_c)))
#ll_fs_proj_c = lmap(lambda i: ll_rs_proj_c[i]/(ll_xv_proj_c[i]*data.l_at_den[i]+1e-15),range(len(ll_rs_proj_c)))

#exit()

'''
if ll_fe[k][0] > ll_ce[k][0]:
    ll_fe[k] = np.array([ll_ce[k][0]]+list(ll_fe[k]))
    for i in range(len(ll_fv)):
        ll_fv[i] = np.array([0]+list(ll_fv[i]))
        #ll_fs[i] = np.array([0]+list(ll_fs[i]))

if ll_fe[k][-1]<ll_ce[k][-1]:
    ll_fe[k] = np.array(list(ll_fe[k])+[ll_ce[k][-1]])
    for i in range(len(ll_fv)):
        ll_fv[i] = np.array(list(ll_fv[i])+[0])
        #ll_fs[i] = np.array(list(ll_fs[i])+[0])
'''


#lll_cov = lmap(lambda i: cor_sig_to_cov(lll_cor[i], ll_xs_proj_c[i]), range(data.nb_dosi))
#ll_cov = ll_cor*1.
#ll_cov *= (l_xs_proj_c[:, None])
#ll_cov *= (l_xs_proj_c[None, :])

def cat(ll, log=False, cut=False):
    r = []
    l_junction = []
    pos = 0
    for il, l in enumerate(ll):
        new = l if not log else (np.log10(l))
        new = list(new-new[0]+pos)
        r += new if not cut or il== 0 else new[1:]
        pos = r[-1]
        l_junction += [r[-1]]
    return l_junction[:-1], np.array(r)

#print(len(ll_xv_bin))
#print(len(ll_xv_bin[0]))
if True:
    print("# check")
    l_xv_bin = sum(map(lambda v: list(v), ll_xv_bin), [])
    #print(l_xv_bin)
    #exit()
    #print(l_xv_bin.shape, len(ll_vtot), len(ll_vtot[0]))
    ll_rr = []
    for i in range(nb_dosi):
        #sub_c = cov_tot[nb_nrj*i: nb_nrj*(i+1), nb_nrj*i: nb_nrj*(i+1)]
        suc_x = l_xv_bin[nb_nrj*i: nb_nrj*(i+1)]
        l_rr = []
        #print(np.array(ll_vtot).shape)
        #exit()
        for l_vtot in ll_vtot:
            #id = d_pos2nro[l_pos_dosi[i]]
            id = l_pathpos.index((data.l_sss_path_nuis[i], l_pos_dosi[i]))
            sub_f = l_vtot[nb_nrj*(id): nb_nrj*(id+1)]
            #print(id, len(sub_f), len(l_vtot), nb_nrj*(id), nb_nrj*(id+1))
            #print(len(sub_f), len(suc_x))
            #print(suc_x)
            #exit()
            l_rr += [sum(np.array(sub_f)*np.array(suc_x))]
        ll_rr += [l_rr]
        print(nb_nrj*(i+1), nb_nrj*(i+2))
        print(suc_x[:10])
        print(sub_f[:10])
        #print(l_rr)
        #print()
        #print(suc_x)
        #exit()
        #print(sub_x)
        #print(i, np.std(l_rr)/np.average(l_rr), np.std(l_rr), np.average(l_rr))
    check = ""
    if len(ll_rr)>1:
        check_cov, check_cor,check_cov_sig, check_cor_sig = icovar_jkk(np.array(ll_rr).T, l_w=None, do_cor=True, do_jackknife=True, fast_jackknife=False, blabla=False, nb_jkk=None, fast=True)
        print("#", np.diag(check_cov)**0.5 / np.array(lmap(lambda l_rr: np.average(l_rr), ll_rr)))
        print("#", check_cor)

        check += aff_list("chk_stdv_rel [%]", np.diag(check_cov)**0.5 / np.array(lmap(lambda l_rr: np.average(l_rr), ll_rr)) * 100)+"\n"
        check += aff_mat("chk corr", check_cor)+"\n"
    print("# end check")
#exit()

def cat_mat(lm):
    size = sum(map(lambda m: len(m), lm))
    r = np.zeros((size, size))
    pos = 0
    
    d_key_irdff_done = {}
    for im, m in enumerate(lm):
        r[pos:pos+len(m), pos:pos+len(m)] = m                               # matrice par bloc dans la diagonale
        if data.l_key_irdff_iaea[im] not in d_key_irdff_done:               # matrice par bloc hors diagonale si meme isotope
            d_key_irdff_done[data.l_key_irdff_iaea[im]] = [pos]
        else:
            for cross_pos in d_key_irdff_done[data.l_key_irdff_iaea[im]]:
                r[cross_pos:cross_pos+len(m), pos:pos+len(m)] = m
                r[pos:pos+len(m), cross_pos:cross_pos+len(m)] = m
            d_key_irdff_done[data.l_key_irdff_iaea[im]] += [pos]
        pos += len(m)
    return r
#lll_cov
if data.nb_dosi == 1:
    aff_mat4(l_fe_bin, l_fe_bin, cov_to_sig_cor(lll_cov)[1], axmat, "horizontal", "", "Energy [MeV]", "Energy [MeV]", # xlim=None, ylim=None, minimaxi=None, , , xlim=(1e-10,20), ylim=(1e-10,20)
            minimaxi=(-1,1.001), logz=False, logx=True, logy=True, smooth=None, pad=None, pcol=True, head_top=True, midblanc=True)
else:
    #print(len(l_fe_bin), len())
    l_juntion, l_fe_all = cat([l_fe_bin]*nb_dosi,True, True)
    #print(l_juntion)
    #print(l_fe_all)
    #print(l_fe_bin)
    #print(cat([l_fe_bin]*nb_dosi,True, True))
    #exit()
    i_xlabel = lmap(lambda v: l_fe_all[list(np.array(l_fe_bin) > v).index(True)], [1e-9, 1e-6, 1e-3, 1])
    #print(i_xlabel)
    #exit()
    #aff_mat4(l_fe_all, l_fe_all, cov_to_sig_cor(lll_cov)[1], axmat, "horizontal", "", "Lethargy [a.u.]", "Lethargy [a.u.]", # xlim=None, ylim=None, minimaxi=None, , , xlim=(1e-10,20), ylim=(1e-10,20)
    aff_mat4(l_fe_all, l_fe_all, cov_to_sig_cor(lll_cov)[1], axmat, "horizontal", "", " ", r"Position \times Energy", # xlim=None, ylim=None, minimaxi=None, , , xlim=(1e-10,20), ylim=(1e-10,20)
        minimaxi=(-1,1.001), logz=False, logx=False, logy=False, smooth=None, pad=None, pcol=True, head_top=True, midblanc=True)
    for junction in l_juntion:
        c = (0,0,0) #(0.7,0.7,0.7)
        axmat.plot([junction,junction], axmat.get_ylim(),    c=c, linewidth=0.75)#, dashes=[6,4])
        axmat.plot(axmat.get_xlim(),    [junction,junction], c=c, linewidth=0.75)#, dashes=[6,4])
    if data.nb_dosi <= 6:
        for sub_junction in i_xlabel:
            for junction in [0]+l_juntion:
                c = (0.,0.,0.) #(0.7,0.7,0.7)
                axmat.plot([junction+sub_junction,junction+sub_junction], axmat.get_ylim(),    c=c, linewidth=0.5, dashes=[6,4])
                axmat.plot(axmat.get_xlim(),    [junction+sub_junction,junction+sub_junction], c=c, linewidth=0.5, dashes=[6,4])
    
    axmat.set_xticks(i_xlabel)
    axmat.set_xticklabels("meV eV keV MeV".split(), size=12, rotation=45)
    axmat.set_yticks([])
    axmat.set_yticklabels([])

#plt.show()
#exit()

# aff_mat4(lx, lx, cor, l_ax2[imat][0], "horizontal", blabla, "", "", pad=0.01,
# xlim=None, ylim=None,
# logz=None, logx=False, logy=False, minimaxi=(mini,maxi), midblanc=True if mini==-1 else False, midgreen=False, minblanc=True if blabla=="ND_{dosi}" else False, nb_leg=4,
# maxblanc=False, centered=False, smooth=None, pcol=False,head_top=True, maskout=False, simple_scale=False)

key_printed = []
for i in range(len(data.l_key_irdff_iaea)):                                        # some plots
    c = get_c(i,len(data.l_key_irdff_iaea))
    if data.l_key_irdff_iaea[i] not in key_printed:
        key_printed += [data.l_key_irdff_iaea[i]]
        #aff_curve(l_ax[0,-1], ll_xe[i],ll_xv[i],ll_xs[i],c,1.,0.3,linewidth=1)
        #print(len(ll_xe_c0[i]), len(ll_xv_c0[i]))
        l_ax[0,-1].plot(ll_xe_c0[i],ll_xv_c0[i],c=c,linewidth=1)
        #l_ax[0,-2].plot(ll_xe[i],ll_xs[i]/(ll_xv[i]+1e-15)*100,c=c)
        #l_ax[0,-2].set_ylim([0.1,100])
        
        
# No idea whats for

# l_vol = [1.3601E+02 , 7.5601E+01, 8.4615E+01]

l_vol=[1.3601E+02]*len(ll_fv_bin)

l_integ_1ev = []
l_integ_tot = []

for i in range(nb_dosi):                                                # some plots
    print(i)
    print(len(ll_fv_bin))
    print(len(l_vol))
    c = get_c(i, nb_dosi)
    #aff_curve(l_ax[0,-3], dup_piquet(l_fe_bin),dup(ll_fv_bin[i]),dup(ll_fs[i]),c,1.,0.3,linewidth=1)
    #aff_curve(l_ax[0,-4], dup_piquet(l_fe_bin),dup(ll_fv_bin[i]*ll_xv_bin[i]),dup(ll_fv[i]*ll_xs_proj_f[i]),c,1.,0.3,linewidth=1)
    
    #print(data.l_volume)
    #exit()
    #l_ax[0,-3].plot(dup_piquet(l_fe_bin), dup(ll_fv_bin[i]),c=c,linewidth=1)
    dl = np.log10(l_nrj[1]) - np.log10(l_nrj[0])
    #print(np.log10(l_nrj[1:]) - np.log10(l_nrj[:-1]))
    l_ax[0,-3].plot(dup_piquet(l_fe_bin), dup(np.array(ll_fv_bin[i])/l_vol[i])/dl,c=c,linewidth=1)
    print("dlet", dl, l_vol[i])
    print("flux a 100W en 1e9 n/cm2/s", sum(np.array(ll_fv_bin[i])/l_vol[i]) * 100 / 1.32169E-11 / 1e9)
    #print(np.sum(np.array(ll_fv_bin[i])))
    #exit()
    #exit()
    #ls1 = np.array(list(map(float, " 5.091901e-08     1.561489e-08     2.004834e-08     2.541497e-08     3.273636e-08     4.186109e-08     5.528319e-08     6.948552e-08     9.001531e-08     1.179216e-07     1.559796e-07     1.997865e-07     2.548357e-07     3.292595e-07     4.234614e-07     5.429363e-07     7.134846e-07     9.223824e-07     1.194138e-06     1.682108e-06     2.184140e-06     2.738118e-06     3.198877e-06     4.153788e-06     5.202260e-06     6.641252e-06     8.541201e-06     1.083217e-05     1.397188e-05     2.028293e-05     2.373005e-05     2.777366e-05     3.497701e-05     4.365013e-05     5.469807e-05     7.873096e-05     8.289196e-05     1.013700e-04     1.267456e-04     1.538864e-04     1.766414e-04     2.141655e-04     2.475582e-04     2.798450e-04     3.161999e-04     3.472928e-04     3.742847e-04     3.969641e-04     4.020931e-04     4.062760e-04     3.842262e-04     3.650388e-04     3.239955e-04     2.775634e-04     2.361835e-04     1.900702e-04     1.542798e-04     1.279405e-04     1.069949e-04     9.431162e-05     8.631390e-05     8.264606e-05     8.053163e-05     7.968027e-05     7.898113e-05     7.855192e-05     7.780284e-05     7.683603e-05     7.568844e-05     7.470855e-05     7.409201e-05     7.327740e-05     7.319984e-05     7.295998e-05     7.255108e-05     7.226146e-05     7.181683e-05     7.179445e-05     7.141338e-05     7.106625e-05     7.065346e-05     6.966005e-05     6.911111e-05     6.848510e-05     6.630484e-05     6.197226e-05     7.144286e-05     7.176911e-05     7.310741e-05     7.313905e-05     7.304082e-05     7.340788e-05     7.284216e-05     7.115947e-05     7.012050e-05     7.503533e-05     7.539857e-05     7.446007e-05     7.148575e-05     7.685492e-05     7.736146e-05     7.698450e-05     7.681759e-05     7.681765e-05     7.742868e-05     7.832187e-05     7.761821e-05     7.856659e-05     7.961072e-05     7.943621e-05     8.013671e-05     7.875558e-05     7.995063e-05     8.042716e-05     8.096600e-05     8.114778e-05     8.134618e-05     8.102384e-05     8.162649e-05     8.181166e-05     8.219442e-05     8.207711e-05     8.236912e-05     8.283500e-05     8.305907e-05     8.325507e-05     8.379220e-05     8.424789e-05     8.419932e-05     8.458163e-05     8.479457e-05     8.556447e-05     8.544063e-05     8.622441e-05     8.635457e-05     8.698487e-05     8.793839e-05     8.729288e-05     8.850643e-05     8.920635e-05     8.991554e-05     9.100998e-05     9.192077e-05     9.276059e-05     9.395642e-05     9.528227e-05     9.663720e-05     9.842076e-05     1.010263e-04     1.048374e-04     1.083919e-04     1.008167e-04     1.085292e-04     1.127533e-04     1.172559e-04     1.226739e-04     1.295382e-04     1.354689e-04     1.301863e-04     1.436755e-04     1.506478e-04     1.661514e-04     1.626735e-04     1.775651e-04     1.912755e-04     2.014492e-04     2.255794e-04     2.384507e-04     2.628828e-04     2.413004e-04     2.144301e-04     2.874765e-04     3.215789e-04     3.502414e-04     3.929947e-04     4.056085e-04     3.254136e-04     3.276376e-04     3.907948e-04     3.821516e-04     3.945340e-04     3.920143e-04     3.862445e-04     4.401736e-04     4.128781e-04     3.544181e-04     2.644347e-04     2.370327e-04     1.963312e-04     1.559932e-04     1.075864e-04     7.229062e-05     4.009200e-05     2.118168e-05     1.001679e-05     4.104885e-06     1.457157e-06     4.274357e-07     1.146039e-07     2.501506e-08".split())))
    #ls2 = np.array(list(map(float,  " 5.060387e-08     1.495324e-08     1.931247e-08     2.504905e-08     3.336018e-08     4.217163e-08     5.422309e-08     6.927986e-08     9.047361e-08     1.182682e-07     1.551506e-07     1.989423e-07     2.529070e-07     3.297709e-07     4.207141e-07     5.472544e-07     7.076598e-07     9.271852e-07     1.188087e-06     1.675388e-06     2.182509e-06     2.745715e-06     3.186610e-06     4.152981e-06     5.184660e-06     6.644938e-06     8.546621e-06     1.082248e-05     1.393089e-05     2.027336e-05     2.372092e-05     2.774676e-05     3.500090e-05     4.369484e-05     5.472452e-05     7.875032e-05     8.285886e-05     1.012973e-04     1.267643e-04     1.539516e-04     1.764779e-04     2.140789e-04     2.475521e-04     2.796310e-04     3.159836e-04     3.471634e-04     3.742940e-04     3.970319e-04     4.021407e-04     4.064990e-04     3.840140e-04     3.652967e-04     3.242267e-04     2.781385e-04     2.365282e-04     1.902969e-04     1.545635e-04     1.283184e-04     1.074168e-04     9.479636e-05     8.674020e-05     8.292459e-05     8.086197e-05     7.992113e-05     7.941996e-05     7.881589e-05     7.798456e-05     7.718070e-05     7.603547e-05     7.520826e-05     7.432582e-05     7.352030e-05     7.356898e-05     7.331564e-05     7.286281e-05     7.259107e-05     7.212709e-05     7.213622e-05     7.186004e-05     7.148161e-05     7.102104e-05     7.012152e-05     6.952141e-05     6.876848e-05     6.668034e-05     6.222052e-05     7.194346e-05     7.219450e-05     7.347285e-05     7.342486e-05     7.345566e-05     7.372208e-05     7.333972e-05     7.166891e-05     7.041225e-05     7.564845e-05     7.576555e-05     7.512110e-05     7.222336e-05     7.719057e-05     7.759764e-05     7.734379e-05     7.738658e-05     7.706746e-05     7.810211e-05     7.860078e-05     7.816095e-05     7.882678e-05     7.993673e-05     8.001036e-05     8.059229e-05     7.921120e-05     8.033211e-05     8.084982e-05     8.107548e-05     8.159742e-05     8.173894e-05     8.134914e-05     8.208876e-05     8.208895e-05     8.268599e-05     8.245696e-05     8.282764e-05     8.325340e-05     8.336444e-05     8.353348e-05     8.408438e-05     8.450189e-05     8.464330e-05     8.498825e-05     8.522547e-05     8.557767e-05     8.559318e-05     8.667184e-05     8.677873e-05     8.732404e-05     8.818118e-05     8.765905e-05     8.906082e-05     8.978167e-05     9.029300e-05     9.113093e-05     9.231378e-05     9.350899e-05     9.443199e-05     9.576885e-05     9.719766e-05     9.875553e-05     1.016105e-04     1.054857e-04     1.090319e-04     1.012560e-04     1.089306e-04     1.134027e-04     1.176456e-04     1.227074e-04     1.298781e-04     1.359204e-04     1.319749e-04     1.451603e-04     1.516773e-04     1.674223e-04     1.638591e-04     1.787450e-04     1.926918e-04     2.031168e-04     2.265886e-04     2.406379e-04     2.650131e-04     2.434178e-04     2.166380e-04     2.889103e-04     3.220222e-04     3.493320e-04     3.916805e-04     4.033751e-04     3.234949e-04     3.242364e-04     3.818158e-04     3.754166e-04     3.840157e-04     3.808546e-04     3.769955e-04     4.273239e-04     4.058541e-04     3.505552e-04     2.621834e-04     2.348979e-04     1.944954e-04     1.554919e-04     1.078522e-04     7.271979e-05     4.011195e-05     2.115597e-05     1.005356e-05     4.116242e-06     1.471310e-06     4.436897e-07     1.072203e-07     2.309131e-08".split())))
    #ls2 = np.array(list(map(float,  " 2.556691e-08     7.580242e-09     9.704492e-09     1.250521e-08     1.685727e-08     2.056522e-08     2.682696e-08     3.496438e-08     4.642485e-08     5.913887e-08     7.720163e-08     1.001635e-07     1.266051e-07     1.649828e-07     2.161112e-07     2.766038e-07     3.605144e-07     4.691244e-07     5.997795e-07     8.208876e-07     1.065631e-06     1.349708e-06     1.627913e-06     2.128832e-06     2.662283e-06     3.419950e-06     4.387073e-06     5.608353e-06     7.191944e-06     9.999464e-06     1.200273e-05     1.438458e-05     1.806332e-05     2.257742e-05     2.822540e-05     3.906565e-05     4.263540e-05     5.197693e-05     6.438888e-05     7.779318e-05     8.973565e-05     1.074479e-04     1.236757e-04     1.389770e-04     1.556770e-04     1.697013e-04     1.809767e-04     1.891808e-04     1.894849e-04     1.882839e-04     1.748146e-04     1.628575e-04     1.406225e-04     1.170531e-04     9.607392e-05     7.355936e-05     5.658902e-05     4.445526e-05     3.520403e-05     2.975021e-05     2.663406e-05     2.514142e-05     2.427716e-05     2.379876e-05     2.346163e-05     2.325559e-05     2.291034e-05     2.271590e-05     2.235266e-05     2.202625e-05     2.176539e-05     2.157346e-05     2.153428e-05     2.142516e-05     2.130159e-05     2.120190e-05     2.120826e-05     2.126387e-05     2.114973e-05     2.111574e-05     2.095404e-05     2.061886e-05     2.066377e-05     2.069014e-05     2.057608e-05     2.046416e-05     2.105264e-05     2.115048e-05     2.137955e-05     2.135936e-05     2.141321e-05     2.149205e-05     2.148021e-05     2.131592e-05     2.146411e-05     2.191724e-05     2.193721e-05     2.188382e-05     2.166872e-05     2.213698e-05     2.225008e-05     2.221678e-05     2.213009e-05     2.237656e-05     2.229392e-05     2.243920e-05     2.251515e-05     2.253929e-05     2.266200e-05     2.271287e-05     2.273396e-05     2.271733e-05     2.274333e-05     2.278762e-05     2.296978e-05     2.294035e-05     2.291467e-05     2.302251e-05     2.308880e-05     2.313306e-05     2.318686e-05     2.304768e-05     2.324571e-05     2.329312e-05     2.329542e-05     2.339146e-05     2.344049e-05     2.353761e-05     2.352493e-05     2.368566e-05     2.368653e-05     2.378022e-05     2.383409e-05     2.399926e-05     2.418419e-05     2.409164e-05     2.449378e-05     2.415861e-05     2.466890e-05     2.473724e-05     2.489736e-05     2.513878e-05     2.533008e-05     2.564667e-05     2.586762e-05     2.619260e-05     2.654905e-05     2.694839e-05     2.764901e-05     2.865119e-05     2.988934e-05     2.703504e-05     2.945964e-05     3.059242e-05     3.162344e-05     3.302376e-05     3.488797e-05     3.674105e-05     3.476881e-05     3.842298e-05     3.998971e-05     4.439120e-05     4.314905e-05     4.689288e-05     5.028437e-05     5.239719e-05     5.826285e-05     6.100733e-05     6.713526e-05     6.452479e-05     5.876561e-05     7.466402e-05     8.126369e-05     8.752477e-05     9.543026e-05     9.700503e-05     8.218908e-05     8.247523e-05     9.399106e-05     9.152991e-05     9.386955e-05     9.330955e-05     9.214131e-05     1.020198e-04     9.570868e-05     8.369107e-05     6.423949e-05     5.802477e-05     4.875936e-05     3.900327e-05     2.729134e-05     1.848879e-05     1.045888e-05     5.566737e-06     2.693499e-06     1.136793e-06     4.219795e-07     1.256359e-07     2.870702e-08     7.082338e-09".split())))
    
    #print(sum(ls1), ls1)
    #print(sum(ll_fv_bin[i]), ll_fv_bin[i])
        
    #print(ls2/ls1)
    
    #print(np.array(ll_fv_bin[i+1])/np.array(ll_fv_bin[i]))
    #Material plexi_C       : 0.0000E+00 1.3296E+02 (0.017) :     N/A (100.0 % den.)
    #Material plexi_CR      : 0.0000E+00 7.5071E+01 (0.020) :     N/A (100.0 % den.)
    #Material plexi_R       : 0.0000E+00 8.6004E+01 (0.019) :     N/A (100.0 % den.)
    '''
    tally = np.sum(np.array(ll_fv_bin[i]))          # cm/src
    flux_surf_par_src = tally/l_vol[i]          # /cm2/src
    dl = np.log10(l_nrj[1]) - np.log10(l_nrj[0])
    #print("tally" , tally)
    print("dl", dl)
    print("r", data.l_radius[i])
    print("th", data.l_thickness[i])
    print("vol", l_vol[i])
    print("tally", tally)
    print("flux_surf_par_src", flux_surf_par_src)

    puiss    = 100                                  # J/s
    #J_par_eV   = 1.6022e-19
    J_par_src  = 1.32169E-11                        # J/src
    src_par_s  = puiss / J_par_src                  # src/s
    print("src_par_s", src_par_s)
    cmm2_par_src = flux_surf_par_src * src_par_s    # /cm2/s
    print( cmm2_par_src / 1e9)
    #CROCUS has a license to produce 100 watts (0.13 hp) or a neutron flux of ~2.5 × 109 cm-2s-1 at the core's center.[2]
    exit()'''
    

    std_rel = np.array(ll_fs_bin[i])/np.array(ll_fv_bin[i])
    #print(len(std_rel), len(l_srel_ave_dosi))
    #print(d_pos_2_stat.keys())
    #exit()
    l_rsd_stat = d_pos_2_stat[(data.l_sss_path_nuis[i], l_pos_dosi[i])]
    #print(ipos, type(ipos))
    #l_rsd_stat = l_srel_ave[(len(l_fe_bin)-1)* ipos: (len(l_fe_bin)-1)* (ipos+1)]
    print(nb_dosi, len(std_rel), len(l_rsd_stat))
    l_ax[0,-2].plot(dup_piquet(l_fe_bin), dup(std_rel)*100,c=c,linewidth=1)
    #l_ax[0,-2].plot(dup_piquet(l_fe_bin), dup((std_rel**2 - np.array(l_rsd_stat)**2)**0.5)*100,c=c,linewidth=1, alpha=0.3)
    l_ax[0,-2].plot(dup_piquet(l_fe_bin), dup(l_rsd_stat)*100,c=c,linewidth=1, alpha=0.3)

    
    l_ax[0,-4].plot(dup_piquet(l_fe_bin),dup(ll_fv_bin[i]*ll_xv_bin[i]),c=c,linewidth=1)
    
    i_1 = 0
    i_2 = list(l_fe_bin).index(list(filter(lambda e:e>1e-6, l_fe_bin))[0])
    l_integ_1ev += [integ(l_fe_bin, ll_fv_bin[i]*ll_xv_bin[i])[i_2]-integ(l_fe_bin, ll_fv_bin[i]*ll_xv_bin[i])[i_1]]
    l_integ_tot += [integ(l_fe_bin, ll_fv_bin[i]*ll_xv_bin[i])[-1]   ]
    tmp = integ(l_fe_bin, ll_fv_bin[i]*ll_xv_bin[i])
    if True:
        l_ax[0,0].plot(dup_piquet(l_fe_bin),dup(tmp/tmp.max()),c=c)
    else:
        l_m = np.array([0.0005,0.001,0.002,0.004,0.008,0.016,0.032,0.064,0.128,0.256])
        l_ax[0,0].plot(dup_piquet(l_fe_bin),dup(tmp/l_m[i]),c=c)
        
    if False:
        tmpb = integ(l_fe_bin, ll_fv_bin[i]*ll_xv_bin[i] * std_rel)
        l_ax[0,0].plot(dup_piquet(l_fe_bin),dup(tmpb/tmpb.max()),c=c, alpha=0.3)



if False:
    l_integ_1ev = np.array(l_integ_1ev) #/max(l_integ_1ev)
    l_integ_tot = np.array(l_integ_tot) #/max(l_integ_tot)
    print (l_integ_1ev)
    print (l_integ_tot)
    print ("autop",(l_integ_tot/l_integ_1ev      )/(l_integ_tot/l_integ_1ev).max())
    print ("autop",(l_integ_tot/l_integ_tot.max())/(l_integ_1ev/l_integ_1ev.max()))
    print (((l_integ_tot/l_integ_1ev)/(l_integ_tot/l_integ_1ev).max())/((l_integ_tot/l_integ_tot.max())/(l_integ_1ev/l_integ_1ev.max())))


#ll_dlet = []
#for i in range(data.nb_dosi):
ll_dlet = np.array([dlet(l_fe_bin)]*nb_dosi)
#ll_dlet = np.array(ll_dlet)


l_rr, l_rrs = np.zeros(len(ll_fv_bin)), np.zeros(len(ll_fv_bin))
l_sens = []
for i in range(data.nb_dosi):                                               # calcul de sensi&RR
    #sens = ll_dlet[i]*ll_fv_bin[i]*data.l_at_den[i]                      # sensitivity          TODOTODOTODO f->x
    sens = ll_dlet[i]*ll_xv_bin[i]*data.l_at_den[i]                      # sensitivity
    #print "\t".join(map(lambda v:str(v), ll_fv_proj_c[i]))
    #print "\t".join(map(lambda v:str(v), ll_ce[i]))
    #exit()
    l_sens += [sens]
    rr   = sum(ll_dlet[i]*ll_xv_bin[i]*data.l_at_den[i]*ll_fv_bin[i]) # reaction rate
    #rrs  = ((sens.T).dot(lll_cov[i].dot(sens)))**0.5
    l_rr[i] = rr
    #l_rrs[i] = rrs

def in_coll(ll):                                                            # passage sur une colonne des l_sensi
    size = sum(map(lambda l:len(l), ll))
    r = np.zeros((len(ll),size))
    pos = 0
    for i,l in enumerate(ll):
        r[i, pos:pos+len(l)] = l
        pos += len(l)
    return np.array(r)



coll_sens = in_coll(l_sens)
#l_rr = sum(ll_dlet[i]*ll_xv_proj_c[i]*l_at_den[i]*ll_fv_proj_c[i])
#l_rrs  = ((coll_sens.T).dot(cat_mat(lll_cov).dot(coll_sens)))**0.5
#cov_rr  = ((coll_sens).dot(cat_mat(lll_cov).dot(coll_sens.T)))
cov_rr  = ((coll_sens).dot(lll_cov.dot(coll_sens.T)))
cov_rr_sig  = ((coll_sens).dot(lll_cov_sig.dot(coll_sens.T)))
print("cor_sig calc")
print(cov_rr.shape)
print(cov_rr_sig.shape)
sh=cov_rr.shape
if len(lcase_csv)>10:
    print("large file mode")
    N_samp=2**14
else:
    N_samp=2**16
samp=np.random.normal(cov_rr,cov_rr_sig,size=(N_samp,sh[0],sh[1]))
print(samp.shape)
samp_cor=np.zeros(samp.shape)
for i in range(sh[0]):
    for j in range(sh[1]):
        samp_cor[:,i,j]=samp[:,i,j]/(samp[:,i,i]*samp[:,j,j])**0.5
cor_sig=np.std(samp_cor,axis=0)

stddev, cor = cov_to_sig_cor(cov_rr)

print (aff_list("l_rr", l_rr))
print (aff_list("stddev", stddev))
print (aff_list("stddev [%]", stddev/l_rr*100))
print (aff_mat("corr", cor))

#exit()
#rr   = sum(ll_dlet[i]*ll_xv_proj_c[i]*l_at_den[i]*ll_fv_proj_c[i])
#rrs  = ((sens.T).dot(lll_cov[i].dot(sens)))**0.5
##l_rr[i] = rr
#l_rrs[i] = rrs

# 2.65236816888e-09 1.42474098881e-09 7.33710367979e-08 1.18010649669e-06
# 7.07999915439e-11 1.03003612194e-11 1.22131125564e-09 1.27037705998e-08
# 0.0266931236677 0.00722963773787 0.0166456862128 0.0107649357371
'''

print "cov2"
#print " ".join(map(lambda v:str(v),l_rr / get_at_density("Au", "79197")))
print aff_list("l_rr", l_rr)
print aff_mat("l_rrs", l_rrs)
#print " ".join(map(lambda v:str(v),l_rr))
#print " ".join(map(lambda v:str(v),l_rrs))
#print " ".join(map(lambda v:str(v),l_rrs/l_rr))
print
exit()

sens = l_dlet*ll_fv_proj_c
for i in range(len(sens)):
    sens[i] *= l_at_den[i]
cov_rr  = (sens).dot(ll_cov.dot(sens.T))
print "rr cov_rr**0.5"
print "\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(cov_rr**0.5)))
print
'''
#cor = cov_rr*1.
#stddev = np.sqrt(np.diag(cov_rr))
#stddev = np.sqrt(np.diag(cov_rr))
#print "stddev"
#print " ".join(map(lambda v:str(v),stddev))
#print " ".join(map(lambda v:str(v),stddev/l_rr))
#cor /= (stddev[:, None]+1e-50)
#cor /= (stddev[None, :]+1e-50)
#print "rr cor3"
#print "\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(cor)))



if not os.path.exists("ndupnuis_out"):
    os.mkdir("ndupnuis_out")

path = "ndupnuis_out/out_"+(data.get_key_for_ndup_nuis())

print ("write res in",path)
open(path,"w").write(
    "val      "+" ".join(map(lambda v:str(v),l_rr))+"\n"+
    "stdv     "+" ".join(map(lambda v:str(v),stddev))+"\n"+
    "stdv_rel "+" ".join(map(lambda v:str(v),stddev/l_rr))+"\n"+
    "corr   \n"+"\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(cor)))
)
stddev=np.diag(check_cov)
open(path+"_TMC","w").write(
    "val      "+" ".join(map(lambda v:str(v),l_rr))+"\n"+
    "stdv     "+" ".join(map(lambda v:str(v),stddev))+"\n"+
    "stdv_rel "+" ".join(map(lambda v:str(v),stddev/l_rr))+"\n"+
    "corr   \n"+"\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(check_cor)))
)
open("ndupnuis_out/out_"+"ll_rr","w").write(
    "Reaction rates   \n"+"\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(ll_rr)))
)

print("rappel check:")
print(check)

l_x = np.arange(len(cor)+1)+0.5


#aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(0.75,1.001), pad=None, pcol=True, head_top=True, midgreen=True)
#aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(0.5,1), pad=None, pcol=True, head_top=True, midgreen=True)
aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midgreen=True)
aff_mat4(l_x, l_x, check_cor, axmatsup, "horizontal", "Correlation", "Dosimeter number", "Dosimeter number",cov=check_cor_sig,Cbar_label=r"\sigma_{Correlation}", minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midgreen=True)





for i in [1,2,3,4]:
    l_ax[0,i].set_xscale("log")
    l_ax[0,i].set_yscale("log")
    
    
toto = False
    
l_ax[0,0].set_xscale("log")

xlims, ylims = get_lim(l_ax[0,2])
l_ax[0,2].set_ylim((ylims[1]/5e2,ylims[1]*1.3))
#l_ax[0,2].set_ylim((ylims[1]/5e2,ylims[1]))

xlims, ylims = get_lim(l_ax[0,1])
l_ax[0,1].set_ylim((ylims[1]/1e6,ylims[1]))

l_ax[0,-2].set_ylim([0.1,20])

set_nice_ax(l_ax[0,0],x="MeV")
if not toto and False:
    set_nice_ax(axmat,x="MeV",y="MeV")


set_nice_ax(l_ax[0,1], y="pow", powmodulo=(3,0))
set_nice_ax(l_ax[0,4], y="pow", powmodulo=(3,0))


my_sub6_finalise(l_ax, y=False)


#therm = min(map(lambda l_ce: l_ce[0],ll_ce)) <0.001
therm = min(map(lambda l: l[0],ll_xe_c0)) <0.001
#therm = ll_xe_c0[0] < 0.001

lims = (1e-10 if therm else 0.1, 20)
if toto:
    lims = 0.4, 19.99
if data.nb_dosi == 1:
    axmat.set_xlim(lims)
    axmat.set_ylim(list(reversed(lims)))
else:
    axmat.set_ylim(list(reversed(axmat.get_ylim())))
    
axmat2.set_ylim(list(reversed(axmat2.get_ylim())))
axmatsup.set_ylim(list(reversed(axmatsup.get_ylim())))



for i in [1,2,3,4]:
    l_ax[0,i].set_xlim(lims)
if not therm :
    print("aff - not therm mode")
    for i in [1,2,4]:
        l_ax[0,i].set_yscale("linear")
        set_nice_ax(l_ax[0,i],y="pow")


l_ax[0,4].set_ylabel(r"$\mathrm{XS~[barn]}$", size=get_aff_size("s_xylabel"))
#l_ax[0,3].set_ylabel(r"$\mathrm{\sigma_{XS}~[\%]}$", size=get_aff_size("s_xylabel"))
l_ax[0,3].set_ylabel(r"$\mathrm{rsd(\phi)~[\%]}$", size=get_aff_size("s_xylabel"))
l_ax[0,2].set_ylabel(r"$\mathrm{\phi~[cm/let/n_{src}]}$", size=get_aff_size("s_xylabel"))
l_ax[0,2].set_ylabel(r"$\mathrm{\phi~[/cm^2/let/n_{src}]}$", size=get_aff_size("s_xylabel"))
l_ax[0,1].set_ylabel(r"$\mathrm{RR~[at/let/n_{src}]}$", size=get_aff_size("s_xylabel"))
l_ax[0,0].set_ylabel(r"$\mathrm{Norm.}~\int_0^{E} RR \mathrm{d}E$", size=get_aff_size("s_xylabel"))
l_ax[0,0].set_xlabel(r"$\mathrm{Energy}$", size=get_aff_size("s_xylabel"))
l_ax[0,1].set_xticklabels([])
l_ax[0,2].set_xticklabels([])
l_ax[0,3].set_xticklabels([])
l_ax[0,4].set_xticklabels([])

print("WARNING - script developpe de facon a ce que fonnctionnel si plusieurs sss_path_nduc utilises (pour PETALE) mais non teste sur ce point. A faire avec les 'check' inclus")
print ("save fig")
fig.savefig("ndupnuis_out/img.png", bbox_inches=('tight'), dpi=200)
fig.savefig("ndupnuis_out/hist/"+"+".join(lcase_csv)+".png", bbox_inches=('tight'), dpi=200)
fig2.savefig("ndupnuis_out/corr_zoom.png", bbox_inches=('tight'), dpi=200)
# plt.show()



#((sens.T).dot(cov.dot(sens)))**0.5

#name,keyname,dosi_den = "Au","_0_Au_102_791970", 5.90079E-02  # 1/barn*cm
#name,keyname,dosi_den = "Ni","_1_Ni_103_280580", 6.24027E-02
#name,keyname,dosi_den = "Ti46","_2_Ti_103_220460", 4.68102E-03
#name,keyname,dosi_den = "Ti48","_2_Ti_103_220480", 4.18285E-02
#name,keyname,dosi_den = "Fe54","_3_Fe_103_260540", 4.96293E-03
#name,keyname,dosi_den = "Fe56","_3_Fe_103_260560", 7.79075E-02
