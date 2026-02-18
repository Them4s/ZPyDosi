from utils_p11_WIP import *
import datetime
from scipy.optimize import curve_fit
import scipy
import math
import statsmodels as sm
import matplotlib.animation as ani
def flin(X,a,b):
    s=[]
    for x in X:
        s+=[a*x+b]
    return s
    
'''
# path_csv_data  = get_param_vari("csv_data", str)
# path_csv_dosi  = get_param_vari("csv_dosi", str)
# lcase_csv  = get_param_vari("lcase", str).split("/")
path_csv_CE = get_param_vari("csv_CE", str,"irra2hpge_out/Inden/Cr_ni.csv")

data_CE= get_csv_lines(path_csv_CE)
while "Corrected C/E-1" not in data_CE[i]:i+=1
data_CE=data_CE[i+1:]
vec  =[]
sig  =[]
corr =[]
is_corr=False
for line in data_CE:
    if "vec" in line:
        vec=[float(v) for v in line.split(";")[1:]]
        is_corr=False
    if "sig" in line and "rel" not in line:
        sig=[float(v) for v in line.split(";")[1:]]
    if "cor" in line: is_corr=True
    if is_corr:
        corr+=[[float(v) for v in line.split(";")[1:]]]
# vec  =np.array(vec )
# sig  =np.array(sig )
# corr =np.array(corr)
pos=[0,1,3,4,5,6,7,8]
# a,b=True,True
sig=np.ones(8)*0.2
corr=np.ones((8,8))*0.75+np.diag(np.ones(8)*0.25)
vec=np.random.rand(8)*2-1
cov = cor_sig_to_cov(corr,sig)
print(vec)
print(cov)
print(corr)
COEF  = []
COEF2 = []
l_sample = np.random.multivariate_normal(vec,cov,size=1000)
for sample in l_sample:
    COEF   += [curve_fit(flin,pos,sample)[0][0]]

# print(COEF)
l_sample2= np.random.multivariate_normal(vec,np.diag(sig**2),size=1000)
for sample in l_sample2:
    COEF2   += [curve_fit(flin,pos,sample)[0][0]]
a=abs(np.mean(COEF)/np.std(COEF))<2
b=abs(np.mean(COEF2)/np.std(COEF2))<2
print("coef with cov : a= %f +- %f" % (np.mean(COEF),np.std(COEF))) 
print("coef no cov : a= %f +- %f" % (np.mean(COEF2),np.std(COEF2))) 
# coef,cov=curve_fit(flin,pos,vec)[0][0]
while(a or (not b) or abs(np.mean(COEF))<0.05):
    print("coucou")
    sig=np.ones(8)*0.2
    corr=np.ones((8,8))*0.75+np.diag(np.ones(8)*0.25)
    vec=np.random.rand(8)*2-1
    cov = cor_sig_to_cov(corr,sig)
    COEF  = []
    COEFo  = []
    COEF2 = []
    l_sample = np.random.multivariate_normal(vec,cov,size=100)
    for sample in l_sample:
        COEF   += [curve_fit(flin,pos,sample)[0][0]]
        COEFo   += [curve_fit(flin,pos,sample)[0][1]]
    l_sample2= np.random.multivariate_normal(vec,np.diag(sig**2),size=100)
    for sample in l_sample2:
        COEF2   += [curve_fit(flin,pos,sample)[0][0]]
    a=abs(np.mean(COEF)/np.std(COEF))<3
    b=abs(np.mean(COEF2)/np.std(COEF2))<2
    print("coef with cov : a= %f +- %f" % (np.mean(COEF),np.std(COEF))) 
    print("coef no cov : a= %f +- %f" % (np.mean(COEF2),np.std(COEF2))) 
print(vec)
print(sig)

# vec=np.array([-0.21064158,  0.24145358,  0.17753469,  0.49891402,  0.88813987,  0.85903566,  0.41734773, -0.08141494])
# sig=np.array([0.2, 0.2, 0.2
# , 0.2, 0.2, 0.2, 0.2, 0.2])
vec=np.asarray(pos)*0.4/8-0.2+np.random.rand(8)*0.3
sig=np.array([0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])
COEF  = []
COEFo  = []
COEF2 = []
l_sample = np.random.multivariate_normal(vec,cov,size=1000)
for sample in l_sample:
    COEF   += [curve_fit(flin,pos,sample)[0][0]]
    COEFo   += [curve_fit(flin,pos,sample)[0][1]]
l_sample2= np.random.multivariate_normal(vec,np.diag(sig**2),size=1000)
for sample in l_sample2:
    COEF2   += [curve_fit(flin,pos,sample)[0][0]]
print("coef with cov : a= %f +- %f" % (np.mean(COEF),np.std(COEF))) 
print("coef no cov : a= %f +- %f" % (np.mean(COEF2),np.std(COEF2))) 
xp=np.linspace(-1*2.2,9*2.2,10000)
plt.figure()
plt.errorbar(np.asarray(pos)*2.2, vec*10-np.mean(vec*10), sig*10, linestyle="",marker="|")
plt.hlines(0,-1*2.2,9*2.2,linestyle="--",colors="k")
plt.plot(xp,xp*np.mean(COEF)/2.2*10-np.mean(vec*10)+np.mean(COEFo)*10)
plt.xlim(-1*2.2,9*2.2)
plt.xlabel("Position [cm]")
plt.ylabel("Difference [\%]")
# plt.show()
plt.figure()
plt.errorbar(np.asarray(pos)*2.2, vec*10-np.mean(vec*10), sig*10, linestyle="",marker="|")
plt.hlines(0,-1*2.2,9*2.2,linestyle="--",colors="k")
# plt.plot(xp,xp*np.mean(COEF)/2.2*10-np.mean(vec*10)+np.mean(COEFo)*10)
plt.xlim(-1*2.2,9*2.2)
plt.xlabel("Position [cm]")
plt.ylabel("Difference [%%]")



'''
num_tot=10**6
vec=np.array([-1.33,0,0,0,0,0,0,0,1.33])
sig=np.array([0.33]*9)
# corr=np.ones((9,9))
corr=np.ones((9,9))*0.75+np.diag(np.ones(9)*0.25)
cov=cor_sig_to_cov(corr,sig)
l_samp=np.random.multivariate_normal(vec,cov,num_tot)
fig, ax =plt.subplots()
red,green,blue,white = map(lambda c:np.array(c), [(255,0,0), (0,255,0),(0,0,255),(255,255,255)])
cmap = make_cmap([( 0, 0,255), (0,150,255), (40,255,255), (255,255,255),(255,255,40), (255,150,0), (255,0, 0 )])
im=ax.imshow(corr,cmap=cmap, vmin=-1, vmax=1, interpolation='nearest')
plt.tick_params(axis="both",which="both",bottom=False,left=False, labelleft=False)
orientation="horizontal"
pad=0.01
logz=None
pos=[-1,-0.5,0,0.5,1]
titre = "correlations"
xlab=""
if orientation:
        if pad is None: pad = 0.05 if orientation == "vertical" else (0.15 if len(xlab)>0 else 0.01)
        cbar = plt.colorbar(im, ax=ax, format='%.1e',  orientation=orientation, aspect=30, pad=pad) #, pad=0.01) fraction=0.046
        cbar.set_ticks(pos)
        cbar.set_ticklabels(list(map(lambda p: nice_nb(p, mode_exp=False, log=logz),pos)))
        cbar.ax.tick_params(labelsize=get_aff_size("s_tick")*0.8)
        if titre is not None and len(titre)>0:
            cbar.set_label(tex(titre), rotation=0, size=get_aff_size("s_leg"))
