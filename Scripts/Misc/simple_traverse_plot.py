# py ~/Link_to_analysis/python/Misc/simple_traverse_plot.py path=...
import numpy as np
import matplotlib.pyplot as plt


dico_color = {"Al":(0.6,0.6,0.6), "Fe":(0.2,0.2,0.2), "In":(0.8,0.85,1), "Ni":(0.8,0.6,0.4), "Au":(0.8,0.8,0.5)}

# diff_no_cradle=[-0.387099051708772,1.43444849946264,0.567062117523109,-0.405792968458851,-0.147041585198304,1.19883899614073,0.402481216860817,-1.39556807791464,-0.279584121833876,-2.04480802579092,0.685015990060611,-1.16002445892736,-0.489336196711865]
# diff_no_cradle_s=[0.179728778464322,0.561671155612995,1.08079434385641,1.67362225584541,2.58634697157015,2.99971467933532,3.16940948654129,2.04909293054853,0.764054429466955,2.27994432430515,19.4705240594326,3.09829351413228,38.1643571871547]

# diff_old=[2.19171506588292,1.86586053441404,0.627350631238244,0.826752133151421,0.35822631087854,-1.39415546180409,-2.85763499399604,-3.78004967917654,-4.41007300180624,-0.801921848641773,2.4693393017599,-0.732348148290862,-1.21664704845142]
# diff_old_s=[0.0843622637566905,0.262121655523362,0.593595610319384,0.969181677571642,1.53354138020574,1.93053086522377,1.97202714083725,1.39129289281089,0.508532203717049,1.94998551604519,10.3558186454181,3.15974002474359,28.1472162228294]

# plt.figure()
# plt.rcParams['font.size']=18
# plt.errorbar(range(1,10),diff_no_cradle[:9],diff_no_cradle_s[:9],linestyle="",marker=".",markersize=12,label="No cradle")
# plt.errorbar(range(1,10),diff_old[:9],diff_old_s[:9],linestyle="",marker=".",markersize=12,label="Old")
# plt.legend()
# plt.grid(which="major",axis="y")
# plt.xlim((0,10))


#Pcr_au)
# v_au_old  =np.array([5.61871533333333E-06,6.16040666666667E-07,3.59334883333333E-07,0.00000026056425,1.65320066666667E-07,0.00000014051175,0.00000010890355,8.36329033333333E-08,7.26544583333333E-08,9.28422116666667E-08])
# v_au_old_s=np.array([5.12972959045953E-08,3.30073771897854E-09,2.57378846015583E-09,2.16478796970501E-09,1.65120142388422E-09,1.52826809770693E-09,1.31487225882918E-09,1.04537034092406E-09,9.29779202257271E-10,9.36180671984595E-10])

# v_au_new  =np.array([0.000005665548,0.0000005990549,0.0000003524117,0.0000002571609,0.0000001600926,0.0000001376737,0.0000001107146,0.00000008700018,0.00000007689167,0.00000009422948,0.0000001954754,0.000000009103187])[:10]
# v_au_new_s=np.array([0.00000003632203,0.000000003968845,0.000000002823866,0.000000002253578,0.000000001565735,0.000000001514337,0.00000000129109,0.000000001036232,8.735718E-10,8.678223E-10,6.608068E-10,3.627365E-11])[:10]

#Pcr_in1)
v_in_new  =np.array([0.000009857942,0.000004306324,0.000002456521,0.000001542905,0.000001066365,0.0000008077148,0.0000007082815,0.0000008244098,0.000001555167,0.000004747096,0.0000002675412,0.0000001972286,0.000000009232916])[:10]
v_in_new_s=np.array([0.00000001369702,0.000000008627719,0.000000006030397,0.000000004186552,0.000000003226759,0.000000002521914,0.000000002162807,0.000000002157135,0.000000002794299,0.00000001931992,0.000000001577995,4.282105E-10,2.845516E-11])[:10]

