# nohup python3.9 /home/thomasligonnet/Link_to_analysis/python/Misc/run_multi_sim.py num=32 num_mult=2 time=24. &

# to be lauch from the main folder
from utils_p9 import *
from pathlib import Path
import time
import signal
import psutil

num  = get_param_vari("num", int) #total sim number
start_num  = get_param_vari("start_num", int,1)
num_mult  = get_param_vari("num_mult", int) #num of simultaneous sim
sim_time  = get_param_vari("time", float, 24.) #simulation time in hour
timed_mod  = get_param_vari("time_mod", bool, True) # True for solver with infinite run_time


processes=[]
pid=0
for i in range(start_num,num+start_num):
    pid+=1
    #bash_cmd = "bash run"+str(i)
    #bash_cmd_args = bash_cmd.split()
    #bash_cmd_args[1] = os.path.expandvars(bash_cmd_args[1])
    f=open("num"+str(i)+"/run"+str(i),"r")
    commands = f.readlines()
    for bash_cmd in commands:
        #print(bash_cmd)
        #print(len(bash_cmd))
        if "rm" in bash_cmd or "cp in bash_cmd": process = subprocess.call(bash_cmd,shell=True, cwd="num"+str(i))
        elif len(bash_cmd)>2 and bash_cmd[0]!="#": 
            processes  = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8', preexec_fn=os.setsid, cwd="num"+str(i))
    if timed_mod:    
        if (pid==num_mult or pid==(num+start_num-1)):
            processes = filter(lambda p: "sss2" in p.name(), psutil.process_iter())
            print("entering sleep for "+ str(sim_time)+"h, num="+str(i))
            time.sleep(sim_time*3600)
            print("continue")
            for p in processes:
                p.terminate()
            processes=[]
            pid=0
    else:
        wait_var=True
        while wait_var:
            processes = filter(lambda p: "sss2" in p.name(), psutil.process_iter())
            if len(list(processes))< num_mult:
                print("Max number of sim not reached, launching new one")
                wait_var=False
            else:
                print("Max number of sim reached, entering sleep for 10 min")
                time.sleep(600)
                print("retest")

            
print("terminated")