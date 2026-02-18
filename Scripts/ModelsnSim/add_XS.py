import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from utils_p11_WIP import *
import os
from pathlib import Path

path = get_param_vari("path", str,"")
do_print=True
correct=True
l_element=["11","17"] #["24","26","28"]
to_exclude=[]#["24054","28061","28062","28064"]
# mat_petale=["11023","17035","17037"] 
l_done=[]
num=32
f_in=open(path,"r").readlines()
f_out=open(path,"w")
for line in f_in:
    if line.split():
        elem=line.split()[0]
        if elem[:2] in l_element and elem[:5] not in to_exclude and elem[:5] not in l_done:
            l_done+=[elem[:5]]
            f_out.write(line)
            for i in range(1,num+1):
                f_out.write(line.replace("gr0000","gr0000"[:-len(str(i))]+str(i)).replace("ga-0300","ga-0300_r"+str(i)))
                with open(line.split()[-1].replace("ga-0300","ga-0300_r"+str(i)), 'r') as file :
                    filedata = file.read()

                # Replace the target string
                filedata = filedata.replace(filedata.split()[0],line.split()[0].replace("gr0000","gr0000"[:-len(str(i))]+str(i)))

                # Write the file out again
                with open(line.split()[-1].replace("ga-0300","ga-0300_r"+str(i)), 'w') as file:
                    file.write(filedata)  
        elif elem[:5] not in l_done:
            f_out.write(line)
        print(line.split()[0],"done")
f_out.close()