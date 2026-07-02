from ..Common.utils_general import lmap, lfilter
import os
import numpy as np
def get_sss_res(path, key):   #key : get_res
    """
    Extract a result value (and uncertainty, if available) from an Serpent2 result file.

    The function reads an Serpent2 result file, searches for a line containing the
    specified key, and parses the numerical result. If the expected file does
    not exist, a fallback filename is attempted. Depending on the file format,
    the function returns either a value alone or a value together with its
    associated uncertainty.

    Parameters
    ----------
    path : str
        Path to the Serpent2 result file.
    key : str
        Identifier used to locate the desired result within the file.

    Returns
    -------
    float or tuple of float
        If an uncertainty is provided in the file, returns ``(value, uncertainty)``.
        Otherwise, returns the value alone.
    """
    if not os.path.isfile(path):
        path=path[:-6]+"1_res.m"
        print("Warning in get_sss_res for "+str(key)+", change from tmp to tmp1")
    lines = open(path).readlines()
    while key not in lines[0]: lines.pop(0)
    if lines[0].split()[-3] != "=" :
        vals = lines[0].split("]")[1].split("[")[1].split()
        v = np.array(lmap(lambda s:float(s), vals[0:-1:2]))
        s = np.array(lmap(lambda s:float(s), vals[1::2]))
        if len(v)==1:
            return v[0], v[0]*s[0]
        return v, v*s
    else :
        v = float(lines[0].split()[-2])
        return v

def get_sss_det(path, key, mid_E=False, no_E=False,spatial=False,time=False):   #key : get_res
    """
    Extract detector spectral data from an Serpent2 detector file.

    The function parses an Serpent2 detector result file to retrieve energy bins,
    detector values, and associated uncertainties for a given key. Depending
    on the ``mid_E`` option, the energy representation corresponds either to
    bin edges or to mid-bin energies.

    Parameters
    ----------
    path : str
        Path to the Serpent2 detector output file.
    key : str
        Identifier used to locate the detector data block in the file.
    mid_E : bool, optional
        If ``False``, return energy bin edges. If ``True``, return mid-bin
        energy values.
    no_E : bool, optional
        If ``True``, leave the energy list empty.
    spatial : bool, optional
        If ``True``, load the detector spatial discretization.
    time : bool, optional
        If ``True``, load the detector time discretization.
    

    Returns
    -------
    tuple
        Tuple ``(E, v, dv,[T,X,Y,V)]`` where:
        - ``E`` is a list of energy values (empty if no_E is True),
        - ``v`` is a list of detector values,
        - ``dv`` is a list or array of absolute uncertainties associated
          with ``v``,
        - ``T`` is a list of time values (if time is True not included otherwise),
        - ``X`` is a list of X coord. values (if spatial is True not included otherwise),
        - ``Y`` is a list of Y coord. values (if spatial is True not included otherwise),
        - ``Z`` is a list of Z coord. values (if spatial is True not included otherwise).
    """
    # if not os.path.isfile(path):
        # path=path[:-6]+"1_res.m"
        # print("Warning in get_sss_res for "+str(key)+", change from tmp to tmp1")

    E = []
    v = []
    s = []
    with open(path, 'r') as file:
        lines = iter(file)
        # Skip lines until key is found
        for line in lines:
            if key in line:
                break

        # Parse v and s
        for line in lines:
            if "]" in line:
                break
            parts = line.split()
            v.append(float(parts[-2]))
            s.append(float(parts[-1]))

        if not no_E:
            # Skip lines until key+E is found
            for line in lines:
                if (key + "E") in line:
                    break

            # Parse E
            for line in lines:
                if "]" in line:
                    parts = line.split()
                    if not mid_E:
                        E.append(float(parts[0]))
                        if len(parts) > 1:
                            E.append(float(parts[1]))
                    else:
                        E.append(float(parts[2]))
                    break
                parts = line.split()
                if not mid_E:
                    E.append(float(parts[0]))
                else:
                    E.append(float(parts[2]))
        l_list=[np.array(E),np.array(v),np.multiply(v,s)]
        if time:
            T=[]
            for line in lines:
                if (key + "T") in line:
                    break

            # Parse X
            for line in lines:
                if "]" in line:
                    break
                parts = lmap(lambda s: float(s),line.split())
                T +=[parts]
            l_list+=[np.array(T)]
        if spatial:
            X=[]
            for line in lines:
                if (key + "X") in line:
                    break

            # Parse X
            for line in lines:
                if "]" in line:
                    break
                parts = lmap(lambda s: float(s),line.split())
                X +=[parts]
            Y=[]
            for line in lines:
                if (key + "Y") in line:
                    break

            # Parse Y
            for line in lines:
                if "]" in line:
                    break
                parts = lmap(lambda s: float(s),line.split())
                Y +=[parts]
            Z=[]
            for line in lines:
                if (key + "Z") in line:
                    break

            # Parse Z
            for line in lines:
                if "]" in line:
                    break
                parts = lmap(lambda s: float(s),line.split())
                Z +=[parts]
            l_list+=[np.array(X),np.array(Y),np.array(Z)]
    return tuple(l_list)


