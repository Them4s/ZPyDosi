# python ~/data/python/irrad/nducup1.py &

# https://www-nds.iaea.org/exfor/servlet/E4sSearch2
# https://www-nds.iaea.org/exfor/servlet/E4sMakeE4

'''
Compute and save the uncertainties due to dosimetry nuclear data.
'''

import os
from ZPyDosi.Common.utils_general import lmap, get_aff_size, get_c, dup, dup_piquet,set_nice_ax
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.Prints.PrintnSave import aff_list, aff_mat
from ZPyDosi.Plots.SubPlots import my_sub6, my_sub6_finalise, get_lim, aff_curve
from ZPyDosi.Plots.MatrixPlots import aff_mat4, make_cmap
from ZPyDosi.Stats.Stats import cov_to_sig_cor, cor_sig_to_cov
from ZPyDosi.XSnFlux.GetIRDFF import get_irdff_iaea
from ZPyDosi.XSnFlux.Projections import projet_vec_intervals_from_continus, projet_vec_intervals_from_integrated
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams.update({'font.size': 18})
print ("#"*50)
#key      = get_param_vari("key", str, None)
#path_sss = get_param_vari("path_sss", str, None)
#csv_corr = get_param_vari("csv_corr", str, None)

#path_csv = get_param_vari("csv", str, None)
#case_csv = get_param_vari("case", str, None)

path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv  = get_param_vari("lcase", str).split("/")
save_key  = get_param_vari("save", str, "")
do_rm=get_param_vari("do_rm",bool,"False") #To remove commented detectors
gr_order = get_param_vari("gr_order", int,0) # to gain ram by decreasing the spectral resolution by 2**gr_order
do_GPU = get_param_vari("do_GPU",bool,"False") # multivariate not yet implemented in numba

data = DataIrrad(path_csv_data, path_csv_dosi, lcase_csv, load_sss_results=True, load_sss_spectrum=True, remove_data=do_rm,group_order=gr_order)

print ("#"*50)





#fig = plt.figure(1, figsize=(10,12))
fig = plt.figure(1, figsize=(12,17.5))
fig.patch.set_facecolor('white')
axmat = plt.subplot(2,2,1)
axmat2 = plt.subplot(2,2,3)
l_ax = my_sub6(fig,1,2,1,list_rx=[1],list_ry=[1,1,1,1,1],list_sy=[0.1,0.1,0.1,0.1],auto_y=False, list_idx_none=[(0,1),(0,2),(0,3),(0,4)])


def recup_sss(path, key):                                # get serpent results
    l_e, l_v, l_s = [],[],[]
    lignes = open(path).readlines()
    ligne  = lignes.pop(0)
    while key not in ligne:
        ligne  = lignes.pop(0)
    ligne  = lignes.pop(0)
    while "]" not in ligne:
        v,s = ligne.split()[-2:]
        l_v += [float(v)]
        l_s += [float(s)]
        ligne  = lignes.pop(0)
    while key.split()[0]+"E" not in ligne:
        ligne  = lignes.pop(0)
    ligne  = lignes.pop(0)
    while "]" not in ligne:
        l_e += [float(ligne.split()[0])]
        last_e = ligne.split()[1]
        ligne  = lignes.pop(0)
    l_e += [float(last_e)]
    print(l_v)
    return np.array(l_e), np.array(l_v), np.array(l_s)*np.array(l_v)

ll_ce   = []
lll_cor = []
ll_xe   = []
ll_xv   = []
ll_xs   = []
ll_fv, ll_fs = [],[]
#l_at_den = []
#l_key_irdff_iaea = []
#nb_dosi = 0



