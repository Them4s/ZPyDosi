# 1 - select an experiment in the log file, e.g. Reflector:Fe dosimeter:Ni/Fe
#     enter in the_big_conversion.py:
#   - "name_exp"       is the corresponding name the petale_analysis.xlsx file "expFe_fe_ni" (the one for the python analysis input)
#   - "relf"           is the reflector name "Fe"
#   - "name_exp_raw"   is the experiment name for the CNF path finding "Fe Fe"
#   - "exp_to_analyse" is the exp name in the log file "17T11FeFeNi"
#   - "l_obj"          is the list of dosimeter materials, the first one is used for the ref naming ["Ni", "Fe"] (the gold dosi is then Au-Pfe-ni-rc and not Au-Pfe-fe-rc)
# 2 - a nice list of values to be copy-pasted (by column) in the petale_analysis.xlsx file appears
#   - start with the "name_dosi_py" column to check the ordering match the one of petale_analysis.xlsx, the gprd/p13 might be swapped it is not a problem
#   - report the dosimeter mass in the "data_dosi.xlsx" file
#   - copy-paste the two last columns "path_in" - "path_out" in the convert.txt file for the convert.py scrit that copy-paste the CNF file in the modified data tree and convert is the TKA
#   - add the the experiment identification as below right above the juste copied path. It must begin as "# name....", the space is important and format is important.
# 3 - find the power history CNF and add the corresponding lines in the convert.txt file
#   - run python script convert.py
#   - add the path in the "monitor_path" key of the petale_analysis.xlsx
#   - set the "time_start_irrad" and "time_stop_irrad" keys, the first one is not very important here (irradiation start from the begining) but the second is (=scram)
#   - follow "# How to run the script:" at the top of petale_analysis.xlsx



# mv hpge_data/raw/data/Fu/Fe\ Fe/2020_11_24_18_36_52_Ni_P_5_F_pgrd.CNF hpge_data/raw/data/Fu/Fe\ Fe/2020_11_24_18_36_52_Ni_P_45_F_pgrd.CNF
# mv hpge_data/raw/data/Fu/Ni\ In\ 2/07_55_19_In_P_20.CNF               hpge_data/raw/data/Fu/Ni\ In\ 2/07_55_19_In_P_20_p13.CNF
# mv hpge_data/raw/data/Ho/07T01NiFeNi                                  hpge_data/raw/data/Ho/Ni\ Fe
# mv hpge_data/raw/data/Zm/01T07NiFeNi                                  hpge_data/raw/data/Zm/Ni\ Fe
# mv hpge_data/raw/data/Fu/Ni\ Fe/2020_10_27_19_59_53_Ni_P5_F_p13.CNF   hpge_data/raw/data/Fu/Ni\ Fe/2020_10_27_19_59_53_Ni_P_5_F_p13.CNF

# mv hpge_data/raw/data/Fu/Ni\ In\ 2/Au_P_1.CNF                hpge_data/raw/data/Fu/Ni\ Fe/Au_P_1.CNF
# mv hpge_data/raw/data/Fu/Ni\ In\ 2/07_55_19_In_P_20.CNF      hpge_data/raw/data/Fu/Ni\ In\ 2/07_55_19_In_P_20_p13.CNF
# mv hpge_data/raw/data/Fu/Cr\ Fe/13_53_51_Fe_P_20_grd.CNF     hpge_data/raw/data/Fu/Cr\ Fe/13_53_51_Fe_P_20_pgrd.CNF

# find $petale_analysis/../../../-\ Exchange\ -/CEA/PETALE/programme/Spectra -name "*Fe_P_11*"
from ZPyDosi.Common.ExcelSheet import ExcelSheet
from .cnf import read_cnf_file
import os

path_log        = "hpge_data/raw/Log_5.2_recup.xlsx"
path_analysis   = "petale_analysis_8.xlsx"
#exp_to_analyse  = "07T01NiFeNi"    # refl Ni, dosi Ni+Fe
#exp_to_analyse  = "08T02NiIng"    # refl Ni, dosi In (n,g)