v_in_old  =np.array([0.000010074,0.000004386674,0.000002471932,0.000001555661,0.000001070185,0.000000796454,0.0000006880414,0.0000007932467,0.000001486583,0.000004709028,0.0000002741477,0.0000001957842,0.000000009120584])[:10]
v_in_old_s=np.array([0.00000001983933,0.00000001224462,0.000000009456623,0.00000000698773,0.000000005630878,0.000000004333594,0.0000000035804,0.000000003614614,0.000000004903639,0.00000004856845,0.0000000025825,0.000000001251521,7.858344E-11])[:10]
#old geom new xs
v_in_ONXS  = np.array([1.000061e-05,4.377761e-06,2.467922e-06,1.562584e-06,1.069809e-06,8.038818e-07,6.901333e-07,7.928380e-07,1.484491e-06,4.702967e-06,2.736457e-07,1.962053e-07,9.022840e-09])[:10]
v_in_ONXS_s= np.array([2.380022e-08,1.500908e-08,1.034482e-08,7.311798e-09,5.431140e-09,4.306242e-09,3.504028e-09,3.329488e-09,4.586360e-09,3.377427e-08,2.548084e-09,7.671666e-10,4.838013e-11])[:10]
#Current old location
v_in_COL   = np.array([1.003305e-05,4.375364e-06,2.486636e-06,1.551452e-06,1.078902e-06,8.113264e-07,7.115908e-07,8.318602e-07,1.575799e-06,4.722198e-06,2.737564e-07,1.957961e-07,9.063920e-09])[:10]
v_in_COL_s = np.array([2.705830e-08,1.728515e-08,1.149901e-08,8.221851e-09,6.011229e-09,4.902904e-09,4.091470e-09,4.106090e-09,5.671170e-09,3.667971e-08,3.246242e-09,8.800429e-10,5.275574e-11])[:10]
#No Craddle
v_in_NoCra   = np.array([ 9.835611e-06, 4.339010e-06, 2.460319e-06, 1.540607e-06, 1.064716e-06, 8.133019e-07, 7.064509e-07, 8.172253e-07, 1.552047e-06, 4.686139e-06, 2.709671e-07, 1.967060e-07, 9.264370e-09])[:10]
v_in_NoCra_s = np.array([2.637000e-08,1.696704e-08,1.165159e-08,7.948673e-09,6.084158e-09,4.831169e-09,3.927203e-09,3.742856e-09,7.754310e-09,3.646844e-08,3.093172e-09,8.115591e-10,6.285530e-11])[:10]

v_in_NGOR   = np.array([9.878078e-06,4.320396e-06,2.437306e-06,1.552104e-06,1.055787e-06,8.046473e-07,7.049104e-07,8.237553e-07,1.553387e-06,4.705668e-06,2.644077e-07,1.986536e-07,9.184112e-09])[:10]
v_in_NGOR_s = np.array([4.010870e-08,2.530765e-08,1.694628e-08,1.260395e-08,9.016897e-09,7.000008e-09,5.950141e-09,5.961235e-09,8.480409e-09,5.807309e-08,4.585989e-09,1.364703e-09,8.358503e-11])[:10]

rel_sig=((v_in_old_s/v_in_old)**2+(v_in_new_s*v_in_new)**2)**0.5
rel_sig_ONXS=((v_in_ONXS_s/v_in_ONXS)**2+(v_in_new_s*v_in_new)**2)**0.5
rel_sig_COL=((v_in_COL_s/v_in_COL)**2+(v_in_new_s*v_in_new)**2)**0.5
rel_sig_NoCra=((v_in_NoCra_s/v_in_NoCra)**2+(v_in_new_s*v_in_new)**2)**0.5
rel_sig_NGOR=((v_in_NGOR_s/v_in_NGOR)**2+(v_in_new_s*v_in_new)**2)**0.5