plt.figure()
plt.errorbar(range(9),vec,sig,linestyle="",marker=".")
lim=plt.ylim()
plt.hlines([-1,1],-1,10,linestyle="--",colors="k")
plt.xlim(-1,10)
plt.show()



fig=plt.figure()
print(l_samp.shape)
nb_frame=180
num=0
def update(frame):
    global num
    plt.ylim(lim)
    plt.hlines([-1,1],-1,10,linestyle="--",colors="k")
    plt.xlim(-1,10)
    for sample in l_samp[int(len(l_samp)/nb_frame*(frame)):int(len(l_samp)/nb_frame*(frame+1))]:
        if all(abs(sample)<1):
            plt.plot(range(9),sample,linestyle="",marker=".",c="b",alpha=0.01)
            num+=1
    plt.title("try: {0}/{1}, success rate {2:.3f}\%".format(int(len(l_samp)/nb_frame*(frame+1)),int(len(l_samp)),num/(len(l_samp)/nb_frame*(frame+1))*100))
    print(num/(len(l_samp)/nb_frame*(frame+1))*100)
# print(num/num_tot)
anim = ani.FuncAnimation(fig=fig,func=update,frames=nb_frame,interval=17)
anim.save(filename="test_w_cor.gif", writer="ffmpeg")
# plt.show()
# vec=np.array([-2,0,0,0,0,0,0,0,2])
# sig=np.array([1]*9)
# corr=np.ones((9,9))
cov=sig2covdiag(sig)
l_samp=np.random.multivariate_normal(vec,cov,num_tot)
# plt.figure()
# plt.errorbar(range(9),vec,sig,linestyle="",marker=".")

