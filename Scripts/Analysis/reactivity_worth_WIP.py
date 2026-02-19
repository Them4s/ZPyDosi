# py ~/Link_to_analysis/python/irrad/reactivity_worth_WIP.py csv_data=$csv_data csv_dosi=$csv_dosi
from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
import numpy as np
import datetime
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
from numpy.random import default_rng
import pandas as pd
from statsmodels.formula.api import ols #For ordinary least square 

### DataCrit from the pile oscillation part, should be an import in the future

# default kinetic param CROCUS
beta_J33=np.array([2.24952E-04,1.09109E-03,6.58035E-04,1.44130E-03,2.45583E-03,8.03684E-04,6.69582E-04,2.52243E-04])
# beta_J33_rel=np.array([0.01]*8)
beta_J33_rel=np.array([0.00761,0.00348,0.00451,0.00304,0.00233,0.00407 ,0.00445 ,0.00724])
beta_J33_sig=beta_J33*beta_J33_rel
lambda_J33=np.array([1.24667E-02,  2.82917E-02,4.25244E-02,1.33042E-01 , 2.92467E-01 , 6.66488E-01 , 1.63478E+00 , 3.55460E+00 ])
Lambda_J33=4.76746E-05
CFUL_clock_factor=1.000 #correction with respect to SAFFRON

def to_datetime(hour):
    if isinstance(hour,datetime.datetime):
        return hour
    if isinstance(hour,datetime.time):
        fake_day=datetime.datetime(2024,1,1)
        return datetime.datetime.combine(fake_day,hour)
    else:
        return datetime.datetime.strptime(hour,    '%H:%M:%S')

d_offset_CFUL={ # linearity measurements
    "C1":-0.137,
    "C2":-0.116,
    "C3":-0.1565,
    "C4":-0.2965}

def load_CFUL(path,offest=True):
    off=0
    if offest:
        for key in d_offset_CFUL.keys():
            if key in path: 
                off = d_offset_CFUL[key]
        if off ==0:
            print("ERROR in load_CFUL: CFUL id not found")
            exit()
        else:
            print("Offset correction applied")
    signal=(np.loadtxt(path,skiprows=5,dtype=np.float64)-off)
    return signal

