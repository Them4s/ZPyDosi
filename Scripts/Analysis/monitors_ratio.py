#Detector ratio Check
# cd $petale_analysis/irrad/petale
# py $petale_analysis/python/irrad/monitors_ratio.py

import os
import numpy as np
import matplotlib.pyplot as plt
from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.Common.GetParam import get_param_vari
import datetime

plt.rcParams.update({'font.size': 22})
effective_integrated_counts = get_param_vari("eff_count",bool,"False") # gold foil only (print value)
if effective_integrated_counts:
    half_life= 2.6941*24*3600
    lamb=np.log(2)/half_life
    dt_moni_1=2.531*10**(-7)
    dt_moni_2=2.402*10**(-7)
    dt_moni_1_s=0.006*10**(-7)
    dt_moni_2_s=0.005*10**(-7)
    def corr1(C):
        C=np.array(C)
        return np.divide(C,1-np.multiply(C,dt_moni_1))
    def corr2(C):
        C=np.array(C)
        return np.divide(C,1-np.multiply(C,dt_moni_2))
    def corr_var1(C):
        sol=[]
        C=np.array(C)
        if C.ndim==1 :
            for i in C :
                sol+=[(i*i/(1-i*dt_moni_1)**2)**2*dt_moni_1_s**2]
        else:
            i=C
            sol+=[(i*i/(1-i*dt_moni_1)**2)**2*dt_moni_1_s**2]
        return np.array(sol)
    def corr_var2(C):
        sol=[]
        C=np.array(C)
        if C.ndim==1 :
            for i in C :
                sol+=[(i*i/(1-i*dt_moni_2)**2)**2*dt_moni_2_s**2]
        else:
            i=C
            sol+=[(i*i/(1-i*dt_moni_2)**2)**2*dt_moni_2_s**2]
        return np.array(sol)
    

include = set(["Pc","Pf","Ps","Pn"])
# exclude = set(["raw","bad_name","to_delete",""])
ratio=[]
ratio_s=[]
power_estimate=[]
integrated_counts1=[]
integrated_counts2=[]
integrated_counts1_s=[]
integrated_counts2_s=[]
integrated_counts_raw1=[]
integrated_counts_raw2=[]
integrated_counts_raw1_s=[]
integrated_counts_raw2_s=[]
num=0
date_irrad=[]
for (root,dirs,files) in os.walk("power_history/", topdown=True):
    dirs[:]=[d for d in dirs if (d[:2] in include and "crit" not in d )]
    tka=[]
    num_file=len(files)/4 #2 types (tka,cnf) and 2 monitors
    for file in files :
        if "TKA" in file : tka.append(file)
        
    tka=sorted(tka)
    print(dirs)
    print(tka)
    if num_file == 2 or num_file == 2.5 : #exclude the third of moni 1
        if ( "v2" not in tka[1]) and ( "v1" not in tka[0]) : # correction for an exception
            tka[1],tka[0]=tka[0],tka[1]
        print(tka)
        if ( "v2" not in tka[3]) and ( "v1" not in tka[2]) : # correction for an exception
            tka[2],tka[3]=tka[3],tka[2]
        f1_1 = list(open(os.path.join(root,tka[0]),"r").readlines()[2:])
        f1_2 = list(open(os.path.join(root,tka[2]),"r").readlines()[2:])
        f2_1 = list(open(os.path.join(root,tka[1]),"r").readlines()[2:])
        f2_2 = list(open(os.path.join(root,tka[3]),"r").readlines()[2:])
        if ( "v2" not in tka[1]) or ( "v2" not in tka[3]) : #Check
            print("error with file and monitors")
            print(tka[1],tka[3])
            exit()
        f1   = f1_1 + f1_2 
        f2   = f2_1 + f2_2 
        date_i=datetime.datetime(*map(lambda j : int(j),tka[0].split("_")[0:6]))
    elif num_file==1 :
        print(tka)
        f1 = list(open(os.path.join(root,tka[0]),"r").readlines()[2:])
        f2 = list(open(os.path.join(root,tka[1]),"r").readlines()[2:])
        date_i=datetime.datetime(*map(lambda j : int(j),tka[1].split("_")[0:6]))
    elif num_file==0: print(0)
    else :
        print("Error  with the number of file")
        print(tka)
        exit()
    if num_file!=0:
        f1=np.array(lmap(lambda s : float(s) , f1))
        f2=np.array(lmap(lambda s : float(s) , f2))
        index1=np.where((f1[1:]-f1[:-1])==min(f1[1:]-f1[:-1]))[0][0]
        index2=np.where((f2[1:]-f2[:-1])==min(f2[1:]-f2[:-1]))[0][0]
        #if index1==3759:index1=index2+60 #exception for Pfe_Au
        #if index1==2017:index1,index2=2119,2119-60 #exception for Pfe_ing
        print(index1,index2)
        while (0 in f1[index1+10:index1+50]) and (0 in f1[index1-50:index1-10]) :# Check for non physical pikes present when turning off electronics
            f1[index1-10:index1+10]=np.zeros(20)
            f2[index2-10:index2+10]=np.zeros(20)
            index1=np.where((f1[1:]-f1[:-1])==min(f1[1:]-f1[:-1]))[0][0]
            index2=np.where((f2[1:]-f2[:-1])==min(f2[1:]-f2[:-1]))[0][0]
            print(index1,index2)
        f1[index1+400:]=np.zeros(len(f1[index1+400:]))
        f2[index2+400:]=np.zeros(len(f2[index2+400:]))
        power_estimate.append(int(round(np.mean(f1[index1-100:index1-1])/2614,-1)))
        plt.figure(num_file)
        num+=1
        plt.plot(range(len(f1)),f1,label=str(num))
        plt.axvline(index1)
        plt.legend()
        date_irrad.append(date_i+datetime.timedelta(seconds=int(index1)))
        if effective_integrated_counts:
            integrated_counts1.append(sum(corr1(f1)*np.exp(-lamb*(index1-np.array(range(len(f1)))))))
            integrated_counts2.append(sum(corr2(f2)*np.exp(-lamb*(index2-np.array(range(len(f2)))))))
            integrated_counts1_s.append(np.sqrt(sum(corr1(f1)*np.exp(-2*lamb*(index1-np.array(range(len(f1))))))  + sum(corr_var1(f1)*np.exp(-2*lamb*(index1-np.array(range(len(f1))))))))
            integrated_counts2_s.append(np.sqrt(sum(corr2(f2)*np.exp(-2*lamb*(index2-np.array(range(len(f2))))))  + sum(corr_var2(f1)*np.exp(-2*lamb*(index1-np.array(range(len(f1))))))))
            integrated_counts_raw1.append(sum(f1*np.exp(-lamb*(index1-np.array(range(len(f1)))))))
            integrated_counts_raw2.append(sum(f2*np.exp(-lamb*(index2-np.array(range(len(f2)))))))
            integrated_counts_raw1_s.append(np.sqrt(sum(f1*np.exp(-2*lamb*(index1-np.array(range(len(f1))))))))
            integrated_counts_raw2_s.append(np.sqrt(sum(f2*np.exp(-2*lamb*(index2-np.array(range(len(f2))))))))
        ratio.append(np.mean(np.divide(sum(f1[index1-index2:]),sum(f2[:-(index1-index2)])))) #Key: ratio_calcul
        ratio_s.append((1/np.sqrt(sum(f1[index1-index2:]))+1/np.sqrt(sum(f2[:-(index1-index2)])))*np.divide(sum(f1[index1-index2:]),sum(f2[:-(index1-index2)])))
        if index1-index2> 61 or index2>index1 : print("Warning strange indices")   
