# python petale_bmc_loop_v5.py Nxs=0 calc=4 omp=24
# python petale_bmc_loop_v5.py Nxs=32 calc=4 omp=24

'''
This is clearly not ready for general usage !
'''


import os
import subprocess as sb
import shutil
import time as tm
import sys
from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np
import serpentTools # type: ignore
import pandas as pd

# from utils_p11_WIP import *


def get_param(nom, defaut="def_forbiden"):
        for param in sys.argv[1:]:
                if param[:len(nom)]==nom and param[len(nom)] == "=":
                        if param[len(nom)+1:]=="auto":return "0"
                        return param[len(nom)+1:]
        if defaut != "def_forbiden":
                return defaut
        print("ERROR - please, provide parameter: "+nom)
        exit()


# exit()

RNG= np.random.default_rng()

#load config
f=open("config","r").readlines()
lib=f[0].strip().split("=")[-1]
mat=f[1].strip().split("=")[-1]
Only_dosi=None if f[2].strip().split("=")[-1]=="None" else f[2].strip().split("=")[-1].replace(" ","").split(",")
Is_annealed=bool(int(f[3].strip().split("=")[-1]))

if Is_annealed:
    if "inter" in f[4]: 
        inter_folder_suffix=f[4].strip().split("=")[-1]
    print("annealed mode On!")
###### setings ######
# advance settings
Looping=True
# Is_annealed=False
do_anneal=True

print("Is annealed:", Is_annealed)
print("Do anneal:", do_anneal)

# XS Generations #
No_MAYA=False  # Debug
skip_XS_gen=False
nb_sample = int(get_param("Nxs","0")) # if Zero the XS gen part is skipped
l_zz_elt_aaa = [(26, "Fe", 54),(26, "Fe", 56),(26, "Fe", 57),(26, "Fe", 58)]
# l_zz_elt_aaa = [(92, "U", 238),(92, "U", 235), (8, "O", 16), (1,"H",1), (13,"Al",27)]
l_mt=[2,4,102]
# l_mt=[2,4,18,102,455,456]
#l_zz_elt_aaa = [(1,"H",1), (13,"Al",27)]
import socket
add_csv_path="ref_calc_dir_{}_{}".format(lib,mat)
if not No_MAYA:
    bd = "{}_crocus_bmc_".format(lib)+socket.gethostname()
    socket_name=socket.gethostname()
    # paf_xs = f"/msfrdata1/data/xsdata/sss/jeff33_crocus_bmc_{socket.gethostname()}/ace"
    # paf_bp = f"/msfrdata1/data/xsdata/sss/jeff33_crocus_bmc_{socket.gethostname()}"+"/"+bd
    paf_bp = "/msfrdata1/data/xsdata/sss/"+bd
else:
    paf_bp="/media/thomasligonnet/sup_disk_1/jeff33_pert"
    socket_name="s1"
do_sample     = True
do_plot      = False
do_recup      = True
do_xsdata     = True


# Sim Running #

omp_sim = int(get_param("omp","16"))

nb_sim =  int(get_param("calc","0")) # if 0 the simulation part is skipped


start_num=1


# Merging #

force_merging=False # To perform merging even so no simulation ran (mostly for Debug)
Merge_here = True # Do not touch
gr_order = 0 # to gain ram by decreasing the spectral resolution Default to 0
IVW = False #Use inverse variance weighting (WARNING: may be biases if rare events), Default is Number of history weigthing
outputs2merge=["perspectra","rr_vec","rrperspectra","rr_vecdiff","keff_perspectra","keff_perspectra_diff"] # files to keep in the merged forlder
# path_csv_dosi  = get_param_vari("csv_dosi", str)
# lcase_csv  = get_param_vari("lcase", str).split("/")


# XS weighting and storing #

force_weighting=False # To perform XS weighting (Chi2) even so no simulation ran (mostly for Debug)

den_fact=100 # correction for the virtual dosimeter density
path_ref="inputs/result.csv" # path to the CSV containing the reference results
path_calcs=["num0/"]
# path_calc="num0/" #standard
wgt_thresh=True # Activate XS trimming using their wgt
Cthresh=0.999 # cumumlative wgt threshold (once the relative cumulative wgt is above we do russian roulette)
proba_roulette=0.5 # 0.1 # probility of survival
ref_dosi=3 # set None to remove normalization
l_nums=["-rp","-rc","-10","-1","-2","-3","-4","-5","-6","-7","-8","-9"]
Nsample_unc=2**18 # number of sample for the MC uncertainty propagation
f_wgt_name="Chi2_file_list" # name of the save file for the XS wgt


# BMC assimilation #

Skip_BMC=True # To skip the BMC (mostly for Debug)
only_plot_fast=True
### General FCT ###


def lmap(f,l):
    return list(map(f,l))

def easy_replace(inputstr,l_2rep,newstr):
    for rep,new in zip(l_2rep,newstr):
        inputstr=inputstr.replace(rep,new)
    return inputstr

def easy_id(A,B,Virtual_BMC_replace=False): # returns the position of the element of A in B
    l_ids=[]
    for a in A:
        if Virtual_BMC_replace:
            a=a.replace("BMC","Fe")
        pos=-1
        for i in range(len(B)):
            if a==B[i]:
                pos=i
                break
        if pos==-1:
            print("Error: No position found in easy_id for: {}".format(a))
            exit()
        l_ids+=[i]
    return np.array(l_ids)

