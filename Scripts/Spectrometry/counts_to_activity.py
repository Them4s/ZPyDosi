#cd "$petale_analysis"/irrad/petale 
#py ../../python/hpge/counts_to_activity.py csv_data=$csv_data csv_dosi=$csv_dosi lcase=$case


from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.Common.ExcelSheet import ExcelSheet
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.DosiFunctions.Dictionaries import d_spectro
from ZPyDosi.Common.GetParam import get_param_vari
import numpy as np
import datetime
import matplotlib.pyplot as plt
# import ipyparallel as ipp
# rc = ipp.Client()
# view = rc.load_balanced_view()

# with rc[:].sync_imports():
    # from utils_p11_WIP import *
    # import datetime
    # from scipy.optimize import curve_fit
    # import ipyparallel as ipp
   
   
   
dico_name={"expNi_ni_fe":"07T01NiFeNi",
           "expNi_in1"  :"08T02NiIng" ,
           "expNi_in2"  :"09T03NiIni" ,
           "expNi_au"   :"10T04NiAu"  ,
           "expNi_al"   :"11T05NiAl"  ,
           "expCr_ni_fe":"12T06CrFeNi",
           "expCr_in1"  :"13T07CrIng" ,
           "expCr_in2"  :"14T08CrIni" ,
           "expCr_au"   :"15T09CrAu"  ,
           "expCr_al"   :"16T10CrAl"  ,
           "expFe_ni_fe":"17T11FeFeNi",
           "expFe_in1"  :"18T12FeIng" ,
           "expFe_in2"  :"19T13FeIni" ,
           "expFe_au"   :"20T14FeAu"  ,
           "expFe_al"   :"21T15FeAl"  ,
           "expSS_ni_fe":"23T16ssFeNi",
           "expSS_in1"  :"25T17ssIng" ,
           "expSS_in2"  :"26T18ssIni" ,
           "expSS_au"   :"27T19ssAu"  ,
           "expSS_al"   :"29T20ssAl"  ,
           "expNi_fe"   :"37T21NiFe"  }
           
dico_mt={  "102":"ng",
           "11004"  :"ninel" ,
           "103"  :"np" ,
           "107"   :"nalpha"  }










print()
print("#"*50)

path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv  = get_param_vari("lcase", str).split("/")
save_key  = get_param_vari("save", bool, "False")
compare_CEA  = get_param_vari("CEA", bool, "False")
compare_LBA = get_param_vari("LBA", bool, "False")
DT_corr  = get_param_vari("dt_corr", bool, "True")

puiss_max_plot = get_param_vari("puiss_max_plot", float, "110")

data_irrad = DataIrrad(    path_csv_data,
            path_csv_dosi,
            lcase_csv,
            use_sqrt_for_meas_sig=False,
            load_hpge_eff=True,
            load_sss_results=False,
            load_ndup=False,
            remove_data=False)

data_irrad.aff_description()


ar_counts               =np.array(data_irrad.l_counts_v)
ar_mass                 =np.array(data_irrad.l_masse)
ar_iso                  =np.array(data_irrad.l_iso)
print(ar_mass)
ar_hpge_eff             =np.array(data_irrad.l_eff_gamma)
ar_hpge_ratio           =np.array(data_irrad.l_calib_ratio_v)
ar_gamma_int            =np.array(data_irrad.l_gamma_inten)
ar_auto_abs             =np.array(data_irrad.l_auto_abs)
print(ar_hpge_eff)
print(ar_auto_abs)
ar_date_hpge            =lmap(lambda i : data_irrad.l_ymd[i]+"_"+data_irrad.l_hms[i],range(len(data_irrad.l_hms)))
ar_date_hpge            =lmap(lambda i : lmap(lambda j : int(j),i.split("_")),ar_date_hpge)

