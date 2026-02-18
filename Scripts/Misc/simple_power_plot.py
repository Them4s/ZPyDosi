# py ~/Link_to_analysis/python/Misc/simple_power_plot.py path=...
from utils_p11_WIP import *
import datetime
from scipy.optimize import curve_fit
from scipy.stats import linregress
import math
import matplotlib.pyplot as plt 

path_spec  = get_param_vari("path", str)
def f_exp(X,a,b):
    return [a*np.exp(b*x) for x in X]
def f_lin(X,a,b):
    return [np.log(a)+b*x for x in X]
def f_DT(X,a,t):
    return np.array([a*x/(1+a*x*t) for x in X])
def f_dt_sig(X,coef,sig):
    l_samp=np.random.multivariate_normal(coef,sig,2*13)
    l_val=[]
    for i in range(len(l_samp)):
        l_val+=[f_DT(X,*l_samp[i])]
    return np.std(l_val,axis=0)
def f_gauss(X,mu,s,A):
    sol=[]
    for x in X:
        sol+=[A*np.exp(-(x-mu)**2/(2*s*s))]
    return sol

def f_dgauss(X,mu,s,A,mu2,s2,A2):
    sol=[]
    for x in X:
        sol+=[A*np.exp(-(x-mu)**2/(2*s*s))+A2*np.exp(-(x-mu2)**2/(2*s2*s2))]
    return sol
def f_tgauss(X,mu,s,A,mu2,s2,A2,mu3,s3,A3):
    sol=[]
    for x in X:
        sol+=[A*np.exp(-(x-mu)**2/(2*s*s))+A2*np.exp(-(x-mu2)**2/(2*s2*s2))+A3*np.exp(-(x-mu3)**2/(2*s3*s3))]
    return sol
# val=np.loadtxt(path_spec,dtype=int)[:,8000:-8000]
val=np.loadtxt(path_spec,dtype=int)
# for i in range(len(val)):
#     print("Var_o_Mean of {0}: {1}".format(i,np.var(val[i])/np.mean(val[i])))

# val2=np.loadtxt("/home/thomasligonnet/Experiments/BLOOM/Oscil/Au_4mm_2024_07_22/Monitors/2024_07_22_12_10_01_1,0s_CH2.TKA",dtype=int)[2:]

# val149=val[149][1547:4145]
valx=np.sum(val,axis=0)
# for i in range(len(val)):
#     val[i]=np.roll(val[i],int((np.random.rand()-0.5)*20))
val=np.sum(val,axis=0)
# val[5]=83000
# val[6]=83000
plt.figure()
plt.plot(np.arange(len(val)),val)
plt.yscale("log")
plt.ylabel("Count rate [1/s]")
plt.xlabel("Time [s]")
# plt.show()
val2=np.loadtxt("/media/thomasligonnet/SAFFRON_out/2024_09_11/Monitors/2024_09_11_13_19_42_1,0s_CH1.TKA",dtype=int)[2:]
plt.figure()
plt.plot(np.arange(len(val2)),val2)
plt.yscale("log")
plt.ylabel("Count rate [1/s]")
plt.xlabel("Time [s]")


val=val[100:2202] 
val2=val2[4990:7092] 