class DataCrit:
    def __init__(self,signal_f,dwell_t=1,Mes_start="00:00:00",P_start="00:00:00",P_end="00:00:00", nums_to_exclude=[], mstart=-1,
                 beta=beta_J33,
                 lambda_=lambda_J33,
                 Lambda=Lambda_J33,
                 beta_sig=beta_J33_sig,
                 det_Type="Monitor"):
        self.measurment_start=to_datetime(Mes_start)
        self.Crit_start=to_datetime(P_start)
        self.Crit_end=to_datetime(P_end)
        self.Crit_duration=(self.Crit_end-self.Crit_start).total_seconds()
        self.signal_file=signal_f
        self.Lambda=Lambda
        self.lambda_=np.array(lambda_)
        self.beta=np.array(beta)
        self.beta_sig=np.array(beta_sig)
        self.Beta=sum(self.beta)
        self.Beta_sig=np.sqrt(sum(self.beta_sig**2))
        self.period=-1
        self.omega=-1
        self.omega_sig=-1
        self.reactivity=-1
        self.reactivity_sig=-1
        self.total_duration=(self.Crit_start-self.measurment_start).total_seconds()
        self.Mstart=mstart
        self.det_Type=det_Type
        if det_Type=="SAFFRON":
            self.signal=np.array(lmap(lambda line: [float(s) for s in line.split()],open(self.signal_file,"r").readlines()))
            #local signal as sum of local Mimi 
            #global signal as sum of SAFFRON except locals
            self.signal_global=self.signal[0]
            for i in range(1,len(self.signal)): 
                if i not in nums_to_exclude: 
                    self.signal_global+=self.signal[i]
        elif det_Type=="CFUL": #loading CFUl results in positive
            tmp=load_CFUL(self.signal_file)
            self.signal_global= np.abs(tmp[:,1])
            self.dwell_time=np.mean(np.diff(tmp[:,0]))/CFUL_clock_factor
            # self.signal_global=np.array(lmap(lambda s: abs(float(s.replace(","," ").split()[1])) ,open(self.signal_file,"r").readlines()[5:]))
            # self.dwell_time=np.mean(np.diff(lmap(lambda s: float(s.replace(","," ").split()[0]) ,open(self.signal_file,"r").readlines()[5:])))
            self.signal_local=[]
            print("CFUL dwell_time = {} s".format(self.dwell_time))
        elif det_Type=="Monitor":
            if "//" in self.signal_file:
                f=[]
                for path in self.signal_file.split("//"):
                    f+=lmap(lambda s: float(s) ,open(path,"r").readlines()[2:-1])
            else:
                f=lmap(lambda s: float(s) ,open(self.signal_file,"r").readlines()[2:-1])
            self.signal_global=np.array(f)
            self.dwell_time=dwell_t
            self.signal_local=[]

        else:
            print("ERROR DataCrit: Unknown detector type entered!")
            print(exit())

    def __str__(self):
        return "DataCrit"

    def CalcPeriod(self, signal=[-1],First_order_fit=False): #linear Fit of the stable period (=1st order Taylor)
        
        def flin(X,a,b):
            X=np.array(X)
            return X*a+b
        
        if signal[0]==-1:
            signal=self.signal_global
        
        if self.Mstart!=-1:
            # print("period in manual mode")
            fstart=(self.Crit_start-self.measurment_start).total_seconds()+self.Mstart
        elif self.Crit_duration > 600:
            fstart=(self.Crit_start-self.measurment_start).total_seconds()+300
            self.Mstart=300
        elif self.Crit_duration > 200:
            fstart=(self.Crit_start-self.measurment_start).total_seconds()+100
            self.Mstart=100
        else:
            print("ERROR DataCrit: signal duration too short for auto-fit please enter start point manually!")
        fend=(self.Crit_end-self.measurment_start).total_seconds()
        tofit=signal[int(fstart/self.dwell_time):int(fend/self.dwell_time)]
        if not First_order_fit:
            coef,cov=curve_fit(flin,np.arange(len(tofit))*self.dwell_time,np.log(tofit))
            self.period=1/coef[0]
            self.omega=coef[0]
            self.omega_sig=cov[0,0]**0.5
        else:
            coef,cov=curve_fit(flin,np.arange(len(tofit))*self.dwell_time,(tofit))
            self.period=coef[1]/coef[0]
            self.omega=coef[0]/coef[1]
            self.omega_sig=cov[0,0]**0.5
        return self.period
    
    def CalcRho(self, signal=[-1], unc_poisson=False,unc_beta=False):
        if signal[0]==-1:
            signal=self.signal_global
        if not unc_poisson and not unc_beta:
            if self.period==-1:
                self.CalcPeriod(signal)
            self.reactivity=self.Lambda*self.omega+sum(self.beta*self.omega/(self.lambda_+self.omega))
        else:
            Nsample=2**10
            l_reactivity=[]
            if self.det_Type in ["SAFFRON","Monitor"]: #counters
                for i in range(Nsample):
                    if unc_poisson:
                        l_signal=np.random.poisson(signal,size=(1,len(signal)))
                    else:
                        l_signal=np.random.normal(signal,[0]*len(signal),size=(1,len(signal)))
                    if unc_beta:
                        l_beta=np.random.normal(self.beta,self.beta_sig,size=(1,len(self.beta)))
                    else:
                        l_beta=np.random.normal(self.beta,[0]*len(self.beta),size=(1,len(self.beta)))
                    omeg=1/self.CalcPeriod(l_signal[0])
                    l_reactivity+=[self.Lambda*omeg+sum(l_beta[0]*omeg/(self.lambda_+omeg))]
            elif self.det_Type in ["CFUL"]: #currents
                omeg_ref=1/self.CalcPeriod(signal)
                for i in range(Nsample):
                    if unc_poisson:
                        rand_omeg=np.random.normal(self.omega,self.omega_sig)
                    else:
                        rand_omeg=self.omega
                    if unc_beta:
                        l_beta=np.random.normal(self.beta,self.beta_sig)
                    else:
                        l_beta=self.beta
                    l_reactivity+=[self.Lambda*rand_omeg+sum(l_beta*rand_omeg/(self.lambda_+rand_omeg))]
            else:
                print("Error in DataPeriod.CalcRho: det_Type unkown")
                exit()
            self.reactivity=np.mean(l_reactivity)
            self.reactivity_sig=np.std(l_reactivity)
    
    def Delta_rho(self, unc_poisson=False,unc_beta=False,plot=False):
        if not unc_poisson and not unc_beta:
            if self.reactivity==-1:
                self.CalcRho()
            self.delta_rho=self.reactivity*1e5
            return self.delta_rho
        else:
            self.CalcRho(unc_poisson=unc_poisson,unc_beta=unc_beta)
            self.delta_rho=self.reactivity*1e5
            self.delta_rho_sig=self.reactivity_sig*1e5
            return self.delta_rho,self.delta_rho_sig

    def Plot_fit(self):
        if self.reactivity==-1:
            self.CalcRho()
        fstart=(self.Crit_start-self.measurment_start).total_seconds()+self.Mstart
        fend=(self.Crit_end-self.measurment_start).total_seconds()
        delta_T=np.arange(int((fend-fstart)/self.dwell_time))*self.dwell_time
        plt.figure()
        plt.plot(np.arange(len(self.signal_global))*self.dwell_time,self.signal_global)
        plt.plot(np.arange(len(self.signal_global))[int(fstart/self.dwell_time):int(fstart/self.dwell_time)+len(delta_T)]*self.dwell_time,self.signal_global[int(fstart/self.dwell_time)]*np.exp(self.omega*delta_T))
        print("Plot_fit stable period={}".format(1/self.omega))
        plt.xlabel("Time [s]")
        plt.ylabel("Count [-]")
        plt.yscale("log")
        plt.show()

    def Feynman_VoM(self,signal=[-1]):
        l_VoM=[]
        l_dt=[]
        if signal[0]==-1:
            signal=self.signal_global
        dt=self.dwell_time
        max_dt=len(signal)*dt//32
        l_dtm=np.unique(np.divmod(np.logspace(dt,max_dt,5000),dt)[0])
        for m in l_dtm:
            l_val=[sum(signal[i*m:(i+1)*m]) for i in range(len(signal)//m)]
            l_VoM+=[np.var(l_val)/np.mean(l_val)]
            l_dt+=[dt*m]
        plt.figure()
        plt.plot(l_dt,l_VoM)
        plt.ylabel("Var to mean ratio")
        plt.xlabel("dwell_timw [s]")
        plt.xscale("log")
        plt.show()



path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
#lcase_csv  = get_param_vari("lcase", str).split("/")
lcase_csv=["expNi_ni_fe","expNi_in1","expNi_in2","expNi_au","expNi_al","expCr_ni_fe_J311","expCr_in1_J311","expCr_in2_J311","expCr_au","expCr_al_J311","expFe_ni_fe","expFe_in1","expFe_in2","expFe_au","expFe_al","expSS_ni_fe","expSS_in1","expSS_in2","expSS_au","expSS_al","expNi_crit_h2o","expNi_crit_bcn","expNi_crit_bcs","expCr_crit_h2o","expCr_crit_bcn","expCr_crit_bcs","expSS_crit_h2o","expSS_crit_bcn","expSS_crit_bcs","expFe_crit_h2o","expFe_crit_bcn","expFe_crit_bcs","expWa_crit_h2o","expWa_crit_bcn","expWa_crit_bcs"]
tt="expNi_ni_fe/expNi_in1/expNi_in2/expNi_au/expNi_al/expCr_ni_fe_J311/expCr_in1_J311/expCr_in2_J311/expCr_au/expCr_al_J311/expFe_ni_fe/expFe_in1/expFe_in2/expFe_au/expFe_al/expSS_ni_fe/expSS_in1/expSS_in2/expSS_au/expSS_al/expNi_crit_h2o/expNi_crit_bcn/expNi_crit_bcs/expCr_crit_h2o/expCr_crit_bcn/expCr_crit_bcs/expSS_crit_h2o/expSS_crit_bcn/expSS_crit_bcs/expFe_crit_h2o/expFe_crit_bcn/expFe_crit_bcs/expWa_crit_h2o/expWa_crit_bcn/expWa_crit_bcs"
data = DataIrrad  (   path_csv_data,
                      path_csv_dosi,
                      lcase_csv,
                      use_sqrt_for_meas_sig=False,
                      load_hpge_eff=False,
                      load_sss_results=True,
                      remove_data=False,
                      keff_only=True )
d_MatDosi2babs={} #to store the rods positions

def replace_all(txt,L,res):
    for l in L:
        txt=txt.replace(l,res)
    return str(txt)
def ref_wgt(X):
    val=[]
    for x in X:
        val +=[-192.39*x**6 + 1690.9*x**5 -3473.6*x**4 +2363.3*x**3 -260.91*x**2 +37.974*x -0.001]
    return np.array(val)

def serpent_SE_wgt_PETALE(crit=192): #returns the coeficient of the fit use crit=None if no reference level to be use
    keff=np.array([1.00289,1.00293,1.00295,1.00291,1.00300,1.00311,1.00319,1.00342,1.00362,1.00372,1.00392,1.00406,1.00431,1.00440,1.00453,1.00452,1.00457,1.00459,1.00464])
    rho=(keff-1)/keff
    keff_sig=np.array([2.2,2.2,2.2,2.2,2.2,1.9,2.2,1.8,2.2,1.8,2.2,2.2,1.7,1.9,2.2,1.9,2.2,1.9,2.2])*1.e-5
    rho_sig=keff_sig/keff**2
    heights=[0,50,100,150,200,250,300,400,450,500,550,600,700,750,800,850,900,950,1000]
    def poly(X,a,b,c,d,e,f,g):
        A=[a,b,c,d,e,f,g]
    # def poly(X,a,b,c,d,e):
        # A=[a,b,c,d,e]
        val=[]
        for x in X:
            val+=[sum([A[i]*x**i for i in range(len(A))])]
        return np.array(val)
    # def poly(X,a,b,c):#sigmoid
        # A=[a,b,c,d]
        # val=[]
        # for x in X:
            # val+=[c/(1+np.exp(-a*(x+b)))]
        # return np.array(val)
    def unc_poly(X,cov): #for polynomial
        val=[]
        for x in X:
            exp=np.array([x**i for i in range(len(cov))])
            val+=[exp.dot(cov.dot(exp.T))**0.5]
        return np.array(val)
        
    # def unc_poly(X,cov):#dummy
        # return np.array(X)*0
        
    coef,cov=curve_fit(poly,heights,rho,sigma=rho_sig)
    def SE_wgt(X):   
        if crit is not None:
          rng = default_rng()
          sample_coef=rng.multivariate_normal(coef,cov,size=2**13)
          res_samp=[]
          for x in X:
              res_samp+=[np.var([poly([x],*sample_coef[i])-poly([crit],*sample_coef[i]) for i in range(len(sample_coef))])**0.5]        
          return (poly(X,*coef)-poly([crit],*coef),res_samp) # (poly(X,*coef)-poly([crit],*coef),res)
        else:
          return (poly(X,*coef),unc_poly(X,cov))
          
    return SE_wgt




def load_rod_rwgt(library="JEFF",do_nickel=False,do_plot=False,do_2004=False, do_student=False): #loads the rod reactivity wgt, returns them in dict
    path_south_nickel=["2020_12_11_14_07_00_TP3_Periodes_PETALE_38C10Ni_CHI1_1.TKA","2020_12_11_16_23_36_TP3_Periodes_PETALE_38C10Ni_CHI1_2.TKA"]
    path_south=["2020_12_02_08_11_30_PETALE_28C02wa_CHI1_1_400_1s.TKA","2020_12_02_09_47_00_PETALE_28C02wa_CHI1_2_500-600_0.4s.TKA","2020_12_02_10_37_30_PETALE_28C02wa_CHI1_3_700-800_0.4s.TKA","2020_12_02_11_31_00_PETALE_28C02wa_CHI1_4_900_0,1s.TKA","2020_12_02_11_58_00_PETALE_28C02wa_CHI1_6_1000_0.1s.TKA","2020_12_02_12_08_30_PETALE_28C02wa_CHI1_7_300_1s.TKA"]
    path_north=["2020_11_25_08_23_30_PETALE_24C01wa_CHI1_1_Critical-400_1s.TKA","2020_11_25_09_56_00_PETALE_24C01wa_CHI1_2_500-600_0,4s.TKA","2020_11_25_10_49_30_PETALE_24C01wa_CHI1_3_700-800_0,4s.TKA","2020_11_25_11_35_30_PETALE_24C01wa_CHI1_4_900_0,1s.TKA","2020_11_25_12_01_30_PETALE_24C01wa_CHI1_6_1000_0,1s.TKA"]
    path_south_student=["2022_11_23_12_05_03_TPMaster_Control rod worth_South_Mon2_100_1.0_1.TKA","200_1.TKA","300_0,2.TKA","2022_11_23_11_26_33_TPMaster_Control rod worth_South_Mon2_350_1.0.TKA","2022_11_23_09_47_28_TPMaster_Control rod worth_South_Mon2_400_1.0.TKA","450_0,1_2.TKA","600_0,04.TKA","2022_11_23_10_33_09_TPMaster_Control rod worth_South_Mon2_650_0.1.TKA","700_0,04.TKA","2022_11_23_10_15_25_TPMaster_Control rod worth_South_Mon2_800_0.04.TKA","2022_11_23_11_10_24_TPMaster_Control rod worth_South_Mon2_900_0.04.TKA","2022_11_23_09_28_13_TPMaster_Control rod worth_South_Mon2_1000_0.04.TKA"]
    north_time=lmap(lambda s: datetime.datetime(*lmap(lambda t: int(t),s.split("_"))),["2020_11_25_09_22_00","2020_11_25_09_59_00","2020_11_25_10_35_00","2020_11_25_11_01_00","2020_11_25_11_23_00","2020_11_25_11_43_00","2020_11_25_12_04_30"])
    south_time=lmap(lambda s: datetime.datetime(*lmap(lambda t: int(t),s.split("_"))),["2020_12_02_09_15_30","2020_12_02_09_51_30","2020_12_02_10_21_00","2020_12_02_10_49_30","2020_12_02_11_10_00","2020_12_02_11_34_30","2020_12_02_12_00_30","2020_12_02_12_18_00"])
    south_nickel_time=lmap(lambda s: datetime.datetime(*lmap(lambda t: int(t),s.split("_"))),["2020_12_11_14_36_00","2020_12_11_15_11_00","2020_12_11_15_35_00","2020_12_11_15_53_00","2020_12_11_16_08_00","2020_12_11_16_20_00","2020_12_11_16_30_00","2020_12_11_16_41_00"])
    north_time_end=lmap(lambda s: datetime.datetime(*lmap(lambda t: int(t),s.split("_"))),["2020_11_25_09_31_40","2020_11_25_10_07_00","2020_11_25_10_39_40","2020_11_25_11_04_25","2020_11_25_11_25_46","2020_11_25_11_45_30","2020_11_25_12_06_59"])
    south_time_end=lmap(lambda s: datetime.datetime(*lmap(lambda t: int(t),s.split("_"))),["2020_12_02_09_24_45","2020_12_02_09_59_00","2020_12_02_10_24_40","2020_12_02_10_52_50","2020_12_02_11_12_44","2020_12_02_11_37_02","2020_12_02_12_02_59","2020_12_02_12_30_28"])
    south_nickel_time_end=lmap(lambda s: datetime.datetime(*lmap(lambda t: int(t),s.split("_"))),["2020_12_11_15_01_00","2020_12_11_15_22_00","2020_12_11_15_42_00","2020_12_11_15_59_00","2020_12_11_16_11_00","2020_12_11_16_23_00","2020_12_11_16_33_00","2020_12_11_16_44_00"])
    crit_north=196
    crit_south=192
    crit_south_nickel=192
    pos_north=[400,500,600,700,800,900,1000]
    pos_south=[400,500,600,700,800,900,1000,300]
    pos_south_nickel=[350,450,550,650,750,850,950,1000]
    pos_south_student=[100,200,300,350,400,450,600,650,700,800,900,1000]
    pos_2004_n=[100.0 ,200.0 ,300.0 ,322.5 ,365.0 ,400.0 ,442.4 ,456.0 ,470.0 ,483.1 ,500.0 ,515.0 ,530.0 ,550.0 ,560.0 ,580.0 ,600.0 ,650.0 ,700.0 ,750.0 ,800.0 ,850.0 ,900.0 ,1000.0]
    periode_2004_n=[2540.341, 718.719,268.697,223.043,162.214,127.857,98.779 ,91.567 ,84.899 ,78.177 ,72.702 ,67.566 ,62.716 ,57.730 ,55.160 ,50.713 ,46.983 ,39.736 ,34.666 ,31.205 ,28.692 ,27.091 ,26.260 ,25.620]
    period_2004_sig_n=np.array([2.113,1.553,0.166,0.148,0.128,0.116,0.096,0.094,0.094,0.086,0.083,0.088,0.077,0.072,0.069,0.068,0.066,0.058,0.056,0.055,0.053,0.049,0.049,0.052])/2
    d_p2time_n={}
    d_p2time_s={}
    d_p2time_nickel_s={}
    d_p2time_student_s={}
    d_p2stime_n={}
    d_p2stime_s={}
    d_p2stime_nickel_s={}
    d_p2stime_student_s={}
    d_p2wgt_n={} # reactivity inserted in pcm
    d_p2wgt_s={} # reactivity inserted in pcm
    d_p2wgt_nickel_s={} # reactivity inserted in pcm
    d_p2wgt_student_s={} # reactivity inserted in pcm
    d_p2wgt_2004_n={} # reactivity inserted in pcm
    if library=="old":    
      betas   =[2.43e-04,1.45e-03,1.35e-03,2.96e-03,1.10e-03,3.47e-04] #enter beta_i to compute 
      lambdas =[1.29e-02,3.14e-02,1.19e-01,3.16e-01,1.197,3.495]
      gen_time=5.93e-05
    elif library=="JEFF": #With Jeff-3.3
      betas   =[22.87e-05,109.92e-05, 64.99e-05,142.22e-05,246.89e-05,80.52e-05,66.26e-05,25.00e-05] # values from Yifeng thesis with Jeff-3.3
      lambdas =[ 0.01247,0.02829,0.4252 ,0.13304,0.29247,0.66649, 1.63478, 3.55460] #values from Yifeng thesis with Jeff-3.3
      gen_time=4.7703e-05                                                                                                 #values from Yifeng thesis with Jeff-3.3
      betas_sig   =[0.24e-05, 0.53e-05, 0.41e-05, 0.60e-05, 0.80e-05, 0.46e-05, 0.41e-05, 0.25e-05] # values from Yifeng thesis with Jeff-3.3
      gen_time_sig= 0.001e-6 # values from Yifeng thesis with Jeff-3.3
    elif library=="ENDFB7":   #ENDF/B7.1 
      betas   =[23.78e-05, 126.50e-05,123.64e-05, 284.42e-05, 126.41e-05,52.47e-05] # values from Yifeng thesis 
      lambdas =[0.01338, 0.03252, 0.12118, 0.30603, 0.85826, 2.88337] #values from Yifeng thesis
      gen_time=4.7502e-05                                         #values from Yifeng thesis
      betas_sig   =[0.18e-05, 0.50e-05, 0.45e-05, 0.60e-05, 0.43e-05, 0.39e-05] #enter beta_i to compute  values from Yifeng thesis
      gen_time_sig= 0.001e-6   # values from Yifeng thesis
    else:
      print("Error: Wrong library for betas_i : exit")
      exit()      
    tau=2.531E-07
    for i in range(len(pos_north)):
        d_p2time_n[str(pos_north[i])]=north_time[i]
        d_p2stime_n[str(pos_north[i])]=north_time_end[i]
    for i in range(len(pos_south)):
        d_p2time_s[str(pos_south[i])]=south_time[i]
        d_p2stime_s[str(pos_south[i])]=south_time_end[i]
    for i in range(len(pos_south_nickel)):
        d_p2time_nickel_s[str(pos_south_nickel[i])]=south_nickel_time[i]
        d_p2stime_nickel_s[str(pos_south_nickel[i])]=south_nickel_time_end[i]
    
    # def periodes_eqt(T,P0,w1,w2,w3,w4,w5,w6,w7,B1,B2,B3,B4,B5,B6,B7):
        # B=[B1,B2,B3,B4,B5,B6,B7]
        # w=[w1,w2,w3,w4,w5,w6,w7]
        # sol=[]
        # for t in T:
            # sol+=[sum([B[i]*np.exp(w[i]*t) for i in range(len(w))])]
        # return sol
    # def periodes_eqt(T,P0,w1):
    #     sol=[]
    #     for t in T:
    #         sol+=[P0*np.exp(w1*t)]
    #     return sol
    # def periodes_eqt(T,P0,w1):
    #     sol=[]
    #     for t in T:
    #         sol+=[np.log(P0)+(w1*t)]
    #     return sol
    def periodes_eqt(T,B1,B2,w1,w2):
        sol=[]
        for t in T:
            sol+=[B1*np.exp(w1*t)+B2*np.exp(w2*t)]
        return sol
    for path in path_south:
        sp=path.split("_")
        path="power_history/south_rod_eject/"+path
        print(path)
        history=lmap(lambda s: float(s), open(path).readlines())
        start=datetime.datetime(*lmap(lambda s: int(s),sp[:6])) # file start time
        dt=float(sp[-1].split("s")[0].replace(",",".")) # dwell time
        history=np.divide(history,1-np.multiply(history,tau/dt))
        heights=sp[-2].split("-")
        for h in heights:
            if h in d_p2time_s:
                id_start=int((d_p2time_s[h]-start).total_seconds()/dt)
                #cut one sec on the end time to be sure (should not change much 
                id_stop=int((d_p2stime_s[h]-start).total_seconds()/dt-1/dt)
                sub_hist=history[id_start:id_stop]
                # coef,cov= curve_fit(periodes_eqt,range(len(sub_hist)),sub_hist,sigma=np.sqrt(sub_hist),p0=[sub_hist[0],1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1])
                est=0.05 if len(sub_hist)<300 else 0.001
                # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist)/dt,p0=[sub_hist[0],est])
                # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,np.log(sub_hist/dt),sigma=np.sqrt(sub_hist)/dt,p0=[np.log(sub_hist[0]),1e-3])
                coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist+1.0e-15)/dt,p0=[sub_hist[0]/2,sub_hist[0]/2,-1e-3,est],bounds=(np.array([-np.inf,-np.inf,-np.inf,0]),np.array([np.inf,np.inf,0,np.inf])))                
                print(id_start,id_stop)
                print(coef)
                #print(cov)
                if do_plot:
                    plt.figure()
                    plt.subplot(221)
                    plt.plot(np.arange(0,len(sub_hist))*dt,sub_hist/dt)
                    plt.plot(np.arange(0,len(sub_hist))*dt,periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef))
                    plt.subplot(223)
                    plt.plot(np.arange(0,len(sub_hist))*dt,(periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef)-sub_hist/dt)/(sub_hist**0.5/dt))
                    plt.subplot(222)
                    plt.hist((periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef)-sub_hist/dt)/(sub_hist**0.5/dt),bins=[-5,-2,-1,0,1,2,5],density=True)
                d_p2wgt_s[h]={}
                d_p2wgt_s[h]["val"]=(gen_time*coef[-1]+sum([betas[i]*coef[-1]/(coef[-1]+lambdas[i]) for i in range(len(betas))]))*1e5
                if library!="old":
                    coef_sig=np.diag(cov)[-1]**0.5             
                    rng = default_rng()
                    sample_coef=rng.normal(loc=coef[-1],scale=coef_sig,size=2**16)
                    sample_betas=[rng.normal(loc=betas[i],scale=betas_sig[i],size=2**16).tolist() for i in range(len(betas))]       
                    l_wgt=[gen_time*sample_coef[j]+sum([sample_betas[i][j]*sample_coef[j]/(sample_coef[j]+lambdas[i]) for i in range(len(lambdas))]) for j in range(len(sample_coef))]
                    d_p2wgt_s[h]["sig"]=np.var(l_wgt)**0.5 *1e5
                
    for path in path_north:
        sp=path.split("_")
        path="power_history/north_rod_eject/"+path
        print(path)
        history=lmap(lambda s: float(s), open(path).readlines())
        start=datetime.datetime(*lmap(lambda s: int(s),sp[:6])) # file start time
        dt=float(sp[-1].split("s")[0].replace(",",".")) # dwell time
        history=np.divide(history,1-np.multiply(history,tau/dt))
        heights=sp[-2].split("-")
        for h in heights:
            if h in d_p2time_n:
                id_start=int((d_p2time_n[h]-start).total_seconds()/dt)
                #cut one sec on the end time to be sure (should not change much 
                id_stop=int((d_p2stime_n[h]-start).total_seconds()/dt-1/dt)
                sub_hist=history[id_start:id_stop]
                # coef,cov= curve_fit(periodes_eqt,range(len(sub_hist)),sub_hist,sigma=np.sqrt(sub_hist),p0=[sub_hist[0],1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1])
                est=0.05 if len(sub_hist)<300 else 0.001
                # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist)/dt,p0=[sub_hist[0],est])
                # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,np.log(sub_hist/dt),sigma=np.sqrt(sub_hist)/dt,p0=[np.log(sub_hist[0]),1e-3])
                coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist+1.0e-15)/dt,p0=[sub_hist[0]/2,sub_hist[0]/2,-1e-3,est],bounds=(np.array([-np.inf,-np.inf,-np.inf,0]),np.array([np.inf,np.inf,0,np.inf])))
                print(id_start,id_stop)
                print(coef)
                #print(cov)
                if do_plot:
                    plt.figure()
                    plt.subplot(221)
                    plt.plot(np.arange(0,len(sub_hist))*dt,sub_hist/dt)
                    plt.plot(np.arange(0,len(sub_hist))*dt,periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef))
                    plt.subplot(223)
                    plt.plot(np.arange(0,len(sub_hist))*dt,(periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef)-sub_hist/dt)/(sub_hist**0.5/dt))
                    plt.subplot(222)
                    plt.hist((periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef)-sub_hist/dt)/(sub_hist**0.5/dt),bins=[-5,-2,-1,0,1,2,5],density=True)
                d_p2wgt_n[h]={}
                # d_p2wgt_n[h]["val"]=(gen_time*coef[1]+sum([betas[i]*coef[1]/(coef[1]+lambdas[i]) for i in range(len(betas))]))*1e5
                d_p2wgt_n[h]["val"]=(gen_time*coef[-1]+sum([betas[i]*coef[-1]/(coef[-1]+lambdas[i]) for i in range(len(betas))]))*1e5
                x = Symbol('x')
                res=solve(gen_time*x+sum([betas[i]*x/(x+lambdas[i]) for i in range(len(betas))])-d_p2wgt_n[h]["val"]/1e5,x)
                print("res")
                print(res)
                if library!="old":
                    coef_sig=np.diag(cov)[-1]**0.5             
                    rng = default_rng()
                    sample_coef=rng.normal(loc=coef[-1],scale=coef_sig,size=2**16)
                    sample_betas=[rng.normal(loc=betas[i],scale=betas_sig[i],size=2**16).tolist() for i in range(len(betas))]       
                    l_wgt=[gen_time*sample_coef[j]+sum([sample_betas[i][j]*sample_coef[j]/(sample_coef[j]+lambdas[i]) for i in range(len(lambdas))]) for j in range(len(sample_coef))]
                    d_p2wgt_n[h]["sig"]=np.var(l_wgt)**0.5 *1e5                
    
    if do_nickel:
      it=0
      heights=[["350","450","550","650","750","850"],["950","1000"]]
      for path in path_south_nickel:
        it+=1
        sp=path.split("_")
        path="power_history/south_rod_eject_nickel/"+path
        print(path)
        history=lmap(lambda s: float(s), open(path).readlines())
        start=datetime.datetime(*lmap(lambda s: int(s),sp[:6])) # file start time
        dt=1. # dwell time
        history=np.divide(history,1-np.multiply(history,tau/dt))
        for h in heights[it-1]:
            if h in d_p2time_nickel_s:
                # print(h)
                id_start=int((d_p2time_nickel_s[h]-start).total_seconds()/dt)
                #cut one sec on the end time to be sure (should not change much 
                id_stop=int((d_p2stime_nickel_s[h]-start).total_seconds()/dt-1/dt)
                sub_hist=history[id_start+int(120/dt):id_stop]
                # coef,cov= curve_fit(periodes_eqt,range(len(sub_hist)),sub_hist,sigma=np.sqrt(sub_hist),p0=[sub_hist[0],1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1])
                est=0.05 if len(sub_hist)<300 else 0.001
                # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist)/dt,p0=[sub_hist[0],est])
                # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,np.log(sub_hist/dt),sigma=np.sqrt(sub_hist)/dt,p0=[np.log(sub_hist[0]),1e-3])
                coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist+1.0e-15)/dt,p0=[sub_hist[0]/2,sub_hist[0]/2,-1e-3,est],bounds=(np.array([-np.inf,-np.inf,-np.inf,0]),np.array([np.inf,np.inf,0,np.inf])))
                print(id_start,id_stop)
                print(coef)
                #print(cov)
                if do_plot:
                    plt.figure()
                    plt.subplot(221)
                    plt.plot(np.arange(0,len(sub_hist))*dt,sub_hist/dt)
                    plt.plot(np.arange(0,len(sub_hist))*dt,periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef))
                    plt.subplot(223)
                    plt.plot(np.arange(0,len(sub_hist))*dt,(periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef)-sub_hist/dt)/(sub_hist**0.5/dt))
                    plt.subplot(222)
                    plt.hist((periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef)-sub_hist/dt)/(sub_hist**0.5/dt),bins=[-5,-2,-1,0,1,2,5],density=True)
                d_p2wgt_nickel_s[h]={}
                # d_p2wgt_nickel_s[h]["val"]=(gen_time*coef[1]+sum([betas[i]*coef[1]/(coef[1]+lambdas[i]) for i in range(len(betas))]))*1e5
                d_p2wgt_nickel_s[h]["val"]=(gen_time*coef[-1]+sum([betas[i]*coef[-1]/(coef[-1]+lambdas[i]) for i in range(len(betas))]))*1e5
                x = Symbol('x')
                res=solve(gen_time*x+sum([betas[i]*x/(x+lambdas[i]) for i in range(len(betas))])-d_p2wgt_nickel_s[h]["val"]/1e5,x)
                print("res")
                print(res)
                if library!="old":
                    coef_sig=np.diag(cov)[-1]**0.5             
                    rng = default_rng()
                    sample_coef=rng.normal(loc=coef[-1],scale=coef_sig,size=2**16)
                    sample_betas=[rng.normal(loc=betas[i],scale=betas_sig[i],size=2**16).tolist() for i in range(len(betas))]       
                    l_wgt=[gen_time*sample_coef[j]+sum([sample_betas[i][j]*sample_coef[j]/(sample_coef[j]+lambdas[i]) for i in range(len(lambdas))]) for j in range(len(sample_coef))]
                    d_p2wgt_nickel_s[h]["sig"]=np.var(l_wgt)**0.5 *1e5
      return d_p2wgt_nickel_s    
      
    if do_student:
      it=0
      for path in path_south_student:
        h=pos_south_student[it]
        sp=path.split("_")
        path="power_history/south_rod_student/"+path
        print(path)
        history=lmap(lambda s: float(s), open(path).readlines())
        id_start=0 # file start time
        dt=float(path.split("_")[-1][:-4].replace(",",".")) # dwell time
        history=np.divide(history,1-np.multiply(history,tau/dt))
        # print(h)
        #cut one sec on the end time to be sure (should not change much 
        id_stop=np.argmax(history)
        sub_hist=history[id_start+10:id_stop]
        sub_hist[sub_hist==0]=0.01
        # coef,cov= curve_fit(periodes_eqt,range(len(sub_hist)),sub_hist,sigma=np.sqrt(sub_hist),p0=[sub_hist[0],1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1])
        est=0.05 if len(sub_hist)<300 else 0.001
        # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist)/dt,p0=[sub_hist[0],est])
        # coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,np.log(sub_hist/dt),sigma=np.sqrt(sub_hist)/dt,p0=[np.log(sub_hist[0]),1e-3])
        coef,cov= curve_fit(periodes_eqt,np.arange(0,len(sub_hist))*dt,sub_hist/dt,sigma=np.sqrt(sub_hist+1.0e-15)/dt,p0=[sub_hist[0]/2,sub_hist[0]/2,-1e-3,est],bounds=(np.array([-np.inf,-np.inf,-np.inf,0]),np.array([np.inf,np.inf,0,np.inf])))
        print(id_start,id_stop)
        print(coef)
        #print(cov)
        if do_plot:
            plt.figure()
            plt.subplot(221)
            plt.plot(np.arange(0,len(sub_hist))*dt,sub_hist/dt)
            plt.plot(np.arange(0,len(sub_hist))*dt,periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef))
            plt.subplot(223)
            plt.plot(np.arange(0,len(sub_hist))*dt,(periodes_eqt(np.arange(0,len(sub_hist+1.0e-15))*dt,*coef)-sub_hist/dt)/(sub_hist**0.5/dt))
            plt.subplot(222)
            plt.hist((periodes_eqt(np.arange(0,len(sub_hist))*dt,*coef)-sub_hist/dt)/((sub_hist+1.0e-15)**0.5/dt),bins=[-5,-2,-1,0,1,2,5],density=True)
        d_p2wgt_student_s[h]={}
        # d_p2wgt_nickel_s[h]["val"]=(gen_time*coef[1]+sum([betas[i]*coef[1]/(coef[1]+lambdas[i]) for i in range(len(betas))]))*1e5
        d_p2wgt_student_s[h]["val"]=(gen_time*coef[-1]+sum([betas[i]*coef[-1]/(coef[-1]+lambdas[i]) for i in range(len(betas))]))*1e5
        x = Symbol('x')
        res=solve(gen_time*x+sum([betas[i]*x/(x+lambdas[i]) for i in range(len(betas))])-d_p2wgt_student_s[h]["val"]/1e5,x)
        print("res")
        print(res)
        if library!="old":
            coef_sig=np.diag(cov)[-1]**0.5
            rng = default_rng()
            sample_coef=rng.normal(loc=coef[-1],scale=coef_sig,size=2**16)
            sample_betas=[rng.normal(loc=betas[i],scale=betas_sig[i],size=2**16).tolist() for i in range(len(betas))]       
            l_wgt=[gen_time*sample_coef[j]+sum([sample_betas[i][j]*sample_coef[j]/(sample_coef[j]+lambdas[i]) for i in range(len(lambdas))]) for j in range(len(sample_coef))]
            d_p2wgt_student_s[h]["sig"]=np.var(l_wgt)**0.5 *1e5
        it+=1
      return d_p2wgt_student_s
      
    if do_2004:
      for k in range(len(pos_2004_n)):
        omega=1/periode_2004_n[k]
        omega_sig=period_2004_sig_n[k]/periode_2004_n[k]/periode_2004_n[k]
        d_p2wgt_2004_n[str(pos_2004_n[k])]={}
        d_p2wgt_2004_n[str(pos_2004_n[k])]["val"]=(gen_time*omega+sum([betas[i]*omega/(omega+lambdas[i]) for i in range(len(betas))]))*1e5
        x = Symbol('x')
        res=solve(gen_time*x+sum([betas[i]*x/(x+lambdas[i]) for i in range(len(betas))])-d_p2wgt_2004_n[str(pos_2004_n[k])]["val"]/1e5,x)
        print("res")
        print(res)
        if library!="old":          
            rng = default_rng()
            sample_coef=rng.normal(loc=omega,scale=omega_sig,size=2**16)
            sample_betas=[rng.normal(loc=betas[i],scale=betas_sig[i],size=2**16).tolist() for i in range(len(betas))]       
            l_wgt=[gen_time*sample_coef[j]+sum([sample_betas[i][j]*sample_coef[j]/(sample_coef[j]+lambdas[i]) for i in range(len(lambdas))]) for j in range(len(sample_coef))]
            d_p2wgt_2004_n[str(pos_2004_n[k])]["sig"]=np.var(l_wgt)**0.5 *1e5
      return d_p2wgt_2004_n
    return d_p2wgt_s, d_p2wgt_n