plt.figure(figsize=(16,9))
plt.rcParams['font.size']=18
# plt.errorbar(range(1,10),v_in_new[1:10],v_in_new_s[1:10],linestyle="",marker=".",markersize=12,label="New")
# plt.errorbar(range(1,10),v_in_old[1:10],v_in_old_s[1:10],linestyle="",marker=".",markersize=12,label="Old")
plt.errorbar(range(1,10),np.divide(v_in_old[:9],v_in_new[:9])*100-100,np.divide(v_in_old[:9],v_in_new[:9])*100*(rel_sig[:9]),linestyle="",marker=".",markersize=12,label="Old model")
plt.errorbar(range(1,10),np.divide(v_in_ONXS[:9],v_in_new[:9])*100-100,np.divide(v_in_ONXS[:9],v_in_new[:9])*100*(rel_sig_ONXS[:9]),linestyle="",marker=".",markersize=12,label="Old model new XS")
plt.errorbar(range(1,10),np.divide(v_in_COL[:9],v_in_new[:9])*100-100,np.divide(v_in_COL[:9],v_in_new[:9])*100*(rel_sig_COL[:9]),linestyle="",marker=".",markersize=12,label="Current model old location")
plt.errorbar(range(1,10),np.divide(v_in_NoCra[:9],v_in_new[:9])*100-100,np.divide(v_in_NoCra[:9],v_in_new[:9])*100*(rel_sig_NoCra[:9]),linestyle="",marker=".",markersize=12,label="Current model no cradle on sides")
plt.errorbar(range(1,10),np.divide(v_in_NGOR[:9],v_in_new[:9])*100-100,np.divide(v_in_NGOR[:9],v_in_new[:9])*100*(rel_sig_NGOR[:9]),linestyle="",marker=".",markersize=12,label="Current model with old reflectors")
plt.legend()
plt.xlabel("Dosimeter position [-]")
plt.ylabel("Relative difference to reference [\%]")
plt.grid(which="major",axis="y")
plt.xlim((0,10))
plt.title("$^{115}$In(n,g) dosimeters")

#Fast In dosi

v_cr_new  =np.array([1.525871E-10,9.756555E-11,6.436429E-11,4.389952E-11,2.994828E-11,2.106976E-11,1.469473E-11,7.402691E-12])
v_cr_new_s=np.array([6.53718E-13,5.100434E-13,3.954516E-13,3.155097E-13,2.408121E-13,1.834672E-13,1.472997E-13,9.59212E-14])

v_cr_NGOR   = np.array([0.0000000268649,0.00000001841197,0.00000001296185,0.000000009050681,0.000000006417356,0.000000004577344,0.000000003213267,0.000000002193695,0.000000001413808,0.0000001964877,0.000000009052523])[:10]
v_cr_NGOR_s = np.array([2.331577E-11,1.86321E-11,1.481424E-11,1.109428E-11,8.714416E-12,6.802922E-12,6.322876E-12,4.250636E-12,3.164508E-12,2.600988E-10,1.731089E-11])[:10]


rel_sig_NGOR=((v_in_NGOR_s/v_in_NGOR)**2+(v_in_new_s*v_in_new)**2)**0.5



plt.figure(figsize=(16,9))
plt.rcParams['font.size']=18
# plt.errorbar(range(1,10),v_in_new[1:10],v_in_new_s[1:10],linestyle="",marker=".",markersize=12,label="New")
# plt.errorbar(range(1,10),v_in_old[1:10],v_in_old_s[1:10],linestyle="",marker=".",markersize=12,label="Old")
# plt.errorbar(range(1,10),np.divide(v_in_old[:9],v_in_new[:9])*100-100,np.divide(v_in_old[:9],v_in_new[:9])*100*(rel_sig[:9]),linestyle="",marker=".",markersize=12,label="Old model")
# plt.errorbar(range(1,10),np.divide(v_in_ONXS[:9],v_in_new[:9])*100-100,np.divide(v_in_ONXS[:9],v_in_new[:9])*100*(rel_sig_ONXS[:9]),linestyle="",marker=".",markersize=12,label="Old model new XS")
# plt.errorbar(range(1,10),np.divide(v_in_COL[:9],v_in_new[:9])*100-100,np.divide(v_in_COL[:9],v_in_new[:9])*100*(rel_sig_COL[:9]),linestyle="",marker=".",markersize=12,label="Current model old location")
# plt.errorbar(range(1,10),np.divide(v_in_NoCra[:9],v_in_new[:9])*100-100,np.divide(v_in_NoCra[:9],v_in_new[:9])*100*(rel_sig_NoCra[:9]),linestyle="",marker=".",markersize=12,label="Current model no cradle on sides")
plt.errorbar(range(1,10),np.divide(v_in_NGOR[:9],v_in_new[:9])*100-100,np.divide(v_in_NGOR[:9],v_in_new[:9])*100*(rel_sig_NGOR[:9]),linestyle="",marker=".",markersize=12,label="Current model with old reflectors")
plt.legend()
plt.xlabel("Dosimeter position [-]")
plt.ylabel("Relative difference to reference [\%]")
plt.grid(which="major",axis="y")
plt.xlim((0,10))
plt.title("$^{115}$In(n,n') dosimeters")