for idosi in range(data.nb_dosi):
    idata_irdff = get_irdff_iaea(os.path.expandvars("$petale_analysis/data/iaea_data/"+data.l_key_irdff_iaea[idosi]), e_min = None)
    
    ll_ce   += [idata_irdff[0][0]]
    lll_cor += [idata_irdff[0][1]]
    ll_xe   += [idata_irdff[1][0]]
    ll_xv   += [idata_irdff[1][1]]
    ll_xs   += [idata_irdff[1][2]]
    #name = data.l_name_sss[idosi]
    #print "dos_"+name+"_spectrum"    #DETdos_E4_spectrum
    
    
    #l_fv_tmp, l_fs_tmp = get_sss_out_det(data.l_path_case[idosi]+"_det0.m", "dos_"+name+"_spectrum")
    #l_fs_tmp = np.array(l_fs_tmp) * np.array(l_fv_tmp)
    #l_fe_tmp = get_sss_out_det(data.l_path_case[idosi]+"_det0.m", "dos_"+name+"_spectrumE", id1=0)[0] + [get_sss_out_det(data.l_path_case[idosi]+"_det0.m","dos_"+name+"_spectrumE", id1=1)[0][-1]]
    #ll_fv    += [l_fv_tmp]
    #ll_fs    += [l_fs_tmp]
    #l_fe      = l_fe_tmp
    
ll_fv = list(data.ll_fv)
ll_fs = list(data.ll_fs)
l_fe  = list(data.l_fe)
#print(ll_fv)
'''
dos_Fe-R1_spectrum
dos_Al-R1_spectrum
dos_Au-R2_spectrum
dos_In-R1_spectrum
dos_Au-R2_spectrum
l_rr                     2.67040741258e-09 1.42062421406e-09 1.17970590395e-06 7.34036238347e-08 1.17970590395e-06 
stddev                   7.1126648342e-11  1.02832337747e-11 1.26593598905e-08 1.22163254879e-09 1.26593598905e-08 
stddev [%]               0.0266351299083   0.00723853195862  0.0107309456095   0.0166426735489   0.0107309456095   
corr                     1.0               0.0               0.0               0.0               0.0               
                         0.0               1.0               0.0               0.0               0.0               
                         0.0               0.0               1.0               0.0               1.0               
                         0.0               0.0               0.0               1.0               0.0               
                         0.0               0.0               1.0               0.0               1.0           '''

'''
elif mode == "je sais plus":
    direct_rr = False
    keydata, csv = tuple(key.split("_")), csv_corr
    e_min = None if csv not in ["Au_j33","Co59"] else 10e-11
    (l_ce, ll_cor), (l_xe,l_xv,l_xs) = recup("../../../irdff/iaea_data/"+csv, e_min) # +keydata[0]
    ll_fv, ll_fs = [],[]
    print "recup sss out"
    path_case = path_sss
    data, l_matzaimt = recup_sss_out(path_case + "/", dim_p=1)
    l_dosi = filter(lambda (key, matzaimt): key==keydata , l_matzaimt)[0][1]
    key_mat_name = "_".join(l_dosi[0].split("_")[:5])
    tmp_paf = path_case+"/tmp.out"
    if not os.path.exists(tmp_paf) : tmp_paf=path_case+"/input.out"
    lines = open(tmp_paf).readlines()
    while key_mat_name    not in lines[0]: lines.pop(0)
    while keydata[1][:-1] not in lines[0]: lines.pop(0)
    #print lines[0]
    dosi_den = float(lines[0].split()[-3])
    print "dosi_den",dosi_den
    
    tmp_proj_xs = None
    for i in range(9):
        #dosi_data = data['mat_dosi_'+str(i)+keyname]
        dosi_data = data[l_dosi[i]]
        l_fe = dosi_data["l_nrj_piquet"]
        print dosi_data['rv'], dosi_data['rs']
        
        dlet = np.log(l_fe[1:])-np.log(l_fe[:-1])
        
        ll_fv += [dosi_data["l_"+("rr" if direct_rr else "")+"spectra_v"]/dlet]
        ll_fs += [dosi_data["l_"+("rr" if direct_rr else "")+"spectra_s"]/dlet]
        if direct_rr:
            if tmp_proj_xs is None:
                tmp_proj_xs = projet_vec_intervals_from_continus(l_fe, l_xe, l_xv)+1e-30
            ll_fv[-1] /= tmp_proj_xs * dosi_den
            ll_fs[-1] /= tmp_proj_xs * dosi_den
else:
    print "Error - unrecognized mode"
    exit()
'''