if False:
    '''
    for i in range(len(data.l_compo_plate)):
        if data.l_compo_plate[i] not in d_MatDosi2babs:
            d_MatDosi2babs[data.l_compo_plate[i]]={}
            d_MatDosi2babs[data.l_compo_plate[i]][data.l_case_csv[i][6:]]={"NO":data.CR_north_cm[i],"SE":data.CR_south_cm[i]}
        elif data.l_case_csv[i] not in d_MatDosi2babs[data.l_compo_plate[i]]:
            d_MatDosi2babs[data.l_compo_plate[i]][data.l_case_csv[i][6:]]={"NO":data.CR_north_cm[i],"SE":data.CR_south_cm[i]}
    # print(d_MatDosi2babs)
    wgt_s,wgt_n=load_rod_rwgt(library="old")
    print(wgt_s)
    toplotx_s=[]
    toploty_s=[]
    toplotx_n=[]
    toploty_n=[]
    for key in [*wgt_s]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_s[key]["val"]]
    for key in [*wgt_n]:
        toplotx_n+=[float(key)]
        toploty_n+=[wgt_n[key]["val"]]
    plt.figure(100)
    plt.plot(toplotx_s,toploty_s,linestyle="",marker=".",label="south control rod, old")
    plt.plot(toplotx_n,toploty_n,linestyle="",marker=".",label="north control rod, old")
    # plt.xlabel("Control rod height [mm]")
    # plt.ylabel("reactivity (pcm)")
    # plt.legend()
    # plt.grid(which="both")


    wgt_s,wgt_n=load_rod_rwgt(do_plot=False)
    print(wgt_s)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_s]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_s[key]["val"]]
        toploty_s_sig+=[wgt_s[key]["sig"]]
    for key in [*wgt_n]:
        toplotx_n+=[float(key)]
        toploty_n+=[wgt_n[key]["val"]]
        toploty_n_sig+=[wgt_n[key]["sig"]]
    plt.figure(100)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, JEFF-3.3")
    plt.errorbar(toplotx_n,toploty_n,yerr=toploty_n_sig,linestyle="",marker=".",label="north control rod, JEFF-3.3")
    # plt.xlabel("Control rod height [mm]")
    # plt.ylabel("reactivity (pcm)")
    # plt.legend()
    # plt.grid(which="both")


    wgt_s,wgt_n=load_rod_rwgt(library="ENDFB7")
    print(wgt_s)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_s]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_s[key]["val"]]
        toploty_s_sig+=[wgt_s[key]["sig"]]
    for key in [*wgt_n]:
        toplotx_n+=[float(key)]
        toploty_n+=[wgt_n[key]["val"]]
        toploty_n_sig+=[wgt_n[key]["sig"]]
    plt.figure(100)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, ENDF/B-VII.1")
    plt.errorbar(toplotx_n,toploty_n,yerr=toploty_n_sig,linestyle="",marker=".",label="north control rod, ENDF/B-VII.1")


    plt.plot(range(300,1000),ref_wgt(np.divide(list(range(300,1000)),1000)),label="Reference curve")
    plt.plot(range(300,1000),ref_wgt(np.divide(list(range(300,1000)),1000))*max(toploty_s)/ref_wgt([1]),label="Reference curve renorm")



    plt.xlabel("Control rod height [mm]")
    plt.ylabel("reactivity (pcm)")
    plt.legend()
    plt.grid(which="both")

    '''
    plt.figure(200)
    rwgt_serpent=serpent_SE_wgt_PETALE(crit=None)
    keff=np.array([1.00289,1.00293,1.00295,1.00291,1.00300,1.00311,1.00319,1.00342,1.00362,1.00372,1.00392,1.00406,1.00431,1.00440,1.00453,1.00452,1.00457,1.00459,1.00464])
    rho=(keff-1)/keff
    keff_sig=np.array([2.2,2.2,2.2,2.2,2.2,1.9,2.2,1.8,2.2,1.8,2.2,2.2,1.7,1.9,2.2,1.9,2.2,1.9,2.2])*1.e-5
    rho_sig=keff_sig/keff**2
    heights=[0,50,100,150,200,250,300,400,450,500,550,600,700,750,800,850,900,950,1000]
    (value,sig_val)=rwgt_serpent(range(0,1000))
    value=np.multiply(value,1.e5)
    print(value[192])
    sig_val=np.multiply(sig_val,1.e5)
    plt.plot(range(0,1000),value-value[192],label="serpent sim wgt fit")
    plt.fill_between(range(0,1000),value-value[192]-sig_val,value-value[192]+sig_val,label=None,alpha=0.2)
    plt.errorbar(heights,np.multiply(rho,1.e5)-value[192],yerr=np.multiply(2*rho_sig,1.e5),linestyle="",marker=".",label="south control rod, ENDF/B-VII.1")
    # plt.errorbar(heights,np.multiply(rho-rho[0],1.e5),yerr=np.multiply(2*rho_sig,1.e5),linestyle="",marker=".",label="south control rod, ENDF/B-VII.1")
    plt.xlabel("Control rod height [mm]")
    plt.ylabel("reactivity (pcm)")
    plt.legend()
    plt.grid(which="both")
    '''

    wgt_nickel=load_rod_rwgt(library="old",do_nickel=True)
    print(wgt_nickel)
    toplotx_s=[]
    toploty_s=[]
    toplotx_n=[]
    toploty_n=[]
    for key in [*wgt_nickel]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_nickel[key]["val"]]
    plt.figure(300)
    plt.plot(toplotx_s,toploty_s,linestyle="",marker=".",label="south control rod, old")
    # plt.xlabel("Control rod height [mm]")
    # plt.ylabel("reactivity (pcm)")
    # plt.legend()
    # plt.grid(which="both")


    wgt_nickel=load_rod_rwgt(do_nickel=True,do_plot=True)
    print(wgt_nickel)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_nickel]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_nickel[key]["val"]]
        toploty_s_sig+=[wgt_nickel[key]["sig"]]
    plt.figure(300)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, JEFF-3.3")
    # plt.xlabel("Control rod height [mm]")
    # plt.ylabel("reactivity (pcm)")
    # plt.legend()
    # plt.grid(which="both")


    wgt_nickel=load_rod_rwgt(library="ENDFB7",do_nickel=True)
    print(wgt_nickel)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_nickel]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_nickel[key]["val"]]
        toploty_s_sig+=[wgt_nickel[key]["sig"]]
    plt.figure(300)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, ENDF/B-VII.1")

    plt.plot(range(0,1000),ref_wgt(np.divide(list(range(0,1000)),1000)),label="Reference curve")
    plt.plot(range(0,1000),ref_wgt(np.divide(list(range(0,1000)),1000))*np.mean(np.divide(toploty_s,ref_wgt([0.350,0.450,0.550,0.650,0.750,0.850,0.950,1.000]))),label="Reference curve renorm")

    '''

    wgt_student=load_rod_rwgt(library="old",do_student=True)
    print(wgt_student)
    toplotx_s=[]
    toploty_s=[]
    toplotx_n=[]
    toploty_n=[]
    for key in [*wgt_student]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_student[key]["val"]]
    plt.figure(3000)
    plt.plot(toplotx_s,toploty_s,linestyle="",marker=".",label="south control rod, old")
    # plt.xlabel("Control rod height [mm]")
    # plt.ylabel("reactivity (pcm)")
    # plt.legend()
    # plt.grid(which="both")


    wgt_student=load_rod_rwgt(do_student=True,do_plot=True)
    print(wgt_student)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_student]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_student[key]["val"]]
        toploty_s_sig+=[wgt_student[key]["sig"]]
    plt.figure(3000)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, JEFF-3.3")
    # plt.xlabel("Control rod height [mm]")
    # plt.ylabel("reactivity (pcm)")
    plt.legend()
    # plt.grid(which="both")

    '''
    wgt_student=load_rod_rwgt(library="ENDFB7",do_student=True)
    print(wgt_student)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_student]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_student[key]["val"]]
        toploty_s_sig+=[wgt_student[key]["sig"]]
    plt.figure(3000)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, ENDF/B-VII.1")
    '''
    plt.plot(range(0,1000),ref_wgt(np.divide(list(range(0,1000)),1000)),label="Reference curve")
    plt.plot(range(0,1000),ref_wgt(np.divide(list(range(0,1000)),1000))*np.mean(np.divide(toploty_s,ref_wgt([100,200,300,350,400,450,600,650,700,800,900,1000]))),label="Reference curve renorm")


    '''



    wgt_nickel=load_rod_rwgt(do_2004=True)
    print(wgt_nickel)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_nickel]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_nickel[key]["val"]]
        toploty_s_sig+=[wgt_nickel[key]["sig"]]
    plt.figure(300)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, JEFF-3.3, 2004")
    # plt.xlabel("Control rod height [mm]")
    # plt.ylabel("reactivity (pcm)")
    # plt.legend()
    # plt.grid(which="both")


    wgt_nickel=load_rod_rwgt(library="ENDFB7",do_2004=True)
    print(wgt_nickel)
    toplotx_s=[]
    toploty_s=[]
    toploty_s_sig=[]
    toplotx_n=[]
    toploty_n=[]
    toploty_n_sig=[]
    for key in [*wgt_nickel]:
        toplotx_s+=[float(key)]
        toploty_s+=[wgt_nickel[key]["val"]]
        toploty_s_sig+=[wgt_nickel[key]["sig"]]
    plt.figure(300)
    plt.errorbar(toplotx_s,toploty_s,yerr=toploty_s_sig,linestyle="",marker=".",label="south control rod, ENDF/B-VII.1, 2004")

    # def fsin(X,a,b,c):
        # val=[]
        # for x in X:
            # val+=[a*np.sin(b*x+c)-a*np.sin(c)]
        # return val
    # coef,cov=curve_fit(fsin,toplotx_s,toploty_s,sigma=toploty_s_sig,p0=[max(toploty_s)/2,0.003,-1.57])
    # plt.plot(range(0,1000),fsin(range(0,1000),*coef),label="test curve")

    plt.xlabel("Control rod height [mm]")
    plt.ylabel("reactivity (pcm)")
    plt.legend()
    plt.grid(which="both")

    '''