ar_dosi_irrad_hpge_time =np.array(lmap(lambda i : (datetime.datetime(*ar_date_hpge[i])-data_irrad.l_irrad_time_stop[i]).total_seconds(),range(len(data_irrad.l_irrad_time_stop))))
ar_dosi_meas_time       =np.array(lmap(lambda i: float(i[:-1]) ,data_irrad.l_time_in_hpge_raw))
#print(ar_dosi_meas_time)
print(data_irrad.l_time_in_hpge_raw)
print(data_irrad.l_time_in_hpge)
print(ar_dosi_meas_time)
ar_half_life            =np.array(lmap(lambda i : d_spectro[(data_irrad.l_iso[i],data_irrad.l_mt[i])]["halftime"] ,range(len(data_irrad.l_iso))))
print("coucou")
print(ar_half_life/3600/24)
print(data_irrad.l_half_time/3600/24)
ar_decay_fact=np.array(lmap(lambda i : np.exp(np.log(2)/ar_half_life[i]*ar_dosi_irrad_hpge_time[i])*np.log(2)/ar_half_life[i]/(1-np.exp(-np.log(2)/ar_half_life[i]*ar_dosi_meas_time[i])),range(len(ar_dosi_meas_time))))
#ar_decay_fact=np.array(lmap(lambda i : np.exp(np.log(2)/ar_half_life[i]*ar_dosi_irrad_hpge_time[i])/ar_dosi_meas_time[i],range(len(ar_dosi_meas_time)))) #no decay correction

ar_counts_s=np.array(data_irrad.l_counts_s)
ar_hpge_eff_s=np.array(data_irrad.l_eff_gamma_s)
# ar_gamma_int_s=np.array(data_irrad.l_gamma_inten_s) # information inconnue
ar_auto_abs_s=np.array(data_irrad.l_auto_abs_s)
print(ar_counts_s)
print(ar_hpge_eff)
print(ar_gamma_int)
ar_activity=ar_counts*ar_decay_fact/ar_auto_abs/ar_mass/ar_hpge_eff/ar_hpge_ratio/ar_gamma_int
ar_activity_s=np.sqrt(np.power(ar_counts_s*ar_decay_fact/ar_auto_abs/ar_mass/ar_hpge_eff/ar_hpge_ratio,2) +np.power(ar_counts*ar_decay_fact/ar_auto_abs/ar_auto_abs/ar_mass/ar_hpge_eff/ar_hpge_ratio*ar_auto_abs_s,2)+np.power(ar_counts*ar_decay_fact/ar_auto_abs/ar_mass/ar_hpge_eff/ar_hpge_ratio/ar_hpge_ratio/ar_hpge_eff*ar_hpge_eff_s,2)+np.power(ar_counts*ar_decay_fact/ar_auto_abs/ar_mass/ar_mass/ar_hpge_eff/ar_hpge_ratio*0.00002,2))
print("Acitivity (Bq)")
for i in range(len(ar_activity)):
    print(data_irrad.l_name[i]+" "*(int(data_irrad.l_name[i].replace("-i","").replace("rc","10").replace("rp","3").replace("-g","").split("-")[-1]) < 10),data_irrad.l_iso[i],":","{:13f}".format(ar_activity[i]*ar_mass[i])," +- ","{:10f}".format(ar_activity_s[i]*ar_mass[i]), "("+"{:.2f}".format(ar_activity_s[i]/ar_activity[i]*100)+" %)")

print("Specific acitivity (Bq/g)")
for i in range(len(ar_activity)):
    print(data_irrad.l_name[i]+" "*(int(data_irrad.l_name[i].replace("-i","").replace("rc","10").replace("rp","3").replace("-g","").split("-")[-1]) < 10),data_irrad.l_iso[i],":","{:13f}".format(ar_activity[i])," +- ","{:10f}".format(ar_activity_s[i]), "("+"{:.2f}".format(ar_activity_s[i]/ar_activity[i]*100)+" %)")