for k in range(len(data.l_key_irdff_iaea)):
    if l_fe[0] >ll_ce[k][0]:
        l_fe = np.array([ll_ce[k][0]]+list(l_fe))
        for i in range(len(ll_fv)):
            ll_fv[i] = np.array([0]+list(ll_fv[i]))
            ll_fs[i] = np.array([0]+list(ll_fs[i]))
    
    if l_fe[-1]<ll_ce[k][-1]:
        l_fe = np.array(list(l_fe)+[ll_ce[k][-1]])
        for i in range(len(ll_fv)):
            ll_fv[i] = np.array(list(ll_fv[i])+[0])
            ll_fs[i] = np.array(list(ll_fs[i])+[0])


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


ll_xv_proj_f = lmap(lambda i: projet_vec_intervals_from_continus(l_fe, ll_xe[i], ll_xv[i]), range(len(ll_ce)))
ll_xs_proj_f = lmap(lambda i: projet_vec_intervals_from_continus(l_fe, ll_xe[i], ll_xs[i]), range(len(ll_ce)))

ll_xv_proj_c = lmap(lambda i: projet_vec_intervals_from_continus(ll_ce[i], ll_xe[i], ll_xv[i]), range(len(ll_ce)))
ll_xs_proj_c = lmap(lambda i: projet_vec_intervals_from_continus(ll_ce[i], ll_xe[i], ll_xs[i]), range(len(ll_ce)))

ll_rv_proj_c = lmap(lambda i: projet_vec_intervals_from_integrated(np.log(ll_ce[i]), np.log(l_fe), ll_fv[i]*ll_xv_proj_f[i]*data.l_at_den[i]),range(len(ll_fv)))
ll_rs_proj_c = lmap(lambda i: projet_vec_intervals_from_integrated(np.log(ll_ce[i]), np.log(l_fe), ll_fs[i]*ll_xv_proj_f[i]*data.l_at_den[i]),range(len(ll_fv)))

ll_fv_proj_c = lmap(lambda i: ll_rv_proj_c[i]/(ll_xv_proj_c[i]*data.l_at_den[i]+1e-15),range(len(ll_rv_proj_c)))
ll_fs_proj_c = lmap(lambda i: ll_rs_proj_c[i]/(ll_xv_proj_c[i]*data.l_at_den[i]+1e-15),range(len(ll_rs_proj_c)))



lll_cov = lmap(lambda i: cor_sig_to_cov(lll_cor[i], ll_xs_proj_c[i]), range(data.nb_dosi))
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



if data.nb_dosi == 1:
    aff_mat4(ll_ce[0], ll_ce[0], lll_cor[0], axmat, "horizontal", "", "Energy [MeV]", "Energy [MeV]", # xlim=None, ylim=None, minimaxi=None, , , xlim=(1e-10,20), ylim=(1e-10,20)
            minimaxi=(-1,1.001), logz=False, logx=True, logy=True, smooth=None, pad=None, pcol=True, head_top=True, midblanc=True)
else:
    l_juntion, l_ce_all = cat(ll_ce,True, True)
    aff_mat4(l_ce_all, l_ce_all, cat_mat(lll_cor), axmat, "horizontal", "", "Lethargy [a.u.]", "Lethargy [a.u.]", # xlim=None, ylim=None, minimaxi=None, , , xlim=(1e-10,20), ylim=(1e-10,20)
        minimaxi=(-1,1.001), logz=False, logx=False, logy=False, smooth=None, pad=None, pcol=True, head_top=True, midblanc=True)
    for junction in l_juntion:
         axmat.plot([junction,junction], axmat.get_ylim(),    c=(0.7,0.7,0.7), dashes=[6,4])
         axmat.plot(axmat.get_xlim(),    [junction,junction], c=(0.7,0.7,0.7), dashes=[6,4])
    

