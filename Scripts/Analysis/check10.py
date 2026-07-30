'''
retrieve the number of counts for all HPGe measurement of an experiments and print it in a tabular form
'''
import os
import shutil
import sys
import subprocess
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Common.ExcelSheet import ExcelSheet
from ZPyDosi.DosiFunctions.Dictionaries import d_spectro
from ZPyDosi.Common.utils_general import str2time
from ZPyDosi.Common.TabPrinter import TabPrinter
from ZPyDosi.Prints.PrintnSave import aff
from pathlib import Path
print ("#"*50)
#key      = get_param_vari("key", str, None)
#path_sss = get_param_vari("path_sss", str, None)
#csv_corr = get_param_vari("csv_corr", str, None)

path_csv_data  = get_param_vari("csv_data",  str)
path_csv_dosi  = get_param_vari("csv_dosi",  str)
lcase_csv      = get_param_vari("lcase",     str).split("/")
do_print       = get_param_vari("print",     bool, "false")
plot           = get_param_vari("plot",      bool, "false")
th_deadtime   =  get_param_vari("th_deadtime",float, "1e-4")
Cumulative_plot= get_param_vari("cumulative_plot", bool, "True")
do_dead_time_corr    = get_param_vari("dead_time_corr", bool, "True")
lin_warning    = get_param_vari("lin_warning", bool, "True")
bkg_sub= get_param_vari("bkg_sub", bool, "False")

#python_exe = "python3.8"
# python_exe = "python3.10"



print ("#"*50, "check of:")
print ("#"+" "*49, "- time in csv vs tka")
print ("#"+" "*49, "- count in csv vs tka")
print ("#"+" "*49, "- csv uncertainties")
print ("#"+" "*49, "- dead_time csv vs tka")


data = DataIrrad(path_csv_data, path_csv_dosi, lcase_csv, remove_data=False,load_ratio=False)
path_hpge      = data.path_spectra_folder
print(path_hpge)

if not os.path.exists("check_out"):
    os.mkdir("check_out")


#print (aff_s_v("th_deadtime", th_deadtime))
tprint = TabPrinter("name mat time_g2k delta_time count_tka sig_tka count_file sig_file count_diff_[%] sig_diff_[%] deadtime_csv deadtime_tka deadtime_diff_[pt] pos_calc_vs_reel_[cm]".split(), sep_size=2)
global linearity_warning
linearity_warning=[]


