
from ZPyDosi.Common.GetParam import get_param_vari

path = get_param_vari("path", str,"")
do_print=True
correct=False

f_in=open(path,"r").readlines()
if not correct: f_out=open(path,"w")
for line in f_in:
  if correct:
    if line!="\n":
        with open(line.split()[-1], 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("gr1","gr01").replace("gr2","gr02")

        # Write the file out again
        with open(line.split()[-1], 'w') as file:
            filedata = file.write(filedata) 
        print(line.split()[0],"done")
  else:
    if "g." in line:
        f_out.write(line.replace("g.","gr0000."))
        with open(line.split()[-1], 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace("g.","gr0000.")

        # Write the file out again
        with open(line.split()[-1], 'w') as file:
            file.write(filedata)  
    elif "gr" in line:
        idr=0
        iddot=0
        while line[idr]!="r":
            idr+=1
            iddot+=1
        while line[iddot]!=".": iddot+=1
        dist=iddot-idr
        f_out.write(line.replace("gr","gr"+"0"*(5-dist)))
        with open(line.split()[-1], 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(line.split()[0],line.split()[0].replace("gr","gr"+"0"*(5-dist)))

        # Write the file out again
        with open(line.split()[-1], 'w') as file:
            file.write(filedata)  
    else:
        f_out.write(line)
    print(line.split()[0],"done")
if not correct: f_out.close()