l_act=[]
l_act_s=[]
l_num=[]
l_mass=[]
l_HPGe=[]
output=open("Traverse/traverse_EPFL.out","w")
out=""
if save_key:
    for i in range(len(ar_activity)):
        if (i==0 or (ar_iso[i]==ar_iso[i-1] and data_irrad.l_case_csv[i]==data_irrad.l_case_csv[i-1])) and i !=(len(ar_activity)-1) :
            if data_irrad.l_name[i]!=data_irrad.l_name[i-1]:
                l_act+=[ar_activity[i]]
                l_act_s+=[ar_activity_s[i]]
                l_num+=[float(data_irrad.l_name[i].split("-")[2])]
                l_mass+=[ar_mass[i]]
                l_HPGe+=[data_irrad.l_hpge_id[i]]
        elif i ==(len(ar_activity)-1):
            l_act  +=[ar_activity[i]]
            l_act_s+=[ar_activity_s[i]]
            l_num+=[float(data_irrad.l_name[i].split("-")[2])]
            l_mass+=[ar_mass[i]]
            l_HPGe+=[data_irrad.l_hpge_id[i]]
            fig=plt.figure()
            plt.errorbar(l_num,np.divide(l_act,1),np.divide(l_act_s,1),linestyle="",marker="x")
            plt.xlabel("Dosimeter position")
            plt.ylabel("Specific activity [Bq/g]")
            plt.title("Irradiation "+data_irrad.l_case_csv[i].replace("_","\_")+", dosimeter "+str(int(ar_iso[i][2:-1]))+data_irrad.l_name[i][:2])
            fig.savefig("Traverse/Specific_activity_at_SCRAM/"+data_irrad.l_case_csv[i]+"_"+str(int(ar_iso[i][2:-1]))+data_irrad.l_name[i][:2]+".png", bbox_inches=('tight'), dpi=200)
            out+="Irradiation "+data_irrad.l_case_csv[i].replace("_","\_")+", dosimeter "+str(int(ar_iso[i][2:-1]))+data_irrad.l_name[i][:2]+"\n"
            out+="Position = ["+", ".join([str(i) for i in l_num])+"]\n"
            out+="Mass = ["+", ".join([str(i) for i in l_mass])+"]\n"
            out+="Specific Activity at SCRAM [Bq/g] = ["+", ".join([str(i) for i in l_act])+"]\n"
            out+="Specific Activity uncertainty at SCRAM [Bq/g] = ["+", ".join([str(i) for i in l_act_s])+"]\n"
            out+="\n"
        else:
            fig=plt.figure()
            plt.errorbar(l_num,np.divide(l_act,1),np.divide(l_act_s,1),linestyle="",marker="x")
            plt.xlabel("Dosimeter position")
            plt.ylabel("Specific activity [Bq/g]")
            plt.title("Irradiation "+data_irrad.l_case_csv[i-1].replace("_","\_")+", dosimeter "+str(int(ar_iso[i-1][2:-1]))+data_irrad.l_name[i-1][:2])
            fig.savefig("Traverse/Specific_activity_at_SCRAM/"+data_irrad.l_case_csv[i-1]+"_"+str(int(ar_iso[i-1][2:-1]))+data_irrad.l_name[i-1][:2]+".png", bbox_inches=('tight'), dpi=200)
            out+="Irradiation "+data_irrad.l_case_csv[i-1].replace("_","\_")+", dosimeter "+str(int(ar_iso[i-1][2:-1]))+data_irrad.l_name[i-1][:2]+"\n"
            out+="Position = ["+", ".join([str(i) for i in l_num])+"]\n"
            out+="Mass = ["+", ".join([str(i) for i in l_mass])+"]\n"
            out+="Specific Activity at SCRAM [Bq/g] = ["+", ".join([str(i) for i in l_act])+"]\n"
            out+="Specific Activity uncertainty at SCRAM [Bq/g] = ["+", ".join([str(i) for i in l_act_s])+"]\n"
            out+="\n"
            l_act  =[ar_activity[i]]
            l_act_s=[ar_activity_s[i]]
            l_num=[float(data_irrad.l_name[i].split("-")[2])]
            l_mass=[ar_mass[i]]
            l_HPGe=[data_irrad.l_hpge_id[i]]
    output.write(out)
    output.close()    
          