########################################################################################################################
#Start of the reactivity worth calculation part
ref_worth_SE=serpent_SE_wgt_PETALE(crit=207) #reprendre ici
print("south values 177 and 197:",ref_worth_SE([177,197]))
ref_worth_NW=serpent_SE_wgt_PETALE(crit=191) #for now only SE ref usable
print("north values 1000:",ref_worth_NW([1000]))
keff=data.l_sss_keff
moni=data.l_monitor_path
rho=(keff-1)/keff
keff_s=data.l_sss_keff_s
rho_s=keff_s/keff**2
l_case=data.l_case_csv
l_pos_SE=data.CR_south_cm*10
l_pos_NW=data.CR_north_cm*10
l_pos_Wa=data.l_water_lvl_cm*10
print(l_pos_SE)
dico={"Exp":l_case, "rho":rho,"rho_sig":rho_s,"SE_pos":l_pos_SE,"SE_worth":ref_worth_SE(l_pos_SE)[0],"NW_pos":l_pos_NW,"NW_worth":ref_worth_NW(l_pos_NW)[0],"Water_worth":(963.0 - l_pos_Wa)*4.18*1e-5,"total_worth":l_pos_Wa*0,"moni_path":moni,
      "F_start":data.hh_mm_ss_start,"M_start":data.l_irrad_HH_start,"M_end":data.l_irrad_HH_stop}