# exit()
plt.legend()
# val=val[1547:4145]
# val2=val2[3538:6136]
# val=val[1547:3847]
# val2=val2[3538:5838]
plt.figure()
plt.plot(np.arange(1,len(val2)+1),val2/2614,linestyle="",marker=".")
plt.xlabel("Time [s]")
plt.ylabel("Power [W]")
plt.yscale("log")
plt.grid(which="both")
plt.show()
coef,sig=curve_fit(f_DT,val2/2614,val,p0=[240000,0])
print(coef)
print(np.diag(sig)**0.5)
plt.figure()
plt.plot(val2/2614,val,linestyle="",marker=".")
xfit=np.linspace(min(val2),max(val2))/2614
plt.plot(xfit,f_DT(xfit,*coef),color="orange")
sig_f=f_dt_sig(xfit,coef,sig)
plt.fill_between(xfit,f_DT(xfit,*coef)-sig_f,f_DT(xfit,*coef)+sig_f,alpha=0.2,color="orange")
plt.xlabel("Power [W]")
plt.ylabel("Counts")
plt.figure()
plt.hist((val-f_DT(val2/2614,*coef))/val**0.5)
plt.xlabel("Residual [$\sigma$]")
print("std residual: {}".format(np.std((val-f_DT(val2/2614,*coef))/val**0.5)))
plt.figure()
plt.plot(((val-f_DT(val2/2614,*coef))/val**0.5),linestyle="",marker=".")
plt.ylabel("Residual [$\sigma$]")
plt.xlabel("Bin")
plt.figure()
plt.plot(val2/2614,val/(val2/2614),linestyle="",marker=".")
plt.xlabel("Power [W]")
plt.ylabel("Count per Watt [W$^{-1}$]")
plt.show()
# plt.figure()
# plt.plot(val2[1500:1940]/2614,(val4/val*100)[60:500],linestyle="",marker=".")
# plt.xlabel("Power [W]")
# plt.ylabel("Count per Watt [W$^{-1}$")
plt.figure()
plt.plot(val2[1500:1750]/2614,val[60:310]/(val2[1500:1750]/2614),linestyle="",marker=".")
plt.xlabel("Power [W]")
plt.ylabel("Count per Watt [W$^{-1}$")
plt.figure()
plt.plot(val2[1750:1940]/2614,val3[310:500]/(val2[1750:1940]/2614),linestyle="",marker=".")
plt.xlabel("Power [W]")
plt.ylabel("Count per Watt [W$^{-1}$")
# plt.yscale("log")
# plt.xscale("log")
plt.grid()
plt.show()
coef,cov = curve_fit(f_lin,range(890,980),np.log(val[890:980]))
print(coef)
plt.plot(range(890,980),f_exp(range(890,980),*coef))
print("T2 =",1/(coef[1]/np.log(2)))

betha=0.00001*np.array([23.6102,121.868,116.346,260.858,106.948,44.8001,1.38702,14.6170,17.2844,41.3972,24.0061,8.00203])
lambda_=np.array([0.013336,0.032739,0.12078,0.30278,0.84949,2.8530,0.013230,0.032120,0.13900,0.35900,1.4100,4.0300])
Lambda=5.06413e-5
func2 = lambda w : Lambda*w + betha[0]*w/(lambda_[0]+w) + betha[1]*w/(lambda_[1]+w)+ betha[2]*w/(lambda_[2]+w)+ betha[3]*w/(lambda_[3]+w)+ betha[4]*w/(lambda_[4]+w)+ betha[5]*w/(lambda_[5]+w)+ betha[6]*w/(lambda_[6]+w)+ betha[7]*w/(lambda_[7]+w)+ betha[8]*w/(lambda_[8]+w)+ betha[9]*w/(lambda_[9]+w)+ betha[10]*w/(lambda_[10]+w)+ betha[11]*w/(lambda_[11]+w)
print(func2(coef[1])*1e5,"pcm")

reg = linregress(range(670,790),np.log(val[670:790]))
print(reg.slope)
plt.plot(range(670,790),f_exp(range(670,790),np.exp(reg.intercept),reg.slope))
print("T2 =",1/(reg.slope/np.log(2)))

betha=0.00001*np.array([23.6102,121.868,116.346,260.858,106.948,44.8001,1.38702,14.6170,17.2844,41.3972,24.0061,8.00203])
lambda_=np.array([0.013336,0.032739,0.12078,0.30278,0.84949,2.8530,0.013230,0.032120,0.13900,0.35900,1.4100,4.0300])
Lambda=5.06413e-5
func2 = lambda w : Lambda*w + betha[0]*w/(lambda_[0]+w) + betha[1]*w/(lambda_[1]+w)+ betha[2]*w/(lambda_[2]+w)+ betha[3]*w/(lambda_[3]+w)+ betha[4]*w/(lambda_[4]+w)+ betha[5]*w/(lambda_[5]+w)+ betha[6]*w/(lambda_[6]+w)+ betha[7]*w/(lambda_[7]+w)+ betha[8]*w/(lambda_[8]+w)+ betha[9]*w/(lambda_[9]+w)+ betha[10]*w/(lambda_[10]+w)+ betha[11]*w/(lambda_[11]+w)
print(func2(reg.slope)*1e5,"pcm")
plt.yscale('log')
plt.show() 