#Al dosi - Cr

v_in_new  =np.array([0.00000002693568,0.00000001840418,0.00000001296837,0.000000009088246,0.000000006407201,0.000000004565403,0.000000003205347,0.000000002197819,0.000000001410786,0.0000001963771,0.000000009150834])[:10]
v_in_new_s=np.array([5.704985E-11,4.275384E-11,3.33569E-11,2.638356E-11,1.938708E-11,1.54417E-11,1.189384E-11,9.051098E-12,7.168188E-12,6.048255E-10,4.389029E-11])[:10]

v_in_NGOR   = np.array([0.0000000268649,0.00000001841197,0.00000001296185,0.000000009050681,0.000000006417356,0.000000004577344,0.000000003213267,0.000000002193695,0.000000001413808,0.0000001964877,0.000000009052523])[:10]
v_in_NGOR_s = np.array([2.331577E-11,1.86321E-11,1.481424E-11,1.109428E-11,8.714416E-12,6.802922E-12,6.322876E-12,4.250636E-12,3.164508E-12,2.600988E-10,1.731089E-11])[:10]


rel_sig_NGOR=((v_in_NGOR_s/v_in_NGOR)**2+(v_in_new_s*v_in_new)**2)**0.5



plt.figure(figsize=(16,9))
plt.rcParams['font.size']=18
# plt.errorbar(range(1,10),v_in_new[1:10],v_in_new_s[1:10],linestyle="",marker=".",markersize=12,label="New")
# plt.errorbar(range(1,10),v_in_old[1:10],v_in_old_s[1:10],linestyle="",marker=".",markersize=12,label="Old")
# plt.errorbar(range(1,10),np.divide(v_in_old[:9],v_in_new[:9])*100-100,np.divide(v_in_old[:9],v_in_new[:9])*100*(rel_sig[:9]),linestyle="",marker=".",markersize=12,label="Old model")
# plt.errorbar(range(1,10),np.divide(v_in_ONXS[:9],v_in_new[:9])*100-100,np.divide(v_in_ONXS[:9],v_in_new[:9])*100*(rel_sig_ONXS[:9]),linestyle="",marker=".",markersize=12,label="Old model new XS")
# plt.errorbar(range(1,10),np.divide(v_in_COL[:9],v_in_new[:9])*100-100,np.divide(v_in_COL[:9],v_in_new[:9])*100*(rel_sig_COL[:9]),linestyle="",marker=".",markersize=12,label="Current model old location")
# plt.errorbar(range(1,10),np.divide(v_in_NoCra[:9],v_in_new[:9])*100-100,np.divide(v_in_NoCra[:9],v_in_new[:9])*100*(rel_sig_NoCra[:9]),linestyle="",marker=".",markersize=12,label="Current model no cradle on sides")
plt.errorbar(range(1,10),np.divide(v_in_NGOR[:9],v_in_new[:9])*100-100,np.divide(v_in_NGOR[:9],v_in_new[:9])*100*(rel_sig_NGOR[:9]),linestyle="",marker=".",markersize=12,label="Current model with old reflectors")
plt.legend()
plt.xlabel("Dosimeter position [-]")
plt.ylabel("Relative difference to reference [\%]")
plt.grid(which="major",axis="y")
plt.xlim((0,10))
plt.title("$^{115}$In(n,n') dosimeters")

