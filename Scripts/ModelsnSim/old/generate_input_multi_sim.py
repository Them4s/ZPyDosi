from utils_p9 import *
from pathlib import Path

original_name  = get_param_vari("original", str)
num  = get_param_vari("num", int)
run_name=get_param_vari("run_name", str,"run")
omp_num = get_param_vari("omp_num",int,1)
Scitas = get_param_vari("Scitas" , bool, "false")
start_num = get_param_vari("start_num",int,1)

f=open(original_name,"r")
for i in range(start_num,num+start_num):
    
    Path("num"+str(i)).mkdir(parents=True, exist_ok=True)
    f_out=open("num"+str(i)+"/"+"input"+str(i),"w")
    for j in f.readlines():
        if " seed " not in j:
            f_out.write(j)
        else :
            f_out.write("set seed "+str(int(42+i*10))+"\n")
    f_out.close()
    shutil.copyfile("auto_geom.out","num"+str(i)+"/auto_geom.out" )
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
        elif "sss2" in j:
            if not Scitas:
                f_out.write(j.split()[0]+ " tmp"+str(i) +" -omp " +str(omp_num) +"\n")
            else:
                tmp=j.split()
                tmp[5]="tmp"+str(i)
                f_out.write(" ".join(tmp)+"\n")
        else :
            f_out.write(j)
    f_out.close()
    f.seek(0)
f.close()
