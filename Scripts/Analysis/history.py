from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.Common.GetParam import  get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
import matplotlib.pyplot as plt
import os 
import numpy as np

path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv  = get_param_vari("lcase", str).split("/")

data_irrad = DataIrrad(path_csv_data,
                       path_csv_dosi,
                       lcase_csv,
                       use_sqrt_for_meas_sig=True,
                       load_hpge_eff=True,
                       load_sss_results=True,
                       load_ndup=True)
path_dir=data_irrad.l_sss_path[0]+"_mat_sss_2_of/old"
val_iter=[]
keff=[]
keff_s=[]
rr=[]
rr_s=[]
print(path_dir)
for root,dirs,files in os.walk(path_dir,topdown=True):
    for file in files :
        if ("keff" in str(file) ) and ("diff" not in str(file)) and ("sig" not in str(file)):
            val_iter.append(float(str(file).split("_")[-1]))
            keff.append(float(str(open(os.path.join(root,file),"r").readlines()[1]).split()[0]))
        if ("keff" in str(file) ) and ("diff" not in str(file)) and ("sig"  in str(file)):
            keff_s.append(float(str(open(os.path.join(root,file),"r").readlines()[1]).split()[0]))
        if ("rr" in str(file) ) and ("diff" not in str(file)) and ("trunc" not in str(file)) and ("sig" not in str(file)):
            rr.append(lmap(lambda i: float(i.split()[0]),open(os.path.join(root,file),"r").readlines()[1:]))
        if ("rr" in str(file) ) and ("diff" not in str(file)) and ("trunc" not in str(file)) and ("sig"  in str(file)):
            rr_s.append(lmap(lambda i: float(i.split()[0]),open(os.path.join(root,file),"r").readlines()[1:]))
print( len(rr),len(rr_s),len(keff),len(keff_s))
rr=np.array(rr)
rr_s=np.array(rr_s)
fig1=plt.figure(100)
plt.errorbar(val_iter,keff,keff_s,linestyle="")
plt.grid()
plt.xlabel("Iteration number [-]")
plt.ylabel("keff [-]")
print(keff)
for i in range(len(rr[0])):
    fig1=plt.figure(i)
    plt.errorbar(val_iter,rr.T[i],rr_s.T[i],linestyle="")
    plt.grid()
    plt.xlabel("Iteration number [-]")
    plt.ylabel("reaction rate [1/n]")
    
plt.show()     