# py ~/Link_to_analysis/python/Misc/generate_input_xs_unc.py original="input" omp_num=6 
from utils_p9 import *
from pathlib import Path
import os

original_name  = get_param_vari("original", str)
geom_name  = get_param_vari("geom_name", str,"auto_geom.out")
num  = get_param_vari("num", int,8)
run_name=get_param_vari("run_name", str,"run")
omp_num = get_param_vari("omp_num",int,1)
Scitas = get_param_vari("Scitas" , bool, "false")
start_num = get_param_vari("start_num",int,1)


# mat_petale=["24050","24052","24053","24054","26054","26054","26056","26057","26058","28058","28060","28062"] # Ni-64 to add Ni-61
# mat_petale=["26054","26054","26056","26057","26058"] 
# at_petale=["24050","24052","24053","24054"] 
mat_petale=["11023","17035","17037"] 


f=open(original_name,"r")
for i in range(start_num,num+start_num):
    
    Path("num"+str(i)).mkdir(parents=True, exist_ok=True)
    f_out=open("num"+str(i)+"/"+"input"+str(i),"w")
    for j in f.readlines():
        if "%" != j[0] and any(mat in j for mat in mat_petale):
            f_out.write("       "+"    ".join( [n.replace("g0","gr"+str(i)) if n[:5] in mat_petale else n for n in j.split()])+"\n")
        elif "%" != j[0] and "/jeff33_pert/xsdata" not in j and "set acelib" in j:
            f_out.write(j.replace("\n","")+"    "+"/".join(j.replace("set acelib","").split("/")[:-2])+"/jeff33_pert/xsdata\""+"\n")
        elif "wwin" in j and ".." not in j:
            f_out.write(" ".join(["\"../"+n.replace("\"","")+"\"" if "wwd" in n else n for n in j.split()])+"\n")
        # elif "include" in j and ".." not in j:
        #     f_out.write(" ".join(["\"../"+n.replace("\"","")+"\"" if "include" not in n else n for n in j.split()])+"\n")
        else :
            f_out.write(j)
    f_out.close()
    #shutil.copyfile("auto_geom.out","num"+str(i)+"/auto_geom.out" )
    f.seek(0)
f.close()
    

f=open(geom_name,"r")
for i in range(start_num,num+start_num):
    
    Path("num"+str(i)).mkdir(parents=True, exist_ok=True)
    f_out=open("num"+str(i)+"/"+geom_name,"w")
    for j in f.readlines():
        if "%" != j[0] and any(mat in j for mat in mat_petale):
            f_out.write("       "+"    ".join( [n.replace("g0","gr"+str(i)) if n[:5] in mat_petale else n for n in j.split()])+"\n")
        else :
            f_out.write(j)
    f_out.close()
    shutil.copyfile("source_input","num"+str(i)+"/source_input" )
    f.seek(0)
f.close()

if len(original_name)>5 : sufix=original_name[5:]
else : sufix=""

f=open(run_name,"r")
n_name="run" if not Scitas else "run_scitas"
for i in range(1,num+1):
    
    f_out=open("num"+str(i)+"/"+n_name+str(i),"w")
    for j in f.readlines():
        if "rm" in j:
            f_out.write("rm -rf tmp"+str(i)+"*"+"\n")
        elif "cp " in j:
            f_out.write("cp "+"input"+str(i)+" tmp"+str(i)+"\n")
        elif "sss" in j:
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
