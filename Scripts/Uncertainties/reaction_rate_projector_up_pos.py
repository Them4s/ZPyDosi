# py /home/thomasligonnet/ownCloud/Experimental\ activities\ LRS@EPFL/Projects/PETALE/analysis/python/Misc/reaction_rate_projector.py input=tmp
print("In devloppement, manual editing still necessary")
# Project reaction rate and relative uncertainty from sim spectra

from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.DosiFunctions.Functions import get_at_density
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Plots.MatrixPlots import make_cmap
from ZPyDosi.Serpent2_utils.sss2_utils import get_sss_res
from ZPyDosi.XSnFlux.GetIRDFF import get_irdff_iaea
from ZPyDosi.XSnFlux.Projections import projet_vec_intervals_from_continus, projet_vec_intervals_from_integrated
import numpy as np
import matplotlib.pyplot as plt


np.seterr(divide='ignore', invalid='ignore')

# inputs_name=["J3","T2019","T2021","J4","b8","b71","JENDL4","Uppsala"]
# inputs_name=["J3","J4","b8"]
inputs_name = get_param_vari("input",     str).split("//")
save_key = get_param_vari("save_key",     str,None)
save_mat = get_param_vari("save_mat",     str,None)
add_all  = get_param_vari("add_all", bool, "False")

# matplotlib.use('Agg')
dico_color = {"Al":(0.6,0.6,0.6), "Fe":(0.2,0.2,0.2), "In":(0.8,0.85,1), "Ni":(0.8,0.6,0.4), "Au":(0.8,0.8,0.5)}

# print("Il faut corriger l'histoire des densités")
# exit()
name_num=[""]
name_num=name_num+lmap(str,range(1,100))

def nice_array_print(arr):
    for i in arr:
        print(" ".join(i.astype(str)))

def get_c_elt(elt):
    if elt in dico_color:
        return dico_color[elt]
    c = np.random.rand(3,)
    dico_color[elt] = c
    return c
def dlet(le, log10=False):
    if not log10: return np.log(le[1:])-np.log(le[:-1])
    else: return np.log10(le[1:])-np.log10(le[:-1])

def integ(l_e,l_v,quad=False, log10=False):
    l_dlet = dlet(l_e, log10=log10)
    l_integ = l_v*l_dlet
    if quad: l_integ = l_integ**2
    for i in range(len(l_integ))[1:]:
        l_integ[i]+= l_integ[i-1]
    if quad: l_integ = l_integ**0.5
    return l_integ

rad=10.0 # dosimeter radius in cm
ep=0.15 # dosimeter width in cm 
l_mat1=["In","Au","In","Ni","Fe","Fe","Al"]
l_matid=["in1","au","in2","ni","fe","fe","al"]
# l_mat1=["In","Au","Fe","In","Ni","Fe","Fe","Al"]
l_AAA=["115","197","115","58","54","56","27"]
l_ZZAAA=["49115","79197","49115","28058","26054","26056","13027"]
# l_AAA=["115","197","58","115","58","54","56","27"]
l_R1=["ng","ng","inel","np","np","np","na"]
mat_rr="Au" # actual dosimeter material as in sim
ZZAAA_rr="79197"

minlim = (150,150,255)
maxlim = (255,150,150)
midlim = [(255,255,255)] 
cmap = make_cmap([minlim, (40,40,222), (0,0,85), (40,255,255), (20,114,0)]+ midlim +[(255,255,0), (255,75,0), (85,0,0), (222,40,40), maxlim])
cmap = make_cmap([( 0, 0,255), (0,150,255), (40,255,255), (255,255,255),(255,255,40), (255,150,0), (255,0, 0 )])
bins=np.linspace(-1,1,20)
id_mat=0
spectra_=[]
spectra_s_=[]
rr_=[]
rr_s_=[]
spectra=[]
spectra_s=[]
rr=[]
rr_s=[]
spectra_std2=[]
spectra_std=[]
spectra_cov=[]
cov_tot=[]
cov_tot_s=[]
rr_=[]
rr_s_=[]
l_at_den=np.array(list(map(lambda mat,iso: get_at_density(mat,iso),l_mat1,l_ZZAAA)))

real_at_dens=get_at_density(mat_rr,ZZAAA_rr)