l_act=[]
l_act_s=[]
l_num=[]
l_HPGe=[]
if compare_CEA:
    def CEA_val(case,iso,name,data,mt):
        print(case,iso,name)
        index=0
        while( not all([case in data[index],name+iso in data[index]])):
            # print(index)
            index+=1
        print("done")
        inel = 7 if "11004" in mt else 0
        pos=lmap(lambda j : float(j), data[index+1+inel].split("[")[1].split("]")[0].split(", "))
        val=lmap(lambda j : float(j), data[index+4+inel].split("[")[1].split("]")[0].split(", "))
        sig=lmap(lambda j : float(j), data[index+5+inel].split("[")[1].split("]")[0].split(", "))
        return pos, val, sig
    f=open("Traverse/Resultats_traverses_CEA.out","r")
    Data_CEA=f.readlines()
    # print(Data_CEA)    
    for i in range(len(ar_activity)):
        if (i==0 or (ar_iso[i]==ar_iso[i-1] and data_irrad.l_case_csv[i]==data_irrad.l_case_csv[i-1]) ) and i !=(len(ar_activity)-1) :
            if data_irrad.l_name[i]!=data_irrad.l_name[i-1]:
                l_act+=[ar_activity[i]*ar_mass[i]]
                l_act_s+=[ar_activity_s[i]]
                l_num+=[float(data_irrad.l_name[i].split("-")[2])]
                l_HPGe+=[data_irrad.l_hpge_id[i]]
        elif i ==(len(ar_activity)-1):
            l_act  +=[ar_activity[i]*ar_mass[i]]
            l_act_s+=[ar_activity_s[i]]
            l_num+=[float(data_irrad.l_name[i].split("-")[2])]
            l_HPGe+=[data_irrad.l_hpge_id[i]]
            fig=plt.figure()
            plt.errorbar(l_num,np.divide(l_act,l_act[0]),np.divide(l_act_s,l_act[0]),linestyle="",marker="x",label="EPFL")
            for x,y,n in zip(l_num,np.divide(l_act,l_act[0]),l_HPGe):
                plt.annotate(n,(x+0.1,y+0.01))
            pos, val, sig=CEA_val(dico_name[data_irrad.l_case_csv[i]][:7],str(int(ar_iso[i][2:-1])),data_irrad.l_name[i][:2],Data_CEA,data_irrad.l_mt[i])
            plt.errorbar(pos,val,sig,linestyle="",marker="x",label="CEA")
            plt.xlabel("Dosimeter position")
            plt.ylabel("Normalized saturated activity [-]")
            plt.legend()
            plt.title("Irradiation "+data_irrad.l_case_csv[i].replace("_","\_")+", dosimeter "+str(int(ar_iso[i][2:-1]))+data_irrad.l_name[i][:2])
            fig.savefig("Traverse/Comparaison_CEA/"+dico_name[data_irrad.l_case_csv[i]]+"_"+str(int(ar_iso[i][2:-1]))+data_irrad.l_name[i][:2]+".png", bbox_inches=('tight'), dpi=200)
            plt.close()

        else:
            fig=plt.figure()
            plt.errorbar(l_num,np.divide(l_act,l_act[0]),np.divide(l_act_s,l_act[0]),linestyle="",marker="x",label="EPFL")
            for x,y,n in zip(l_num,np.divide(l_act,l_act[0]),l_HPGe):
                plt.annotate(n,(x+0.1,y+0.01))
            pos, val, sig=CEA_val(dico_name[data_irrad.l_case_csv[i-1]][:7],str(int(ar_iso[i-1][2:-1])),data_irrad.l_name[i-1][:2],Data_CEA,data_irrad.l_mt[i-1])
            plt.errorbar(pos,val,sig,linestyle="",marker="x",label="CEA")
            plt.xlabel("Dosimeter position")
            plt.ylabel("Normalized saturated activity [-]")
            plt.legend()
            plt.title("Irradiation "+dico_name[data_irrad.l_case_csv[i-1]]+", dosimeter "+str(int(ar_iso[i-1][2:-1]))+data_irrad.l_name[i-1][:2])
            fig.savefig("Traverse/Comparaison_CEA/"+dico_name[data_irrad.l_case_csv[i-1]]+"_"+str(int(ar_iso[i-1][2:-1]))+data_irrad.l_name[i-1][:2]+".png", bbox_inches=('tight'), dpi=200)
            l_act  =[ar_activity[i]*ar_mass[i]]
            l_act_s=[ar_activity_s[i]]
            l_num=[float(data_irrad.l_name[i].split("-")[2])]
            l_HPGe=[data_irrad.l_hpge_id[i]]

