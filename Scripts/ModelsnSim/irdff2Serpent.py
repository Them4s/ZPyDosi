f=open("/home/thomasligonnet/Documents/IRDFF-II_TAB/IRDFF-II.tab.txt","r").readlines()

outp="/home/thomasligonnet/Documents/IRDFF-II_TAB/cor/Mn55ng_xs"
h=open(outp,"w")
h.write(outp.split("/")[-1]+"\n//\n")
txt=""
g=open("irdff2seprent_out.txt","w")
start = False
s_line="Mn-55(n,g)" 
out_name="double tmp_Mn55ng"
l_e=["0.0"]
l_v=["0.0"]
for line in f:
    if start:
        if len(line.split())<2:
            break
        s=line.split()
        l_e+=[str(float(s[0].replace("-","E-"))/1000000)]
        l_v+=[s[1].replace("E","e")]
        txt+=line.split("   ")[0].replace("E","").replace("-","e-").replace("+","e+")+"\n"
    if s_line in line:
        start =True


g.write(out_name+"_e[{}] = ".format(len(l_e))+"{"+", ".join(l_e)+"};\n\n")
g.write(out_name+"_v[{}] = ".format(len(l_v))+"{"+", ".join(l_v)+"};")
g.close()

txt+="//"
h.write(txt)
h.close()