# 
for i in range(len(dico["Exp"])):
    if "bcn" not in dico["Exp"][i] and "Ni" not in dico["Exp"][i]:
        dico["NW_worth"][i]=0
    if "bcs" not in dico["Exp"][i] and "Ni" not in dico["Exp"][i]:
        dico["SE_worth"][i]=0
    if "h2o" not in dico["Exp"][i]:
        dico["Water_worth"][i]=0
    dico["total_worth"][i]=dico["NW_worth"][i]+dico["SE_worth"][i]+dico["Water_worth"][i]
    
data_sss_keff= pd.DataFrame(data=dico)
data_sss_keff= data_sss_keff.drop_duplicates(subset=["Exp"])
data_rho=data_sss_keff.set_index("Exp")
print(data_rho)
# for ind in data_rho.index:
#     if "crit" in ind:
#         print(ind, (data_rho.loc[ind].loc["total_worth"]-data_rho.loc[replace_all(ind,["Ni","Fe","SS","Cr"],"Wa")].loc["total_worth"])*1e5,"pcm")

base="dum"
Drho=[]
A_rho=[]
A_rho_s=[]
Drho_s=[]
Cor_rho=[]
Cor_rho_s=[]
Drho_corr=[]
Drho_corr_s=[]
Names=data_sss_keff["Exp"].to_list()
l_Name=[]