fig=plt.figure()
print(l_samp.shape)

# nb_frame=180

num=0
def update(frame):
    global num
    plt.ylim(lim)
    plt.hlines([-1,1],-1,10,linestyle="--",colors="k")
    plt.xlim(-1,10)
    # plt.title("{0}/{1}".format(int(len(l_samp)/nb_frame*frame),int(len(l_samp))))
    for sample in l_samp[int(len(l_samp)/nb_frame*(frame)):int(len(l_samp)/nb_frame*(frame+1))]:
        if all(abs(sample)<1):
            plt.plot(range(9),sample,linestyle="",marker=".",c="b",alpha=0.01)
            num+=1
    plt.title("try: {0}/{1}, success rate {2:.1f}\%".format(int(len(l_samp)/nb_frame*(frame+1)),int(len(l_samp)),num/(len(l_samp)/nb_frame*(frame+1))*100))
    print(num/(len(l_samp)/nb_frame*(frame+1))*100)
# print(num/num_tot)
anim = ani.FuncAnimation(fig=fig,func=update,frames=nb_frame,interval=17)
anim.save(filename="test_wo_cor.gif", writer="ffmpeg")

# plt.ylim(lim)
# plt.hlines([-1,1],-1,10,linestyle="--",colors="k")
# plt.xlim(-1,10)
plt.show()




exit()
id_del=[]
for i in range(len(vec)):
    if vec[i ]==0.00: id_del+=[i]

vec =np.delete(vec,id_del)
sig =np.delete(sig,id_del)
corr= np.delete(np.delete(corr,id_del,axis=0),id_del,axis=1)
cov = cor_sig_to_cov(corr/100,sig)
# COEF_no,COV_no   = curve_fit(flin,[1,2,4,5,6,7,8,9],vec,sigma=sig)
# COEF_yes,COV_yes = curve_fit(flin,[1,2,4,5,6,7,8,9],vec,sigma=cov)
# print("coef no cov : a= %f +- %f" % (COEF_no[0],COV_no[0][0]**0.5)) 
# print("coef with cov : a= %f +- %f" % (COEF_yes[0],COV_yes[0][0]**0.5)) 

l_sample= np.random.multivariate_normal(vec,cov,size=8000000)
COEF=[]
for sample in l_sample[0:10000]:
    COEF   += [curve_fit(flin,pos,sample)[0][0]]
print("coef with cov : a= %f +- %f" % (np.mean(COEF),np.std(COEF))) 
results=sm.OLS()
print(l_sample.shape)
red_sample=[]
c_all_c=0
c_all_c2=0
for sample in l_sample:
    if sample[-1]< sig[-1] and sample[-1]>-sig[-1]:
        red_sample+=[sample]
    if all(sample<2*sig) and all(sample>-2*sig):
        c_all_c+=1
    if all(sample<0.01) and all(sample>-0.01):
        c_all_c2+=1