for i in range(data.nb_dosi):
    print ("check", aff(data.l_case_csv[i]),aff(data.l_name[i], 25),end="", flush=True)
    tprint.add("name",    data.l_name[i])
    tprint.add("mat",    data.l_mat[i])
    
                                            # check uncertainty
    #sig_to_sqrt = (data.l_counts_s[i] - data.l_counts_v[i]**0.5)/(data.l_counts_s[i]+1e-50)*100
    #tprint.add("count_sig_to_sqrt_[%]",sig_to_sqrt)
                                            # check position reel given vs computed
    fct = data.l_barre_fct_pos[i]
    fct = fct.replace("x",str(data.l_pos_rel_barre[i]))
    #pos_reel_calculee = float(subprocess.Popen(("python3.8 -c print("+fct+")").split(), stdout=subprocess.PIPE).communicate()[0])
    pos_reel_calculee = eval(fct)
    #print
    #print fct
    #print data.l_pos_rel_barre[i], pos_reel_calculee,data.l_pos_reel[i]
    #print
    
    if pos_reel_calculee-data.l_pos_reel[i] != 0:
        tprint.add("pos_calc_vs_reel_[cm]",aff(pos_reel_calculee,5)+str(data.l_pos_reel[i]))
    else:
        tprint.add("pos_calc_vs_reel_[cm]","")
                                            # check tka/cnf exist and time
    #name_file_tka = path_hpge+"/"+"_".join([data.l_ymd[i], data.l_hms[i], data.l_hpge_id[i], data.l_hpge_pos[i], data.l_time_in_hpge_raw[i], data.l_name[i]])
    name_file_tka = "_".join([data.l_ymd[i], data.l_hms[i], data.l_hpge_id[i], data.l_hpge_pos[i], data.l_name[i]])
    d_file_2_path = {}
    # print("COUCOU")
    print(path_hpge)
    for path, subdirs, files in os.walk(path_hpge+"/"):
        # print("COUCOU")
        for file in files:
            d_file_2_path[file] = path+"/"+file
            # print(file, path+"/"+file)
    
    #print(d_file_2_path)
    #exit()
    tka_exist =  name_file_tka+".TKA" in d_file_2_path
    csv_exist =  name_file_tka+".CNF" in d_file_2_path
    
    
    if not tka_exist :
        splits=name_file_tka.split("_")
        sub_splits=splits[-1].split("-")
        sub_splits[1]=sub_splits[1][:3]
        splits[-1]="-".join(sub_splits)
        name_file_tka="_".join(splits)
        tka_exist =  name_file_tka+".TKA" in d_file_2_path
        csv_exist =  name_file_tka+".CNF" in d_file_2_path
        if not tka_exist:
            print ()
            print ("Error - no TKA file - "+name_file_tka+".TKA") # - file with a matching date:
        else:
            print("New TKA - "+name_file_tka+".TKA")
        #tmp = (len("Error   - no TKA file - "+path_hpge+"/"))
        #print (" "*tmp+("\n"+" "*tmp).join(filter(lambda s: s.startswith(data.l_ymd[i]+"_"+data.l_hms[i]) and "TKA" in s, os.listdir(path_hpge))))
    #if not csv_exist :
    #    print
    #    print "Warning - no CNF file -",name_file_tka+".CNF - file with a matching date:"
    #    tmp = len("Error   - no CNF file - "+path_hpge+"/")
    #    print " "*tmp+("\n"+" "*tmp).join(filter(lambda s: s.startswith(data.l_ymd[i]+"_"+data.l_hms[i]) and "CNF" in s, os.listdir(path_hpge)))
    if tka_exist:
                                            # check deadtime
        file_tmp = open(d_file_2_path[name_file_tka+".TKA"])
        
        time_aquis = float(file_tmp.readline())
        time_measu = float(file_tmp.readline())
        
        if str2time(data.l_time_in_hpge_raw[i]) != time_measu:
            tprint.add("delta_time",str2time(data.l_time_in_hpge_raw[i])-time_measu)
        tprint.add("time_g2k", str(time_measu)+"s")
        
        dead_time_tka = 1-time_aquis/time_measu
        file_tmp.close()
        tprint.add("deadtime_csv",data.l_deadtime[i])
        tprint.add("deadtime_tka",dead_time_tka)
        if abs(data.l_deadtime[i]-dead_time_tka)>th_deadtime:
            tprint.add("deadtime_diff_[pt]",data.l_deadtime[i]-dead_time_tka)
        #else:    tprint.add("deadtime_diff_[pt]","")
                                            # check count
        path_example=data.path_checkout_xlsx                               
        try:
            counter_input = ExcelSheet(path_example)    # generation of the spectrum_counter4 xslx input
        except:
            print("ERROR - I need an example for the script spectrum_counter11.py - e.g. testdata/check_files/input_exemple.xlsx")
            exit()
        j = 0
        while counter_input.get(j,0) != "############################################################### MEASUREMENT":
            j += 1
        counter_input.set(j+1,0, name_file_tka)
        counter_input.set(j+4,1, d_file_2_path[name_file_tka+".TKA"] )
        counter_input.save("check_out/input_exemple.xlsx")
        #bash_cmd = "python $petale_analysis/hpge/spectrum_counter1.py path_bkg="+path_hpge+"/bkg_L1_112h.TKA path_src="+name_file_tka+".TKA"+" data_hpge="+hpge_peak_data+" serv=1"
        bonus = " free_gain_keV=50" if "_Li_" in name_file_tka else ""
        Cumulative=" cumulative_plot=False" if not Cumulative_plot else ""
        corr_dead_time=" dead_time_corr=False" if not do_dead_time_corr else ""
        background=""
        if (("26054" in data.l_iso[i]) and ("Ho" in name_file_tka) and False): #does not work currently
            background=" Triche=True"
        elif (bkg_sub or ("26054" in data.l_iso[i])):
            background=" bkg_sub=True bkg_peak=False Triche=False"
        

        script_path = Path(__file__).resolve()
        script_dir = Path(__file__).resolve().parent.parent
        cwd = Path.cwd()

        relative_script_dir = Path(os.path.relpath(script_dir, cwd))

        bash_cmd = sys.executable+" "+"/Spectrometry/spectrum_counter11.py  csv=check_out/input_exemple.xlsx   case="+name_file_tka+"     serv=1 plot="+str(plot) + bonus + Cumulative + corr_dead_time + background
        bash_cmd_args = bash_cmd.split()
        bash_cmd_args[1] = str(relative_script_dir)+"/Spectrometry/spectrum_counter11.py"
        process = subprocess.Popen(bash_cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8',cwd=Path.cwd())
        output, error = process.communicate()
        print(error)
        count = None
        nrj_gamma = float(d_spectro[(data.l_iso[i], data.l_mt[i])]["keV"])
        for l in output.split("\n"):
            if len(l.split())>2 and l.split()[0] == "energy" and l.split()[2] == "counts":
                if abs(float(l.split()[1])-nrj_gamma)<0.5:
                    count = float(l.split()[3])
                    sig = float(l.split()[5])
                    break
        for l in output.split("\n"):
            if "spectrum " in str(l) or "Background" in str(l)  or "BACKGROUND " in str(l) :
                linearity_warning += str(l)
                linearity_warning += " \n"
        tprint.add("count_file",data.l_counts_v[i])
        tprint.add("sig_file",  data.l_counts_s[i])
        def err():
            new_name = "check_out/input_exemple_"+name_file_tka.split("/")[-1]+".xlsx"
            shutil.copyfile("check_out/input_exemple.xlsx", new_name)
            print(" "+bash_cmd.replace("serv=1","").replace("check_out/input_exemple.xlsx",new_name))
        if count is not None:
            count_ratio = (count/(float(data.l_counts_v[i])+1e-50)-1)*100
            sig_ratio   = (sig/(float(data.l_counts_s[i])+1e-50)-1)*100
            print(sig, data.l_counts_s[i])
            good = abs(count_ratio)<0.5
            tprint.add("count_diff_[%]",float(int(count_ratio*100))/100)
            tprint.add("sig_diff_[%]",float(int(sig_ratio*100))/100)
            tprint.add("count_tka",count)
            tprint.add("sig_tka",sig)
            print (aff(round(count,2)) , aff(round(data.l_counts_v[i],2)),end="", flush=True)
            if not good:
                #print()
                #print (bash_cmd.replace("serv=1",""))
                err()
            elif do_print:
                #print()
                #print (bash_cmd.replace("serv=1",""))
                err()
            else:
                print()
        else:
            tprint.add("count_diff_[%]","")
            print ("Error - peak analysis is not working:")
            #print (bash_cmd.replace("serv=1",""))
            err()
        
    else:
        print()
        tprint.add("count_diff_[%]","X")
        tprint.add("deadtime_diff_[pt]","X")

if linearity_warning and lin_warning:
    print("\n"+"#"*30+" Warning " +"#"*30+   "\n")
    print("".join(linearity_warning))
print (tprint.get_text())


#d_spectro = {
#    ("791970" ,"102"): {"halftime":2.6941*d,  "keV":411.8020,"eff":0.04,  "inten":0.9562   }, #197Au(n,g)198Au(b)          (h2 i-)