def get_sss_out(path, key):
    """
    Extract an output array or list from an Serpent2 output file.

    The function scans an Serpent2 output file for a line containing the specified
    key, then reads and parses the associated output block. The output may
    span multiple lines and can contain either numerical values or strings,
    which are returned accordingly.

    Parameters
    ----------
    path : str
        Path to the Serpent2 output file.
    key : str
        Identifier used to locate the desired output block in the file.

    Returns
    -------
    tuple or list
        If the key is not found, returns ``(None, None)``.
        Otherwise, returns a list of parsed values:
        - list of float if the output contains numerical values,
        - list of str if the output contains quoted string values.
    """
    fichier = open(path)
    n_vide = 0
    line = fichier.readline()
    while key not in line and n_vide<10:
        line = fichier.readline()
        if len(line) == 0: n_vide += 1
        else:              n_vide  = 0
    if len(line)==0:
        return None,None
    out = " ".join(line.split()[2:])
    while ";" not in line:
        line = fichier.readline()
        out += line
    out = out.replace("[","").replace("]","").replace(";","")
    if "'" in out:
        return lmap(lambda s:" ".join(s.replace("_"," ").replace("'","").split()),out.replace(" ","_").split())
    return lmap(lambda s:float(s), out.split())



def recup_sss_out(paf, n=None, dim_p=None, trunc=False, recup_spectre=True,gr_order=0):
    """
    Collect and post-process Serpent2 output data for dosimeters/material samples.

    This function parses Serpent2 input/output files in a given directory to build a
    structured dictionary of results for each detector/material instance. It
    extracts geometry/material metadata from the Serpent2 input, reads reaction-rate
    results and associated uncertainties, optionally reads and groups spectra,
    and computes derived quantities such as perturbed totals, NDUP-like
    dispersion metrics, and spectral thresholds.

    Multiple result directories may be supported (e.g., merged auto-generated
    cross-section cases), in which case differential perturbations and spectra
    are concatenated across cases.

    Parameters
    ----------
    paf : str
        Path to the Serpent2 case directory containing the ``input`` file and result
        subdirectories/files (e.g., ``*_mat_sss_2_of`` structures).
    n : int, optional
        Optional selector/limit for the amount of data to retrieve (behavior
        depends on downstream usage; may be unused in the current implementation).
    dim_p : int, optional
        Maximum number of perturbed samples (differential results) to keep for
        each key. If provided, arrays of perturbations are truncated to this
        length.
    trunc : bool, optional
        If ``True``, use truncated result filenames (suffix ``"_trunc"``).
    recup_spectre : bool, optional
        If ``True``, also retrieve per-detector spectra and reaction-rate spectra
        from SSS output files.
    gr_order : int, optional
        Exponent controlling grouping of spectral bins. A value of ``k`` groups
        bins by a factor of ``2**k`` (summing groups of bins).

    Returns
    -------
    tuple
        Tuple ``(data, l_matzaimt)`` where:

        - ``data`` is a dictionary keyed by detector/material identifier
          strings. Each entry contains metadata (e.g., composition, density,
          geometry) and numerical arrays for reaction rates, uncertainties,
          perturbations, and (optionally) spectra and derived spectral metrics.

        - ``l_matzaimt`` is a list of grouping descriptors of the form
          ``((mat, zai, mt), list_of_keys)`` used to organize detectors by
          material/reaction, optionally sorted by spectral characteristics.

    Notes
    -----
    - The function assumes specific Serpent2 file naming conventions (e.g.,
      ``rr_vecdiff``, ``perspectra``, and their ``_sig`` counterparts).
    - Several computations are performed in-place within the returned ``data``
      structure (e.g., totals from differential terms, dispersion estimates,
      threshold energies).
    """
    data = {}
    trunc = "" if not trunc else "_trunc"
    d_mt = {"11004":"51", "12102":"102"}
    lines_input   = open(paf+"/input").readlines()                            # get dosimeter information from sss input
    #if os.path.exists(paf+"/auto_geom.out"):
    if "auto_geom.out" in "".join(lines_input):
        lines_input   += open(paf+"/auto_geom.out").readlines()
    list_idet_raw = lmap(lambda l:l.split()[1:], filter(lambda l: "idet" in l.split()[:1], lines_input))
    list_name     = lmap(lambda t:t[0], list_idet_raw)
    list_zai      = lmap(lambda t:t[1], list_idet_raw)
    list_mt       = lmap(lambda t:t[2] if t[2] not in d_mt else d_mt[t[2]], list_idet_raw)
    list_den      = lmap(lambda idet : -float(lfilter(lambda l: "mat"  in l.split()[:1] and idet in l.split(), lines_input)[0].split()[2])    , list_name)
    list_compo    = lmap(lambda idet :        lfilter(lambda l: "mat"  in l.split()[:1] and idet in l.split(), lines_input)[0].split()[3:]    , list_name)
    list_surf     = lmap(lambda mat  :        lfilter(lambda l: "cell" in l.split()[:1] and mat  in l.split(), lines_input)[0].split()[-2][1:], list_name)
    if list_surf[0][:3]=="at_":    # new version
        list_surf     = map(lambda mat  :     lfilter(lambda l: "cell" in l.split()[:1] and mat  in l.split(), lines_input)[0].split()[-1][1:], list_name)
    list_r_d1_d2  = lmap(lambda sur  :        lfilter(lambda l: "surf" in l.split()[:1] and sur  in l.split(), lines_input)[0].split()[-3:]   , list_surf)
    list_vol      = lmap(lambda r_d1_d2 : np.pi*float(r_d1_d2[0])**2*(float(r_d1_d2[2])-float(r_d1_d2[1])), list_r_d1_d2)
    list_masse    = np.array(list_vol)*np.array(list_den)
    list_mat      = lmap(lambda name: name.split("_")[-1], list_name)
    if os.path.exists(paf+"/tmp_mat_sss_2_of/rr_vecdiff"):                        # seek the data position
        l_path = [paf+"/tmp_mat_sss_2_of"]                                        #  case1: in the given directory
    elif os.path.exists(paf+"/input_mat_sss_2_of/rr_vecdiff"):                    # seek the data position
        l_path = [paf+"/input_mat_sss_2_of"]                                    #  case1: in the given directory
    elif os.path.exists(paf+"/auto_cs/case_0/input_mat_sss_2_of/rr_vecdiff"):    #  case2: in the auto_cs - results have to be merged
        l_path = [paf+"/auto_cs/case_0/input_mat_sss_2_of"]
        i = 1
        while os.path.exists(paf+"/auto_cs/case_"+str(i)+"/input_mat_sss_2_of/rr_vecdiff"):
            l_path += [paf+"/auto_cs/case_"+str(i)+"/input_mat_sss_2_of"]
            i += 1
    else:
        print ("ERROR - recup_sss_out -",paf,"- no data")
        exit()
    #print l_path
    #exit()
    for ipath, path in enumerate(l_path):
        lignes = open(path+"/rr_vecdiff"+trunc).readlines()                        # load rr data
        dim = lmap(lambda s:int(s),lignes.pop(0).split())                        # get data shape
        vec = np.array(lmap(lambda s:float(s), " ".join(lignes).split()))        # get all words and convert to float
        list_rr       = vec.reshape(dim)
        list_rr_sig   = np.array(lmap(lambda s:float(s), " ".join(open(path+"/rr_vecdiff"+trunc+"_sig").readlines()[1:]).split())).reshape(dim)
        #print list_name
        #print len(list_name), list_rr.shape
        for imat, name in enumerate(list_name):
            key = name+"_"+list_mt[imat]+"_"+list_zai[imat]
            if ipath==0:
                data[key] = {"zai":list_zai[imat], "mt"   :list_mt[imat],    "den":list_den[imat], "compo" :list_compo[imat],
                        "vol":list_vol[imat], "masse":list_masse[imat], "mat":list_mat[imat], "e"     :float(list_r_d1_d2[imat][2])-float(list_r_d1_d2[imat][1]),
                        }
                data[key]["rv"]    = list_rr    [imat,0]
                data[key]["rs"]    = list_rr_sig[imat,0]
                data[key]["l_dpv"] = list_rr    [imat,1:]
                data[key]["l_dps"] = list_rr_sig[imat,1:]
            else:
                data[key]["l_dpv"] = np.array(list(data[key]["l_dpv"])+list(list_rr    [imat][1:]))
                data[key]["l_dps"] = np.array(list(data[key]["l_dps"])+list(list_rr_sig[imat][1:]))
        if recup_spectre:
            dim = lmap(lambda s:int(s),open(path+"/perspectra"+trunc).readlines()[0].split())    # get data shape
            dim[-1]=int(dim[-1]/(2**gr_order))
            for (datapath, dataname) in [("perspectra", "spectra"), ("rrperspectra", "rrspectra")]:
                specdata       = np.array(lmap(lambda lv: sum(lv),np.reshape(lmap(lambda s:float(s), " ".join(open(path+"/"+datapath+trunc       ).readlines()[1:]).split()),(-1,2**gr_order)))).reshape(dim)
                specdata_sig   = np.array(lmap(lambda lv: sum(lv),np.reshape(lmap(lambda s:float(s), " ".join(open(path+"/"+datapath+trunc+"_sig").readlines()[1:]).split()),(-1,2**gr_order)))).reshape(dim)
                for imat, name in enumerate(list_name):
                    key = name+"_"+list_mt[imat]+"_"+list_zai[imat]
                    if ipath==0:
                        data[key]["l_" +dataname+"_v"]  = specdata    [1+imat,0,:]
                        data[key]["l_" +dataname+"_s"]  = specdata_sig[1+imat,0,:]
                        data[key]["ll_"+dataname+"_dpv"] = specdata    [1+imat,1:,:]
                        data[key]["ll_"+dataname+"_dps"] = specdata_sig[1+imat,1:,:]
                        E1,E2 = 1e-10, 20.
                        nb_e = len(specdata[imat,0,:])
                        data[key]["l_nrj_piquet"] = 10**(((np.log10(E2)-np.log10(E1)) * np.array(range(nb_e+1))*1./(nb_e  )) + np.log10(E1))
                        data[key]["l_nrj"]        = (data[key]["l_nrj_piquet"][1:] +data[key]["l_nrj_piquet"][:-1])/2
                    else:
                        data[key]["ll_"+dataname+"_dpv"] = np.array(list(data[key]["ll_"+dataname+"_dpv"])+list(specdata     [imat,1:,:]))
                        data[key]["ll_"+dataname+"_dps"] = np.array(list(data[key]["ll_"+dataname+"_dps"])+list(specdata_sig[imat,1:,:]))
        #print data.keys()
        #print key
        if dim_p is not None and len(data[key]["l_dpv"]) >= dim_p:
            break
    
    for key in data.keys():                                            # few additional calculations ...
        if dim_p is not None:                                        # limit the number of perturbed data
            data[key]["l_dpv"] =  data[key]["l_dpv"][:dim_p]
            data[key]["l_dps"] =  data[key]["l_dps"][:dim_p]
        data[key]["l_pv"] =  data[key]["rv"]   +data[key]["l_dpv"]                    # compute the total result from differential value
        data[key]["l_ps"] = (data[key]["rs"]**2+data[key]["l_dps"]**2)**0.5
        if recup_spectre:
            for (datapath, dataname) in [("perspectra", "spectra"), ("rrperspectra", "rrspectra")]:
                data[key]["ll_"+dataname+"_pv"] =  data[key]["l_"+dataname+"_v"]   +data[key]["ll_"+dataname+"_dpv"]
                data[key]["ll_"+dataname+"_ps"] = (data[key]["l_"+dataname+"_s"]**2+data[key]["ll_"+dataname+"_dps"]**2)**0.5
        
        rv_moy = sum(data[key]["l_pv"]) / len(data[key]["l_pv"])                    # compute result dispertion
        rv_sig = sum((data[key]["l_pv"] - rv_moy)**2  / len(data[key]["l_pv"]))**0.5
        data[key]["rv_ndup"] = (rv_moy,rv_sig)
        if recup_spectre:
            tmp_l_rrspectra_v = data[key]["l_rrspectra_v"] * 1.                        # compute the threshold
            for i in range(len(tmp_l_rrspectra_v))[1:]: tmp_l_rrspectra_v[i] += tmp_l_rrspectra_v[i-1]
            tmp_l_rrspectra_v /= (tmp_l_rrspectra_v[-1]+1e-15)
            for lim in [0.1,0.25,0.5,0.75]:
                filtered_l = filter(lambda v:v>lim, tmp_l_rrspectra_v)
                if len(filtered_l) > 0:
                    i0 = list(tmp_l_rrspectra_v).index(filtered_l[0])
                    e0,e1, v0,v1 = data[key]["l_nrj"][i0-1], data[key]["l_nrj"][i0], tmp_l_rrspectra_v[i0-1], tmp_l_rrspectra_v[i0]
                    avt = (lim-v0)/(v1-v0)
                    data[key]["threshold_"+str(lim)] = avt*e1 + (1-avt)*e0
                else:
                    data[key]["threshold_"+str(lim)] = data[key]["l_nrj"][0]
            #data[key]["ave_nrj"] = sum(data[key]["l_nrj"] * data[key]["l_rrspectra_v"]) / sum(data[key]["l_rrspectra_v"])
            data[key]["ave_nrj"] = 10**(sum(np.log10(data[key]["l_nrj"]) * data[key]["l_rrspectra_v"]) / sum(data[key]["l_rrspectra_v"]))
    l_zai,l_mt,l_mat = map(lambda l:list(set(l)), [list_zai, list_mt, list_mat])
    l_matzaimt = []
    for mt in l_mt:
        for mat in l_mat:
            for key in data.keys():
                if mat == data[key]["mat"] and mt == data[key]["mt"]:
                    if (mat,data[key]["zai"],mt) not in l_matzaimt:
                        l_matzaimt += [(mat,data[key]["zai"],mt)]
    def list_dosi(mat,zai,mt):
        list_dosi = []
        for key in data.keys():
            if mat == data[key]["mat"] and mt == data[key]["mt"] and zai == data[key]["zai"]: list_dosi += [key]
        return sorted(list_dosi)
    def th_of(mat,zai,mt, th="ave_nrj"): # "threshold_0.5"
        ilist_dosi = list_dosi(mat,zai,mt)
        return sum(map(lambda ke : data[ke][th], ilist_dosi))/len(ilist_dosi)
    if recup_spectre:
        l_matzaimt = lmap(lambda key: (key,list_dosi(*key)), sorted(l_matzaimt, key=lambda mat_zai_mt:th_of(*mat_zai_mt)))
    else:
        l_matzaimt = lmap(lambda key: (key,list_dosi(*key)), sorted(l_matzaimt, key=lambda mat_zai_mt:mat_zai_mt[1]+mat_zai_mt[2]))
    return data, l_matzaimt