'''
val_nn=[-0.163823836466193,-0.556861198506937,0.124010297264405,0.519781704119254,0.35966370498177,0.748542275800702,1.37022818517028,1.07889874036201,2.0291955100306,1.41251802619723]
sig_nn=[0.276225989207981,0.251647322496732,0.302054378755694,0.330945042116137,0.369110064166061,0.417264379834196,0.436736702069612,0.516382907069848,0.569299695635697,0.670790155732603]
num=[0,1,2,3,4,5,6,7,8,9]
val_ng=[-0.193258293624041,0.0791103542135119,0.555286372765067,1.22194833885175,0.968903357968316,1.1459654988295,2.04217674819473,1.46609710494141,2.33580420872201,1.01220315474816]
sig_ng=[0.179193611800662,0.145348005132555,0.227342454324798,0.306379998254236,0.365731250784742,0.430772915701985,0.489853366658059,0.500219359586409,0.414987718774535,0.240417997453112]

plt.subplots(2,1,sharex=True)
plt.subplots_adjust(hspace=0)
plt.subplot(211)
plt.rcParams['font.size']=18
plt.errorbar(num[1:],val_nn[1:],sig_nn[1:],linestyle="",marker=".",markersize=12,label="$^{115}$In(n,n')")
plt.errorbar(num[1:],val_ng[1:],sig_ng[1:],linestyle="",marker=".",markersize=12,label="$^{115}$In(n,g)")
plt.grid(which="major",axis="y")
plt.ylabel("Relative difference [\%]")
plt.legend()
plt.subplot(212)
plt.plot(num[1:],np.divide(val_nn[1:],sig_nn[1:]),linestyle="",marker=".",markersize=12,label="$^{115}$In(n,n')")
plt.plot(num[1:],np.divide(val_ng[1:],sig_ng[1:]),linestyle="",marker=".",markersize=12,label="$^{115}$In(n,g)")
plt.xlabel("Dosimeter number [-]")
plt.ylabel("Residual [$\sigma$]")
# plt.ylim((-2.2,2.2))
# plt.xlim((0,11))
# plt.yticks([-2,-1,0,1,2])
plt.grid(which="major",axis="y")
'''
'''
val     = [1.60E-02,5.20E-02,-3.83E-02,-1.76E-01,-1.49E-01,-1.39E-01,-2.83E-01,-4.15E-01,-5.31E-01] # do an array if multiple
val_sig = [2.94E-02,3.53E-02,4.15E-02,4.53E-02,4.83E-02,5.08E-02,5.36E-02,5.91E-02,6.76E-02]

plt.figure()

plt.errorbar(range(1,len(val)+1),val,val_sig,linestyle="",marker=".",label="$^{115}$In(n,n')")
plt.xlabel("Position [-]",fontsize=14)
plt.ylabel("Relative difference [\%]",fontsize=14)
plt.grid()
# plt.legend()
plt.title("$^{115}$In(n,n'), impurities concentration"+r" \textbf{x10}",fontsize=14)
plt.ylim((-0.6,0.1))
plt.hlines(0,0,10,linestyle="--",color="k")
plt.xlim((0.5,9.5))

val=[1.52E-01,-1.58E-01,2.09E-02,-1.45E-01,5.95E-01,1.26E-01,-1.26E-02,6.78E-01,6.07E-02] # do an array if multiple
val_sig=[1.31E-01,1.94E-01,2.42E-01,2.73E-01,3.23E-01,3.27E-01,3.23E-01,3.16E-01,2.33E-01]
plt.figure()

plt.errorbar(range(1,len(val)+1),val,val_sig,linestyle="",marker=".",label="$^{115}$In(n,n')")
plt.xlabel("Position [-]",fontsize=14)
plt.ylabel("Relative difference [\%]",fontsize=14)
plt.grid()
# plt.legend()
plt.title("$^{115}$In(n,g), impurities concentration"+r" \textbf{x10}",fontsize=14)
plt.hlines(0,0,10,linestyle="--",color="k")
plt.xlim((0.5,9.5))
# plt.ylim((-0.6,0.1))
# plt.show() 

val=[7.67E-02, 2.64E-01, 2.85E-01, 1.58E-01, 1.16E+00, 1.19E-01, -2.62E-01, -2.12E-01, -5.32E-01] # do an array if multiple
val_sig=[1.72E-01, 2.42E-01, 2.92E-01, 3.09E-01, 3.25E-01, 3.41E-01, 3.35E-01, 3.63E-01, 2.77E-01]
plt.figure()

plt.errorbar(range(1,len(val)+1),val,val_sig,linestyle="",marker=".",label="$^{115}$In(n,n')")
plt.xlabel("Position [-]",fontsize=14)
plt.ylabel("Relative difference [\%]",fontsize=14)
plt.grid()
# plt.legend()
plt.title("$^{197}$Au(n,g), impurities concentration"+r" \textbf{x10}",fontsize=14)
plt.hlines(0,0,10,linestyle="--",color="k")
plt.xlim((0.5,9.5))
# plt.ylim((-0.6,0.1))
# plt.show() 

val=[-3.05E-02, 2.45E-02, -9.42E-02, -2.71E-01, -1.61E-01, -1.10E-01, -3.92E-01, -3.90E-01, -5.03E-01] # do an array if multiple
val_sig=[4.51E-02, 5.76E-02, 7.29E-02, 8.09E-02, 9.15E-02, 9.94E-02, 1.09E-01, 1.23E-01, 1.45E-01]
plt.figure()

plt.errorbar(range(1,len(val)+1),val,val_sig,linestyle="",marker=".",label="$^{115}$In(n,n')")
plt.xlabel("Position [-]",fontsize=14)
plt.ylabel("Relative difference [\%]",fontsize=14)
plt.grid()
# plt.legend()
plt.title("$^{58}$Ni(n,p), impurities concentration"+r" \textbf{x10}",fontsize=14)
plt.hlines(0,0,10,linestyle="--",color="k")
plt.xlim((0.5,9.5))
# plt.ylim((-0.6,0.1))
# plt.show() 

val=[-3.96E-02, 1.01E-02, -1.07E-01, -2.85E-01, -1.60E-01, -1.00E-01, -4.21E-01, -3.96E-01, -4.98E-01] # do an array if multiple
val_sig=[4.93E-02, 6.35E-02, 8.12E-02, 9.07E-02, 1.03E-01, 1.13E-01, 1.25E-01, 1.41E-01, 1.67E-01]
plt.figure()

plt.errorbar(range(1,len(val)+1),val,val_sig,linestyle="",marker=".",label="$^{115}$In(n,n')")
plt.xlabel("Position [-]",fontsize=14)
plt.ylabel("Relative difference [\%]",fontsize=14)
plt.grid()
# plt.legend()
plt.title("$^{54}$Fe(n,p), impurities concentration"+r" \textbf{x10}",fontsize=14)
plt.hlines(0,0,10,linestyle="--",color="k")
plt.xlim((0.5,9.5))
# plt.ylim((-0.6,0.1))
# plt.show() 

val=[-1.25E-01, -1.82E-01, -2.99E-02, -1.01E-01, 1.96E-01, -9.52E-02, -7.77E-01, -8.79E-01, 2.48E-01] # do an array if multiple
val_sig=[1.41E-01, 1.84E-01, 2.82E-01, 2.79E-01, 3.30E-01, 3.69E-01, 4.39E-01, 4.54E-01, 5.43E-01]
plt.figure()

plt.errorbar(range(1,len(val)+1),val,val_sig,linestyle="",marker=".",label="$^{115}$In(n,n')")
plt.xlabel("Position [-]",fontsize=14)
plt.ylabel("Relative difference [\%]",fontsize=14)
plt.grid()
# plt.legend()
plt.title("$^{56}$Fe(n,p), impurities concentration"+r" \textbf{x10}",fontsize=14)
plt.hlines(0,0,10,linestyle="--",color="k")
plt.xlim((0.5,9.5))
# plt.ylim((-0.6,0.1))
# plt.show() 

val=[-1.31E-01, -1.59E-01, -6.13E-02, 7.86E-02, 5.06E-01, 3.20E-02, -8.72E-01, -1.03E+00, 6.72E-01] # do an array if multiple
val_sig=[2.04E-01, 2.63E-01, 4.17E-01, 3.97E-01, 4.66E-01, 5.24E-01, 6.46E-01, 6.27E-01, 7.57E-01]
plt.figure()

plt.errorbar(range(1,len(val)+1),val,val_sig,linestyle="",marker=".",label="$^{115}$In(n,n')")
plt.xlabel("Position [-]",fontsize=14)
plt.ylabel("Relative difference [\%]",fontsize=14)
plt.grid()
# plt.legend()
plt.title(r"$^{27}$Al(n,$\alpha$), impurities concentration"+r" \textbf{x10}",fontsize=14)
plt.hlines(0,0,10,linestyle="--",color="k")
plt.xlim((0.5,9.5))
# plt.ylim((-0.6,0.1))
'''
plt.show() 