#                                                                     nom_py         refl    nom_manip    code_manip       dosi_concerne(1er en ref)
# name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expNi_ni_fe", "Ni",   "Ni Fe",       "07T01NiFeNi",  ["Ni", "Fe"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expNi_in_g",  "Ni",   "Ni In",       "08T02NiIng",   ["In"],       "-g"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expNi_in_i",  "Ni",   "Ni In 2",     "09T03NiIni",   ["In"],       "-i"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expNi_au",    "Ni",  "Ni Au",      "10T04NiAu",     ["Au"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expNi_al",    "Ni",  "Ni Al",      "11T05NiAl",     ["Al"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expCr_ni_fe", "Cr",  "Cr Fe",      "12T06CrFeNi",  ["Ni", "Fe"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expCr_in1",  "Cr",    "Cr In",        "13T07CrIng",   ["In"], "-g"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expCr_in2",  "Cr",    "Cr In 2",      "14T08CrIni",   ["In"], "-i"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expCr_au",    "Cr",  "Cr Au",      "15T09CrAu",     ["Au"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expCr_al",    "Cr",  "Cr Al",      "16T10CrAl",     ["Al"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expFe_ni_fe", "Fe",  "Fe Fe",      "17T11FeFeNi",  ["Ni", "Fe"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expFe_in1",  "Fe",    "Fe Ing",       "18T12FeIng",   ["In"], "-g"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expFe_in2",  "Fe",    "Fe InI",       "19T13FeIni",   ["In"], "-i"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expFe_au",    "Fe",  "Fe Au",      "20T14FeAu",     ["Au"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expFe_al",    "Fe",  "Fe Al",      "21T15FeAl",     ["Al"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expSS_ni_fe", "SS",  "SS Fe",      "23T16ssFeNi",  ["Ni", "Fe"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expSS_in1",  "SS",    "SS Ing",       "25T17ssIng",   ["In"], "-g"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expSS_in2",  "SS",    "SS InI",       "26T18ssIni",   ["In"], "-i"
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expSS_au",    "SS",  "SS Au",      "27T19ssAu",     ["Au"], ""
#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expSS_al",    "SS",  "SS Al",      "29T20ssAl",     ["Al"], ""
# name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expNi_fe", "Ni",   "Ni Fe 2",     "37T21NiFe",  ["Fe"], ""
name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin  = "expSS_crit_bcn", "SS",   "SS Crit",     "03R03ss",  [""], ""


'''
python3.8 $petale_analysis/python/hpge/spectrum_counter5.py  csv=check_out/input_exemple_2020_12_01_09_23_26_Ho_pgrd_Ni-Pfe-1.xlsx   case=2020_12_01_09_23_26_Ho_pgrd_Ni-Pfe-1      plot=False
check expFe_ni_fe  Ni-Pfe-2                 -24161.797522210592  0.0
python3.8 $petale_analysis/python/hpge/spectrum_counter5.py  csv=check_out/input_exemple_2020_11_30_08_19_28_Li_pgrd_Ni-Pfe-2.xlsx   case=2020_11_30_08_19_28_Li_pgrd_Ni-Pfe-2      plot=False
check expFe_ni_fe  Ni-Pfe-3                 110329.62602271509  0.0
python3.8 $petale_analysis/python/hpge/spectrum_counter5.py  csv=check_out/input_exemple_2020_12_01_17_08_21_Ho_pgrd_Ni-Pfe-3.xlsx   case=2020_12_01_17_08_21_Ho_pgrd_Ni-Pfe-3      plot=False
'''

#name_exp, refl, name_exp_raw, exp_to_analyse, l_obj, comment_fin   = "expNi_in_g",   "Ni",    "Ni In",    "08T02NiIng",  ["In"], "-g"   # -> il manque les CNF des Ni


#print(read_cnf_file("hpge_data/raw/data/Fu/Ni In 2/Au_P_1.CNF", 'TRUE')["Start time"])
#exit()

d_hpge_exp2lpath = {}
for path, subdirs, files in os.walk("hpge_data/raw/data"):
    for file in files:
        reflecteur, exp = path.split("/")[-2:]
        if (reflecteur,exp) not in d_hpge_exp2lpath:
            d_hpge_exp2lpath[(reflecteur,exp)] = []
        d_hpge_exp2lpath[(reflecteur,exp)] += [path+"/"+file]
        #d_file_2_path[file] = path+"/"+file

