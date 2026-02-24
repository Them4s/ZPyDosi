import gc
import psutil # type: ignore
# from sklearn.covariance import MinCovDet
# print('RAM memory % used:', psutil.virtual_memory()[2])

'''
Compute and save the uncertainties due to PETALE position using multiple data from a set of perturbed simulations
'''

import os
from ZPyDosi.Common.utils_general import lmap, get_aff_size, get_c,  dup, dup_piquet,set_nice_ax
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.Prints.PrintnSave import aff_list, aff_mat
from ZPyDosi.Plots.SubPlots import my_sub6, my_sub6_finalise, get_lim
from ZPyDosi.Plots.MatrixPlots import aff_mat4
from ZPyDosi.Stats.Stats import icovar_jkk, icovar_jkk_w_nan, imoyvar, cov_to_sig_cor
from ZPyDosi.XSnFlux.GetIRDFF import get_irdff_iaea
from ZPyDosi.XSnFlux.Projections import projet_vec_intervals_from_continus
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import time
# print('RAM memory % used:', psutil.virtual_memory()[2])

def array32(mat):
    return np.array(mat,dtype=np.float16)

def kick_outliers(mat): # Look into the matrix of uncertainties if there are unconverged data
    mat=np.array(mat).T
    new_mat=np.zeros(mat.shape)
    for i in range(len(mat)) :
       for j in range(len(mat[i])) :
           if not np.isnan(mat[i][j]):
               idx=[k!=j for k in range(len(mat[i]))]
               tmp_var_w=np.var(mat[i])
               tmp_var=np.var(mat[i][idx])
               tmp_val=np.mean(mat[i][idx])
               if tmp_var_w/tmp_var>1.4:
                   new_mat[i][j]=np.nan
               else:
                   new_mat[i][j]=mat[i][j]
           else:
               new_mat[i][j]=np.nan
    return new_mat.T
def len_w_nan(mat):
    mat=np.array(mat).T
    length=[]
    for line in mat:
        length += [len([x for x in line if x != 'nan'])]
    return length

'''
# covar with minimal covariance determinant
def icovar_jkk_MCD(l_l_v, l_w=None, do_cor=False, do_jackknife=False, fast_jackknife=False, blabla=False, nb_jkk=None, fast=True):
    t0 = time.time()
    err = 1e-50
    if l_w:
        print("l_w not implemented in icovar_jkk_w_nan yet, exit")
        exit()
    l_l_v = np.array(l_l_v)
    cov = MinCovDet(support_fraction=1).fit(l_l_v).covariance_
    moy = np.nanmean(l_l_v,axis=0)
    t1 = time.time()
    if do_cor:
        cor = cov*1.
        stddev = np.sqrt(np.diag(cov))
        cor /= (stddev[:, None]+err)
        cor /= (stddev[None, :]+err)
    t2 = time.time()
    if do_jackknife:
        if l_w is not None and sum(l_w) != len(l_w):
            new_l_l_v = []
            # for i in range(len(l_w)):
                # if rand()<l_w[i]:
                    # new_l_l_v += [l_l_v[i]]
            # l_l_v = np.array(new_l_l_v)
            # print("only",len(l_l_v),"remainings")
            # l_w = None
            # loc_cov = np.cov(l_l_v.T, aweights=l_w)/
        else:
            loc_cov = cov
            loc_moy = moy
            if do_cor:
                loc_cor = cor
            
        if nb_jkk is None: nb_jkk = len(l_l_v)
        if nb_jkk > len(l_l_v): nb_jkk = len(l_l_v)
        def moy_without(idx):
            if not fast_jackknife:
                return icovar_jkk_MCD(l_l_v[np.arange(len(l_l_v))!=idx])
            else:
                print("fast_jkk not allowed")
                exit()
            
                tmp_cov = loc_cov*1.
                if not fast:
                    for i in range(len(tmp_cov)):
                        #tmp_cov[i,:] = (tmp_cov[i,:] * len(l_l_v) - (l_l_v[idx][i]-moy[i])*(l_l_v[idx][:]-moy[:])) / (len(l_l_v)-1)
                        for j in range(len(tmp_cov)):
                            tmp_cov[i,j] = (tmp_cov[i,j] * len(l_l_v) - (l_l_v[idx][i]-loc_moy[i])*(l_l_v[idx][j]-loc_moy[j])) / (len(l_l_v)-1)
                else:
                    #tmp_cov[:,:] = (tmp_cov[:,:] * len(l_l_v) - (l_l_v[idx][:,None]-moy[:,None])*(l_l_v[idx][None,:]-moy[None,:])) / (len(l_l_v)-1)
                    tmp_cov = (tmp_cov * len(l_l_v) - (l_l_v[idx][:,None]-loc_moy[:,None])*(l_l_v[idx][None,:]-loc_moy[None,:])) / (len(l_l_v)-1)
                return tmp_cov
            
        def moy_without_cor(idx):
            tmp_cor = moy_without(idx)
            tmp_stddev = np.sqrt(np.diag(tmp_cor)+err)
            tmp_cor /= (tmp_stddev[:, None]+err)
            tmp_cor /= (tmp_stddev[None, :]+err)
            return tmp_cor
        l_jkk = list(range(len(l_l_v)))
        while len(l_jkk) > nb_jkk: l_jkk.pop(int(rand()*len(l_jkk)))
        jackknife_cov_var = np.sum((moy_without(i)-loc_cov)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        #jackknife_cov_var = np.sum((dmoy_without(i))**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        if do_cor:
            jackknife_cor_var = np.sum((moy_without_cor(i)-loc_cor)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
    t3 = time.time()
    #print t3-t2
    if not do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s")
        return cov
    if do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s")
        return cov, cor
    if not do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and jkk in",t3-t2,"s")
        return cov, jackknife_cov_var**0.5
    if do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s and jkk in",t3-t2,"s")
        return cov, cor, jackknife_cov_var**0.5, jackknife_cor_var**0.5
    print("icovar_jkk_w_nan - error")
    exit()
'''




