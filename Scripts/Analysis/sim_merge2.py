from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Common.CsvSeeker import CsvSeeker
import os
import shutil
import serpentTools # type: ignore
#rc['serpentVersion'] = '2.1.21'

print ("#"*50)
path_csv_data  = get_param_vari("csv_data", str,"")
lcase_csv  = get_param_vari("lcase", str,"").split("/")
Merge_here = get_param_vari("Merge_here", bool,"false") #overide the above to merge the files in current folder
gr_order = get_param_vari("gr_order", int,0) # to gain ram by decreasing the spectral resolution
IVW = get_param_vari("IVW", bool,"false") #Use inverse variance weighting (WARNING: may be biases if rare events)
print ("#"*50)
files=["perspectra","rr_vec","rrperspectra","keff_perspectra"]

if not Merge_here: data_csv = CsvSeeker(path_csv_data)
for case_csv in lcase_csv:
    if not Merge_here:
        path_to_sss=data_csv.get(case_csv, "sss_path")
        sub_path="/".join(path_to_sss.split("/")[:-1])[:-1]
    else:
        sub_path=os.getcwd()+"/num"
    os.makedirs(sub_path+"0",exist_ok=True)
    os.makedirs(sub_path+"0/input_mat_sss_2_of",exist_ok=True)
    for file in files:
        f1=open(sub_path+"1/input_mat_sss_2_of/"+file,"r+")
        l1=f1.readline()
        if file=="perspectra":
            l1=l1.split()
            l1[-1]=str(int(float(l1[-1])/2**gr_order))
            l1=" ".join(l1)+"\n"
        f1.close()
        vec=[]
        vec_s=[]
        res_all=[]
        id_dir=1
        while os.path.isdir(sub_path+str(id_dir)):
            f=open(sub_path+str(id_dir)+"/input"+"_mat_sss_2_of/"+file,"r+")
            vec +=   [lmap(lambda s: (lmap(lambda t:float(t), s.split()) if s!="" else s.split()),f.readlines()[1:])]
            fs=open(sub_path+str(id_dir)+"/input"+"_mat_sss_2_of/"+file+"_sig","r+")
            vec_s += [lmap(lambda s: (lmap(lambda t:float(t), s.split()) if s!="" else s.split()),fs.readlines()[1:])]
            res_tmp=serpentTools.read(sub_path+str(id_dir)+"/input"+"_res.m")
            res_all+=[res_tmp]
            f.close()
            fs.close()
            id_dir+=1
            if file=="perspectra" and gr_order!=0:
             for j in range(len(vec[-1])):
              if vec[-1][j]!="":
               vec[-1][j]  =[sum([  vec[-1][j][t*int(2**gr_order)+s]    for s in range(int(2**gr_order))])      for t in range(int(len(  vec[-1][j])/2**gr_order))]
               vec_s[-1][j]=[sum([vec_s[-1][j][t*int(2**gr_order)+s]**2 for s in range(int(2**gr_order))])**0.5 for t in range(int(len(vec_s[-1][j])/2**gr_order))]
        res_meta_keys=res_tmp.metadata.keys()
        res_resdata_key=res_tmp.resdata.keys()
        #print(res_resdata_key)
        #print(res_meta_keys)
        sum_w=[]
        w=[]
        vec_fin=[]
        vec_s_fin=[]
        #print(np.asarray(vec_s[0][0]).shape)
        #print(vec_s[0][0])
        #exit()
        for i in range(len(vec_s[0])): # calculation of means with inverse variance weighting
          sub_vec_fin=[]
          sub_vec_s_fin=[]
          # sub_w=[]
          # sub_sum_w=[]
          if vec_s[0][i] != "":
            for j in range(len(vec_s[0][i])):
                if (float(vec_s[1][i][j])==0. and float(vec[1][i][j])!=0.0):
                    print("error")
                    exit()
                #w_tmp=[1/float(vec_s[s][i][j])**2 if float(vec_s[s][i][j])!=0 else 0 for s in range(len(vec_s))]
                #w_tmp=[(1/(vec_s[s][i][j]))**2 if vec_s[s][i][j]!="0.000000e+00" else 0. for s in range(len(vec_s))]  #standard
                #w_tmp=[1./(float(vec_s[s][i][j])/float(vec[s][i][j])) if vec[s][i][j]!="0.000000e+00" else 0 for s in range(len(vec_s))]
                if not IVW:
                    w_tmp=[float(res_all[s].resdata["sourceNeutrons"]) if vec[s][i][j]!="0.000000e+00" else 0 for s in range(len(vec_s))]
                else:
                    w_tmp=[1/float(vec_s[s][i][j])**2 if float(vec_s[s][i][j])!=0 else 0 for s in range(len(vec_s))]
                #print(w_tmp)
                #exit()
                sum_w_tmp=sum(w_tmp)
                # sub_w+=[w_tmp]
                # sub_sum_w+=[sum_w_tmp]
                if sum_w_tmp!=0:
                    sub_vec_fin+=["{:6e}".format(sum([vec[s][i][j]*w_tmp[s] for s in range(len(vec_s))])/sum_w_tmp)]
                    #sub_vec_s_fin+=["{:6e}".format((1/sum_w_tmp)**0.5)] #standard
                    sub_vec_s_fin+=["{:6e}".format(sum([(vec_s[s][i][j]*w_tmp[s]/sum_w_tmp)**2 for s in range(len(vec_s))])**0.5)] #general
                #    sub_vec_s_fin+=["{:6e}".format(sum([float(vec_s[s][i][j])/sum_w_tmp for s in range(len(vec_s))])/sum_w_tmp**0.5)]
                else:
                   sub_vec_fin+=["0.000000e+00"]
                   sub_vec_s_fin+=["0.000000e+00"]
            sub_vec_fin="\t ".join(sub_vec_fin)
            sub_vec_s_fin="\t ".join(sub_vec_s_fin)
          vec_fin+=[sub_vec_fin]
          vec_s_fin+=[sub_vec_s_fin]
        f_v=open(sub_path+"0/input_mat_sss_2_of/"+file,"w+")
        f_s=open(sub_path+"0/input_mat_sss_2_of/"+file+"_sig","w+")
        f_v.write(l1)
        f_s.write(l1)
        f_v.write(" "+"\n ".join(vec_fin)+"\n")
        f_s.write(" "+"\n ".join(vec_s_fin)+"\n")
        f_v.close()
        f_s.close()
    # shutil.copy(sub_path+"1/input",sub_path+"0/input")
    shutil.copy(sub_path+"1/input",sub_path+"0/input")
    # shutil.copy(sub_path[:-3]+"/auto_geom.out",sub_path+"0/auto_geom.out")
    f_res=open(sub_path+"0/input_res.m","w+")
    f_res_1=open(sub_path+"1/input_res.m","r+").readlines()
    # print(res_resdata_key)
    for line in f_res_1:
        #print(len(line))
        arg=line.split()[0] if line!="\n" else ""
        #print(arg)
        if line=="\n" or line=="":
            f_res.write("\n")
        elif arg.replace("_","").lower() not in lmap(lambda s: s.lower(),list(res_resdata_key)):
            f_res.write(line)
        else:
            #print("coucou")
            idl=lmap(lambda s: s.lower(),list(res_resdata_key)).index(arg.replace("_","").lower())
            arg=list(res_resdata_key)[idl]
            # print(arg)
            # if arg=="totPower":
            #     for s in range(len(res_all)):
            #         print((res_all[s].resdata["totPower"][0]*res_all[s].resdata["totPower"][1])**2)
            if len(res_all[0][arg])>1:
                nline="= ["
                for i in range(int(len(res_all[0][arg])/2)):
                  if not IVW:
                    w_tmp=[float(res_all[s].resdata["sourceNeutrons"]) for s in range(len(res_all))]
                  else:
                    w_tmp=[1/float(res_all[s].resdata[arg][2*i+1]*res_all[s].resdata[arg][2*i])**2 if (res_all[s].resdata[arg][2*i+1]!=0 and res_all[s].resdata[arg][2*i]!=0) else 0 for s in range(len(res_all))]
                  sum_w_tmp=sum(w_tmp)
                  val=sum([res_all[s].resdata[arg][2*i]*w_tmp[s] for s in range(len(res_all))])/sum_w_tmp if sum_w_tmp!=0 else 0
                  sig=sum([(res_all[s].resdata[arg][2*i]*res_all[s].resdata[arg][2*i+1]*w_tmp[s]/sum_w_tmp)**2 for s in range(len(vec_s))])**0.5 if sum_w_tmp!=0 else 0
                  nline += ("  "+str(val)+" "+str(sig/val)) if val!=0 else  ("  "+str(0)+" "+str(0))
                nline += " ];\n"
                
                # if arg=="totPower":
                #    print(nline)
                f_res.write(line.split("=")[0]+nline)
            else:
                tmp=str(sum([float(res_all[s].resdata[arg]) for s in range(len(res_all))]))
                f_res.write(line.split("=")[0]+"= "+tmp+" ;\n")
    
    print ()
    print ("#"*50)
    print (case_csv+" Done!")
    print ("#"*50)
    print ()