to_order=[1,6,17,2,18,20,13,8,19,11,15,9,16,14,12,10,4,3,7,21,5]
# to_order=[10,9,7,8,6,15,14,12,13,11,5,4,21,2,3,1,20,19,17,18,16]
order=lmap(lambda s : to_order.index(s),range(1,22))
print(order)
print(len(ratio))
ratio_tmp=ratio
ratio_tmp_s=ratio_s
print(ratio)
ratio=[ratio[i] for i in order]
ratio_s=[ratio_s[i] for i in order]
power_estimate=[power_estimate[i] for i in order]
date_irrad=[date_irrad[i] for i in order]
if effective_integrated_counts:
    integrated_counts1  =[integrated_counts1[i] for i in order]
    integrated_counts2  =[integrated_counts2[i] for i in order]
    integrated_counts1_s=[integrated_counts1_s[i] for i in order]
    integrated_counts2_s=[integrated_counts2_s[i] for i in order]
    integrated_counts_raw1  =[integrated_counts_raw1[i] for i in order]
    integrated_counts_raw2  =[integrated_counts_raw2[i] for i in order]
    integrated_counts_raw1_s=[integrated_counts_raw1_s[i] for i in order]
    integrated_counts_raw2_s=[integrated_counts_raw2_s[i] for i in order]
    print("Effective counts Monitor 1")
    print(integrated_counts1   )
    print(integrated_counts1_s )
    print("Effective counts Monitor 2")
    print(integrated_counts2   )
    print(integrated_counts2_s )
    
    print("Effective counts raw Monitor 1")
    print(integrated_counts_raw1   )
    print(integrated_counts_raw1_s )
    print("Effective counts raw Monitor 2")
    print(integrated_counts_raw2   )
    print(integrated_counts_raw2_s )

print(ratio)
fig0,axs=plt.subplots(2,1, figsize=(16,9))
axs[0].errorbar(range(1 ,len(ratio)),ratio[:-1],ratio_s[:-1],linestyle="",marker=".",markersize=12.)
for i in [2,7,12,17] :
    axs[0].errorbar(i+1,ratio[i],ratio_s[i],linestyle="",marker=".",markersize=12.,color="r")