print(d_hpge_exp2lpath.keys())

#name_exp, exp_to_analyse, l_obj  = "expNi_in2", "09T03NiIni", ["Ini", "In"]

log_meas = ExcelSheet(path_log, "Measurements")
log_dosi = ExcelSheet(path_log, "Dosimeters")

l_msg  = ["name_exp_log", "name_dosi_log", "name_dosi_py", "name", "pos", "dosi_mass", "pos", "cm", "start", "time", "during", "dead_time", "path_in", "path_out"]
l_size = [15,             17,              16,              5,       6,    10,          5,     4,    12,      12,     10,       10,          70,        30]


l_d_info = []
l_name2msg = []
d_used_path_associated_to_key = {}
for i in range(log_meas.get_nb_row()):
    dosi_name, dosi_name, dosi_name_bibi, hpge_name, hpge_pos, dosi_masse, core_pos = ["-"]*7
    if exp_to_analyse == log_meas.get(i,3) and log_meas.get(i,5) != "Al_P_18" : # exception for the deleted spectrum Al_P_18
#    if exp_to_analyse == log_meas.get(i,3): # exception for the deleted spectrum Al_P_18
        dosi_name = log_meas.get(i,5)
        hpge_name = log_meas.get(i,6)
        if dosi_name=="Fe_P_18" : print(log_meas.get(i-3,6),log_meas.get(i-2,6),log_meas.get(i-1,6),log_meas.get(i,6),log_meas.get(i+1,6))
        if dosi_name=="Fe_P_18" : print(log_meas.get(i-3,5),log_meas.get(i-2,5),log_meas.get(i-1,5),log_meas.get(i,5),log_meas.get(i+1,5))
        hpge_name = hpge_name[:2].replace("ö","o")
        hpge_pos  = log_meas.get(i,7)
        #date     = log_meas.get(i,9)
        #date     = str(date.year)+"_"+str(date.month).zfill(2)+"_"+str(date.day).zfill(2)
        #start    = str(log_meas.get(i,10)).replace(":","_")
        print(dosi_name, hpge_name, hpge_pos)
        l_path   = list(filter(lambda s: (dosi_name in s or dosi_name.replace("P_","P") in s) and (dosi_name+"0") not in s and ("inter") not in s and s.endswith(".CNF"), d_hpge_exp2lpath[(hpge_name,name_exp_raw)]))
        l_path_save = l_path+[]
        #if len(l_path)>1:               Key: empty_list comment this obselete option creating problem
        #    print("coucou2")
        #    l_path = list(filter(lambda s: hpge_pos in s or hpge_pos in s.replace("grnd","pgrd"), l_path))
        #    print("coucou3")
        nro_path_a_utiliser = 0
        if len(l_path)>1:
            if dosi_name+hpge_name not in d_used_path_associated_to_key:
                d_used_path_associated_to_key[dosi_name+hpge_name] = 0
            else:
                d_used_path_associated_to_key[dosi_name+hpge_name] += 1
            nro_path_a_utiliser = d_used_path_associated_to_key[dosi_name+hpge_name]
            print("WARNING - trouve plusieurs path pour - "+dosi_name+" at "+hpge_pos.ljust(4),"in", hpge_name,":",l_path, "use #"+str(nro_path_a_utiliser))
        if len(l_path)==0:
            print("ERROR - pas de fichier CNF pour - "+dosi_name,hpge_name,hpge_pos,"avant filtre position il y avait :",l_path_save)
            exit()
        c = read_cnf_file(l_path[nro_path_a_utiliser], 'TRUE')
        d, mo, y, h, mi, s = c["Start time"].replace("-"," ").replace(":"," ").replace(",","").split()
        start = y+"_"+mo+"_"+d
        time  = h+"_"+mi+"_"+s
        time_meas = str(int(c["Real time"]))+"s"
        dead_time = str(round((c["Real time"]-c["Live time"])/c["Real time"], 6))
        for j in range(log_dosi.get_nb_row()):
            if dosi_name == log_dosi.get(j,0):
                dosi_masse = log_dosi.get(j,6)
                if exp_to_analyse == log_dosi.get(j,9):
                    core_pos = log_dosi.get(j,9+2)
                elif exp_to_analyse == log_dosi.get(j,17):
                    core_pos = log_dosi.get(j,17+2)
                #print(log_dosi.get(j,9))
                if core_pos.startswith("c_"):
                    core_pos = core_pos[2:]
                else:
                    core_pos = "P"+core_pos
                break
        
        #dosi_name_bibi = dosi_name.split("_")[0] + "-P"+exp_to_analyse[5:7].lower()+(("-"+ core_pos[1:].split("_")[0]) if core_pos.startswith("P") else "")
        dosi_name_bibi = dosi_name.split("_")[0] + "-P"+refl.lower()
        if dosi_name.split("_")[0] in l_obj:
            if core_pos.startswith("P"):
                dosi_name_bibi += "-"+ core_pos[1:].split("_")[0]
            else:
                dosi_name_bibi += "-10"
        else:
            if core_pos.startswith("P"):
                dosi_name_bibi += "-"+l_obj[0].lower()+"-rp"
            else:
                dosi_name_bibi += "-"+l_obj[0].lower()+"-rc"
        dosi_name_bibi += comment_fin
        #if core_pos.startswith("P")
        #(("-"+ core_pos[1:].split("_")[0]) if core_pos.startswith("P") else "")
        #l_name2msg += [(dosi_name, exp_to_analyse, dosi_name, dosi_name_bibi, hpge_name, hpge_pos, dosi_masse, core_pos)]
        core_pos_cm = 50 if core_pos.startswith("P") else core_pos
        core_pos    = core_pos if core_pos.startswith("P") else "C"
        #path_out    = refl+"-"+l_obj[0]+"/"+y+"_"+mo+"_"+d+"_"+h+"_"+mi+"_"+s+"_"+hpge_name+"_"+hpge_pos+"_"+dosi_name_bibi.split("-")[0]+"-P"+refl.lower()
        path_out    = "hpge_data/P"+refl.lower()+"-"+l_obj[0]+comment_fin+"/"+y+"_"+mo+"_"+d+"_"+h+"_"+mi+"_"+s+"_"+hpge_name+"_"+hpge_pos+"_"+dosi_name_bibi+".CNF"
        l_txt  =  [exp_to_analyse, dosi_name, dosi_name_bibi, hpge_name, hpge_pos, dosi_masse, core_pos, core_pos_cm, start, time, time_meas, dead_time, l_path[nro_path_a_utiliser].replace(" ","~"), path_out]
        l_name2msg += [(dosi_name_bibi, "".join(map(lambda i:str(l_txt[i]).ljust(l_size[i]),range(len(l_txt)))))]
        
input_analysis = ExcelSheet(path_analysis)
nb_lines = input_analysis.get_nb_row()
i = 0
while input_analysis.get(i,0) != name_exp     and i<nb_lines : i += 1
while input_analysis.get(i,0) != "dosimeters" and i<nb_lines : i += 1
if i>= nb_lines:
    print("ERROR - pb to find",name_exp,"in file",path_analysis)
    exit()
i += 1
d_dosiname2nro = {}
while input_analysis.get(i,1) is not None:
    #print(input_analysis.get(i,1))
    d_dosiname2nro[input_analysis.get(i,1).replace(" ","")] = i
    i += 1
def name2nro(name):
    if name in d_dosiname2nro:
        return d_dosiname2nro[name]
    print("WARNING - "+name+" not found in "+path_analysis)
    return 1e6
#l_name2msg = sorted(l_name2msg, key=lambda v:"".join(v[0].split("-")[:-1])+str(v[0].split("-")[-1].zfill(2)))
l_name2msg = sorted(l_name2msg, key=lambda v:name2nro(v[0]))


print("".join(map(lambda i:str(l_msg[i]).ljust(l_size[i]),range(len(l_msg)))))

for _, msg in l_name2msg :
    print(msg)
                    