l_val=[]
for i in range(len(Names)):
    A_rho  +=[1e5*(data_rho["rho"][i])]
    A_rho_s  +=[1e5*(data_rho["rho_sig"][i])]
    if "crit" in Names[i]:
       print(Names[i])
       l_Name+=[Names[i]]
       DC=DataCrit(data_rho["moni_path"][i],Mes_start=data_rho["F_start"][i],P_start=data_rho["M_start"][i],P_end=data_rho["M_end"][i])
       val=DC.Delta_rho()
    #    DC.Plot_fit()
       l_val+=[val]
       Drho  +=[1e5*(data_rho["rho"][i]-data_rho.loc[replace_all(Names[i],["Ni","Fe","SS","Cr"],"Wa")].loc["rho"])]
       Drho_s+=[1e5*(data_rho["rho_sig"][i]**2 + data_rho.loc[replace_all(Names[i],["Ni","Fe","SS","Cr"],"Wa")].loc["rho_sig"]**2)**0.5]
       Drho_corr  +=[(1e5*data_rho["rho"][i] - val  -1e5*data_rho.loc[replace_all(Names[i],["Ni","Fe","SS","Cr"],"Wa")].loc["rho"])]
    #    Drho_corr_s+=[1e5*(data_rho["rho_sig"][i]**2 + data_rho.loc[replace_all(Names[i],["Ni","Fe","SS","Cr"],"Wa")].loc["rho_sig"]**2)**0.5]
    #    DC.CalcRho()
       Cor_rho+=[DC.Delta_rho()]
       Cor_rho_s+=[DC.Delta_rho(True)[1]]
    else:
        l_val+=[0]