bot,top=axs[0].set_ylim()
bot=bot-0.0025
top=top+0.001
axs[0].fill_between([0,5.5],y2=bot,y1=top,color="goldenrod", alpha=0.2, label="Nickel")
axs[0].fill_between([5.5,10.5],y2=bot,y1=top,color="grey", alpha=0.2, label="Chromium")
axs[0].fill_between([10.5,15.5],y2=bot,y1=top,color="green", alpha=0.2, label="Iron")
axs[0].fill_between([15.5,21],y2=bot,y1=top,color="blue", alpha=0.2, label="Stainless-Steel 304L")
# axs[0].fill_between([20.5,22],y2=bot,y1=top,color="orange", alpha=0.2, label="Nickel reflector (repetition)")
pow_txt=lmap(lambda i:str(i)+" W",power_estimate)
CR_SE_pos=[0,100,285,0,0,296,290,410,290,288.5,175,180,344,160,163,137,140,331,117,124,0] #copied from log4.5
CR_NO_pos=[843,870,1000,830,832,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,853.5] #copied from log4.5
print(pow_txt)
for i, txt in enumerate(pow_txt[:-1]): 
    axs[0].annotate(txt+"\n S: "+str(CR_SE_pos[i])+" \n N:"+str(CR_NO_pos[i])+" ", (i+1.1, ratio[i]-0.0011),fontsize=14)
axs[0].annotate("Nickel",  (0.7 ,0.945),fontsize=22)
axs[0].annotate("Chromium",(5.7 ,0.945),fontsize=22)
axs[0].annotate("Iron",    (10.7,0.945),fontsize=22)
axs[0].annotate("Steel",   (15.7,0.945),fontsize=22)
# axs[0].annotate("Nickel",      (20.7,0.945),fontsize=12)
axs[0].grid(axis="y")
# axs[0].legend()
axs[0].set_xticks(range(1 ,len(ratio)),range(1 ,len(ratio)))
axs[0].set_ylabel("Ratio monitor1/monitor2 [-]",fontsize=22)
axs[0].set_xlabel("Experiment number [-]",fontsize=22)
axs[0].set_ylim(bot,top)
axs[0].set_xlim(0,21)
print("stop time irrad")
for i in date_irrad:
    print(i)
    
print(ratio)    

def f_lin(x,a,b):
    return a*x+b
def f_lin_var(X,covar):
    sol=[]
    for x in X :
        sol+=[(np.array([x,1]).dot(covar)).dot(np.array([x,1]))]
    return  sol

# coef, cov = curve_fit(f_lin,CR_SE_pos[5:20],ratio[5:20],sigma=ratio_s[5:20],p0=[1,0])
# coef2, cov2 = curve_fit(f_lin,CR_SE_pos[10:20],ratio[10:20],sigma=ratio_s[10:20],p0=[1,0])
# xlin=np.linspace(0,420,421)
# val_f=f_lin(xlin,*coef)
# sigma_f=np.sqrt(f_lin_var(xlin,cov))
# val_f2=f_lin(xlin,*coef2)
# sigma_f2=np.sqrt(f_lin_var(xlin,cov2))

# fig3= plt.figure(3,figsize=(14.,5.))
axs[1].errorbar(CR_SE_pos[0:5],ratio[0:5],ratio_s[0:5],c="goldenrod",linestyle="",marker=".",markersize=12.,label="Nickel")
axs[1].errorbar(CR_SE_pos[5:10],ratio[5:10],ratio_s[5:10],c="grey",linestyle="",marker=".",markersize=12.,label="Chromium")
axs[1].errorbar(CR_SE_pos[10:15],ratio[10:15],ratio_s[10:15],c="green",linestyle="",marker=".",markersize=12.,label="Iron")
axs[1].errorbar(CR_SE_pos[15:20],ratio[15:20],ratio_s[15:20],c="blue",linestyle="",marker=".",markersize=12.,label="Stainless-Steel 304L")
# axs[1].errorbar(CR_SE_pos[20],ratio[20],ratio_s[20],c="orange",linestyle="",marker=".",markersize=8.,label="Reflector : Nickel (repetition)")
# axs[1].plot(xlin,val_f,color="c",label="Linear adjustment")
# axs[1].fill_between(xlin,val_f-sigma_f,val_f+sigma_f,color="c",alpha=0.2)
# axs[1].plot(xlin,val_f2,color="r",label="Linear adjustment without chromium")
# axs[1].fill_between(xlin,val_f2-sigma_f2,val_f2+sigma_f2,color="r",alpha=0.2)
axs[1].set_ylabel("Ratio monitor1/monitor2 [-]",fontsize=22)
axs[1].set_xlabel("South rod height [mm]",fontsize=22)
#for i, txt in enumerate(pow_txt):
#    axs[1].annotate(txt, (CR_SE_pos[i], ratio[i]),fontsize=12)
axs[1].legend()
axs[1].grid()
# fig3.savefig("petale_monitors_vs_S_CR.png", bbox_inches=('tight'), dpi=300)
plt.tight_layout()
fig0.savefig("petale_monitors_ratio.png", bbox_inches=('tight'), dpi=400)

# plt.show()