for i in range(len(inputs_name)) :
    spectra_=[]
    spectra_s_=[]
    ncycle=[]
    tmp_mean_fv=[]
    tmp_mean_fs=[]
    tmp_mean_fvar=[]
    tmp_mean_fvar2=[]
    tmp_mean_to_cov=[]
    
    ncycle.append(float(get_sss_res(inputs_name[i]+"_res.m", "CYCLE_IDX")))
    f=open(inputs_name[i]+"_mat_sss_2_of/perspectra").readlines()
    n_copy=int(f[0].split()[1])+1
    spec= [ f[n_copy*m+1] for m in range(int((len(f)-1)/n_copy))]
    nb_nrj=int(f[0].split()[-1])
    #print(nb_nrj)
    dleth = (np.log(20.)-np.log(1e-10))/nb_nrj
    spectra_.append(lmap(lambda j : lmap(lambda k : float(k)/dleth , j.split()), spec))
    
    f_s=open(inputs_name[i]+"_mat_sss_2_of/perspectra_sig").readlines()
    spec_s= [ f_s[n_copy*m+1] for m in range(int((len(f_s)-1)/n_copy))]
    spectra_s_.append(lmap(lambda j : lmap(lambda k : float(k)/dleth , j.split()), spec_s))
    
    f=open(inputs_name[i]+"_mat_sss_2_of/rr_vec").readlines()
    r= [ f[m] for m in range(1,int(len(f)))]
    rr_.append(lmap(lambda j : float(j.split()[0]), r))
    
    f_s=open(inputs_name[i]+"_mat_sss_2_of/rr_vec_sig").readlines()
    r_s= [ f_s[m] for m in range(1,int(len(f_s)))]
    rr_s_.append(lmap(lambda j : float(j.split()[0]), r_s))
    
    print(np.array(spectra_).shape)
    #print(np.transpose(np.array(spectra_),(1,2,0)).shape)
    if len(spectra_)>0:                      
        # fig = plt.figure(1000+id_mat,figsize=(36.,6))
        plt.title(inputs_name[i])
        plt.axis('off')
        id_mat+=1  
        nb_nrj=len(spectra_[0][0])
        E3=10**(((np.log10(20)-np.log10(1e-10)) * np.array(range(nb_nrj+1))*1./(nb_nrj)) + np.log10(1e-10))
        id_col=1
        cov_dist=[]
        cov_dist_s=[]
        for (mat1,AAA,R1,ZZAAA) in zip(l_mat1,l_AAA,l_R1,l_ZZAAA):
            print(mat1)
            rr_for_cov=[]
            rr_for_cov_s=[]
            path_irdff_case = "/home/thomasligonnet/ownCloud/Experimental activities LRS@EPFL/Projects/PETALE/analysis/data/iaea_data/"+mat1+AAA+R1
            (l_cor_e, cor), (l_xs_e,l_xs_v,l_xs_s) = get_irdff_iaea(path_irdff_case)

            E1,E2 = 1e-10, 20.
            l_fe = 10**(((np.log10(E2)-np.log10(E1)) * np.array(range(nb_nrj+1))*1./(nb_nrj)) + np.log10(E1))
            ll_fv = np.array(spectra_).tolist()
            ll_fs = np.array(spectra_s_).tolist()


            print(len(ll_fv[0][0]))
            print(len(spectra_[0][0]))
            if l_fe[0] >l_cor_e[0]:
                #print("done 1")
                l_fe = np.array([l_cor_e[0]]+list(l_fe))
                for k in range(len(ll_fv)):
                  for i in range(len(ll_fv[k])):
                    ll_fv[k][i] = np.array([0]+list(ll_fv[k][i]))
                    ll_fs[k][i] = np.array([0]+list(ll_fs[k][i]))
    
            if l_fe[-1]<l_cor_e[-1]:
                #print("done 2")
                l_fe = np.array(list(l_fe)+[l_cor_e[-1]])
                for k in range(len(ll_fv)):
                  for i in range(len(ll_fv[k])):
                    ll_fv[k][i] = np.array(list(ll_fv[k][i])+[0])
                    ll_fs[k][i] = np.array(list(ll_fs[k][i])+[0])
            #print(len(ll_fv[0][0]))
            at_dens=get_at_density(mat1,ZZAAA)
            cov_dist=[]
            cov_dist_s=[]
            tmp_proj_xs = projet_vec_intervals_from_continus(E3, l_xs_e, l_xs_v)
            ids="123456789"
            g=open(inputs_name[0],"r").readlines()
            if add_all:
                indices=[0]
            else:
                indices=[]
            id_num=0
            for line in g:
                if "idet" in line:
                    id_num+=1
                    if line.split()[1].split("-")[-1] in ids:
                        indices+=[id_num]

            print(indices)
            # exit()
            for k in range(len(ll_fv)) :
                for j in range(len(indices)) :
                    #print(len(l_fe))
                    #print(len(l_xs_e))
                    ll_xv_proj_f = projet_vec_intervals_from_continus(l_fe, l_xs_e, l_xs_v)
                    ll_xs_proj_f = projet_vec_intervals_from_continus(l_fe, l_xs_e, l_xs_s)
                    ll_xv_proj_c = projet_vec_intervals_from_continus(l_cor_e, l_xs_e, l_xs_v)
                    ll_xs_proj_c = projet_vec_intervals_from_continus(l_cor_e, l_xs_e, l_xs_s)
                    print(len(l_fe),len(l_cor_e),len(ll_xv_proj_f),len(ll_fv[k][indices[j]]))
                    ll_rv_proj_c = projet_vec_intervals_from_integrated(np.log(l_cor_e), np.log(l_fe), ll_fv[k][indices[j]]*ll_xv_proj_f*at_dens)
                    ll_rs_proj_c = projet_vec_intervals_from_integrated(np.log(l_cor_e), np.log(l_fe), ll_fs[k][indices[j]]*ll_xv_proj_f*at_dens)

                    ll_fv_proj_c = ll_rv_proj_c/(ll_xv_proj_c*at_dens+1e-15)
                    ll_fs_proj_c = ll_rs_proj_c/(ll_xv_proj_c*at_dens+1e-15)
                    ll_dlet=dlet(l_cor_e)

                    rr_for_cov   += [ sum(ll_dlet*ll_xv_proj_c*at_dens*ll_fv_proj_c)] # reaction rate
                    #rr_for_cov_s += [ np.sqrt(sum(np.power(ll_dlet*ll_xv_proj_c*at_dens*ll_fs_proj_c,2)))] # reaction rate

                    #print(j)
                    #rr_for_cov += [integ(E3, tmp_proj_xs * spectra_[k][indices[j]])[-1] * at_dens]
                    rr_for_cov_s += [integ(E3, tmp_proj_xs * spectra_s_[k][indices[j]],quad=True)[-1] * at_dens ]

            rr+=[rr_for_cov]
            rr_s+=[rr_for_cov_s]