# TODO replace by a ZPyDosi import
def icovar_jkk(l_l_v, l_w=None, do_cor=False, do_jackknife=False, fast_jackknife=True, blabla=False, nb_jkk=None, fast=True):
    t0 = tm.time()
    err = 1e-50
    l_l_v = np.array(l_l_v)
    cov = np.cov(l_l_v.T, aweights=l_w)
    moy = sum(l_l_v) / len(l_l_v)
    t1 = tm.time()
    if do_cor:
        cor = cov*1.
        stddev = np.sqrt(np.diag(cov))
        cor /= (stddev[:, None]+err)
        cor /= (stddev[None, :]+err)
    t2 = tm.time()
    if do_jackknife:
        if l_w is not None and sum(l_w) != len(l_w):
            new_l_l_v = []
            for i in range(len(l_w)):
                if RNG.random()<l_w[i]:
                    new_l_l_v += [l_l_v[i]]
            l_l_v = np.array(new_l_l_v)
            print("only",len(l_l_v),"remainings")
            l_w = None
            loc_cov = np.cov(l_l_v.T, aweights=l_w)
            loc_moy = sum(l_l_v) / len(l_l_v)
            if do_cor:
                loc_cor = loc_cov*1.
                loc_stddev = np.sqrt(np.diag(loc_cov))
                loc_cor /= (loc_stddev[:, None]+err)
                loc_cor /= (loc_stddev[None, :]+err)
        else:
            loc_cov = cov
            loc_moy = moy
            if do_cor:
                loc_cor = cor
            
        if nb_jkk is None: nb_jkk = len(l_l_v)
        if nb_jkk > len(l_l_v): nb_jkk = len(l_l_v)
        def moy_without(idx):
            if not fast_jackknife:
                return icovar_jkk(l_l_v[np.arange(len(l_l_v))!=idx])
            else:
                tmp_cov = loc_cov*1.
                if not fast:
                    for i in range(len(tmp_cov)):
                        #tmp_cov[i,:] = (tmp_cov[i,:] * len(l_l_v) - (l_l_v[idx][i]-moy[i])*(l_l_v[idx][:]-moy[:])) / (len(l_l_v)-1)
                        for j in range(len(tmp_cov)):
                            tmp_cov[i,j] = (tmp_cov[i,j] * len(l_l_v) - (l_l_v[idx][i]-loc_moy[i])*(l_l_v[idx][j]-loc_moy[j])) / (len(l_l_v)-1)
                else:
                    #tmp_cov[:,:] = (tmp_cov[:,:] * len(l_l_v) - (l_l_v[idx][:,None]-moy[:,None])*(l_l_v[idx][None,:]-moy[None,:])) / (len(l_l_v)-1)
                    tmp_cov = (tmp_cov * len(l_l_v) - (l_l_v[idx][:,None]-loc_moy[:,None])*(l_l_v[idx][None,:]-loc_moy[None,:])) / (len(l_l_v)-1)
                return tmp_cov
        def moy_without_cor(idx):
            tmp_cor = moy_without(idx)
            tmp_stddev = np.sqrt(np.diag(tmp_cor)+err)
            tmp_cor /= (tmp_stddev[:, None]+err)
            tmp_cor /= (tmp_stddev[None, :]+err)
            return tmp_cor
        l_jkk = list(range(len(l_l_v)))
        while len(l_jkk) > nb_jkk: l_jkk.pop(int(RNG.random()*len(l_jkk)))
        jackknife_cov_var = np.sum((moy_without(i)-loc_cov)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        #jackknife_cov_var = np.sum((dmoy_without(i))**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        if do_cor:
            jackknife_cor_var = np.sum((moy_without_cor(i)-loc_cor)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
    t3 = tm.time()
    #print t3-t2
    if not do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s")
        return cov
    if do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s")
        return cov, cor
    if not do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and jkk in",t3-t2,"s")
        return cov, jackknife_cov_var**0.5
    if do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s and jkk in",t3-t2,"s")
        return cov, cor, jackknife_cov_var**0.5, jackknife_cor_var**0.5
    print("icovar_jkk - error")
    exit()


# TODO replace by a ZPyDosi import
def imoyvar(l_l_v, l_w = None, do_jackknife=False):
    t = len(l_l_v[0])
    nxs = len(l_l_v)
    sum_w = nxs if l_w is None else sum(l_w[:nxs])
    moy = np.zeros(t)
    for x in range(nxs):
        w = 1 if l_w is None else l_w[x]
        moy += np.array(l_l_v[x]) * w / sum_w
    var = np.zeros(t)
    for x in range(nxs):
        w = 1 if l_w is None else l_w[x]
        var += (np.array(l_l_v[x])-moy)**2 * w / sum_w
    var = var**0.5
    if not do_jackknife:
        return moy, var
    else:    
        l_var = np.array([nxs*var**2 - (nxs-1)*imoyvar(np.array(l_l_v)[np.arange(len(l_l_v))!=num],np.array(l_w)[np.arange(len(l_l_v))!=num])[1]**2 for num in range(nxs)])
        l_moy = np.array([nxs*moy - (nxs-1)*imoyvar(np.array(l_l_v)[np.arange(len(l_l_v))!=num],np.array(l_w)[np.arange(len(l_l_v))!=num])[0]for num in range(nxs)])
        ste = np.var(l_moy,axis=0)/nxs
        std = np.mean(l_var,axis=0)
        jkk_var = np.var(l_var,axis=0)/nxs
        return moy, std**0.5, ste**0.5, jkk_var**0.5 # en realité ça retourne les std ;)

#Input size of big mat, covariance and energy boundaries of covariance
def cov2scale(l_nrj,cov,nrj_cov):
    big_cov=np.zeros((len(l_nrj),len(l_nrj)))
    for i in range(1, len(nrj_cov)):
        l_idx=(l_nrj<nrj_cov[i]) & (l_nrj>nrj_cov[i-1])
        for j in range(i,len(nrj_cov)):
            l_idy=(l_nrj<nrj_cov[j]) & (l_nrj>nrj_cov[j-1])
            big_cov[l_idx,l_idy]=cov[i-1,j-1]
            big_cov[l_idy,l_idx]=cov[i-1,j-1]
    return big_cov
#!/usr/bin/env python3

def order_indices(A, B):
    """
    Given two lists A and B that are permutations of each other,
    returns a list of indices such that for each index i, B[indices[i]] == A[i].
    """
    # Create a mapping from element to its index in B.
    index_map = {element: index for index, element in enumerate(B)}
    # For each element in A, get the corresponding index from B.
    return [index_map[element] for element in A]

def parse_ace_file(filename,No_MT4=False):
    """
    Parse a simplified ACE file and extract cross-section arrays.
    
    The assumed file structure is as follows:
      - First line: title (ignored)
      - Second line: NXS array (space-separated integers; e.g. energy grid size, etc.)
      - Third line: JXS array (space-separated integers; these are pointers into the XSS array)
      - The remaining lines: the XSS array (space-separated floating-point numbers)
      
    The JXS pointers are assumed to be 1-indexed (as in many ACE files) so we subtract 1
    to index into our Python (0-indexed) numpy array.
    
    For example, if you know that the total cross section is stored in the XSS array starting
    at JXS[0] for n_energy points (with n_energy given by the first element of the NXS array),
    then we extract it as shown below.
    
    Adjust the extraction of additional arrays (e.g. elastic, absorption, etc.) as needed.
    """
    with open(filename, 'r') as f:
        # Read the title line (which we ignore for now)
        title = f.readline()
        # print(title)
        # Read the NXS array (e.g., [n_energy, ...])
        for i in range(5):
            skip = f.readline()
        nxs_line = f.readline()
        for i in range(1):
            nxs_line += f.readline()
        # print(nxs_line)
        try:
            nxs = [int(x) for x in nxs_line.split()]
        except Exception as err:
            raise ValueError("Error reading NXS array (second line of the file)") from err

        # Read the JXS array (pointer indices; assumed 1-indexed)
        jxs_line = f.readline()
        for i in range(3):
            jxs_line += f.readline()
        # print(jxs_line)
        try:
            jxs = [int(x) for x in jxs_line.split()]
        except Exception as err:
            raise ValueError("Error reading JXS array (third line of the file)") from err
        
        # Read the remainder of the file: the XSS array (all floating point numbers)
        xss_data = f.read().split()
        try:
            xss = np.array([float(x) for x in xss_data])
        except Exception as err:
            raise ValueError("Error converting XSS array entries to floats") from err

    # Create a dictionary to store the extracted cross section arrays.
    xs_dict = {}
    
    # For demonstration, we assume:
    #   - n_energy (number of energy grid points) is the first element of NXS.
    #   - Total cross section is stored in the XSS array starting at position JXS[0]
    #     and spans n_energy entries.
    #   - Elastic cross section is stored starting at position JXS[1] (if available)
    #     and also spans n_energy entries.
    # (In many ACE files, the meaning and layout of the arrays is defined by the ACE manual.)


    try:
        n_energy = nxs[2]
    except IndexError:
        raise ValueError("NXS array appears empty; cannot determine energy grid length.")
    # print(len(xss))
    # print(n_energy)
    energy = xss[:n_energy]
    xs_dict["1"]={}
    xs_dict["2"]={}
    xs_dict["1"]["l_nrj"]=energy
    xs_dict["2"]["l_nrj"]=energy
    if not No_MT4:
        xs_dict["4"]={}
        xs_dict["4"]["l_nrj"]=energy
        xs_dict["4"]["l_xs"]=np.zeros(len(energy))
    # xs_dict['energy'] = energy
    # Extract Total cross section
    try:
        total_start = n_energy  # convert 1-indexed to 0-indexed
    except IndexError:
        raise ValueError("JXS array does not have an entry for total cross section.")
    # print(total_start)
    total_xs = xss[total_start: total_start + n_energy]
    # print(len(total_xs))
    xs_dict["1"]['l_xs'] = total_xs

    # Example: Extract Elastic cross section if available
    if len(jxs) > 1:
        elastic_start = 3*n_energy
        elastic_xs = xss[elastic_start: elastic_start + n_energy]
        xs_dict["2"]['l_xs'] = elastic_xs

    # radiative Capture (MT 102)
    
    MTR=xss[jxs[2] - 1 : jxs[2]+nxs[3]-1]
    Loc=xss[jxs[5] - 1 : jxs[5]+nxs[3]-1]
    
    # print(Loc)
    # exit()
    for i in range(len(MTR)):
        BLOC_loc=int(jxs[6]+Loc[i]-2)
        start_E=int(xss[BLOC_loc])
        N_E=int(xss[BLOC_loc+1])
        # print(str(int(MTR[i])),start_E,N_E)
        xs_dict[str(int(MTR[i]))]={}
        xs_dict[str(int(MTR[i]))]['l_nrj'] = energy[start_E-1:start_E+N_E-1]
        xs_dict[str(int(MTR[i]))]['l_xs'] = xss[BLOC_loc+2:BLOC_loc+2+N_E]
        # print(int(MTR[i]),xs_dict[str(int(MTR[i]))]['l_xs'][-1],xs_dict[str(int(MTR[i]))]['l_xs'][-1])
        if not No_MT4 and int(MTR[i])>=51 and int(MTR[i])<=91:
            xs_dict["4"]['l_xs'][start_E-1:start_E+N_E-1] += xss[BLOC_loc+2:BLOC_loc+2+N_E]
    if not No_MT4:
        while xs_dict["4"]['l_xs'][1]==0:
            xs_dict["4"]['l_xs'] =xs_dict["4"]['l_xs'][1:]
            xs_dict["4"]['l_nrj'] =xs_dict["4"]['l_nrj'][1:]
        # while xs_dict["4"]['l_xs'][-1]==0:
        #     xs_dict["4"]['l_xs'] =xs_dict["4"]['l_xs'][:-1]
        #     xs_dict["4"]['l_nrj'] =xs_dict["4"]['l_nrj'][:-1]
    return xs_dict


def update_ace_file(source_path: str, dest_path: str, modified_dict: dict):
    """
    Read the ACE file, load original XSS via parse_ace_file, compare with modified_dict,
    and write a new ACE file where each XSS float token is replaced by the modified
    value only if changed, preserving each token's original formatting exactly.
    """
    # 1) Get original and modified flat XSS arrays
    orig_dict = parse_ace_file(source_path,No_MT4=True)

    # 2) Read all lines
    with open(source_path, 'r') as f:
        lines = f.readlines()

    # 3) Extract flat XSS token list by splitting on whitespace for lines[12:]
    xss_tokens = []
    for ln in lines[12:]:
        xss_tokens.extend(ln.split())
    orig_flat = np.array([float(tok) for tok in xss_tokens])

    # 4) Re-read header to get NXS and JXS for block offsets
    with open(source_path, 'r') as f:
        f.readline()  # title
        for _ in range(5): f.readline()
        # NXS two lines
        nxs_line = f.readline() + f.readline()
        nxs = [int(x) for x in nxs_line.split()]
        # JXS four lines
        jxs = [int(x) for x in ''.join(f.readline() for _ in range(4)).split()]

    # 5) Compute reaction block start/length positions
    n_energy = nxs[2]
    blocks = {1: (n_energy, n_energy)}
    if len(jxs) > 1:
        blocks[2] = (3 * n_energy, n_energy)
    # Other MTs via MTR and LOC arrays in orig_flat
    mtr = orig_flat[jxs[2] - 1 : jxs[2] + nxs[3] - 1]
    loc = orig_flat[jxs[5] - 1 : jxs[5] + nxs[3] - 1]
    for i, mt in enumerate(mtr):
        mt_int = int(mt)
        bloc = int(jxs[6] + loc[i] - 2)
        start_E = int(orig_flat[bloc])
        n_E = int(orig_flat[bloc + 1])
        blocks[mt_int] = (bloc + 2, n_E)

    # 6) Build modified_flat by applying diff from modified_dict
    modified_flat = orig_flat.copy()
    for mt_str, orig_entry in orig_dict.items():
        if mt_str not in modified_dict:
            continue
        orig_xs = orig_entry['l_xs']
        new_xs = modified_dict[mt_str]['l_xs']
        start, length = blocks[int(mt_str)]
        for idx in range(length):
            if not np.isclose(orig_xs[idx], new_xs[idx], rtol=0, atol=0):
                modified_flat[start + idx] = new_xs[idx]

    # 7) Format tokens manually, preserving formatting
    def format_token(orig_tok: str, new_val: float) -> str:
        """
        Preserve integer or float formatting:
        - If orig_tok has no '.' and no 'E', treat as integer.
        - Else treat as float: keep number of decimals equal to orig_tok's,
          use uppercase 'E'.
        """
        # Replace NaN values with 0
        if np.isnan(new_val):
            new_val = 0.0
        width = len(orig_tok)
        # Integer case
        if '.' not in orig_tok and 'E' not in orig_tok:
            tok = str(int(round(new_val)))
        else:
            # Determine decimal places from orig_tok (before 'E')
            # Split on 'E'
            parts = orig_tok.split('E')
            mant = parts[0]
            dec_count = len(mant.split('.')[1]) if '.' in mant else 6
            # Format in scientific notation with uppercase E
            fmt = f"{new_val:.{dec_count}E}"  # e.g. '1.234567E+02'
            tok = fmt
        # Pad/truncate to width
        if len(tok) < width:
            tok = tok.rjust(width)
        else:
            tok = tok[:width]
        return tok

    # 8) Rebuild file: tokens replaced in lines[12:]
    new_lines = lines[:12]
    flat_it = iter(modified_flat)
    for ln in lines[12:]:
        out = ''
        i = 0
        while i < len(ln):
            if ln[i].isspace():
                out += ln[i]
                i += 1
            else:
                j = i
                while j < len(ln) and not ln[j].isspace():
                    j += 1
                orig_tok = ln[i:j]
                try:
                    new_val = next(flat_it)
                    new_tok = format_token(orig_tok, new_val)
                except StopIteration:
                    new_tok = orig_tok
                out += new_tok
                i = j
        new_lines.append(out)

    # 9) Write updated ACE file
    with open(dest_path, 'w') as f:
        f.writelines(new_lines)
    print(f"Updated ACE file written to: {dest_path}")

def projette(l_xs_e, l_xs_v, l_e_piquet, aff=False, integ=True):
    l_xs_e, l_xs_v, l_e_piquet = map(list, [l_xs_e, l_xs_v, l_e_piquet])
    if l_e_piquet[0] < l_xs_e[0]:                           # on ajoute les points manquants au debut
        r = (l_e_piquet[0]-l_xs_e[0])/(l_xs_e[1]-l_xs_e[0])
        l_xs_e = [l_e_piquet[0]]+l_xs_e
        l_xs_v = [l_xs_v[1]*r + (1-r)*l_xs_v[0]]+l_xs_v
    i = 0
    l_xs_eb, l_xs_vb = [], []
    for e in filter(lambda e : e not in l_xs_e, l_e_piquet) :
        while i < len(l_xs_e) and l_xs_e[i] < e :       # recup des points ok
            l_xs_eb.append(l_xs_e[i])
            l_xs_vb.append(l_xs_v[i])
            i += 1
        if i < len(l_xs_e):                             # interpol
            r = (e-l_xs_e[i-1])/(l_xs_e[i]-l_xs_e[i-1])
            l_xs_eb.append(e)
            l_xs_vb.append(r*l_xs_v[i]+(1-r)*l_xs_v[i-1])
        else:                                           # extrapol
            r = (e-l_xs_e[i-2])/(l_xs_e[i-1]-l_xs_e[i-2])
            l_xs_eb.append(e)
            l_xs_vb.append(r*l_xs_v[i-1]+(1-r)*l_xs_v[i-2])
    for i in range(i, len(l_xs_e)):                     # on ajoute le points manquants a la fin
        l_xs_eb.append(l_xs_e[i])
        l_xs_vb.append(l_xs_v[i])
        i += 1
    for id in [0, -1]:                                  # nettoyage
        while l_xs_eb[id] != l_e_piquet[id]:
            l_xs_eb.pop(id)
            l_xs_vb.pop(id)

    l_v = []
    i0, i1 = 0, 0
    if integ:
        for e in l_e_piquet[1:] :
            while l_xs_eb[i1] < e : i1 += 1
            if aff : print(l_xs_eb[i0], l_xs_eb[i1], e, i0, i1)
            sv, se = 0, 0
            for i in range(i0, i1):
                se += l_xs_eb[i+1]-l_xs_eb[i]
                sv += (l_xs_eb[i+1]-l_xs_eb[i]) * (l_xs_vb[i+1]+l_xs_vb[i])/2
            l_v.append(sv/se)
            i0 = i1
    else:
        for e in l_e_piquet :
            while l_xs_eb[i1] < e : i1 += 1
            if aff : print(l_xs_eb[i0], l_xs_eb[i1], e, i0, i1)
            l_v.append(l_xs_vb[i1])

    return np.array(l_v)

def Do_ace_project(zz,elt,aaa,which="prior"): # not used currently
    name_ace = "{:02}-{}-{:03}-ga-0300.ace".format(zz,elt,aaa)
    if which=="new": 
        name_ace = name_ace.replace(".ace","{}.ace".format(inter_folder_suffix))
    dico_ace=parse_ace_file("XS_out/ace/"      +name_ace)
    path_numpy_prior="XS_out/archive_numpy_prior/{:02}-{}-{:03}-ga-0300_auto-4_mt2_4_102_eig_cor_i40.npz".format(zz,elt,aaa)
    if which=="new": 
        path_numpy_prior = path_numpy_prior.replace(".npz","{}.npz".format(inter_folder_suffix))
    dico_mat=np.load(path_numpy_prior,allow_pickle=True)['dict_data'].tolist()
    l_MT=[]
    print("Error MT not defined yet in Do_ace_projection")
    exit()
    Big_vec=[]
    for MT in l_MT:
        Big_vec+=[projette(dico_ace[MT]["l_nrj"],dico_ace[MT]["l_xs"],dico_mat["l_nrj"])]
    return np.array(Big_vec)

def get_BigRel(zz,elt,aaa,which="prior"): # not used currently
    path = "{:02}-{}-{:03}-XXXXX.npz".format(zz,elt,aaa)
    if which=="new": 
        path = path.replace(".npz","{}.npz".format(inter_folder_suffix))
    Big_mat=np.load(path,allow_pickle=True)['dict_data'].tolist()["Big_mat"]
    return np.array(Big_mat)

def get_Big(zz,elt,aaa,l_mt,which="prior",mat=False):
    path = "XS_out/archive_numpy_{}/{:02}-{}-{:03}-ga-0300_{}_big_data.npz".format(which, zz,elt,aaa,"_".join(map(str, l_mt)))
    tmp_dico=np.load(path,allow_pickle=True)['dict_data'].tolist()
    Big_vec=tmp_dico["big_vec"]
    if mat:
        Big_mat=tmp_dico["big_mat"]
        return Big_vec,Big_mat
    return Big_vec

def get_samp(zz,elt,aaa,num):
    name_ace = "{:02}-{}-{:03}-ga-0300_r{}.txt".format(zz,elt,aaa,num)
    samp=np.loadtxt("XS_out/ace/"+name_ace)
    return samp


if __name__ == '__main__' and False:
    # if len(sys.argv) != 2:
    #     print("Usage: {} <ace_file>".format(sys.argv[0]))
    #     sys.exit(1)

    # ace_filename = "/home/thomasligonnet/sim_far_away/NI_reflector_BMC_test/XS/ace/26-Fe-057-g0-300.ace"
    ace_filename = "/home/thomasligonnet/sim_local/PETALE/JEFF-3.3/BMC/Fe_In2_test/XS_out/ace/26-Fe-056-ga-0300.ace"
    ace_filename2 = "/home/thomasligonnet/Documents/XS/xs_lib/JEFF4T4/ace/26-Fe-56g"
    try:
        xs_data = parse_ace_file(ace_filename)
        xs_data2 = parse_ace_file(ace_filename2)
    except Exception as e:
        print("Error parsing ACE file:", e)
        sys.exit(1)
    nrj=xs_data["102"]['l_nrj']
    totXS=xs_data["102"]['l_xs']
    nrj2=xs_data2["102"]['l_nrj']
    totXS2=xs_data2["102"]['l_xs']
    plt.figure()
    # plt.plot(nrj,nrj)
    plt.plot(nrj,totXS)
    plt.plot(nrj2,totXS2)
    plt.xlabel("Energy [MeV]")
    plt.ylabel("XS [barn]")
    plt.xscale("log")
    plt.yscale("log")
    plt.show()

if No_MAYA:
    cp = shutil.copyfile
    class Dummy:
        def __init__(self, path):
            self.d_rea=parse_ace_file(path)
    ACE=Dummy
else:
    import maya  # type: ignore
    cp = maya.utils.cp
    ACE=maya.coconust.AceRawData

def copy_modif_write(paf1, paf2, l_paramreplace=[]):
    with open(paf1) as f:
        txt = "".join(f.readlines())
    for paramreplace in l_paramreplace : txt = txt.replace(*paramreplace)
    with open(paf2, "w") as f:
        f.write(txt)

###### Début de lapartie active du code ######






# infinite looping until manual stop

for i_loop in range(1 if not Looping else 123456789):
    ###### Partie génération ######

    if (not skip_XS_gen) and not No_MAYA:
        if Is_annealed:
            path_archive="XS_out/archive_numpy_inter/"
        #f.close() # cest une liste, ca se close pas :)
        # if os.path.isfile("Log_xs_gen.txt"):
        #     LOG=True
        #     fl=open("Log_xs_gen.txt").readlines()[-1].split()
        #     f=open("Log_xs_gen.txt","a")
        #     num=int(fl[0])+1
        #     samp_start=int(fl[7])
        #     f.write("\n{0}   time: {1}   samples: {2} - {3}   ".format(num,dt.datetime.now(),samp_start+1,samp_start+nb_sample))
        #     f.close()
        # else:
        #     LOG=False
        #     f=open("Log_xs_gen.txt","w")
        #     num=1
        #     samp_start=0
        #     f.write("\n{0}   time: {1}   samples: {2} - {3}   ".format(num,dt.datetime.now(),samp_start+1,samp_start+nb_sample))
        #     f.close()

        ######################################################################################################### input param
        print("library: "+bd)
        print("nombre of sample per XS: {}".format(nb_sample))
        ######################################################################################################### generation des samples
        if do_sample :
            print("lancement coconust", i_loop)
                                                                                     # TODO Axel
            coco = maya.coconust.CocoManager(bd, l_T_plot=[300 if i_loop==0 else 900]) # que au premier run pr checker que ok, mais plus apres pcq c'est long    coco.njoy(1, [1, 2],            "*",300)
            coco.njoy(1, [1, 2],               "*",300)
            coco.njoy(2, [3, 4],               "*",300)
            coco.njoy(4, [9],                  "*",300)
            coco.njoy(5, [10,11],              "*",300)
            #coco.njoy(6, [0,12,13],            "*",300)
            coco.njoy(6, "*",            "*",300)
            coco.njoy(7, [14,15],              "*",300)
            #coco.njoy(8, [16,17,18],           "*",300)
            coco.njoy(8, [16,18],           "*",300)
            coco.njoy(12,[24,25,26],           "*",300)
            coco.njoy(13,[27],                 "*",300)
            coco.njoy(14,[28,29,30],           "*",300)
            coco.njoy(16,[32,33,34,36],        "*",300)
            coco.njoy(19,[39,40,41],           "*",300)
            coco.njoy(22,[46,47,48,49,50],     "*",300)
            coco.njoy(23,[50,51],              "*",300)
            coco.njoy(24,[50,52,53,54],        "*",300)
            coco.njoy(25,[55],                 "*",300)
            if 26 != l_zz_elt_aaa[0][0] : coco.njoy(26,[54,56,57,58],        "*",300) # pour eviter le double calcul, a jouter pour Cr et Ni
            coco.njoy(27,[59],                 "*",300)
            coco.njoy(28,[58,60,61,62,64],     "*",300)
            coco.njoy(29,[63,65],              "*",300)
            coco.njoy(30,[0,64,66,67,68,70],   "*",300)
            coco.njoy(31,[69,71],              "*",300)
            coco.njoy(33,[75],                 "*",300)
            coco.njoy(41,[93],                 "*",300)
            coco.njoy(42,"*",                  "*",300)
            coco.njoy(48,"*",                  "*",300)
            coco.njoy(49,[113,115],            "*",300)
            coco.njoy(50,"*",                  "*",300)
            coco.njoy(74,[180,182,183,184,186],"*",300)
            coco.njoy(79,[197],                "*",300)
            coco.njoy(82,[204,206,207,208],    "*",300)
            coco.njoy(83,[209],                "*",300)
            coco.njoy(92,[235, 238],           "*",300)
            coco.njoy(94,[239],                "*",300)
            if nb_sample >0:
                for zz,elt,aaa in l_zz_elt_aaa:
                    coco.njoy(zz, aaa, "g",300, rand_l_mt=l_mt, rand_nb=nb_sample)
            coco.do_your_job()
            print("coconust ok")

        ######################################################################################################### plot des samples
        # paf_bp = maya.utils.param.path_xsdata_sss+"/"+bd
        #if do_plot :
        #    for xlim, ylim, paf in [[(1e-5,  20e6), (1e-6, 1e5), "out_xs_sample.png"     ],
        #                            [(0.1e6, 20e6), (1e-4, 1e1), "out_xs_sample_zoom.png"]]:
        #        maya.coconust.plotXs (
        #                            l_path      = list(map(lambda zz_elt_aaa : paf_bp+"/ace/{:02}-{}-{:03}-ga-0300.ace"       .format(*zz_elt_aaa), l_zz_elt_aaa)),
        #                            l_path_icov = list(map(lambda zz_elt_aaa : paf_bp+"/ace/_icov/{:02}-{}-{:03}-ga-0300_auto-4.npz".format(*zz_elt_aaa), l_zz_elt_aaa)), # [maya.utils.param.path_xsdata_sss+"/endfb8/ace/_icov/28-Ni-060-ga-0300_auto-4.npz"],
        #                            l_name      = list(map(lambda zz_elt_aaa : "^{"+str(zz_elt_aaa[0])+"}_{"+str(zz_elt_aaa[2])+"}{"+zz_elt_aaa[1]+"}", l_zz_elt_aaa)),
        #                            l_mt        = ["2","4","18","102"],
        #                            rand        = True,
        #                            ylabel      = None,
        #                            path_save   = paf,
        #                            xlim        = xlim,
        #                            ylim        = ylim,
        #                        )

        ######################################################################################################### fct utiles



        ######################################################################################################### recup des ace/xsdir
        if do_recup :
            if  True:
                maya.utils.mkdir(paf_bp+"/out_sample_xs", rm=False)
                maya.utils.mkdir(paf_bp+"/out_sample_plot", rm=False)
                maya.utils.mkdir(paf_bp+"/out_sample_plot_rand", rm=False)
            for zz,elt,aaa in l_zz_elt_aaa :
                name_ace = "{:02}-{}-{:03}-ga-0300.ace".format(zz,elt,aaa)
                
                #Check if reference file already in
                # if not LOG:
                # TODO keep the XS in the origin directory
                # maya.utils.cp(paf_bp+"/ace/"+name_ace, "XS/out_sample_xs/"+name_ace)
                #with open(paf_bp+"/ace/"+name_ace,"r") as file:
                #    filedata=file.read()
                #filedata=filedata.replace("g.0300c","gr0000.0300c")
                #with open(paf_bp+"/ace/"+name_ace,"w") as file:
                #    file.write(filedata)
                #avoid sample overwriting
                copy_modif_write(paf_bp+"/ace/"      +name_ace,                          paf_bp+"/out_sample_xs/"      +name_ace,                          [["g.0300c","gr{:04}.0300c".format(0)]])
                #copy_modif_write(paf_bp+"/ace_xsdir/"+name_ace.replace(".ace",".xsdir"), paf_bp+"/out_sample_xsdir/"+name_ace.replace(".ace",".xsdir"), [["g.0300c","gr{:04}.0300c".format(0)]])
                nstart=0
                first=True
                for n in range(nb_sample):
                    psource=paf_bp+"/ace/"+name_ace
                    if os.path.isfile(psource.replace(".ace", "_r"+str(n+1)+".ace")):
                        copy_modif_write(psource.replace(".ace", "_r"+str(n+1)+".ace"),   paf_bp+"/out_sample_xs/"      +name_ace.replace(".ace", "_r"+str(n+1+nstart)+".ace"),   [["gr{}.0300c".format(n+1),"gr{:04}.0300c".format(n+1+nstart)]])
                        copy_modif_write(psource.replace(".ace", "_r"+str(n+1)+".txt"),   paf_bp+"/out_sample_xs/"      +name_ace.replace(".ace", "_r"+str(n+1+nstart)+".txt"),   [["gr{}.0300c".format(n+1),"gr{:04}.0300c".format(n+1+nstart)]])
                    else:
                        if first: 
                            print("Warning in recup XS: {} does not exist, reference file will be used instead".format(name_ace).replace(".ace", "_r"+str(n+1)+".ace"))
                            first=False
                        copy_modif_write(psource,   paf_bp+"/out_sample_xs/"      +name_ace.replace(".ace", "_r"+str(n+1+nstart)+".ace"),   [["g.0300c","gr{:04}.0300c".format(n+1+nstart)]])
                    #copy_modif_write(paf_bp+"/ace_xsdir/"+name_ace.replace(".ace", "_r"+str(n+1)+".xsdir"), paf_bp+"/out_sample_xsdir/"+name_ace.replace(".ace", "_r"+str(n+1+nstart)+".xsdir"), [["gr{}.0300c".format(n+1),"gr{:04}.0300c".format(n+1+nstart)]])
                cp(paf_bp+"/ace_img/"+name_ace.replace(".ace", ".png"), paf_bp+"/out_sample_plot/"+name_ace.replace(".ace", ".png"))
                if nb_sample>0:
                    name_big_data="{:02}-{}-{:03}-ga-0300_{}_big_data.npz".format(zz,elt,aaa,"_".join(map(str, l_mt)))
                    maya.utils.mkdir("out_sample_log_coconust", rm=False)
                    cp("log_coconust/"+name_big_data, "out_sample_log_coconust/"+name_big_data)
                
                #cp(paf_bp+"/ace_img/_rand/"+name_ace.replace(".ace", ".png"), "XS/out_sample_plot_rand/"+name_ace.replace(".ace", "_"+str(n+1+nstart)+".png"))

                if do_plot and nb_sample>0:
                    for xlim, ylim, paf in [[(1e-5,  20e6), (1e-6, 1e5), paf_bp+"/out_sample_plot_rand/"+name_ace.replace(".ace", "_r"+str(n+1+nstart)+".png")     ],
                                            [(0.1e6, 20e6), (1e-4, 1e1), paf_bp+"/out_sample_plot_rand/"+name_ace.replace(".ace", "_r"+str(n+1+nstart)+"_zoom.png")]]:
                        maya.coconust.plotXs (
                                            l_path      = paf_bp+"/ace/"+name_ace,
                                            l_path_icov = paf_bp+"/ace/_icov/"+name_ace.replace(".ace", "_auto-4.npz"),
                                            #l_name      = list(map(lambda zz_elt_aaa : "^{"+str(zz_elt_aaa[0])+"}_{"+str(zz_elt_aaa[2])+"}{"+zz_elt_aaa[1]+"}", l_zz_elt_aaa)),
                                            l_mt        = l_mt,
                                            rand        = True,
                                            ylabel      = None,
                                            path_save   = paf,
                                            xlim        = xlim,
                                            ylim        = ylim,
                                        )


        if do_xsdata:
            #l_name=list(map(lambda s: "{:02}-{}-{:03}-g0-300.ace".format(*s),l_zz_elt_aaa))
            l_name=list(map(lambda s: "{:02}-{}-{:03}-ga-0300.ace".format(*s),l_zz_elt_aaa))
            print(l_name)
            f=open(paf_bp+"/out_sample_xs/xsdata","w")
            #for line in open(paf_bp+"/ace/xsdata","r").readlines():
            for line in open(paf_bp+"/xsdata","r").readlines():
                if "gr" not in line:
                    f.write(line)
                    if  any(map(lambda s: s in line.split("/")[-1],l_name)):
                        f.write(line.replace("g.0300c","gr0000.0300c").replace(paf_bp+"/ace/",paf_bp+"/out_sample_xs/"))
                        for n in range(nb_sample):
                            f.write(line.replace("g.0300c","gr{0:04}.0300c".format(n+1)).replace(paf_bp+"/ace/",paf_bp+"/out_sample_xs/").replace(".ace","_r{}.ace".format(n+1)))
            f.close()
    else:
        print("XS Generation skipped, if simulation are runned the older ones won't be erased")

    ###### Partie lancement de simulations ######

    if nb_sim!=0:  
        # f.close() # cest une liste, ca se close pas :)
        print("number of thread per simulation: {}".format(omp_sim))
        print("number of simulations: {}".format(nb_sim))

        def job(data):
            num=data[0]
            omp=data[1]
            # samp=data[2]
            path="{}_num".format(socket_name)
            tm.sleep(0.1*(num-start_num))# avoids writing issue
            
            if os.path.isdir(path+str(int(num))): # comme ca si sss plante il devait pas penser que tt est ok :)
                shutil.rmtree(path+str(int(num)))
            os.makedirs(path+str(int(num)),exist_ok=True)
            #shutil.copyfile("input","Calc/num"+str(int(num))+"/input")
                                #xsdata
            with open(paf_bp+"/out_sample_xs/xsdata","r") as file:
                filedata=file.read()
            with open(path+str(int(num))+"/xsdata","w") as file:
                file.write(filedata)
            is_6000g=False
            if "6000g.0300c" in filedata:
                is_6000g=True
            if nb_sample!=0:
                with open("inputs/input_{}".format(mat),"r") as file:
                    filedata=file.read()
                filedata=filedata.replace("set seed 42","set seed {}".format(int(42+num*10)))
                filedata=filedata.replace("autopert 1 256","autopert 1 {0}".format(nb_sample))
                if not is_6000g:
                    filedata=filedata.replace("% endfb","")
                else:
                    filedata=filedata.replace("% jeff", "")

            else:
                with open("inputs/input_{}".format(mat),"r") as file:
                    filedata=file.read()
                filedata=filedata.replace("set seed 42","set seed {}".format(int(42+num*10)))
                filedata=filedata.replace("autopert 1 256","")
                filedata=filedata.replace("set pop      20000    330   50","set pop      20000    {}   50".format(int(6e5/nb_sim)))
                if not is_6000g:
                    filedata=filedata.replace("% endfb","")
                else:
                    filedata=filedata.replace("% jeff", "")

            with open(path+str(int(num))+"/input","w") as file:
                file.write(filedata)
            #autogeom
            with open("inputs/auto_geom_{}.out".format(mat),"r") as file:
                filedata=file.read()
            with open(path+str(int(num))+"/auto_geom.out","w") as file:
                file.write(filedata)

            # os.chdir("Calc/num"+str(int(num)))
            if No_MAYA:
                bashcommand="/home/thomasligonnet/Serpent/sss_tfm_2.5_wgt_map_src/sss2 input -omp "+str(omp)
            else:
                bashcommand="../../SERPENT/sss2 input -omp "+str(omp)
            # bashcommand="../SERPENT/sss2 input -omp "+str(omp)
            # f=open("Launch_log.txt","a")
            # f.write("\n{0}   start time: {1}     omp: {2}    sample:{3} ".format(num,dt.datetime.now(),omp,samp))
            # f.close()
            if No_MAYA:
                process=sb.Popen(bashcommand.split(),cwd=path+str(int(num)))
                process.communicate()
            else:
                paf_log = f"/tmp/sss_log_{path}{num}"
                print(f"lancement de la {i_loop} eme serie de calcul de sss, log dans {paf_log}")
                maya.utils.calc.Executeur(bashcommand+" > "+paf_log, position=path+str(int(num)), w8=True)

        if __name__=='__main__':
            with Pool(processes=nb_sim) as pool:
                # resu=pool.map(job,range(20))
                res=pool.map(job,zip(range(start_num,start_num+nb_sim+1),[omp_sim]*nb_sim))
                pool.close()
                pool.join()
    else:
        print("Simulations skipped")

    ### Results merging part ###

    # from utils_p11_WIP import *

    #rc['serpentVersion'] = '2.1.21'

    def get_C(suffix=""): #helper function
        l_name_in_input=[]
        l_name_in_input_OG=[]
        Cref=[]
        Cref_sig=[]
        l_ref_dosi=[]
        IsMn=False # To handle the Mn contamination of the Fe56 dosimeters
        for path_calc in path_calcs:
            Path_calc=socket_name+"_"+path_calc
            Cref+=np.loadtxt(add_csv_path+"/input_mat_sss_2_of/rr_vec{}".format(suffix),skiprows=1)[:,0].tolist()
            Cref_sig+=np.loadtxt(add_csv_path+"/input_mat_sss_2_of/rr_vec{}_sig".format(suffix),skiprows=1)[:,0].tolist()
            with open(Path_calc+"input") as file:
                filedata=file.readlines()
            while "mat_matrix_rr" not in filedata[0]: filedata.pop(0)
            filedata.pop(0)
            while "idet" in filedata[0]:
                name=filedata[0].split()[1].replace("mat_dosi_","")
                l_name_in_input_OG+=[name]
                iso=filedata[0].split()[2]
                if "BMC" in name:
                    if iso=="260540" or iso=="260560" or iso=="260580" or iso=="250550":
                        name=easy_replace(name,["BMC-"],["Fe-"])
                    if iso=="130270":
                        name=easy_replace(name,["BMC-"],["Al-"])
                    if iso=="491150":
                        name=easy_replace(name,["BMC-"],["In-"])
                        name+="-i"
                if iso=="260540":
                    name=easy_replace(name,["Pfe","Pni","Pcr","Pss"],["Pfe54","Pni54","Pcr54","Pss54"])
                elif iso=="260580":
                    name=easy_replace(name,["Pfe","Pni","Pcr","Pss"],["Pfe58","Pni58","Pcr58","Pss58"])   
                if iso=="250550":
                    name=easy_replace(name,["Fe-"],["Mn-"])   
                    IsMn=True
                l_name_in_input+=[name]
                l_ref_dosi+=[easy_replace(name,l_nums, ["-{}".format(ref_dosi)]*len(l_nums))]
                filedata.pop(0)
        return l_name_in_input, l_name_in_input_OG, Cref, Cref_sig, l_ref_dosi, IsMn

    if nb_sim!=0 or force_merging:
        sub_path=os.getcwd()+"/{}_num".format(socket_name)
        os.makedirs(sub_path+"0",exist_ok=True)
        os.makedirs(sub_path+"0/input_mat_sss_2_of",exist_ok=True)
        for file in outputs2merge:
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
                if vec_s[0][i]!= "":
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
        print ("Merging done!")
        print ("#"*50)
        print ()
        if nb_sample==0:
            shutil.copytree(sub_path+"0",add_csv_path,dirs_exist_ok=True)
            print("Reference calculation done!")
            l_name_in_input, l_name_in_input_OG, Cref, Cref_sig, l_ref_dosi, IsMn = get_C()
            df=pd.read_csv(path_ref,delimiter=";")
            j=0
            while df["l_name"][j]!="C":j+=1
            j+=1
            keys=df.keys()
            k=0
            while df["l_name"][k]!="l_thickness":k+=1
            for i in range(len(l_name_in_input)):
                if l_name_in_input[i] in keys:
                    if l_name_in_input[i] not in l_name_in_input_OG:
                        name=l_name_in_input[i]
                        th_factor=float(df.loc[k  ,name])/float(df.loc[k  ,"Fe-"+"-".join(name.replace("-i","").split("-")[1:])])
                        df.loc[j  ,name]=Cref[i]*den_fact*th_factor
                        df.loc[j+1,name]=Cref_sig[i]*den_fact*th_factor
                        df.loc[j+2,name]=Cref_sig[i]/Cref[i]*100
                    else:
                        name=l_name_in_input[i]
                        df.loc[j  ,name]=Cref[i]
                        df.loc[j+1,name]=Cref_sig[i]
                        df.loc[j+2,name]=Cref_sig[i]/Cref[i]*100
            df.to_csv(add_csv_path+"/result.csv",sep=";",index=False,header=lmap(lambda s: s.replace(".1","").replace(".2","").replace(".3","").replace(".4","").replace(".5",""),list(df)))
            print("Reference csv created !")
            exit()
    else:
        print("Merging skipped")

    ### Partie Evaluation des résultats (Chi2) ###
    if nb_sim != 0 or force_weighting or force_merging:
    # df = pd.read_csv("Fe_au.csv")
        def cor_sig_to_cov(cor, std):
            cov  = cor * 1.
            cov *= std[:, None]
            cov *= std[None, :]
            return cov

        def get_res_csv(path,key,return_Cov=True,pop_duplicate=True):
            with open(path,"r") as file:
                readfile=file.readlines()
            l_name=readfile.pop(0).replace(",",";").strip().split(";")[1:]
            while readfile[0].replace(",",";").split(";")[0].strip()!=key:
                if readfile[0].replace(",",";").split(";")[0].strip()=="l_thickness":
                    l_thickness=np.array(readfile.pop(0).replace(",",";").split(";")[1:],dtype=np.float64)
                else:
                    readfile.pop(0)
            readfile.pop(0)
            vec=np.array(readfile.pop(0).replace(",",";").split(";")[1:],dtype=np.float64)
            sig=np.array(readfile.pop(0).replace(",",";").split(";")[1:],dtype=np.float64)
            rel=np.array(readfile.pop(0).replace(",",";").split(";")[1:],dtype=np.float64)/100
            l_dup=[] #to handle ratio duclicate
            for i in range(len(l_name)-1):
                if l_name[i]==l_name[i+1]:
                    l_dup+=[i+1]
            vec=np.delete(vec,l_dup)
            sig=np.delete(sig,l_dup)
            rel=np.delete(rel,l_dup)
            l_thickness=np.delete(l_thickness,l_dup)
            # print(l_dup)
            if return_Cov:
                cor=np.array([readfile.pop(0).replace(",",";").split(";")[1:] for i in range(len(l_name))],dtype=np.float64)/100
                print(cor.shape)
                cor=np.delete(np.delete(cor,l_dup,axis=0),l_dup,axis=1)
                print(cor.shape)
                cov=cor_sig_to_cov(cor,sig)
                l_name=np.delete(l_name,l_dup)
                return vec, sig ,rel ,cov,l_name,l_thickness
            l_name=np.delete(l_name,l_dup)
            return vec, sig ,rel,l_name,l_thickness

        ExE2C,ExE2C_sig,ExE2C_rel,ExE2C_cov,ExE2C_names,_=get_res_csv(path=path_ref,key="E*E2C")
        if os.path.isfile(add_csv_path+"/result.csv"):
            Cref,Cref_sig,Cref_rel,Cref_names,l_thickness=get_res_csv(path=add_csv_path+"/result.csv",key="C",return_Cov=False)   
            CoE_ref,CoE_ref_sig,CoE_ref_rel,CoE_ref_cov,CoE_ref_names,_=get_res_csv(path=add_csv_path+"/result.csv",key="C/(E*E2C)-1") # to compute reference chi2
        else: 
            Cref,Cref_sig,Cref_rel,Cref_names,l_thickness=get_res_csv(path=path_ref,key="C",return_Cov=False)
            CoE_ref,CoE_ref_sig,CoE_ref_rel,CoE_ref_cov,CoE_ref_names,_=get_res_csv(path=path_ref,key="C/(E*E2C)-1") # to compute reference chi2

        l_name_in_input, l_name_in_input_OG, Cdiff, Cdiff_sig, l_ref_dosi, IsMn = get_C(suffix="diff")


        Cdiff=np.array(Cdiff)
        Cdiff_sig=np.array(Cdiff_sig)
        #corection for the virtaul dosimeter thickness, =1 for real dosimeters
        l_name_in_input=np.array(l_name_in_input)
        l_name_in_input_OG=np.array(l_name_in_input_OG)
        l_ref_dosi=np.array(l_ref_dosi)
        if IsMn:
            for i in range(len(l_name_in_input)):
                if (l_name_in_input[i].replace("Fe-","Mn-") in l_name_in_input) and (l_name_in_input[i].replace("Fe-","Mn-") != l_name_in_input[i]) :
                    pos=(l_name_in_input==l_name_in_input[i].replace("Fe-","Mn-"))
                    Cdiff[i]=Cdiff[i]+Cdiff[pos]
                    Cdiff_sig[i]=(Cdiff_sig[i]**2+Cdiff_sig[pos]**2)**0.5
                    pos_ref=(Cref_names==l_name_in_input[i])
                    Cref[pos_ref]=Cref[pos_ref]+Cdiff[pos,0]*den_fact
                    Cref_sig[pos_ref]=(Cref_sig[pos_ref]**2+(Cdiff_sig[pos,0]*den_fact)**2)**0.5
        Cdiff=Cdiff[:,1:]
        Cdiff_sig=Cdiff_sig[:,1:]
        Cdiff=Cdiff.T
        Cdiff_sig=Cdiff_sig.T
        # C_CS=Cdiff.T + Cref
        # C_CS_sig=((Cdiff_sig**2).T + Cref_sig**2)**0.5
        # print(Cdiff[0])
        #Remove results that are not in the simulation from arrays
        l_NotInSim=[]
        for i in range(len(Cref_names)):
            if (Cref_names[i] not in l_name_in_input):
                l_NotInSim+=[i] 
        if l_NotInSim:
            Cref_names      = np.delete(Cref_names     , l_NotInSim, axis=-1)
            l_thickness      = np.delete(l_thickness     , l_NotInSim, axis=-1)
            Cref      = np.delete(Cref     , l_NotInSim, axis=-1)
            Cref_sig  = np.delete(Cref_sig , l_NotInSim, axis=-1)    
            ExE2C     = np.delete(ExE2C    , l_NotInSim, axis=-1) 
            ExE2C_sig = np.delete(ExE2C_sig    , l_NotInSim, axis=-1) 
            ExE2C_cov = np.delete(np.delete(ExE2C_cov, l_NotInSim, axis=0) , l_NotInSim, axis=1)     
            CoE_ref     = np.delete(CoE_ref    , l_NotInSim, axis=-1) 
            CoE_ref_cov = np.delete(np.delete(CoE_ref_cov, l_NotInSim, axis=0) , l_NotInSim, axis=1)   

        l_NotInRes=[]
        for i in range(len(l_name_in_input)):
            if (l_name_in_input[i] not in Cref_names):
                l_NotInRes+=[i] 
        if l_NotInRes:
            l_name_in_input= np.delete(l_name_in_input     , l_NotInRes, axis=-1)
            l_name_in_input_OG= np.delete(l_name_in_input_OG     , l_NotInRes, axis=-1)
            l_ref_dosi= np.delete(l_ref_dosi     , l_NotInRes, axis=-1)
            Cdiff      = np.delete(Cdiff     , l_NotInRes, axis=-1)
            Cdiff_sig  = np.delete(Cdiff_sig , l_NotInRes, axis=-1)   

        # C/E caclulation + propagation

        RNG= np.random.default_rng()
        # putting the C in the C/E vector 
        Nid=order_indices(Cref_names,l_name_in_input)
        l_name_in_input_OG=l_name_in_input_OG[Nid]
        l_name_in_input=l_name_in_input[Nid]
        Cdiff     =Cdiff[:,Nid]
        Cdiff_sig =Cdiff_sig[:,Nid]
        l_ref_dosi=l_ref_dosi[Nid]
        ids_virt_thick=easy_id(l_name_in_input_OG,Cref_names,Virtual_BMC_replace=True)
        print("ok")
        ids_real_thick=easy_id(l_name_in_input,Cref_names,Virtual_BMC_replace=False)
        l_thickness_factor=l_thickness[ids_real_thick]/l_thickness[ids_virt_thick]
        print(l_name_in_input_OG)
        print(l_name_in_input)
        # print(l_thickness)
        # print(l_thickness[ids_real_thick])
        # print(l_thickness[ids_virt_thick])
        print(l_thickness_factor)
        # exit()
        for i in range(len(l_name_in_input_OG)):
            if "BMC" in l_name_in_input_OG[i]:
                Cdiff[:,i]*=den_fact
                Cdiff[:,i]*=l_thickness_factor[i]

        if ref_dosi:
            l_id=[]
            i=0
            for name in Cref_names:
                if ("-10" in name) or (("-rc" in name)) or ("-rp" in name):
                    l_id+=[i]
                elif Only_dosi:
                    if name.split("-")[0] not in Only_dosi:
                        l_id+=[i]
                i+=1
            Cref_names = np.delete(Cref_names     , l_id, axis=-1)
            l_name_in_input= np.delete(l_name_in_input     , l_id, axis=-1)
            l_name_in_input_OG= np.delete(l_name_in_input_OG     , l_id, axis=-1)
            l_thickness= np.delete(l_thickness     , l_id, axis=-1)
            l_ref_dosi= np.delete(l_ref_dosi     , l_id, axis=-1)
            Cdiff      = np.delete(Cdiff     , l_id, axis=-1)
            Cdiff_sig  = np.delete(Cdiff_sig , l_id, axis=-1)   
            Cref      = np.delete(Cref     , l_id, axis=-1)
            Cref_sig  = np.delete(Cref_sig , l_id, axis=-1)    
            ExE2C     = np.delete(ExE2C    , l_id, axis=-1) 
            ExE2C_sig = np.delete(ExE2C_sig    , l_id, axis=-1) 
            ExE2C_cov = np.delete(np.delete(ExE2C_cov, l_id, axis=0) , l_id, axis=1)     
            CoE_ref     = np.delete(CoE_ref    , l_id, axis=-1) 
            CoE_ref_cov = np.delete(np.delete(CoE_ref_cov, l_id, axis=0) , l_id, axis=1)     
        
        
        print(Cref_names)
        print(l_name_in_input)
        print(l_ref_dosi)
        print("mean relative error on the difference per dosi in %")
        print(np.mean(np.abs(Cdiff_sig/Cdiff*100),axis=0))
        # print(Cref)
        # print(Cdiff[0])
        # print(ExE2C_sig)
        # print(np.diag(ExE2C_cov)**0.5)
        # print(C_CS)
        # print(C_CS_sig)
        
        #TODO: check which uncertainty has to be correlated between samples to avoid adding false noise
        # For example we should Cref_sig_should be the same every where as it depends on the reference res 
        # So the sampling of Cref and Cdiff have to be separated  
        CoE_samples=RNG.normal(Cdiff,Cdiff_sig,(Nsample_unc,*Cdiff.shape))
        Cref_samples=RNG.normal(Cref,Cref_sig,(Nsample_unc,*Cref.shape))
        for i in range(CoE_samples.shape[1]):
            CoE_samples[:,i,:]+=Cref_samples
        ExE2C_samples=RNG.multivariate_normal(ExE2C,ExE2C_cov,Nsample_unc) 

        # CoE_ref_samples=RNG.multivariate_normal(CoE_ref,CoE_ref_cov,Nsample_unc)
        print(Cdiff.shape     ,CoE_samples.shape ,ExE2C.shape    ,ExE2C_samples.shape)
        # print(CoE_samples[0][0])
        # print(np.std(CoE_samples[:,0,:],axis=0))
        # C/E calc
        for i in range(CoE_samples.shape[1]):
            CoE_samples[:,i,:]/=ExE2C_samples
        print(CoE_samples[0,0,:])
        ## Free Memory
        del ExE2C_samples
        del Cref_samples

        #Normalization
        if ref_dosi: # Computing reference chi2 to be used as potential wgt threshold for russian roulette
            l_id_ref=easy_id(l_ref_dosi,l_name_in_input)
            l_delete=np.unique(l_id_ref)
            # CoE_ref_samples=RNG.multivariate_normal(CoE_ref,CoE_ref_cov,Nsample_unc)
            # CoE_ref_samples-=CoE_ref_samples[:,l_id_ref]
            # CoE_ref=np.mean(CoE_ref_samples,axis=0)
            # CoE_ref_cov=np.cov(CoE_ref_samples.T)
            # cova=CoE_ref_cov
            # cova=np.delete(np.delete(cova,l_delete,axis=1),l_delete,axis=0)
            # cova_inv = np.linalg.inv(cova)
            # res=np.delete(CoE_ref,l_delete)
            # Chi2_ref = res.T.dot(cova_inv.dot(res))
            CoE_samples-=CoE_samples[:,:,l_id_ref]

        else:
            CoE_samples -=1
            cova=CoE_ref_cov
            cova_inv = np.linalg.inv(cova)
            res=CoE_ref
            # Chi2_ref = res.T.dot(cova_inv.dot(res))

        print(CoE_samples.shape)
        # averaging and Covar
        print(CoE_samples[0,0,:])
        CoE_CS=np.mean(CoE_samples,axis=0)
        sh=Cdiff.shape
        CoE_CS_cov=np.zeros((sh[0],sh[1],sh[1]))
        for i in range(len(CoE_CS_cov)):
            CoE_CS_cov[i]=np.cov(CoE_samples[:,i,:].T)

        print(CoE_CS_cov.shape)
        # print(CoE_CS[100]*100)
        # print(np.diag(CoE_CS_cov[1])**0.5*100)
        print("ref:")
        print((Cref/ExE2C-(Cref/ExE2C)[2])*100) 
        # print(CoE_CS_cov[0])
        # exit()
        Chi2_CS=-np.ones(sh[0])
        for i in range(sh[0]): 
            cova=CoE_CS_cov[i]
            if ref_dosi:
                cova=np.delete(np.delete(cova,l_delete,axis=1),l_delete,axis=0)
                res=np.delete(CoE_CS[i],l_delete)
            cova_inv = np.linalg.inv(cova)
            chis = res.T.dot(cova_inv.dot(res))
            Chi2_CS[i]=chis 

        # exit()
        ### Cross-sections trimming and posterior calculation ###

        wgt_CS=np.exp(-Chi2_CS/2) 

        ### Add correction if annealed
        if Is_annealed and Only_dosi is None:
            l_ACE_ori=[]
            l_ACE_prior=[]
            l_ACE_sampled=[]
            l_wgt_cor_iso=[]
            no_bigmat=False
            if False:
                for zz,elt,aaa in l_zz_elt_aaa :
                    Big_vec_ori, Big_mat_ori=get_Big(zz,elt,aaa,"ori",mat=True)
                    Big_vec_new, Big_mat_new=get_Big(zz,elt,aaa,"new",mat=True)
                    BigM_inv_ori=np.linalg.inv(Big_mat_ori)
                    BigM_inv_new=np.linalg.inv(Big_mat_new)
                    l_wgt_cor_tmp=[]
                    for n in range(1,len(wgt_CS)+1):
                        Big_vec_samp=get_Big(zz,elt,aaa,str(n),mat=False)
                        Diff_ori=Big_vec_samp-Big_vec_ori
                        Diff_new=Big_vec_samp-Big_vec_new
                        l_wgt_cor_tmp+=[np.exp(-1/2 * (Diff_ori.T.dot(BigM_inv_ori.dot(Diff_ori))
                                                            - Diff_new.T.dot(BigM_inv_new.dot(Diff_new))))]
            else:
                for zz,elt,aaa in l_zz_elt_aaa :
                    Big_vec_eq_ori,Big_mat_ori=get_Big(zz,elt,aaa,l_mt,"prior",mat=True)
                    Big_vec_eq_new,Big_mat_new=get_Big(zz,elt,aaa,l_mt,"inter",mat=True)
                    if np.linalg.matrix_rank(Big_mat_ori)<len(Big_mat_ori):
                        Big_mat_ori=Big_mat_ori#+np.eye(len(Big_mat_ori))*1e-10  #give the same results as pinv
                        Big_mat_new=Big_mat_new#+np.eye(len(Big_mat_ori))*1e-10  #give the same results as pinv
                    BigM_inv_ori=np.linalg.pinv(Big_mat_ori)
                    BigM_inv_new=np.linalg.pinv(Big_mat_new)
                    Big_ratio=Big_vec_eq_new/Big_vec_eq_ori
                    l_wgt_cor_tmp=[]
                    for n in range(1,len(wgt_CS)+1):
                        Big_vec_samp=get_samp(zz,elt,aaa,str(n))
                        Diff_ori=Big_vec_samp*Big_ratio-1
                        Diff_new=Big_vec_samp-1
                        expo1=Diff_ori.T.dot(BigM_inv_ori.dot(Diff_ori))
                        expo2=Diff_new.T.dot(BigM_inv_new.dot(Diff_new))
                        expo=-1/2 * (expo1-expo2)
                        # print(expo1,expo2,expo)
                        # l_wgt_cor_tmp+=[np.exp(-1/2 * expo)]
                        l_wgt_cor_tmp+=[expo] # log_weight
                    l_wgt_cor_iso+=[l_wgt_cor_tmp]
            l_wgt_cor_iso=np.array(l_wgt_cor_iso)
            # l_wgt_cor =np.prod(l_wgt_cor_iso,axis=0)
            l_wgt_cor =np.sum(l_wgt_cor_iso,axis=0) # log_weight

        else:
            l_wgt_cor=np.ones(len(wgt_CS))
        l_id_XS_tokeep=[]
        if Is_annealed:
            wgt_CS=np.log(wgt_CS)+l_wgt_cor
            Chi2_CS=wgt_CS*(-2)
        else:
            wgt_CS=wgt_CS*l_wgt_cor
            Chi2_CS= np.log(wgt_CS)*(-2)
        if wgt_thresh: # trim the XS with wgt and russian roulette and create adjusted chi2 for low wgt
            print("Trimming XS")
            def arrenum(X):
                l=[]
                for i, val in enumerate(X, start=1):
                    l+=[[i,val]]
                return np.array(l)

            a_Ewgt=arrenum(wgt_CS)
            print(a_Ewgt.shape)
            # exit()
            a_Ewgt=np.flip(a_Ewgt[np.argsort(a_Ewgt[:,1])],axis=0) #ordered from max to min wgt
            # print(a_Ewgt[:10])
            # exit()
            sum_wgt=sum(a_Ewgt[:,1])
            print("a_Ewgt ", a_Ewgt[:,1])
            print("Chi2_CS", Chi2_CS)
            a_Cwgt=np.cumsum(a_Ewgt[:,1])/sum_wgt
            
            chi2_maxi_ok = 0
            nb_ok, nb_pasok = 0,0
            for i in range(len(a_Ewgt)):
                if i==0 or a_Cwgt[i-1]<Cthresh:
                    chi2_maxi_ok = max(chi2_maxi_ok, Chi2_CS[int(a_Ewgt[i,0]-1)])
                    nb_ok += 1
                else:
                    nb_pasok += 1
                
            print(f"chi2_maxi_ok={chi2_maxi_ok}, soit {nb_ok/(nb_ok+nb_pasok)*100 : .1f} % des xs")
            nb_recup, nb_loss = 0,0
            for i in range(len(a_Ewgt)):
                if i==0 or a_Cwgt[i-1]<Cthresh:
                    l_id_XS_tokeep+=[int(a_Ewgt[i,0])]
                else:
                    ok = True
                    while ok and Chi2_CS[int(a_Ewgt[i,0]-1)] > chi2_maxi_ok :
                        if RNG.random() < proba_roulette:
                            Chi2_CS[int(a_Ewgt[i,0]-1)]-=(2*np.log(1/proba_roulette)) # Compute the equivalent chi2 (corrected for the roullette proba)
                        else:
                            ok = False
                    if Chi2_CS[int(a_Ewgt[i,0]-1)] <= chi2_maxi_ok:
                        l_id_XS_tokeep+=[a_Ewgt[i,0]]
                        nb_recup += 1
                    else:
                        Chi2_CS[int(a_Ewgt[i,0]-1)]*=1000 # => exp(-X²/2)=0
                        nb_loss += 1
            print(f"sauvetage de {nb_recup/(nb_recup+nb_loss)*100 : .1f} % des xs ratees (pour eviter de biaiser la rejection)")
            l_id_XS_tokeep=np.array(l_id_XS_tokeep)
            print("Trimming done! XS kept : {}".format(len(l_id_XS_tokeep)))
        else:
            l_id_XS_tokeep=np.arange(len(wgt_CS))
        # wgt_CS=np.array(wgt_CS)

        if not os.path.isdir("XS_out"):
            os.mkdir("XS_out")
            os.mkdir("XS_out/ace")
            os.mkdir("XS_out/xsdir")
            os.mkdir("XS_out/plot")
            os.mkdir("XS_out/archive_numpy_post")
            os.mkdir("XS_out/archive_numpy_prior")
            os.mkdir("XS_out/archive_numpy_inter")
            for zz,elt,aaa in l_zz_elt_aaa :
                name_ace = "{:02}-{}-{:03}-ga-0300.ace".format(zz,elt,aaa)
                cp(paf_bp+"/out_sample_xs/"+name_ace, "XS_out/ace/"+name_ace)
                name_big_data="{:02}-{}-{:03}-ga-0300_{}_big_data.npz".format(zz,elt,aaa,"_".join(map(str, l_mt)))
                if not os.path.isfile("XS_out/out_sample_log_coconust/"+name_big_data):
                    cp("log_coconust/"+name_big_data, "XS_out/archive_numpy_prior/"+name_big_data)
                # cp(paf_bp+"/xsdir/"+name_ace.replace(".ace", ".xsdir"), "XS_out/xsdir/"+name_ace.replace(".ace", ".xsdir"))
                cp(paf_bp+"/ace_img/"+name_ace.replace(".ace", ".png"), "XS_out/plot/"+name_ace.replace(".ace", ".png"))

        if not os.path.isfile("XS_out/{}".format(f_wgt_name)):   
            with open("XS_out/{}".format(f_wgt_name),"w") as file:
                file.write("XS_num    eq_Chi2\n")

        print(Chi2_CS.shape)
        print(l_id_XS_tokeep.shape)
        # print(l_id_XS_tokeep)
        # exit()
        filedata = open("XS_out/{}".format(f_wgt_name)).readlines()
        if filedata[-1].split()[0]=="XS_num":
            id_XS = 1
        else:
            id_XS=int(filedata[-1].split()[0])+1
        for n in range(1,len(Chi2_CS)+1):
            if n in l_id_XS_tokeep:
                for zz,elt,aaa in l_zz_elt_aaa :
                    name_ace = "{:02}-{}-{:03}-ga-0300.ace".format(zz,elt,aaa)
                    copy_modif_write(paf_bp+"/out_sample_xs/"      +name_ace.replace(".ace", "_r"+str(n)+".ace"),   "XS_out/ace/"      +name_ace.replace(".ace", "_r"+str(id_XS)+".ace"),   [["gr{:04}.0300c".format(n),"gr{:04}.0300c".format(id_XS)]])
                    copy_modif_write(paf_bp+"/out_sample_xs/"      +name_ace.replace(".ace", "_r"+str(n)+".txt"),   "XS_out/ace/"      +name_ace.replace(".ace", "_r"+str(id_XS)+".txt"),   [["gr{:04}.0300c".format(n),"gr{:04}.0300c".format(id_XS)]])
                    # copy_modif_write(paf_bp+"/ace_xsdir/"+name_ace.replace(".ace", "_r"+str(n)+".xsdir"), "XS_out/xsdir/"+name_ace.replace(".ace", "_r"+str(id_XS)+".xsdir"), [["gr{:04}.0300c".format(n),"gr{:04}.0300c".format(id_XS)]])
                filedata+=["{:06}    {}\n".format(id_XS,Chi2_CS[n-1])]
                id_XS+=1
        txt="".join(filedata)
        with open("XS_out/{}".format(f_wgt_name),"w") as file:
            file.write(txt)
    else:
        print("going straight to BMC")




    ### BMC XS prod ###
    Chi2_CS_res=np.loadtxt("XS_out/{}".format(f_wgt_name),skiprows=1)
    if not Skip_BMC and (len(Chi2_CS_res.shape)>1):
        l_mt2=[1]+l_mt
        a_Chi2=Chi2_CS_res[:,1]
        

        print("minimum Chi2 {}".format(min(a_Chi2)))
        a_wgt=np.exp(-a_Chi2/2)/sum(np.exp(-a_Chi2/2))
        # a_wgt=np.exp(-Chi2_CS_res[:,1]/36/2) # Chi reduits
        print("sum_wgt:{}".format(np.sum(a_wgt)))
        # a_wgt=a_wgt/sum(a_wgt)
        a_Ewgt=np.flip(a_wgt[np.argsort(a_wgt)],axis=0) #ordered from max to min wgt
        print("weights:{}".format((a_Ewgt)))
        d_posterior={}
        d_prior={}
        for zz,elt,aaa in l_zz_elt_aaa :
            name_ace = "{:02}-{}-{:03}-ga-0300.ace".format(zz,elt,aaa)
            d_posterior["{:02}{:03}".format(zz,aaa)]={}
            d_prior["{:02}{:03}".format(zz,aaa)]={}
            
            prior=ACE("XS_out/ace/"      +name_ace)
            is_anneal_intermediate=False #check for data that has covariance
            if False:
                path_numpy_prior="XS_out/archive_numpy_prior/{:02}-{}-{:03}-ga-0300_auto-4_mt2_4_102_eig_cor_i40.npz".format(zz,elt,aaa)
                if os.path.isfile(path_numpy_prior.replace("prior","inter")):
                    is_anneal_intermediate=True
                    dico_prior=np.load(path_numpy_prior.replace("prior","inter"),allow_pickle=True)['dict_data'].tolist()
                    dico_post=dico_prior
                else:
                    print("no prior for {}".format(name_ace))
            # print(elt)
            dico_ace_out=prior.d_rea
            for mt in l_mt2:
                print("{}, mt: {}".format(name_ace,mt))
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]={}
                d_prior["{:02}{:03}".format(zz,aaa)][str(mt)]={}
                d_prior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs"]=prior.d_rea[str(mt)]["l_xs"]
                d_prior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_nrj"]=prior.d_rea[str(mt)]["l_nrj"]
                l_xs=[]
                for i in range(1,int(Chi2_CS_res[-1,0]+1)):
                # for i in range(1,5):
                    post = ACE("XS_out/ace/"      +name_ace.replace(".ace", "_r"+str(i)+".ace"))
                    # print("elt.d_rea.keys()", list(elt.d_rea.keys()))
                    l_nrj = post.d_rea[str(mt)]["l_nrj"]
                    l_xs  += [post.d_rea[str(mt)]["l_xs"]]
                    # if do_anneal:
                    #     l_xs_txt+=[np.loadtxt("XS_out/ace/"      +name_ace.replace(".txt", "_r"+str(i)+".txt")).tolist()]
                # a_wgt=a_wgt[:4]
                l_xs=np.array(l_xs)
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_nrj"]=l_nrj
                tmp=imoyvar(l_xs,l_w=a_wgt,do_jackknife=True)
                std=imoyvar(l_xs,l_w=a_wgt,do_jackknife=False)[1] #because results with Jacknife can cause bug with very bad cases
                std=np.max([std,tmp[2]],axis=0)
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs"]=tmp[0]
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs_sig"]=std
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs_ste"]=tmp[2]
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs_cov"]=icovar_jkk(l_xs,l_w=a_wgt)
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["N_eff"]=np.sum(a_wgt)**2/np.sum(a_wgt**2)
                dico_ace_out[str(mt)]["l_xs"]=d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs"]
                if mt==4:
                    for key in dico_ace_out.keys():
                        if int(key)>50 and int(key)<92:
                            # print(key)
                            # print(len(prior.d_rea[str(mt)]["l_xs"]))
                            # print(len(dico_ace_out[key]["l_xs"]))
                            for i in range(1,len(dico_ace_out[key]["l_xs"])+1):
                                dico_ace_out[key]["l_xs"][-i]*=(d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs"][-i]/prior.d_rea[str(mt)]["l_xs"][-i])
                ### Results plotting ###
                if True:
                    name_plot = "{:02}-{}-{:03}-MT-{}-Result.png".format(zz,elt,aaa,mt)
                    l_nrj=d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_nrj"]
                    unc=(d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs_sig"])
                    err=(d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs_ste"])
                    pltpost=d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs"]
                    pltcov=d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs_cov"]
                    pltprior=d_prior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs"]
                    # N_eff=d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["N_eff"]
                    # err=unc/(N_eff**0.5)
                    # unc=np.diag(d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]["l_xs_cov"])**0.5
                    ####  annealing ["{}".format(mt)]
                    ####  annealing ["{}".format(mt)]



                        ######  New part produces big_data ######
                        

                        ######  old part produces auto_cor ######
                    if False:
                    # if do_anneal and is_anneal_intermediate:
                        print("computing posterior matrices")
                        # a_factors=np.ones(len(dico_post["l_nrj"])-1)
                        # a_cov=np.ones((len(dico_post["l_nrj"])-1,len(dico_post["l_nrj"])-1))
                        # #computing the mean factors
                        # for i in range(1,len(dico_post["l_nrj"])):
                        #     l_idx=(l_nrj<dico_post["l_nrj"][i]) & (l_nrj>dico_post["l_nrj"][i-1])
                        #     valpost=np.sum(pltpost[l_idx])
                        #     valprior=np.sum(pltprior[l_idx])
                        #     if valpost==0 or valprior==0:
                        #         a_factors[i-1]=0
                        #     else:
                        #         a_factors[i-1]=valpost/valprior                            
                        #     for j in range(i,len(dico_post["l_nrj"])):
                        #         l_idy=(l_nrj<dico_post["l_nrj"][j]) & (l_nrj>dico_post["l_nrj"][j-1])    
                        #         a_cov[i-1,j-1]=np.mean(pltcov[l_idx][:,l_idy])
                        #         a_cov[j-1,i-1]=np.mean(pltcov[l_idx][:,l_idy])
                        
                        
                        
                        bins     = np.asarray(dico_post["l_nrj"])
                        idx = np.digitize(l_nrj, bins) - 1
                        idx = np.clip(idx, 0, bins.size-2)
                        B = bins.size - 1

                        # 2) compute a_factors via bincount
                        post_sums  = np.bincount(idx, weights=pltpost, minlength=B)
                        prior_sums = np.bincount(idx, weights=pltprior, minlength=B)

                        a_factors = np.zeros(B, dtype=float)
                        mask = (post_sums != 0) & (prior_sums != 0)
                        a_factors[mask] = post_sums[mask] / prior_sums[mask]


                        # 3) compute block‐means of pltcov in one shot:
                        #    build a one‐hot matrix M of shape (N, B)
                        M = np.eye(B, dtype=int)[idx]      # M[r, i] == 1 iff sample r in bin i

                        #    sum of cov entries in each (i,j) block
                        sum_blocks   = M.T @ pltcov @ M    # shape (B, B)

                        #    count how many entries contributed to each block
                        count_blocks = M.T @ M             # shape (B, B)

                        #    mean = sum / count, with zero where count is zero
                        a_cov = np.zeros_like(sum_blocks, dtype=float)
                        nonzero = count_blocks != 0
                        a_cov[nonzero] = sum_blocks[nonzero] / count_blocks[nonzero]
                        dico_post["{}".format(mt)]=dico_post["{}".format(mt)]*a_factors
                        dico_post[(str(mt),str(mt))]=a_cov
                        print("testing singularity")
                        # print("determinant: {}".format(np.linalg.det(a_cov)))
                        # try:
                        rank = np.linalg.matrix_rank(dico_post[(str(mt),str(mt))])
                        rank_old = np.linalg.matrix_rank(dico_prior[(str(mt),str(mt))])
                        # except np.linalg.LinAlgError:
                        #     print("Matrix is not invertible ({0},{0})!".format(mt))
                        #     exit()
                        if rank != rank_old:
                            print("Warning matrix rank are different {0} & {1}".format(rank,rank_old))
                        if rank != len(dico_post[(str(mt),str(mt))]):
                            print("Warning matrix is smaller than size {0} & {1}".format(rank,len(dico_post[(str(mt),str(mt))])))
                        else:
                            print("Matrix invertible")
                    plt.figure()
                    plt.plot(l_nrj,pltpost,label="posterior")
                    plt.plot(l_nrj,pltprior,label="prior",linestyle="--")
                    plt.fill_between(l_nrj,pltpost-unc,pltpost+unc,alpha=0.2)
                    plt.xlabel("Energy [MeV]")
                    plt.ylabel("XS [barn]")
                    plt.xscale("log")
                    plt.yscale("log")
                    plt.legend()
                    plt.title("Posteriror and prior XS for {0}-{1}, MT: {2}".format(elt,aaa,mt))
                    if only_plot_fast:
                        plt.xlim(max([1e-3,min(l_nrj)]),max(l_nrj))
                        plt.savefig("XS_out/plot/{}".format(name_plot.replace(".png","fast.png")))
                    else:
                        plt.xlim(min(l_nrj),max(l_nrj))
                        plt.savefig("XS_out/plot/{}".format(name_plot))
                    plt.close()
                    fig,ax=plt.subplots()
                    if only_plot_fast:
                        vec=(l_nrj>=max([1e-3,min(l_nrj)]))
                    else:
                        vec=(l_nrj>=max([1e-12,min(l_nrj)]))
                    l_nrj=l_nrj[vec]
                    pltpost=pltpost[vec]
                    pltprior=pltprior[vec]
                    unc=unc[vec]
                    err=err[vec]
                    plt.plot(l_nrj,(pltpost/pltprior-1)*100)
                    if only_plot_fast:
                        ax.set_xlim(max([1e-3,min(l_nrj)]),max(l_nrj))

                    ylim=plt.ylim()
                    plt.fill_between(l_nrj,(pltpost/pltprior-1)*100-(unc/pltprior)*100,(pltpost/pltprior-1)*100+(unc/pltprior)*100,alpha=0.2,label="Standard deviation")
                    plt.fill_between(l_nrj,(pltpost/pltprior-1)*100-(err/pltprior)*100,(pltpost/pltprior-1)*100+(err/pltprior)*100,alpha=0.2,label="Uncertainty on the mean")
                    plt.hlines(0,min(l_nrj),max(l_nrj),linestyles="--",colors="k")
                    plt.legend()
                    plt.xlabel("Energy [MeV]")
                    plt.ylabel("$\Delta$XS [%]")
                    plt.xscale("log")
                    # plt.yscale("log")
                    plt.ylim(ylim)
                    plt.title("Difference between posteriror and prior {0}-{1}, MT: {2}".format(elt,aaa,mt))
                    # plt.savefig("XS_out/plot/{}".format(name_plot.replace("Result","diff")))
                    if only_plot_fast:
                        # plt.xlim(max([1e-3,min(l_nrj)]),max(l_nrj))
                        plt.savefig("XS_out/plot/{}".format(name_plot.replace("Result","diff").replace(".png","fast.png")))
                    else:
                        plt.xlim(min(l_nrj),max(l_nrj))
                        plt.savefig("XS_out/plot/{}".format(name_plot.replace("Result","diff")))
                    Array=np.array([l_nrj,(pltpost/pltprior-1)*100,(unc/pltprior)*100,(err/pltprior)*100])
                    print(Array.shape)
                    
                    np.savetxt("XS_out/plot/{}".format(name_plot.replace("png","txt").replace("Result","diff")),
                               Array.T,
                               delimiter="    ",
                               header="Energy [MeV]    Delta_XS [%]    std    ste")
                    # for i in range(len(l_nrj)):
                    #     f_tosave.write("{}    {}    {}    {}".format())
                    plt.close()
                if True: #Low memory mode erase the posterior to gain memory
                    print("Low memory mode erase prior after plotting")
                    d_prior["{:02}{:03}".format(zz,aaa)][str(mt)]={}
            
            if do_anneal: #Computing new big_mat and big_vec 
                l_xs_txt=[]
                for i in range(1,int(Chi2_CS_res[-1,0]+1)):
                    l_xs_txt+=[np.loadtxt("XS_out/ace/"      +name_ace.replace(".ace", "_r"+str(i)+".txt")).tolist()]
                l_xs_txt=np.array(l_xs_txt)
                l_vec=np.array([get_Big(zz,elt,aaa,l_mt2[1:],"prior",mat=False)]*len(l_xs_txt))*l_xs_txt
                Big_mat_posterior=icovar_jkk(l_xs_txt,l_w=a_wgt)
                Big_vec_posterior=imoyvar(l_vec,l_w=a_wgt,do_jackknife=True)[0]
                dict_data={'big_mat':Big_mat_posterior,'big_vec':Big_vec_posterior}
                if Is_annealed:
                    np.savez("XS_out/archive_numpy_post/{:02}-{}-{:03}-ga-0300_{}_big_data.npz".format(zz,elt,aaa,"_".join(map(str,l_mt2[1:]))),dict_data=dict_data)
                else:
                    np.savez("XS_out/archive_numpy_inter/{:02}-{}-{:03}-ga-0300_{}_big_data.npz".format(zz,elt,aaa,"_".join(map(str,l_mt2[1:]))),dict_data=dict_data)

            if False:
            # if do_anneal and is_anneal_intermediate:
                dict_data=np.array(dico_post)
                np.savez("XS_out/archive_numpy_post/{:02}-{}-{:03}-ga-0300_auto-4_mt2_4_102_eig_cor_i40_post.npz".format(zz,elt,aaa),dict_data={"big_mat": Big_mat_posterior,"big_vec":Big_vec_posterior})
            if Is_annealed:
                update_ace_file("XS_out/ace/"      +name_ace,"XS_out/archive_numpy_post/"+name_ace,dico_ace_out)
            else:
                update_ace_file("XS_out/ace/"      +name_ace,"XS_out/archive_numpy_inter/"+name_ace,dico_ace_out)
            if True: #Low memory mode erase the posterior to gain memory
                print("Low memory mode erase posterior")
                d_posterior["{:02}{:03}".format(zz,aaa)][str(mt)]={}
    else:
        print("BMC Assimilation Skipped")