print ("#"*50)
path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv  = get_param_vari("lcase", str).split("/")
do_rm  = get_param_vari("do_rm", bool,"False")
low_mem  = get_param_vari("low_mem", bool,"False") #in case not enough ram
plot_jolimat  = get_param_vari("jolimat", bool,"False")
gr_order = get_param_vari("gr_order", int,2) # to gain ram by decreasing the spectral resolution
do_print = get_param_vari("do_print", bool,"False") # prints intermediate command lines
redo=get_param_vari("redo",bool,"False") 

data = DataIrrad(path_csv_data, path_csv_dosi, lcase_csv, load_ndup_nuis_tosuppress=False, load_up_pos_tosuppress=True, load_sss_results=False, load_sss_spectrum=False,group_order=gr_order, remove_data=do_rm)
print ("#"*50)

path = "up_pos_out/out_"+(data.get_key_for_up_pos())

if (not redo) and os.path.isfile(path):
    print("up_pos data already exist")
    exit()

verif=True
nb_dosi = data.nb_dosi

d_pathidnro2pathpos = {}
d_pathpos2id = {}
id = 0
print('RAM memory % used:', psutil.virtual_memory()[2])

d_reac={
    "280580":{"103":"$^{58}$Ni(n,p)$^{58}$Co" },
    "260560":{"103":"$^{55}$Fe(n,p)$^{56}$Mn" },
    "260540":{"103":"$^{54}$Fe(n,p)$^{54}$Mn" },
    "491150":{"102":"$^{115}$In(n,g)$^{116}$In","11004":"$^{115}$In(n,n')$^{115}$In","51":"$^{115}$In(n,n')$^{115}$In" },
    "791970":{"102":"$^{197}$Au(n,g)$^{198}$Au" },
    "130270":{"107":"$^{27}$Al(n,a)$^{24}$Na" }}

#ll_vtot = [[] for i in range(nb_rand)]
l_path_todo = []
l_pathpos = []
add_all=False
for idosi in range(nb_dosi):
    path = data.l_sss_path_pos[idosi]
    lpos  = data.l_sss_pos_pos[idosi]
    if "C" in lpos: 
        print("Warning : no value for core Center, took ALL instead") 
        add_all=True
    if path not in l_path_todo:
        l_path_todo += [path]
        for ipos, pos in enumerate(lpos.split("/")):
            #if (path, pos) not in d_pathpos2id:
            d_pathidnro2pathpos[(path, ipos, id)] = (path, pos)
            d_pathpos2id[(path, pos)] = id
            l_pathpos += [(path, pos)]
            id += 1

# d_pathpos2pathidnro = {v: k for k, v in d_pathidnro2pathpos.items()}
# d_id2pathpos = {v: k for k, v in d_pathpos2id.items()}

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
print('RAM memory % used:', psutil.virtual_memory()[2])


nb_rand = 10 # todo : chzercher le nombre de calcul utilisable
# while(os.path.isdir(l_path_todo[0]+ str(nb_rand+1))):
#      nb_rand += 1

