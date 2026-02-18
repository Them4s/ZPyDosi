import os
import numpy as np
def get_irdff_iaea(path, e_min=None):
    """
    Load IRDFF/IAEA cross-section data and correlation information from files.

    The function reads IRDFF/IAEA-formatted files associated with a given base
    path and returns both the cross-section tabulation and the correlation
    matrix over energy groups. Energies are converted from eV to MeV.

    The function expects files with suffixes ``"_xs"`` (cross sections),
    ``"_cor"`` (correlation matrix definition), and optionally ``"_sig"``
    (relative uncertainties in percent used to adjust the cross-section
    uncertainties).

    Parameters
    ----------
    path : str
        Base path to the IRDFF/IAEA data files (without suffix).
    e_min : float, optional
        Minimum energy threshold (currently not applied in the implementation).

    Returns
    -------
    tuple
        Tuple ``((l_cor_e, cor), (l_xs_e, l_xs_v, l_xs_s))`` where:

        - ``l_cor_e`` is the correlation energy grid (in MeV),
        - ``cor`` is the correlation matrix,
        - ``l_xs_e`` is the cross-section energy grid (in MeV),
        - ``l_xs_v`` is the cross-section values,
        - ``l_xs_s`` is the cross-section uncertainties (absolute).
    """
    lines = open(path+"_xs").readlines()
    while "//" not in lines[0]:
        lines.pop(0)
    lines.pop(0)
    l_xs_e, l_xs_v, l_xs_s = [], [], []
    while "//" not in lines[0]:
        e,v,s = map(lambda s:float(s), lines.pop(0).split())
        l_xs_e += [e]
        l_xs_v += [v]
        l_xs_s += [s]
    l_xs_e, l_xs_v, l_xs_s = map(lambda l:np.array(l), [l_xs_e, l_xs_v, l_xs_s])
    l_xs_e *= 1e-6
    
    lines = open(path+"_cor").readlines()
    
    iline = 0
    while iline < len(lines):
        if "!" in lines[iline] and lines[iline][0] != "!":
            avt, apr = lines[iline].split("!")
            lines = lines[:iline] + [avt+"\n"]+["!"+apr]+lines[iline+1:]
        if "end" in lines[iline] and lines[iline][0] != "e" and lines[iline][-2]=="d":
            avt, apr = lines[iline].split("end")
            lines = lines[:iline] + [avt+"\n"]+["end"+apr]+lines[iline+1:]
        iline += 1
    
    while "xx" not in lines[0]:
        lines.pop(0)
    lines.pop(0)
    l_cor_e = []
    while "end" not in lines[0]:
        l_cor_e += map(lambda s: float(s)*1e-6, lines.pop(0).split())
    
    cor = np.zeros((len(l_cor_e),len(l_cor_e)))
    for i in range(len(l_cor_e)):
        while "!"+str(i+1) not in lines[0]:
            lines.pop(0)
        lines.pop(0)
        l_val = []
        while "!" not in lines[0] and "end" not in lines[0]:
            l_val += map(lambda s: float(s), lines.pop(0).split())
        cor[i] = np.array(l_val)
        
    if os.path.isfile(path+"_sig"):
        lines = open(path+"_sig").readlines()
        while "lx: "+str(cor.shape[0]) not in lines[0]:
            lines.pop(0)
        lines.pop(0)
        lines.pop(0)
        l_xs_s_rel = []
        while "//" not in lines[0]:
            l_xs_s_rel += [float(lines.pop(0).split()[1])/100.]
        i_s = 0
        for i in range(len(l_xs_v)):
            while i_s<len(l_cor_e)-1 and l_xs_e[i] >= l_cor_e[i_s+1]:
                i_s += 1
            l_xs_s[i] = l_xs_v[i]*l_xs_s_rel[i_s]
    if False:
        l_cor_e = np.array(list(l_cor_e)+[l_xs_e[-1] if l_xs_e[-1]!=l_cor_e[-1] else l_cor_e[-1]*1.01])
    else:
        cor = cor[:-1, :-1]
    return (l_cor_e, cor), (l_xs_e,l_xs_v,l_xs_s)