key_printed = []
for i in range(len(data.l_key_irdff_iaea)):                                        # some plots
    c = get_c(i,len(data.l_key_irdff_iaea))
    if data.l_key_irdff_iaea[i] not in key_printed:
        key_printed += [data.l_key_irdff_iaea[i]]
        aff_curve(l_ax[0,-1], ll_xe[i],ll_xv[i],ll_xs[i],c,1.,0.3,linewidth=1)
        l_ax[0,-2].plot(ll_xe[i],ll_xs[i]/(ll_xv[i]+1e-15)*100,c=c)
        l_ax[0,-2].set_ylim([0.1,99])


l_integ_1ev = []
l_integ_tot = []

for i in range(len(ll_fv)):                                                # some plots
    c = get_c(i,len(ll_fv))
    aff_curve(l_ax[0,-3], dup_piquet(l_fe),dup(ll_fv[i]),dup(ll_fs[i]),c,1.,0.3,linewidth=1)
    aff_curve(l_ax[0,-4], dup_piquet(l_fe),dup(ll_fv[i]*ll_xv_proj_f[i]),dup(ll_fv[i]*ll_xs_proj_f[i]),c,1.,0.3,linewidth=1)

    i_1 = 0
    i_2 = list(l_fe).index(list(filter(lambda e:e>1e-6, l_fe))[0])
    l_integ_1ev += [integ(l_fe, ll_fv[i]*ll_xv_proj_f[i])[i_2]-integ(l_fe, ll_fv[i]*ll_xv_proj_f[i])[i_1]]
    l_integ_tot += [integ(l_fe, ll_fv[i]*ll_xv_proj_f[i])[-1]   ]
    tmp = integ(l_fe, ll_fv[i]*ll_xv_proj_f[i])
    if True:
        l_ax[0,0].plot(dup_piquet(l_fe),dup(tmp/tmp.max()),c=c)
    else:
        l_m = np.array([0.0005,0.001,0.002,0.004,0.008,0.016,0.032,0.064,0.128,0.256])
        l_ax[0,0].plot(dup_piquet(l_fe),dup(tmp/l_m[i]),c=c)



if False:
    l_integ_1ev = np.array(l_integ_1ev) #/max(l_integ_1ev)
    l_integ_tot = np.array(l_integ_tot) #/max(l_integ_tot)
    print (l_integ_1ev)
    print (l_integ_tot)
    print ("autop",(l_integ_tot/l_integ_1ev      )/(l_integ_tot/l_integ_1ev).max())
    print ("autop",(l_integ_tot/l_integ_tot.max())/(l_integ_1ev/l_integ_1ev.max()))
    print (((l_integ_tot/l_integ_1ev)/(l_integ_tot/l_integ_1ev).max())/((l_integ_tot/l_integ_tot.max())/(l_integ_1ev/l_integ_1ev.max())))


ll_dlet = []
for i in range(data.nb_dosi):
    ll_dlet += [np.array(dlet(ll_ce[i]))]
# ll_dlet = np.array(ll_dlet)


l_rr, l_rrs = np.zeros(len(ll_fv)), np.zeros(len(ll_fv))
l_sens = []
l_XS=[]
l_xs_2_rr=[]
for i in range(data.nb_dosi):                                               # calcul de sensi&RR
    sens = ll_dlet[i]*ll_fv_proj_c[i]*data.l_at_den[i]                      # sensitivity
    #print "\t".join(map(lambda v:str(v), ll_fv_proj_c[i]))
    #print "\t".join(map(lambda v:str(v), ll_ce[i]))
    #exit()
    l_sens += [sens]
    rr   = sum(ll_dlet[i]*ll_xv_proj_c[i]*data.l_at_den[i]*ll_fv_proj_c[i]) # reaction rate
    l_XS+=[ll_xv_proj_c[i]]
    l_xs_2_rr+=[ll_dlet[i]*data.l_at_den[i]*ll_fv_proj_c[i]]
    #rrs  = ((sens.T).dot(lll_cov[i].dot(sens)))**0.5
    l_rr[i] = rr
    #l_rrs[i] = rrs
#print(l_rr)
#print(data.l_c)
#exit()

def in_coll(ll):                                                            # passage sur une colonne des l_sensi
    size = sum(map(lambda l:len(l), ll))
    r = np.zeros((len(ll),size))
    pos = 0
    for i,l in enumerate(ll):
        r[i, pos:pos+len(l)] = l
        pos += len(l)
    return np.array(r)