if compare_LBA:
    Ni_csv="Comparison_LBA_MADERE/Nickel_activity_compare.xlsx"
    Fe_csv="Comparison_LBA_MADERE/Iron_activity_comparison.xlsx"
    data_Ni=ExcelSheet(Ni_csv,"for loading")
    for i in range(data_Ni.get_nb_col()):
        # print(i)
        if "EPFL/LBA - 1 (%)" in data_Ni.get(0,i):
            l_Ni_E_L_diff=[float(x) for x in data_Ni.sub_list(i)[1:] if x is not None]
        elif "EPFL/LBA - 1 Residual" in data_Ni.get(0,i):
            l_Ni_E_L_Residual=[float(x) for x in data_Ni.sub_list(i)[1:] if x is not None]
        elif "uncertainty EPFL (%)" in data_Ni.get(0,i):
            l_Ni_E_unc=[float(x) for x in data_Ni.sub_list(i)[1:] if x is not None]
        elif "EPFL/MADERE - 1 (%)" in data_Ni.get(0,i):
            l_Ni_E_M_diff=[float(x) for x in data_Ni.sub_list(i)[1:] if x is not None]
        elif "EPFL/MADERE - 1 Residual " in data_Ni.get(0,i):
            l_Ni_E_M_Residual=[float(x) for x in data_Ni.sub_list(i)[1:] if x is not None]
        elif "Name dosimeter" in data_Ni.get(0,i):
            l_Ni_name=[str(x) for x in data_Ni.sub_list(i)[1:] if x is not None]
    data_Fe=ExcelSheet(Fe_csv,"for loading")
    for i in range(data_Fe.get_nb_col()):
        if "EPFL/LBA - 1 (%)" in data_Fe.get(0,i):
            l_Fe_E_L_diff=[float(x) for x in data_Fe.sub_list(i)[1:] if x is not None]
        elif "EPFL/LBA - 1 Residual" in data_Fe.get(0,i):
            l_Fe_E_L_Residual=[float(x) for x in data_Fe.sub_list(i)[1:] if x is not None]
        elif "uncertainty EPFL (%)" in data_Fe.get(0,i):
            l_Fe_E_unc=[float(x) for x in data_Fe.sub_list(i)[1:] if x is not None]
        elif "Name dosimeter" in data_Fe.get(0,i):
            l_Fe_name=[str(x) for x in data_Fe.sub_list(i)[1:] if x is not None]
    fig=plt.figure(figsize=(16,9))
    plt.errorbar(range(len(l_Ni_name)),l_Ni_E_L_diff,np.divide(l_Ni_E_L_diff,l_Ni_E_L_Residual)*1,linestyle="")
    plt.xticks(range(len(l_Ni_name)),l_Ni_name)
    plt.xlim(-1,10)
    plt.hlines(0,-1,10,linestyles="dashed",color="k")
    plt.ylabel("EPFL/LBA -1[\%]")
    plt.xlabel("Dosimeters")
    plt.title ("Ni dosimeters specific activity comparison (1$\sigma$  unc.)")
    fig=plt.figure(figsize=(16,9))
    plt.errorbar(range(len(l_Ni_name)),l_Ni_E_L_diff,np.divide(l_Ni_E_L_diff,l_Ni_E_L_Residual)*1,linestyle="",label="EPFL and LBA")
    plt.errorbar(range(len(l_Ni_name)),l_Ni_E_M_diff,np.divide(l_Ni_E_M_diff,l_Ni_E_M_Residual)*1,linestyle="",color="purple",label="EPFL and MADERE")
    plt.errorbar(range(len(l_Ni_name)),l_Ni_E_L_diff,l_Ni_E_unc,color="orange",linestyle="",label="EPFL only unc.")
    plt.errorbar(range(len(l_Ni_name)),l_Ni_E_M_diff,l_Ni_E_unc,color="orange",linestyle="",label="")
    plt.xticks(range(len(l_Ni_name)),l_Ni_name)
    plt.xlim(-1,10)
    plt.hlines(0,-1,10,linestyles="dashed",color="k")
    plt.ylabel("Relative Difference [\%]")
    plt.xlabel("Dosimeters")
    plt.legend()
    plt.title ("Ni dosimeters specific activity comparison (1$\sigma$  unc.)")
    plt.grid(axis="y")
    fig.savefig("Comparison_LBA_MADERE/Comp_Ni_dosi_w_Madere.png",dpi='figure')
    fig=plt.figure(figsize=(16,9))
    plt.errorbar(range(len(l_Fe_name)),l_Fe_E_L_diff,np.divide(l_Fe_E_L_diff,l_Fe_E_L_Residual)*1,linestyle="",label="EPFL and LBA")
    plt.errorbar(range(len(l_Fe_name)),l_Fe_E_L_diff,l_Fe_E_unc,linestyle="",label="EPFL only unc.")
    plt.xticks(range(len(l_Fe_name)),l_Fe_name)
    plt.xlim(-1,10)
    plt.hlines(0,-1,10,linestyles="dashed",color="k")
    plt.ylabel("Relative Difference [\%]")
    plt.xlabel("Dosimeters")
    plt.title ("Fe dosimeters specific activity comparison (1$\sigma$  unc.)")
    plt.grid(axis="y")
    fig.savefig("Comparison_LBA_MADERE/Comp_Fe_dosi.png",dpi='figure')