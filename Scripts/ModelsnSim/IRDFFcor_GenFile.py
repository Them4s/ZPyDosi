from utils_p11_WIP import *
import pandas as pd
import numpy as np

path="/home/thomasligonnet/Documents/IRDFF-II_TAB/cor/Mn55ng_cor.csv"


dico_E={"μeV":1e-6,"meV":1e-3,"eV":1.0,"keV":1e3,"MeV":1e6}
outp=path.replace("_cor.csv","_cor")
df=pd.read_csv(path,index_col=0,sep=";")
cor=df.values/1000
l_e=[]
for s in df.index:
    sp=s.split()
    l_e+=[float(sp[0])*dico_E[sp[1]]]
l_e=np.array(l_e)
print(df["1 meV"])
print(cor[0,1])
print(cor.shape)
print(l_e)

g=open(outp,"w")
txt="#begin matrix2/2\n"
txt+="tit: JANIS 2024-May-01,11:37:00\n"
txt+="tit2: IRDFF-II: Mg-55(N,G) MF40.MT102\n"
txt+="fun: IRDFF-II: MG-55(N,G)Mg-56 \n"
txt+="con: 2\n"
txt+="lx2: {}\n".format(len(l_e))
txt+="ly2: {}\n".format(len(l_e))
txt+="//"
txt+="\n$xx:\n"
idn=0
for E in l_e:
    idn+=1
    stxt =" {:.5e}".format(E)
    stxt+=(13-len(stxt))*" "
    if idn==6:
        idn=0
        stxt+="\n"
    txt+=stxt
if txt[-2:]!="\n":
    txt+="\n"
txt+="end\n"

txt+="$yy:\n"
idn=0
for E in l_e:
    idn+=1
    stxt =" {:.5e}".format(E)
    stxt+=(13-len(stxt))*" "
    if idn==6:
        idn=0
        stxt+="\n"
    txt+=stxt
if txt[-2:]!="\n":
    txt+="\n"
txt+="end\n"


txt+="$zz:\n"
for i in range(len(cor)):
    idn=0
    txt+="!{}\n".format(i+1)
    for v in cor[i]:
        idn+=1
        stxt =" {:.5e}".format(v)
        stxt+=(13-len(stxt))*" "
        if idn==6:
            idn=0
            stxt+="\n"
        txt+=stxt
    if txt[-1]!="n":
        txt+="\n"
txt+="end\n//\n"
txt+="#end IRDFF-II: MG-55(N,G)Mg-56\n"
txt+="#begin matrix2/c\n"
txt+="x-units: MeV\n"
txt+="y: Incident Energy\n"
txt+="y-unit: 1e6, (MeV)\n"
txt+="iy-unit: 1        \n"
txt+="//\n"
txt+="#end matrix2/c\n"
g.write(txt)
g.close()