data_rho["Deviation_pcm"]=l_val 
data_rho.to_excel("reactivity_worths.xlsx")
i=0
for ind in data_rho.index:
    if "crit" in ind:
        print(ind, (data_rho.loc[ind].loc["total_worth"]-data_rho.loc[replace_all(ind,["Ni","Fe","SS","Cr"],"Wa")].loc["total_worth"])*1e5-Cor_rho[i]+Cor_rho[9+i%3],"pcm")
        i+=1
Drho  =np.array(Drho  )
print("Delta_rho 197 cm: {} pcm".format(ref_worth_SE([197])[0]-ref_worth_SE([187])[0]))
print("Delta_rho 207 cm: {} pcm".format(ref_worth_SE([207])[0]-ref_worth_SE([187])[0]))
plt.figure()
plt.errorbar(np.arange(len(A_rho)),A_rho,A_rho_s,linestyle="")
l_c_all=["k"]*20+["r","b","g","r","b","g","r","b","g","r","b","g","r","b","g"]
for i in range(len(A_rho)):
    plt.errorbar(np.arange(len(A_rho))[i],A_rho[i],A_rho_s[i],c=l_c_all[i],linestyle="")
    plt.text(i+0.1,A_rho[i],Names[i][3:5].replace("SS","304L"))
plt.ylabel("Reactivity worth (pcm)")
plt.xlabel("Experiment (-)")
Drho_corr  =np.array(Drho_corr  )
Drho_s=np.array(Drho_s)
Cor_rho=np.array(Cor_rho)
print(Cor_rho)
print(Cor_rho_s)
fig=plt.figure()
plt.subplot(221)
# plt.errorbar(range(len(Drho[:-3])),Drho[:-3],(Drho_s[:-3]**2-0.5**2)**0.5,linestyle="")
l_c=["r","b","g","r","b","g","r","b","g","r","b","g"]
for i in range(12):
    plt.errorbar(range(len(Drho[:-3]))[i],Drho[:-3][i],((Drho_s[:-3]**2-0.5**2)**0.5)[i],c=l_c[i],linestyle="")
    plt.text(i+0.1,Drho[:-3][i],l_Name[:-3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho[:-3]),-0.5,11.5)