def in_coll2(vec,ll):                                                            # passage sur une colonne des l_sensi
    size = sum(map(lambda l:len(l), ll))
    r = np.zeros((len(ll),size))
    pos = 0
    for i,l in enumerate(ll):
        r[i, pos:pos+len(l)] = vec[i]
        pos += len(l)
    return np.array(r)

coll_sens = in_coll(l_sens)
coll_XS= in_coll(l_XS)
coll_xs_2_rr= in_coll(l_xs_2_rr)
print(coll_XS.shape,coll_xs_2_rr.shape)
def flatten(xss):
    return [x for xs in xss for x in xs]
print("Coucou")

if not do_GPU:
    # def do_samp():
    #     A_rr=[]
    #     for i in range(data.nb_dosi):   
    #         # print(i)
    #         if i ==0 or len(ll_xv_proj_c[i])!=len(ll_xv_proj_c[i-1]) or any(ll_xv_proj_c[i]!=ll_xv_proj_c[i-1]):
    #             # print(np.shape(ll_xv_proj_c[i]),np.shape(lll_cov[i]))
    #             tmp=np.random.multivariate_normal(ll_xv_proj_c[i],lll_cov[i])
    #             # print(tmp.shape())
    #         A_rr+=[sum(ll_dlet[i]*tmp*data.l_at_den[i]*ll_fv_proj_c[i])]
    #     return np.array(A_rr)
    # l_samp=[]
    # max_val=5000
    # num=0
    # s_time=time.time()
    # print("\rFFT ["+"="*int(round(num/max_val*50))+" "*int(50-round(num/max_val*50))+"] "+str(round(num/max_val*100))+"% ", end='',flush=True)

    # for i in range(max_val):
    #     l_samp+=[do_samp()]
    #     now=time.time()
    #     num+=1
    #     print("\rSampling ["+"="*int(round(num/max_val*50))+" "*int(50-round(num/max_val*50))+"] "+str(round(num/max_val*100))+"% "+str(round(((max_val-num)*(now-s_time)/num)/60)) +" min left", end='',flush=True)

    nb     = data.nb_dosi
    n_samp = 500000
    # 1) identify runs of identical mean/cov as before
    run_starts = [0]
    for i in range(1, nb):
        a, b = ll_xv_proj_c[i], ll_xv_proj_c[i-1]
        if len(a)!=len(b) or not np.array_equal(a, b):
            run_starts.append(i)
    run_starts.append(nb)

    # 2) precompute per‐run: mean, matrix‐sqrt, and stacked factors
    runs = []
    for rs, re in zip(run_starts, run_starts[1:]):
        mean = ll_xv_proj_c[rs]
        cov  = lll_cov[rs]
        # symmetrize and eigendecompose
        # cov = 0.5*(cov + cov.T)
        w, v = np.linalg.eigh(cov)
        # clamp negatives to zero
        if any(w < 0):print("negative eigenvalue found:{}".format(w[w < 0]))
        w[w < 0] = 0
        # build L so that L @ L.T = cov_clamped
        L = v @ np.diag(np.sqrt(w))

        # stack the "factor" vectors for indices rs..re-1
        F = np.stack([
            ll_dlet[i] * data.l_at_den[i] * ll_fv_proj_c[i]
            for i in range(rs, re)
        ], axis=1)  # shape (dim, run_length)

        runs.append((rs, re, mean, L, F))

    # 3) allocate and fill the sample matrix
    l_samp = np.empty((n_samp, nb), float)

    for rs, re, mean, L, F in runs:
        d = mean.shape[0]
        Z = np.random.randn(n_samp, d)   # (5000 × d)
        X = Z.dot(L.T) + mean            # (5000 × d)
        l_samp[:, rs:re] = X.dot(F)     # (5000 × run_length)