print("proba with cov: %f" % (c_all_c/len(l_sample)))
print("proba with cov within 1%%:%f" % (c_all_c2/len(l_sample)))
ms=np.mean(red_sample,axis=0)
mstd=np.std(red_sample,axis=0)
mstd[-1]=sig[-1]
l_prob=[]
l_disp=[]
l_ord=[]
for i in range(len(red_sample[0])):
    sub_part=np.sort(np.transpose(red_sample)[i])
    l_ord+=[sub_part]
    # print(sub_part.shape)
    disp=np.linspace(min(sub_part)-0.00001,max(sub_part)+0.00001,11)
    l_disp+=[disp]
    l_prob+=[np.histogram(sub_part,disp)[0]/len(sub_part)]
l_ord=np.array(l_ord)

Nsize=len(l_ord[0])
id_quant=[Nsize/100*0.15,Nsize/100*5,Nsize/100*17,Nsize/100*83,Nsize/100*95,Nsize/100*99.85]
l_alpha=[0.2,0.4,0.8,0.4,0.2]
# print(l_prob[1])
# print(l_disp[1])
print(l_ord.shape)
# exit()
plt.figure()
# plt.subplots(2,1,sharex=True)
# plt.subplot(2,1,1)
# plt.errorbar(range(len(ms)),ms,mstd,linestyle="",alpha=0.5,linewidth=2)
# plt.errorbar(range(len(vec)),vec,sig,linestyle="",alpha=0.5,linewidth=2,c="r")
'''
for j in range(len(l_prob)):
    for i in range(len(l_prob[j])):
        plt.vlines(j, l_disp[j][i],l_disp[j][i+1],alpha=l_prob[j][i]/max(l_prob[j])/2,colors="b",linewidth=2)
'''
for j in range(len(l_ord)):
    for i in range(len(id_quant)-1):
        plt.vlines(j, l_ord[j][int(id_quant[i])],l_ord[j][int(id_quant[i+1])],alpha=l_alpha[i],colors="b",linewidth=2)
        # print(l_disp[j][i+1],l_disp[j][i+1],l_prob[j][i])
# plt.subplot(2,1,2)

# without covariance
l_sample= np.random.multivariate_normal(vec,np.diag(sig**2),size=800000)
COEF=[]
for sample in l_sample[0:10000]:
    COEF   += [curve_fit(flin,[1,2,4,5,6,7,8,9],sample)[0][0]]
print("coef no cov : a= %f +- %f" % (np.mean(COEF),np.std(COEF))) 
print(l_sample.shape)
red_sample=[]
c_all_nc=0
c_all_nc2=0
for sample in l_sample:
    if sample[-1]< sig[-1] and sample[-1]>-sig[-1]:
        red_sample+=[sample]
    if all(sample<2*sig) and all(sample>-2*sig):
        c_all_nc+=1
    if all(sample<0.01) and all(sample>-0.01):
        c_all_nc2+=1

print("proba no cov: %f" % (c_all_nc/len(l_sample)))
print("proba  no cov within 1%% :%f" % (c_all_nc2/len(l_sample)))
ms=np.mean(red_sample,axis=0)
mstd=np.std(red_sample,axis=0)
mstd[-1]=sig[-1]
# plt.figure()
# plt.subplots(2,1,sharex=True)
# plt.subplot(2,1,1)
plt.errorbar(np.array(range(len(ms)))+0.2,vec,sig,linestyle="",alpha=0.5,linewidth=2,c="g")
# plt.errorbar(np.array(range(len(ms)))+0.2,vec,sig*2,linestyle="",alpha=0.3,linewidth=2,c="g")
# plt.errorbar(np.array(range(len(ms)))+0.2,vec,sig*3,linestyle="",alpha=0.2,linewidth=2,c="g")
# plt.errorbar(np.array(range(len(ms)))+0.1,ms,mstd,linestyle="",alpha=0.5,linewidth=2,c="g")
plt.hlines(0,-1,9,linestyles="--",colors="k")
plt.hlines(0.01,-1,9,linestyles="--",colors="r")
plt.hlines(-0.01,-1,9,linestyles="--",colors="r")
plt.xlim([-1,8])
plt.show()
# print(corr)