plt.title("All Configuration wrt. Water")
plt.xlim(-0.5,11.5)
plt.ylabel(r"$\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
plt.subplot(222)
plt.errorbar(range(len(Drho[0:-3:3])),Drho[0:-3:3],(Drho_s[0:-3:3]**2-0.5**2)**0.5,c=l_c[0],linestyle="")
for i in range(4):
    plt.text(i+0.1,Drho[0:-3:3][i],l_Name[0:-3:3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho[0:-3:3]),-0.5,3.5)
plt.title("Water level criticality")
plt.xlim(-0.5,3.5)
plt.ylabel(r"$\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
plt.subplot(223)
plt.errorbar(range(len(Drho[1:-3:3])),Drho[1:-3:3],(Drho_s[1:-3:3]**2-0.5**2)**0.5,c=l_c[1],linestyle="")
for i in range(4):
    plt.text(i+0.1,Drho[1:-3:3][i],l_Name[1:-3:3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho[1:-3:3]),-0.5,3.5)
plt.title("North Control Rod Criticality")
plt.xlim(-0.5,3.5)
plt.ylabel(r"$\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
plt.subplot(224)
plt.errorbar(range(len(Drho[2:-3:3])),Drho[2:-3:3],(Drho_s[2:-3:3]**2-0.5**2)**0.5,c=l_c[2],linestyle="")
for i in range(4):
    plt.text(i+0.1,Drho[2:-3:3][i],l_Name[2:-3:3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho[2:-3:3]),-0.5,3.5)
plt.title("South Control Rod Criticality")
plt.xlim(-0.5,3.5)
plt.ylabel(r"$\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
fig.tight_layout()

tmp=np.array(Drho_corr[-3:].tolist()*4)
fig=plt.figure()
plt.subplot(221)
# plt.errorbar(range(len(Drho[:-3])),Drho_corr[:-3]+tmp,(Drho_s[:-3]**2-0.5**2)**0.5,linestyle="")
# print(Drho_corr[:-3]+tmp)
for i in range(12):
    plt.errorbar(range(len(Drho[:-3]))[i],(Drho_corr[:-3]+tmp)[i],((Drho_s[:-3]**2-0.5**2)**0.5)[i],c=l_c[i],linestyle="")
    plt.text(i+0.1,Drho_corr[:-3][i],l_Name[:-3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho_corr[:-3]),-0.5,11.5)
plt.title("All Configuration wrt. Water")
plt.xlim(-0.5,11.5)
plt.ylabel(r"Corrected $\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
plt.subplot(222)
plt.errorbar(range(len(Drho[0:-3:3])),Drho_corr[0:-3:3]+Drho_corr[-3],(Drho_s[0:-3:3]**2-0.5**2)**0.5,c=l_c[0],linestyle="")
for i in range(4):
    plt.text(i+0.1,Drho_corr[0:-3:3][i],l_Name[0:-3:3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho_corr[0:-3:3]),-0.5,3.5)
plt.title("Water level criticality")
plt.xlim(-0.5,3.5)
plt.ylabel(r"Corrected $\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
plt.subplot(223)
plt.errorbar(range(len(Drho[1:-3:3])),Drho_corr[1:-3:3]+Drho_corr[-2],(Drho_s[1:-3:3]**2-0.5**2)**0.5,c=l_c[1],linestyle="")
for i in range(4):
    plt.text(i+0.1,Drho_corr[1:-3:3][i],l_Name[1:-3:3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho_corr[1:-3:3]),-0.5,3.5)
plt.title("North Control Rod Criticality")
plt.xlim(-0.5,3.5)
plt.ylabel(r"Corrected $\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
plt.subplot(224)
plt.errorbar(range(len(Drho[2:-3:3])),Drho_corr[2:-3:3]+Drho_corr[-1],(Drho_s[2:-3:3]**2-0.5**2)**0.5,c=l_c[2],linestyle="")
for i in range(4):
    plt.text(i+0.1,Drho_corr[2:-3:3][i],l_Name[1:-3:3][i][3:5].replace("SS","304L"))
plt.hlines(np.mean(Drho_corr[2:-3:3]),-0.5,3.5)
plt.title("South Control Rod Criticality")
plt.xlim(-0.5,3.5)
plt.ylabel(r"Corrected $\Delta \rho$ (pcm)")
plt.xlabel("Experiment (-)")
fig.tight_layout()
plt.show()

exit()
#without In1 because too short irrad (not always critical)
dosi=["au","in2","ni_fe","al"]
reflector=["Ni","Cr","Fe","SS"]
Mat_model=np.zeros((len(data_sss_keff)-4,4+4+1))
i=0
rho_wo_in1=[]
rho_wo_in1_sig=[]
pos_wo_in1_SE=[]
pos_wo_in1_NW=[]
for j in range(len(data_sss_keff["Exp"].tolist())):
  if 'in1' not in data_sss_keff["Exp"].tolist()[j]:
    Mat_model[i,0]=1
    Mat_model[i,1+reflector.index(data_sss_keff["Exp"].tolist()[j][3:5])]=1
    Mat_model[i,5+dosi.index(data_sss_keff["Exp"].tolist()[j][6:])]=1
    rho_wo_in1     += [data_sss_keff["rho"].tolist()[j]]
    rho_wo_in1_sig += [data_sss_keff["rho_sig"].tolist()[j]]
    pos_wo_in1_SE     += [data_sss_keff["SE_pos"].tolist()[j]]
    pos_wo_in1_NW     += [data_sss_keff["NW_pos"].tolist()[j]]
    i+=1
print(data_sss_keff)
print(Mat_model)
rho_wo_in1     =np.array(rho_wo_in1    )  
rho_wo_in1_sig =np.array(rho_wo_in1_sig)
l_worth    =ref_worth_SE(pos_wo_in1_SE)[0] +ref_worth_NW(pos_wo_in1_NW)[0] #TODO + or -  ref_worth_NW(pos_wo_in1_NW)
l_worth_sig=ref_worth_SE(pos_wo_in1_SE)[1] +ref_worth_NW(pos_wo_in1_NW)[1] #TODO + or -  ref_worth_NW(pos_wo_in1_NW)

print(l_worth)
D=np.linalg.inv(Mat_model.T.dot(Mat_model))
U=D.dot(Mat_model.T)
Res=U.dot(rho_wo_in1-l_worth)
Res_sig=D.dot(np.ones(len(D))*np.mean(rho_wo_in1_sig))

print(Res)
print(Res_sig)

df=pd.DataFrame(data=np.c_[rho_wo_in1-l_worth,Mat_model[:,1:]],columns=["rho","Ni","Cr","Fe","SS","Au","in2","ni_fe","Al"])
formula='rho ~ Ni + Cr + Fe + SS + Au + in2 + ni_fe + Al ' # we keep the constant to cope with the fact that the xs library changed
model=ols(formula,data=df)
fitted=model.fit()

print(fitted.summary())
print(fitted.params*1e5)

print(rho_wo_in1-l_worth)



df=pd.DataFrame(data=np.c_[-l_worth,Mat_model[:,1:]],columns=["rho","Ni","Cr","Fe","SS","Au","in2","ni_fe","Al"])
formula='rho ~ Ni + Cr + Fe + SS + Au + in2 + ni_fe + Al ' # we keep the constant to cope with the fact that the xs library changed
model=ols(formula,data=df)
fitted=model.fit()

print(fitted.summary())
print(fitted.params*1e5)

df=pd.DataFrame(data=np.c_[-l_worth,Mat_model[:,1:]],columns=["rho","Ni","Cr","Fe","SS","Au","in2","ni_fe","Al"])
formula='rho ~ Ni + Cr + Fe + SS + Au + in2 + ni_fe + Al -1' # we keep the constant to cope with the fact that the xs library changed
model=ols(formula,data=df)
fitted=model.fit()

print(fitted.summary())
print(fitted.params*1e5)

tmp_f=serpent_SE_wgt_PETALE(crit=None)
rho_ref_new=tmp_f([192])[0]
corr=rho_ref_new-np.mean(rho_wo_in1)
print(tmp_f([192])[0])
print(corr)

df=pd.DataFrame(data=np.c_[-(l_worth-corr),Mat_model[:,1:]],columns=["rho","Ni","Cr","Fe","SS","Au","in2","ni_fe","Al"])
formula='rho ~ Ni + Cr + Fe + SS + Au + in2 + ni_fe + Al ' # we keep the constant to cope with the fact that the xs library changed
model=ols(formula,data=df)
fitted=model.fit()

print(fitted.summary())
print(fitted.params*1e5)

plt.show()