rr   = np.array(rr)
rr_s = np.array(rr_s)
print(np.array(rr).shape)
print(np.array(rr_s).shape)
print()
print(np.divide(rr_s,rr))
print()
print(np.divide(rr_s_,rr_)[0][:9])
print()

print("rr_spec and rr_aut diff in % (only one line is the good one)")
print(l_at_den)
print()

#rr=np.array(list(map(lambda X,Y: X*Y,rr,l_at_den.T))) # *pi*rad*rad*0.15
print(rr_)
print("Reaction rate")

nice_array_print(rr)
print("Reaction rate unc.")
nice_array_print(rr_s)
print()

print((np.divide(rr,rr_[0][:9])-1)*100) #one of them is the good one
print("rr ratio")

print((np.divide(rr[-1],rr_[0][:9]))) #one of them is the good one
print("rr_s ratios")
print((np.divide(rr_s[-1],rr_s_[0][:9]))) #one of them is the good one
#print(1/at_dens)

if save_key:
    if save_mat=="ni_fe" or save_mat=="ni_fe_J311":
        mat_id = slice(3,6)
    else:
        mat_id = l_matid.index(save_mat.replace("_J311",""))#bricolage pas bien
    print ("write res in",save_key)
    open(save_key,"w").write(
        "val      "+" ".join(map(lambda v:str(v),np.asarray(rr[mat_id]).flatten()))+"\n"+
        "stdv     "+" ".join(map(lambda v:str(v),np.asarray(rr_s[mat_id]).flatten()))+"\n"+
        "stdv_rel "+" ".join(map(lambda v:str(v),np.divide(rr_s[mat_id],rr[mat_id]).flatten()))+"\n")
    
