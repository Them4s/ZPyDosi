# py ~/Link_to_analysis/python/Misc/generate_input_pos_unc.py original=input num=16 run_name=run omp_num=4 csv_data=~/Link_to_analysis/irrad/petale/petale_analysis_8.xlsx  csv_dosi=~/Link_to_analysis/irrad/petale/data_dosi.xlsx case=expFe_al pert_position=True larger_dosi=True

from ZPyDosi.Common.GetParam import get_param_vari
import subprocess
from pathlib import Path
import shutil
from os.path import expanduser
import os
home = expanduser("~")

original_name  = get_param_vari("original", str)
num  = get_param_vari("num", int)
start_num  = get_param_vari("start_num", int,1)
run_name=get_param_vari("run_name", str,"run")
omp_num = get_param_vari("omp_num",int,1)
Scitas = get_param_vari("Scitas" , bool, "false")


#variable for petale.py
print("#"*50)
pert_position = get_param_vari("pert_position" , bool, "false")
larger_dosi = get_param_vari("larger_dosi" , bool, "false") #larger dosi for uncertainty propagation on position. (include al dosimeter positions
do_voxel = get_param_vari("do_voxel" , bool, "True")
one_block = get_param_vari("one_block" , bool, "False") #Create one cell with all voxel or one per voxel
lattice_mod = get_param_vari("lattice_mod" , bool, "True") # Voxelize using serpent lattice
experimental_pos = get_param_vari("experimental_pos" , bool, "False") # place the case at the real experimental position
save = get_param_vari("save" , str, "") # place the case at the real experimental position
print("#"*50)

path_csv_data  = get_param_vari("csv_data",  str)
path_csv_dosi  = get_param_vari("csv_dosi",  str)
case_csv       = get_param_vari("case",     str)

path_petale_script=home+"/Link_to_analysis/python/sss_input/petale_26_WIP.py"


f=open(original_name,"r")
for i in range(start_num,start_num+num):
    
    Path("num"+str(i)).mkdir(parents=True, exist_ok=True)
    f_out=open("num"+str(i)+"/"+"input"+str(i),"w")
    for j in f.readlines():
        # if " seed " not in j:
            f_out.write(j)
        # else :
            # f_out.write("set seed "+str(int(42+i*10))+"\n")
    f_out.close()
    # create all autogeoms
    bash_cmd = "python3.9 "+path_petale_script+" csv_data="+path_csv_data+" csv_dosi="+path_csv_dosi+" case="+case_csv+" pert_position="+str(pert_position)+" larger_dosi="+str(larger_dosi)
    bash_cmd_args = bash_cmd.split()
    bash_cmd_args[1] = os.path.expandvars(bash_cmd_args[1])
    process = subprocess.Popen(bash_cmd_args, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8')
    process.wait()
    output, error = process.communicate()
    shutil.copyfile("auto_geom.out","num"+str(i)+"/auto_geom.out" )
    #print(output)
    #print(error)
    f.seek(0)
    print(str(i)+" done")
f.close()
    
if len(original_name)>5 : sufix=original_name[5:]
else : sufix=""

f=open(run_name,"r")
for i in range(start_num,start_num+num):
    
    f_out=open("num"+str(i)+"/"+run_name+str(i),"w")
    for j in f.readlines():
        if "rm" in j:
            f_out.write("rm -rf tmp"+str(i)+"*"+"\n")
        elif "cp " in j:
            f_out.write("cp "+"inpu"+str(i)+" tmp"+str(i)+"\n")
        elif "sss2" in j:
            if not Scitas:
                f_out.write(j.split()[0]+ " tmp"+str(i) +" -omp " +str(omp_num) +" > log"+str(i)+" & \n")
            else:
                tmp=j.split()
                tmp[5]="tmp"+str(i)
                f_out.write(" ".join(tmp)+"\n")
        else :
            f_out.write(j)
    f_out.close()
    f.seek(0)
f.close()