else:
    #chat gpt numba ver
    import numba # type: ignore
    from numba import njit # type: ignore
    @njit
    def do_samp(nb_dosi, ll_xv_proj_c, lll_cov, ll_dlet, l_at_den, ll_fv_proj_c):
        A_rr = np.empty(nb_dosi,)

        prev = np.empty(0)
        tmp  = prev  # will be overwritten
        for i in range(nb_dosi):
            cur = ll_xv_proj_c[i]
            # only recompute if shape or contents changed
            if i == 0 or cur.shape[0] != prev.shape[0] or np.any(cur != prev):
                tmp = np.random.multivariate_normal(cur, lll_cov[i])
            A_rr[i] = np.sum(ll_dlet[i] * tmp * l_at_den[i] * ll_fv_proj_c[i])
            prev = cur

        return A_rr

    # 1) convert your Python lists → Numba‐typed Lists
    xv_list = numba.typed.List()
    cov_list = numba.typed.List()
    fv_list = numba.typed.List()
    for m in ll_xv_proj_c:   xv_list.append(m)
    for C in lll_cov:        cov_list.append(C)
    for f in ll_fv_proj_c:   fv_list.append(f)

    # # 2) cast your 1-D numpy arrays to float64 if necessary
    dlet   = numba.typed.List(ll_dlet)
    at_den = numba.typed.List(data.l_at_den)

    # 3) prepare output storage
    max_val = 5000
    nb      = data.nb_dosi
    l_samp  = np.empty((max_val, nb), dtype=np.float64)

    # 4) warm up compilation with a dummy call
    _ = do_samp(nb, xv_list, cov_list, dlet, ll_dlet, fv_list)

    # 5) the actual loop
    for j in range(max_val):
        l_samp[j, :] = do_samp(nb, xv_list, cov_list, dlet, data.l_at_den, fv_list)

    # 6) compute covariance
# cov_rr = np.cov(l_samp, rowvar=False)



#l_rr = sum(ll_dlet[i]*ll_xv_proj_c[i]*l_at_den[i]*ll_fv_proj_c[i])
#l_rrs  = ((coll_sens.T).dot(cat_mat(lll_cov).dot(coll_sens)))**0.5
# cov_rr  = ((coll_sens).dot(cat_mat(lll_cov).dot(coll_sens.T)))
l_samp=np.array(l_samp)
cov_rr  = np.cov(l_samp.T)



print()
print(cov_rr.shape)
# exit()

stddev, cor = cov_to_sig_cor(cov_rr.T)

print (aff_list("l_rr", l_rr))
print (aff_list("stddev", stddev))
print (aff_list("stddev [%]", stddev/l_rr))
print (aff_mat("corr", cor))

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



if not os.path.exists("nducup_out"):
    os.mkdir("nducup_out")


path = "nducup_out/out_"+(data.get_key_for_ndup())
print ("write res in",path)
open(path,"w").write(
    "val      "+" ".join(map(lambda v:str(v),l_rr))+"\n"+
    "stdv     "+" ".join(map(lambda v:str(v),stddev))+"\n"+
    "stdv_rel "+" ".join(map(lambda v:str(v),stddev/l_rr))+"\n"+
    "corr   \n"+"\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(cor)))
)

l_x = np.arange(len(cor)+1)+0.5


#aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(0.75,1.001), pad=None, pcol=True, head_top=True, midgreen=True)
#aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(0.5,1), pad=None, pcol=True, head_top=True, midgreen=True)
aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midblanc=True)

l_tick =[]
for i in range(1,len(cor)):
    if i%5==0: l_tick +=[i]
axmat2.set_ylim(list(reversed(axmat2.get_ylim())))
axmat2.set_yticks(l_tick)



for i in [1,2,3,4]:
    l_ax[0,i].set_xscale("log")
    l_ax[0,i].set_yscale("log")
    
    
toto = False
    
l_ax[0,0].set_xscale("log")

xlims, ylims = get_lim(l_ax[0,2])
l_ax[0,2].set_ylim((ylims[1]/5e3,ylims[1]))
#l_ax[0,2].set_ylim((ylims[1]/5e2,ylims[1]))

xlims, ylims = get_lim(l_ax[0,1])
l_ax[0,1].set_ylim((ylims[1]/1e6,ylims[1]))


