# py /home/thomasligonnet/ownCloud/Experimental\ activities\ LRS@EPFL/Projects/PETALE/analysis/python/Misc/reaction_rate_projector.py input=tmp
print("In devloppement, manual editing still necessary")
# Project reaction rate and relative uncertainty from sim spectra

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from utils_p11_WIP import *

from multiprocessing import Pool
from itertools import product
plt.rcParams.update({'font.size': 18})
print ("#"*50)

np.seterr(divide='ignore', invalid='ignore')

# inputs_name=["J3","T2019","T2021","J4","b8","b71","JENDL4","Uppsala"]
# inputs_name=["J3","J4","b8"]
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
l_mat1 =["In","Au","In","Ni","Fe","Fe","Al"]
l_matid=["in1","au","in2","ni","fe","fe","al"]
l_AAA  =["115","197","115","58","54","56","27"]
l_ZZAAA=["49115","79197","49115","28058","26054","26056","13027"]
l_R1   =["ng","ng","inel","np","np","np","na"]

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
l_at_den=list(map(lambda mat,iso: get_at_density(mat,iso),l_mat1,l_ZZAAA))

#adding impurit if necessary

l_mat1 +=["Mn"]
l_matid+=["mn_imp"]
l_AAA  +=["55"]
l_ZZAAA+=["25055"]
l_R1   +=["ng"]
l_at_den+=[l_at_den[-2]*5.8e-6]
l_at_den=np.array(l_at_den)

l_key_irdff_iaea=["In115ng","Au197ng","In115inel","Ni58np","Fe54np","Fe56np","Al27na"]
l_label=["$^{115}$In(n,$\gamma$)","$^{197}$Au(n,$\gamma$)","$^{115}$In(n,n')","$^{58}$Ni(n,p)","$^{54}$Fe(n,p)","$^{56}$Fe(n,p)",r"$^{27}$Al(n,$\alpha$)"]
plt.figure(figsize=(16,9))
for i in range(len(l_key_irdff_iaea)):
    idata_irdff = get_irdff_iaea(os.path.expandvars("/home/thomasligonnet/Link_to_analysis/data/iaea_data/"+l_key_irdff_iaea[i]), e_min = None)
    

    plt.plot(idata_irdff[1][0],idata_irdff[1][1],label=l_label[i])
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Energy [MeV]")
plt.ylabel("XS [barn]")
plt.ylim(1e-6,150000)
plt.xlim(1e-11,60)
plt.legend()
plt.tight_layout
plt.show()