ll_vtot   = []
ll_srel   = []
ll_rr2   = []
ll_rr2_s   = []
ll_rr_nice   = []
ll_rr_s_nice   = []
processes = []
for irand in range(nb_rand):
    l_vtot = []
    l_srel = []
    l_rr2 = []
    l_rr2_s = []

    for path_todo in l_path_todo:
        path = path_todo + str(irand+1)+"/input"+"_mat_sss_2_of/perspectra"
        # print(path)r
        # exit()
        bash_cmd="python3.10 /home/thomasligonnet/Link_to_analysis/python/Misc/reaction_rate_projector_up_pos.py input="+path_todo + str(irand+1)+"/input save_key=up_pos_out/num{}".format(irand+1)+(data.get_key_for_up_pos()) + " save_mat="+"_".join(lcase_csv[0].split("_")[1:] ) + " add_all={}".format(add_all) + " path_xsdata={}".format(data.path_xsdata) + " path_irdff_folder={}".format(data.path_iaea_data)
        processes  += [subprocess.Popen(bash_cmd.replace("&","").split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8', preexec_fn=os.setsid)]
        # process = subprocess.Popen(bash_cmd.replace("&","").split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8', preexec_fn=os.setsid)
        # process.wait()

        if do_print: print(bash_cmd)
        # exit()
        if np.mod(irand+1,20)==0 or (irand+1)==nb_rand:
            print("waiting for processeses")
            # print(processes[0].communicate())
            processes[-1].wait()
            processes = []
            
        dim = lmap(lambda s:int(s),open(path).readlines()[0].split())    # get data shape
        nb_pos, nb_per, nb_nrj = dim
        nb_nrj=int(nb_nrj/2**gr_order)
        #specdata       = np.array(lmap(lambda s:float(s), " ".join(open(path       ).readlines()[1:]).split())).reshape(dim)
        #specdata_sig   = np.array(lmap(lambda s:float(s), " ".join(open(path+"_sig").readlines()[1:]).split())).reshape(dim)
        dleth = (np.log(20.)-np.log(1e-10))/(nb_nrj/(2**gr_order))
        specdata       = np.reshape(lmap(lambda lv: sum(lv),np.reshape(lmap(lambda v:float(v)/dleth, " ".join(open(path       ).readlines()[1:]).split()),(-1,2**gr_order))),(nb_pos, nb_per,nb_nrj))
        specdata_sig   = np.reshape(lmap(lambda lv: sum(lv),np.reshape(lmap(lambda v:float(v)/dleth, " ".join(open(path+"_sig").readlines()[1:]).split()),(-1,2**gr_order))),(nb_pos, nb_per,nb_nrj))
        #print(specdata.shape)
        print(specdata.shape)
        #exit()
        #load rr
        path = path_todo + str(irand+1)+"/input_mat_sss_2_of/rr_vec"
        tmp_rr       = lmap(lambda s:float(s.split()[0]), (open(path       ).readlines()[1:]))
        tmp_rr_s     = lmap(lambda s:float(s.split()[0]), (open(path+"_sig").readlines()[1:]))
        for ipos in range(nb_pos):
            for iper in range(1):
                l_v, l_s  = specdata[ipos, iper, :], specdata_sig[ipos, iper, :]
                #d_pos_2_ll_v[d_nro2pos[ipos]] += [l_v]
            l_vtot += list(l_v)
            l_srel += list(l_s / (l_v+1e-15)) # +1e-15 to avoid divide by 0
        l_rr2   += tmp_rr
        l_rr2_s   += tmp_rr_s
    ll_vtot += [l_vtot]
    ll_srel += [l_srel]
    ll_rr2   += [l_rr2]
    ll_rr2_s   += [l_rr2_s]

time.sleep(10) # to avoid the script going to fast
# print("Some times it goes \"FileNotFoundError: [Errno 2] No such file or directory: 'up_pos_out/tmp22d7118a157f8e9defbc4ca0f536468faa'\", just relaunch")

for irand in range(nb_rand):
    for path_todo in l_path_todo:
        print(irand)
        path = "up_pos_out/num{}".format(irand+1)+(data.get_key_for_up_pos())
        # if do_rm:
        ll_rr_s_nice += [lmap(lambda s:float(s), open(path       ).readlines()[2].split()[1:])]
        ll_rr_nice += [lmap(lambda s:float(s), open(path       ).readlines()[0].split()[1:])]
        # else: #in case of missing dosimeters
            # tmp_rr_s_nice = [lmap(lambda s:float(s), open(path       ).readlines()[2].split())]
            # tmp_rr_nice   = [lmap(lambda s:float(s), open(path       ).readlines()[0].split())]
            # tmp2_rr_s     = []
            # tmp2_rr       = []
            # for pos in data.l_pos_name:
                # if "P" in pos:
                # tmp2_rr_s += [tmp_rr_s_nice[int(pos[1])]]
                # tmp2_rr   += [tmp_rr_nice[int(pos[1])]]
            # ll_rr_s_nice += [tmp2_rr_s]
            # ll_rr_nice   += [tmp2_rr  ]
        os.remove(path)
#    print(l_vtot)
#    exit()
print(ll_rr2_s[0])
ll_srel = np.array(ll_srel)
l_rr_nice=imoyvar(ll_rr_nice,do_jackknife=False)[0]
l_srel_ave = np.mean(ll_srel, axis=0)




cov_nice, corr_nice, cov_nice_jkk, corr_nice_jkk = icovar_jkk(ll_rr_nice, l_w=None, do_cor=True, do_jackknife=True, fast_jackknife=True, blabla=False, nb_jkk=None, fast=True)



stddev_nice=cov_to_sig_cor(cov_nice)[0] 

#print(ll_srel)
#print(l_srel_ave)
#exit()
E1,E2 = 1e-10, 20.
l_nrj_piquet = 10**(((np.log10(E2)-np.log10(E1)) * np.array(range(nb_nrj+1))*1./(nb_nrj  )) + np.log10(E1))
l_nrj        = (l_nrj_piquet[1:] + l_nrj_piquet[:-1])/2

print('RAM memory % used:', psutil.virtual_memory()[2])
d_pos_2_cov = {}
d_pos_2_std = {}
d_pos_2_std_ave = {}
d_pos_2_ave = {}
d_pos_2_stat = {}
cov_tot = icovar_jkk(ll_vtot, l_w=None, do_cor=False, do_jackknife=False, fast_jackknife=True, blabla=False, nb_jkk=None, fast=True)
cov_tot =np.array(cov_tot,dtype=np.float32)
diag_cov_tot=np.diag(cov_tot)
# cov_tot, jkk_cov = icovar_jkk(ll_vtot, l_w=None, do_cor=False, do_jackknife=True, fast_jackknife=True, blabla=False, nb_jkk=None, fast=True)
# moy, std, std_std = imoyvar(ll_vtot,do_jackknife=True)
moy, std = imoyvar(ll_vtot,do_jackknife=False)
moy_std, std_std = imoyvar(np.multiply(ll_vtot,ll_srel),do_jackknife=False)
print(cov_tot.nbytes)
print('RAM memory % used:', psutil.virtual_memory()[2])

#for path_todo in l_path_todo:
for ipathposi, pathposi in enumerate(l_pathpos):
    #for ipos in range(nb_pos):
    #    keyi = d_nro2pos[ipos]
    #    for jpos in range(nb_pos):
    for ipathposj, pathposj in enumerate(l_pathpos):
            #keyj = d_nro2pos[jpos]
            keyi, keyj =  pathposi,  pathposj
            ipos, jpos = ipathposi, ipathposj
            d_pos_2_cov[(keyi, keyj)] = cov_tot[nb_nrj*ipos: nb_nrj*(ipos+1), nb_nrj*jpos: nb_nrj*(jpos+1)]
            if ipos==jpos:
                d_pos_2_std[keyi        ] = std[nb_nrj*ipos: nb_nrj*(ipos+1)]
                d_pos_2_std_ave[keyi        ] = moy_std[nb_nrj*ipos: nb_nrj*(ipos+1)]
                d_pos_2_ave[keyi        ] = moy[nb_nrj*ipos: nb_nrj*(ipos+1)]
    d_pos_2_stat[keyi] = l_srel_ave[nb_nrj*ipos: nb_nrj*(ipos+1)]
del(cov_tot)
gc.collect()
#fig = plt.figure(1, figsize=(10,12))
figsup = plt.figure(0, figsize=(9,12))
axmatsup = plt.subplot(1,1,1)


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
ll_fvs_bin  = []
ll_fs_bin  = []
ll_xv_c0   = []
ll_xe_c0   = []
#l_srel_ave_dosi = []
l_fe_bin = list(l_nrj_piquet)
print('RAM memory % used:', psutil.virtual_memory()[2])
if not low_mem:
    lll_cov = np.zeros(((len(l_fe_bin)-1) * nb_dosi, (len(l_fe_bin)-1) * nb_dosi),dtype=np.float32)
    
    for idosi in range(data.nb_dosi):
        print(data.l_key_irdff_iaea[idosi])
        idata_irdff = get_irdff_iaea(os.path.expandvars(data.path_iaea_data+"/"+data.l_key_irdff_iaea[idosi]), e_min = None)
        # get_irdff_iaea -> (l_cor_e, cor), (l_xs_e,l_xs_v,l_xs_s)
        #ll_ce   += [list(l_nrj_piquet)]                            # ori : [idata_irdff[0][0]] irdff cov nrj (bin)     new : phi cov nrj (bin)
        #lll_fc_bin += [list(d_pos_2_cov[data.l_up_pos_name[idosi]])]   # ori : [idata_irdff[0][1]] irdff cov val (bin)     new : phi cov val (bin)
        #ll_xe      += [list(l_nrj_piquet)]                         # ori : [idata_irdff[1][0]] irdff xs  nrj (c0)      new : phi ave nrj (bin)
        
        ll_fv_bin  += [list(d_pos_2_ave[(data.l_sss_path_pos[idosi], data.l_up_pos_name[idosi])])]   # ori : [idata_irdff[1][1]] irdff xs  val (c0)      new : phi ave val (bin)
        ll_fs_bin  += [list(d_pos_2_std[(data.l_sss_path_pos[idosi], data.l_up_pos_name[idosi])])]   # ori : [idata_irdff[1][1]] irdff xs  val (c0)      new : phi ave val (bin)
        ll_fvs_bin  += [list(d_pos_2_std_ave[(data.l_sss_path_pos[idosi], data.l_up_pos_name[idosi])])]   # ori : [idata_irdff[1][1]] irdff xs  val (c0)      new : phi ave val (bin)
        #ll_xs      += [list(d_pos_2_std[data.l_up_pos_name[idosi]])]  # ori : [idata_irdff[1][2]] irdff xs  sig (c0)      new : phi ave sig (bin)
        #print(idosi, data.l_up_pos_name[idosi], len(idata_irdff[0][0]), len(idata_irdff[0][1]), len(idata_irdff[1][0]), len(idata_irdff[1][1]))
        
        ll_xv_c0 += [idata_irdff[1][1]] # ori : list(data.ll_fv) dosi phi val (bin)  new : irdff xs  (c0)
        ll_xe_c0 += [idata_irdff[1][0]] # ori : list(data.l_fe)  dosi phi nrj (bin)  new : irdff nrj (c0)
        #print("a", len(ll_xe_c0[-1]), len(ll_xv_c0[-1]), data.l_key_irdff_iaea[idosi])
        #ll_fs += # ori : list(data.ll_fs) dosi phi sig
        pos1 = (len(l_fe_bin)-1)* idosi
        pos2 = (len(l_fe_bin)-1)*(idosi+1)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        lll_cov[nb_nrj*idosi: nb_nrj*(idosi+1), nb_nrj*idosi: nb_nrj*(idosi+1)] = d_pos_2_cov[((data.l_sss_path_pos[idosi], data.l_up_pos_name[idosi]), (data.l_sss_path_pos[idosi], data.l_up_pos_name[idosi]))]
        for jdosi in range(data.nb_dosi)[idosi+1:]:
            lll_cov[nb_nrj*idosi: nb_nrj*(idosi+1), nb_nrj*jdosi: nb_nrj*(jdosi+1)] = d_pos_2_cov[((data.l_sss_path_pos[idosi], data.l_up_pos_name[idosi]), (data.l_sss_path_pos[jdosi], data.l_up_pos_name[jdosi]))]
            lll_cov[nb_nrj*jdosi: nb_nrj*(jdosi+1), nb_nrj*idosi: nb_nrj*(idosi+1)] = d_pos_2_cov[((data.l_sss_path_pos[idosi], data.l_up_pos_name[idosi]), (data.l_sss_path_pos[jdosi], data.l_up_pos_name[jdosi]))].T
        print('RAM memory % used:', psutil.virtual_memory()[2])
        # exit()
        #l_srel_ave_dosi += list(l_srel_ave[nb_nrj*idosi: nb_nrj*(idosi+1)])
    del(d_pos_2_cov)
    
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
    print('RAM memory % used:', psutil.virtual_memory()[2])
    
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
        ll_rr = []
        for i in range(nb_dosi):
            suc_x = l_xv_bin[nb_nrj*i: nb_nrj*(i+1)]
            l_rr = []
            for l_vtot in ll_vtot:
                id = l_pathpos.index((data.l_sss_path_pos[i], data.l_up_pos_name[i]))
                sub_f = l_vtot[nb_nrj*(id): nb_nrj*(id+1)]
                l_rr += [sum(np.array(sub_f)*np.array(suc_x))]
            ll_rr += [l_rr]
            print(nb_nrj*(i+1), nb_nrj*(i+2))
            print(suc_x[:10])
            print(sub_f[:10])
        check = ""
        if len(ll_rr)>1:
            check_cov, check_cor, check_cov_jkk, check_cor_jkk  = icovar_jkk(np.array(ll_rr).T, l_w=None, do_cor=True, do_jackknife=True, fast_jackknife=False, blabla=False, nb_jkk=None, fast=False)
            print("#", np.diag(check_cov)**0.5 / np.array(lmap(lambda l_rr: np.average(l_rr), ll_rr)))
            print("#", check_cor)
    
            check += aff_list("chk_stdv_rel [%]", np.diag(check_cov)**0.5 / np.array(lmap(lambda l_rr: np.average(l_rr), ll_rr)) * 100)+"\n"
            check += aff_mat("chk corr", check_cor)+"\n"
        print("# end check")
    #exit()
    print('RAM memory % used:', psutil.virtual_memory()[2])
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
    #Currently too expensive in memory so commented
    if plot_jolimat:
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
    
    print('RAM memory % used:', psutil.virtual_memory()[2])
    
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
    
    print('RAM memory % used:', psutil.virtual_memory()[2])
    #exit()     
            
    
    
    l_integ_1ev = []
    l_integ_tot = []
    
    for i in range(nb_dosi):                                                # some plots
        c = get_c(i, nb_dosi)
        l_ax[0,-3].plot(dup_piquet(l_fe_bin), dup(ll_fv_bin[i]),c=c,linewidth=1)
    
        std_rel = np.array(ll_fs_bin[i])/(np.array(ll_fv_bin[i])+1e-15)
        l_rsd_stat = d_pos_2_stat[(data.l_sss_path_pos[i], data.l_up_pos_name[i])]
        print(nb_dosi, len(std_rel), len(l_rsd_stat))
        l_ax[0,-2].plot(dup_piquet(l_fe_bin), dup(std_rel)*100,c=c,linewidth=1)
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
    
    print(ll_dlet[0][0])
    l_rr, l_rrs = np.zeros(len(ll_fv_bin)), np.zeros(len(ll_fv_bin))
    l_sens = []
    for i in range(data.nb_dosi):                                               # calcul de sensi&RR
        #sens = ll_dlet[i]*ll_fv_bin[i]*data.l_at_den[i]                      # sensitivity          TODOTODOTODO f->x
        # sens = ll_dlet[i]*ll_xv_bin[i]*data.l_at_den[i]                      # sensitivity
        sens = ll_xv_bin[i]*data.l_at_den[i]                      # sensitivity
        l_sens += [sens]
        # rr   = sum(ll_dlet[i]*ll_xv_bin[i]*data.l_at_den[i]*ll_fv_bin[i]) # reaction rate
        rr   = sum(ll_xv_bin[i]*data.l_at_den[i]*ll_fv_bin[i]) # reaction rate
        rrs   = sum((ll_xv_bin[i]*data.l_at_den[i]*ll_fvs_bin[i])**2)**0.5 # reaction rate
        l_rr[i] = rr
        l_rrs[i] = rrs
    
    def in_coll(ll):                                                            # passage sur une colonne des l_sensi
        size = sum(map(lambda l:len(l), ll))
        r = np.zeros((len(ll),size))
        pos = 0
        for i,l in enumerate(ll):
            r[i, pos:pos+len(l)] = l
            pos += len(l)
        return np.array(r)
    
    
    print('RAM memory % used:', psutil.virtual_memory()[2])
    print(lll_cov.nbytes)
    print(lll_cov.shape)
    
    coll_sens = in_coll(l_sens)
    coll_sens =np.array(coll_sens,dtype=np.float32)
    
    #l_rr = sum(ll_dlet[i]*ll_xv_proj_c[i]*l_at_den[i]*ll_fv_proj_c[i])
    #l_rrs  = ((coll_sens.T).dot(cat_mat(lll_cov).dot(coll_sens)))**0.5
    #cov_rr  = ((coll_sens).dot(cat_mat(lll_cov).dot(coll_sens.T)))
    cov_rr  = ((coll_sens).dot(lll_cov.dot(coll_sens.T)))
    
    stddev, cor = cov_to_sig_cor(cov_rr)
    
    print('RAM memory % used:', psutil.virtual_memory()[2])
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
    
    
    print('RAM memory % used:', psutil.virtual_memory()[2])
    if not os.path.exists("up_pos_out"):
        os.mkdir("up_pos_out")
    
    
    path = "up_pos_out/out_"+(data.get_key_for_up_pos())
    print ("write res in",path)
    open(path,"w").write(
        "val      "+" ".join(map(lambda v:str(v),l_rr))+"\n"+
        "stdv     "+" ".join(map(lambda v:str(v),stddev))+"\n"+
        "stdv_rel "+" ".join(map(lambda v:str(v),stddev/l_rr))+"\n"+
        "corr   \n"+"\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(cor)))
    )
    print("rappel check:")
    print(check)
    print
else :
    path = "up_pos_out/out_"+(data.get_key_for_up_pos())
    print ("write res in",path)
    open(path,"w").write(
        "val      "+" ".join(map(lambda v:str(v),l_rr_nice))+"\n"+
        "stdv     "+" ".join(map(lambda v:str(v),stddev_nice))+"\n"+
        "stdv_rel "+" ".join(map(lambda v:str(v),np.divide(stddev_nice,l_rr_nice)))+"\n"+
        "corr   \n"+"\n".join(map(lambda l: " ".join(map(lambda v:str(v),l)), list(corr_nice))))


if low_mem:
  corr_w_std=np.ones(corr_nice.shape)
  for (m,n),label in np.ndenumerate(corr_nice):
    if n>m: corr_w_std[m][n]=label
  for (m,n),label in np.ndenumerate(corr_nice_jkk):
    if n<m: corr_w_std[m][n]=label
else:   
  corr_w_std=np.ones(check_cor.shape)
  for (m,n),label in np.ndenumerate(check_cor):
    if n>m: corr_w_std[m][n]=label
  for (m,n),label in np.ndenumerate(check_cor_jkk):
    if n<m: corr_w_std[m][n]=label
    
l_x = np.arange(len(cor)+1)+0.5 if not low_mem else np.arange(len(corr_w_std)+1)+0.5


#aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(0.75,1.001), pad=None, pcol=True, head_top=True, midgreen=True)
#aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(0.5,1), pad=None, pcol=True, head_top=True, midgreen=True)
#aff_mat4(l_x, l_x, cor, axmat2, "horizontal", "", "Dosimeter number", "Dosimeter number", minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midgreen=True)
aff_mat4(l_x, l_x, check_cor, axmat2, "horizontal", r"Uncertainties  \ooalign{{$\longleftrightarrow$}\cr\hfil{$\backslash$}\hfil}  Correlations", "Dosimeter number", "Dosimeter number", minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midgreen=False, midblanc=True)
# aff_mat4(l_x, l_x, check_cor, axmatsup, "horizontal", r"Uncertainties  \ooalign{{$\longleftrightarrow$}\cr\hfil{$\backslash$}\hfil}  Correlations", "Dosimeter number", "Dosimeter number",cov=check_cor_jkk, minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midgreen=False, midblanc=True)
aff_mat4(l_x, l_x, check_cor, axmatsup, "horizontal", "", "Dosimeter number", "Dosimeter number",cov=check_cor_jkk, minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midgreen=True)
axmat2.set_ylim(list(reversed(axmat2.get_ylim())))
axmatsup.set_ylim(list(reversed(axmatsup.get_ylim())))
if not low_mem:
    
    
    
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
        

    print('RAM memory % used:', psutil.virtual_memory()[2])
    
    
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
    l_ax[0,2].set_ylabel(r"$\mathrm{\phi~[cm/let/n]}$", size=get_aff_size("s_xylabel"))
    l_ax[0,1].set_ylabel(r"$\mathrm{RR~[at/let/n]}$", size=get_aff_size("s_xylabel"))
    l_ax[0,0].set_ylabel(r"$\mathrm{Norm.}~\int_0^{E} RR \mathrm{d}E$", size=get_aff_size("s_xylabel"))
    l_ax[0,0].set_xlabel(r"$\mathrm{Energy}$", size=get_aff_size("s_xylabel"))
    l_ax[0,1].set_xticklabels([])
    l_ax[0,2].set_xticklabels([])
    l_ax[0,3].set_xticklabels([])
    l_ax[0,4].set_xticklabels([])
print('RAM memory % used:', psutil.virtual_memory()[2])
print("WARNING - script developpe de facon a ce que fonnctionnel si plusieurs sss_path_nduc utilises (pour PETALE) mais non teste sur ce point. A faire avec les 'check' inclus")
print ("save fig")
fig.savefig("up_pos_out/img.png", bbox_inches=('tight'), dpi=200)

if not low_mem and len(lcase_csv)<2:
    print(stddev)
    print(stddev/l_rr)
    #print(np.mean(ll_rr2_s,axis=0)) # not interesting
    #print( np.var(ll_rr2_s,axis=0)**0.5)
    #print(np.var(ll_rr2_s,axis=0)**0.5/np.mean(ll_rr2_s,axis=0))
    # print(100*(stddev/np.mean(ll_rr2_s)-1))
    
    if len(np.mean(ll_rr_s_nice,axis=0))==len(stddev):
        fig3=plt.figure(3)
        a_rr=np.array(lmap(lambda l_rr: np.average(l_rr), ll_rr))
        for i in range(int(len(stddev)/9)):
            plt.errorbar(range(1,10),(np.diag(check_cov)**0.5/a_rr)[0+i*9:9+i*9]*100,(np.diag(check_cov_jkk)/np.diag(check_cov)**0.5/a_rr/2)[0+i*9:9+i*9]*100,label="tot "+d_reac[data.l_iso[i*9]][data.l_mt[i*9]],linestyle="",marker=".",markersize=8)
            plt.plot(range(1,10),np.mean(ll_rr_s_nice,axis=0)[0+i*9:9+i*9]*100,label="stat "+d_reac[data.l_iso[i*9]][data.l_mt[i*9]],linestyle="",marker=".",markersize=8)
        plt.grid(which="both")
        plt.xlabel("Dosimeter position")
        plt.ylabel("RSD [\%]")
        plt.legend()
        fig3.savefig("up_pos_out/std_comp_"+lcase_csv[0]+".png",dpi=200)
    
    print(l_rr)
    print(np.mean(ll_rr2,axis=0))
    # print(l_rr[5:14]/np.mean(ll_rr2,axis=0))# print(std_std/(std+1e-15))
    # print(((stddev/l_rr)[5:14]/np.mean(np.divide(ll_rr2_s,ll_rr2),axis=0)-1)*100)# print(std_std/(std+1e-15))
    #print(len(l_rr),len(stddev))
    #print(((stddev/l_rr)[5:14]/(l_rrs/l_rr[5:14])-1)*100)# print(std_std/(std+1e-15))
    
    
    print("with rr_nice")
    # print(np.diag(jkk_cov)/np.diag(cov_tot))
    print('RAM memory % used:', psutil.virtual_memory()[2])
    
    
    
    print( ll_rr_s_nice)
    print( np.mean(ll_rr_s_nice,axis=0))
    print( np.var(ll_rr_s_nice,ddof=1,axis=0)**0.5)
    print( np.var(ll_rr_s_nice,ddof=1,axis=0)**0.5/np.mean(ll_rr_s_nice,axis=0)*100)
    print(len(ll_rr_s_nice),len(stddev))
    if len(stddev)==len(np.mean(ll_rr_s_nice,axis=0)):
        print(((stddev/l_rr)/(np.mean(ll_rr_s_nice,axis=0))-1)*100)# print(std_std/(std+1e-15))
    #((sens.T).dot(cov.dot(sens)))**0.5
    
    print("#"*50)
    print("relative std on var")
    print(np.diag(check_cov_jkk/check_cov)*100)
    print((np.diag(check_cov_jkk**2/check_cov**2)/4)**0.5*100)
    print("#"*50)
    
    print("corr comp")
    print(corr_nice)
    # print((np.divide(corr_nice,cor)-1)*100)
    # print((np.divide(cov_nice,cov_rr)-1)*100)
    # print((np.divide(l_rr_nice,l_rr)-1)*100)
    # print((np.divide(stddev_nice,stddev)-1)*100)
    
    print()
    #print("test cov using IVW") 
    #print( cov_to_sig_cor(np.cov(ll_rr_s_nice,ddof=1,aweights=1/np.square(ll_rr_s_nice)))[0])
    #print( cov_to_sig_cor(np.cov(ll_rr_s_nice,ddof=1,aweights=1/np.square(ll_rr_s_nice)))[0]/np.mean(ll_rr_s_nice,axis=0)*100)
    
    print()
    
    print("test kick_outliers")
    print(kick_outliers(ll_rr_s_nice).tolist())
    print(np.cov(kick_outliers(ll_rr_s_nice)))
    print(icovar_jkk(kick_outliers(ll_rr_s_nice), l_w=None, do_cor=False, do_jackknife=False, fast_jackknife=True, blabla=False, nb_jkk=None, fast=True))
    cov_ma=(np.ma.cov(np.ma.masked_invalid(kick_outliers(ll_rr_s_nice)),rowvar=False).tolist())
    print(cov_ma)
    print(np.diag(cov_ma)**0.5)
    print(cov_to_sig_cor(np.array(cov_ma,dtype=np.float64))[1])
    cov_std_stat,cor_std_stat, cov_std_stat_s, cor_std_stat_s= icovar_jkk_w_nan(kick_outliers(ll_rr_s_nice),do_cor=True,do_jackknife=True)
    print(cov_std_stat/cov_ma-1)
    print(cor_std_stat/cov_to_sig_cor(np.array(cov_ma,dtype=np.float64))[1]-1)
    print(cor_std_stat_s)
    fig2=plt.figure(figsize=(8,12))
    axcor=plt.subplot(2,2,3)
    
    corr2_w_std=np.ones(cor_std_stat.shape)
    for (m,n),label in np.ndenumerate(cor_std_stat):
        if n>m: corr2_w_std[m][n]=label
    for (m,n),label in np.ndenumerate(cor_std_stat_s):
        if n<m: corr2_w_std[m][n]=label
    # aff_mat4(l_x, l_x, corr2_w_std, axcor, "horizontal", r"Uncertainties  \ooalign{{$\longleftrightarrow$}\cr\hfil{$\backslash$}\hfil}  Correlations", "Dosimeter number", "Dosimeter number", minimaxi=(-1,1), pad=None, pcol=True, head_top=True, midblanc=True)
    axcor.set_ylim(list(reversed(axcor.get_ylim())))
    fig2.savefig("up_pos_out/img_corr_stat.png", bbox_inches=('tight'), dpi=200)
    cov_var_stat=icovar_jkk_w_nan(kick_outliers(np.multiply(ll_rr_s_nice,l_rr_nice)**2))
    
    cov_pos=cov_nice-np.diag(np.multiply(np.nanmean(kick_outliers(ll_rr_s_nice),axis=0),l_rr_nice)**2) # a debug ici
    # pos_std_std=(np.diag(cov_nice_jkk)**2 + np.diag(cov_var_stat))**0.5
    pos_std_std=(np.diag(cov_nice_jkk)**2 + np.divide(np.diag(cov_var_stat),len_w_nan(kick_outliers(ll_rr_s_nice))))**0.5
    print("pos only cov")
    print(cov_pos)
    print(np.diag(cov_pos)**0.5/l_rr_nice*100)
    print(np.diag(cov_pos)/pos_std_std*100)
    print(pos_std_std/np.diag(cov_pos)*100)
    # print("relative uncertainty")
    #print((cov_pos_std/cov_pos*100)
    
    
    print("test with masking before cov calc")
    ll_rr_s_nice2=kick_outliers(ll_rr_s_nice)
    ll_rr_nice2=np.zeros(np.asarray(ll_rr_nice).shape)
    for (m,n),label in np.ndenumerate(ll_rr_nice):
        ll_rr_nice2[m][n] = label if not np.isnan(ll_rr_s_nice2[m][n]) else np.nan
    cov_nice2, corr_nice2, cov_nice2_jkk, corr_nice2_jkk = icovar_jkk_w_nan(ll_rr_nice2, l_w=None, do_cor=True, do_jackknife=True, fast_jackknife=False, blabla=False, nb_jkk=None, fast=True)
    
    cov_pos2=cov_nice2-np.diag(np.multiply(np.nanmean(kick_outliers(ll_rr_s_nice),axis=0),l_rr_nice)**2) # a debug ici
    # pos_std_std=(np.diag(cov_nice_jkk)**2 + np.diag(cov_var_stat))**0.5
    pos_std_std=(np.diag(cov_nice2_jkk)**2 + np.divide(np.diag(cov_var_stat),len_w_nan(kick_outliers(ll_rr_s_nice))))**0.5
    print(ll_rr_nice)
    print("pos only cov")
    print(cov_pos2)
    print(np.diag(cov_pos2)**0.5/l_rr_nice*100)
    print(np.diag(cov_pos2)/pos_std_std*100)
    print(pos_std_std/np.diag(cov_pos2)*100)
    print(np.diag(cov_nice2_jkk)/np.diag(cov_nice2)*100)
    print(np.diag(cov_nice_jkk)/np.diag(cov_nice)*100)
    moy,std_nice,std_var_nice=imoyvar(ll_rr_nice,do_jackknife=True)
    print(std_var_nice/(std_nice**2)*100)
    print(np.divide(np.diag(cov_var_stat),len_w_nan(kick_outliers(ll_rr_s_nice)))**0.5/np.multiply(np.nanmean(kick_outliers(ll_rr_s_nice),axis=0),l_rr_nice)**2*100)
    
    print(cov_nice_jkk/cov_nice*100)
    '''
    print("test FMCD")
    cov_nice3, corr_nice3, cov_nice3_jkk, corr_nice3_jkk = icovar_jkk_MCD(ll_rr_nice, l_w=None, do_cor=True, do_jackknife=True, fast_jackknife=False, blabla=False, nb_jkk=None, fast=True)
    print(np.diag(cov_nice2)/np.diag(cov_nice3)*100)
    print(np.diag(cov_nice3_jkk)/np.diag(cov_nice3)*100)
    '''    
    print(np.divide(np.diag(cov_nice_jkk),stddev_nice**2)*100)
# plt.show()
    
    #name,keyname,dosi_den = "Au","_0_Au_102_791970", 5.90079E-02  # 1/barn*cm
    #name,keyname,dosi_den = "Ni","_1_Ni_103_280580", 6.24027E-02
    #name,keyname,dosi_den = "Ti46","_2_Ti_103_220460", 4.68102E-03
    #name,keyname,dosi_den = "Ti48","_2_Ti_103_220480", 4.18285E-02
    #name,keyname,dosi_den = "Fe54","_3_Fe_103_260540", 4.96293E-03
    #name,keyname,dosi_den = "Fe56","_3_Fe_103_260560", 7.79075E-02
    