set_nice_ax(l_ax[0,0],x="MeV")
if not toto:
    set_nice_ax(axmat,x="MeV",y="MeV")


set_nice_ax(l_ax[0,1], y="pow", powmodulo=(3,0))
set_nice_ax(l_ax[0,4], y="pow", powmodulo=(3,0))


my_sub6_finalise(l_ax, y=False)


therm = min(map(lambda l_ce: l_ce[0],ll_ce)) <0.001
lims = (1e-10 if therm else 0.1, 20)
if toto:
    lims = 0.4, 19.99
if data.nb_dosi == 1:
    axmat.set_xlim(lims)
    axmat.set_ylim(list(reversed(lims)))
for i in [1,2,3,4]:
    l_ax[0,i].set_xlim(lims)
if not therm :
    print("aff - not therm mode")
    for i in [1,2,4]:
        l_ax[0,i].set_yscale("linear")
        set_nice_ax(l_ax[0,i],y="pow")


l_ax[0,4].set_ylabel(r"$\mathrm{XS~[barn]}$", size=get_aff_size("s_xylabel"))
l_ax[0,3].set_ylabel(r"$\mathrm{\sigma_{XS}~[\%]}$", size=get_aff_size("s_xylabel"))
l_ax[0,2].set_ylabel(r"$\mathrm{\phi~[cm/let/n]}$", size=get_aff_size("s_xylabel"))
l_ax[0,1].set_ylabel(r"$\mathrm{RR~[at/let/n]}$", size=get_aff_size("s_xylabel"))
l_ax[0,0].set_ylabel(r"$\mathrm{Norm.}~\int_0^{E} RR \mathrm{d}E$", size=get_aff_size("s_xylabel"))
l_ax[0,0].set_xlabel(r"$\mathrm{Energy}$", size=get_aff_size("s_xylabel"))

