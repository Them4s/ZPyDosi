import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

half_life=54.29*60
Lambda=np.log(2)/half_life

l_name    =np.array(["T1","T2","T3","M1","M2","M3","B1","B2","B3"])
l_masse   =np.array([2.515,5.019,7.590,2.513,5.155,7.528,2.499,5.028,7.683])
l_counts  =np.array([12430,13400,9876,14250,14840,9965,16880,14880,11700])
l_mes_time=np.array([153.64,401.71,1401.77,156.0,426.2,1496.58,134.17,389.97,1722.61])
l_wait    =np.array([140,295,220,140,305,220,155,225,180])
l_pos     =np.array([12,22,32]*3)
lab=["top","mid","bot"]
l_a1=l_counts*Lambda/(1-np.exp(-Lambda*l_mes_time))/l_masse
l_a0=l_a1*np.exp(Lambda*l_wait)


def lin(X,a,b):
    X=np.array(X)
    return b+a*X


plt.figure()
for i in range(3):
    plt.plot(l_pos[i*3:(i+1)*3],np.log(l_pos*l_a0)[i*3:(i+1)*3],linestyle="",marker="o",label=lab[i])
    coef,cov=curve_fit(lin,l_pos[i*3:(i+1)*3],np.log(l_pos*l_a0)[i*3:(i+1)*3],p0=[0,0])
    print(-1/coef)
plt.legend()

plt.show()