print ("save fig")
if save_key !="" : fig.savefig("nducup_out/img_"+save_key.replace("/","+")+".png", bbox_inches=('tight'), dpi=200)
fig.savefig("nducup_out/img.png", bbox_inches=('tight'), dpi=200)
fig.savefig("nducup_out/hist/"+"+".join(lcase_csv)+".png", bbox_inches=('tight'), dpi=200)
compare=True
if compare & do_rm:
    path="~/Link_to_analysis/data/Xs_for_plot/Table_XS_{}_J33.csv".format(lcase_csv[0][3:5].replace("SS","Fe"))
    df=pd.read_csv(path,skiprows=[1,2],header=0,dtype=np.float64,delimiter=";")
    plt.figure(figsize=(16,9))
    ax1=plt.subplot(3,1,1)
    plt.title("Reflector: {}, Dosimeters: {}".format(data.l_compo_plate_full_name[0], data.l_reaction_txt[0]))
    k=len(ll_fv)//2
    # print(df)
    echl_midg  = make_cmap([( 0, 0,220),(40,205,255), (0,200,0), (255,205,40), (220,0, 0 )])
    echl_midg=list(echl_midg(np.linspace(0,1,k)))
    # l_c=lmap(lambda s: echl_midg[int(1024/k*s)],range(k))
    plt.plot(ll_xe[0],ll_xv[0],linestyle="--",label="Dosimetry")
    # for key in df.keys()[1:]:
    #     plt.plot(df[df.keys()[0]]*10e-7,df[key],label=key)
    plt.legend(loc='center right')
    plt.ylabel(r"$\mathrm{Dosimetry~XS ~(barn)}$")
    plt.xlabel(r"$\mathrm{Energy ~(MeV)}$")
    plt.xscale("log")
    plt.yscale("log")
    ax2=plt.subplot(3,1,2)
    ax2.sharex(ax1)
    for i in range(k):
        v1=dup(integ(l_fe,ll_fv[k+i]*ll_xv_proj_f[k+i]))[4:]
        # v2=dup(integ(l_fe,ll_fv[i]*ll_xv_proj_f[i]))[4:]
        plt.plot(dup_piquet(l_fe)[4:],v1/v1[-1],label="dosi_{}".format(i+1),c=echl_midg[i])
    plt.legend(loc='center right',ncol=3)
    plt.title("Normalized Cumulative Reaction Rate")
    plt.ylabel(r"$\mathrm{Norm.}~\int_0^{E} RR \mathrm{d}E$")
    plt.xlabel(r"$\mathrm{Energy~ MeV}$")
    plt.xscale("log")
    ax3=plt.subplot(3,1,3)
    ax3.sharex(ax1)
    l_residual=[]
    for i in range(k):
        v1=dup(integ(l_fe,ll_fv[k+i]*ll_xv_proj_f[k+i]))[4:]
        v2=dup(integ(l_fe,ll_fv[i]*ll_xv_proj_f[i]))[4:]
        v3=dup(integ(l_fe,ll_fs[k+i]*ll_xv_proj_f[k+i],quad=True))[4:]
        v4=dup(integ(l_fe,ll_fs[i]*ll_xv_proj_f[i],quad=True))[4:]
        vs=(v3**2+v4**2)**0.5/v2[-1]*100
        l_residual+=[((v1-v2)/v2[-1]*100)[-1]/vs[-1]]
        plt.plot(dup_piquet(l_fe)[4:],(v1-v2)/v2[-1]*100,label="dosi_{}".format(i+1),c=echl_midg[i])
        plt.fill_between(dup_piquet(l_fe)[4:],(v1-v2)/v2[-1]*100-vs,(v1-v2)/v2[-1]*100+vs,alpha=0.2,color=echl_midg[i])
    lib=data.l_NDlib
    # plt.title("{0} - {1}".format(lib[k].replace("INDEN_12_23_02_24","INDEN") if "Pni" not in data.l_name[0] else lib[k].replace("JEFF4T3","TENDL-23").replace("JEFF4T4","TENDL-24").replace("INDEN_12_23_02_24","INDEN") ,lib[0].replace("INDEN_12_23_02_24","INDEN")))
    plt.title("{0} - {1}".format(lib[k].replace("INDEN_12_23_02_24","JEFF-4.0") if "Pni" not in data.l_name[0] else lib[k].replace("JEFF4T3","JEFF-4.0").replace("JEFF4T4","JEFF-4.0").replace("INDEN_12_23_02_24","JEFF-4.0") ,lib[0].replace("INDEN_12_23_02_24","JEFF-4.0")))
    # plt.legend(loc='center right',ncol=3)
    plt.ylabel(r"$\Delta(\int_0^{E} RR \mathrm{d}E)$ (\%)")
    plt.xlabel(r"$\mathrm{Energy~(MeV)}$")
    plt.xscale("log")
    if "in1" in lcase_csv[0] or "au" in lcase_csv[0]:
        ax1.set_xlim(1e-9,20)
    elif "in2" in lcase_csv[0]:
        ax1.set_xlim(3e-1,20)
    elif "ni_fe" in lcase_csv[0]:
        if "Ni-P" in data.l_name[0]:
            ax1.set_xlim(1,20)
        else:
            ax1.set_xlim(4,20)
    elif "al" in lcase_csv[0]:
        ax1.set_xlim(5,20)
    else:
        ax1.set_xlim(1e-1,20)
    plt.subplots_adjust(hspace=0.4)
    plt.tight_layout()
    print("residuals",l_residual)
    plt.savefig("nducup_out/compare/"+"+".join(lcase_csv)+".png", bbox_inches=('tight'), dpi=300)
    # plt.yscale("log")
# plt.show()




#((sens.T).dot(cov.dot(sens)))**0.5 

#name,keyname,dosi_den = "Au","_0_Au_102_791970", 5.90079E-02  # 1/barn*cm
#name,keyname,dosi_den = "Ni","_1_Ni_103_280580", 6.24027E-02
#name,keyname,dosi_den = "Ti46","_2_Ti_103_220460", 4.68102E-03
#name,keyname,dosi_den = "Ti48","_2_Ti_103_220480", 4.18285E-02
#name,keyname,dosi_den = "Fe54","_3_Fe_103_260540", 4.96293E-03
#name,keyname,dosi_den = "Fe56","_3_Fe_103_260560", 7.79075E-02

