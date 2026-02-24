import sys
import matplotlib as mpl


mode_serv = False
for param in sys.argv[1:]:
    if param[:len("serv")]=="serv" and param[len("serv")] == "=":
        mode_serv = param[len("serv")+1:] in "1 y Y yes Yes YES"
#if not mode_serv:
#    mpl.use('TkAgg')
#else:
#    mpl.use('Agg')
# if mode_serv:
#     mpl.use('Agg')
# try:
#     import appnope
#     appnope.nope()    # stop the apple power nap
# except ImportError:
#     pass
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal

mpl.rc('text', usetex=True)
#plt.rc('text', usetex=True)
mpl.rc('text.latex',preamble=r"\usepackage{amsmath} \usepackage{graphicx} \usepackage{nicefrac} \usepackage{xcolor}")


import subprocess


#################
def lmap(f,l):
    """
    Apply a function to each element of an iterable and return a list.

    This is a convenience wrapper around the built-in ``map`` function that
    forces evaluation and returns the result as a list.

    Parameters
    ----------
    f : callable
        Function applied to each element of the iterable.
    l : iterable
        Iterable whose elements are passed to the function.

    Returns
    -------
    list
        List containing the results of applying ``f`` to each element of ``l``.
    """
    return list(map(f,l))

def lfilter(f,l):
    return list(filter(f,l))




############################################################################################################
####################################################################################################### vrac

aff_param = {
    "ampli"      :0.8,
    "s_title"    :25,
    "s_xylabel"  :23,
    "s_tick"     :20,
    "s_leg"      :20,
    "alpha_sigma":0.3}




def convtype(itype, s):

    """
    Convert a value to a specified type with special-case handling.

    The function converts the input value to the given type, supporting
    special conventions such as missing values and boolean string parsing.
    If no conversion is required or possible, the original value is returned.

    Parameters
    ----------
    itype : type
        Target type for the conversion.
    s : object
        Value to be converted.

    Returns
    -------
    object
        Converted value according to ``itype``, or ``None`` for missing values.
    """
    if s is None or itype is None:   return s
    if s == "-" :return None
    if itype==bool: return s.lower() in "true yes t y 1".split()
    return itype(s)


def get_aff_size(s):
    if s == "alpha_sigma": return aff_param[s]
    return aff_param["ampli"]*aff_param[s]

def simple(v, n):
    v = float(('%.'+str(n-1)+'e')%v)
    return v if int(v) != v else int(v)

def activity2float(s):
    """
    Convert a radioactive activity string to a floating-point value.

    The function parses a string representing a radioactive activity with
    units and optional SI prefixes, and converts it to a numerical value
    expressed in becquerels.

    Parameters
    ----------
    s : str
        Activity value as a string, including unit and optional SI prefix.

    Returns
    -------
    float
        Activity converted to becquerels.
    """
    if   s[-2:] == "Bq": fact = 1
    elif s[-2:] == "Cu": fact = 37e9
    else:
        print("Error - activity2float -",s)
        exit()
    s = s[:-2]
    if s[-1] not in "0123456789.":
        fact *= {"u":1e-6, "m":1e-3, "k":1e3, "M":1e6, "G":1e9, "T":1e12}[s[-1]]
        s = s[:-1]
    return float(s)*fact


def time2str(v, approx=False, tex=False):
    """
    Convert a time duration to a human-readable string.

    The function expresses a time duration given in seconds using the most
    appropriate unit (seconds, minutes, hours, days, or years). Optional
    approximation and LaTeX formatting can be applied to the output.

    Parameters
    ----------
    v : float
        Time duration in seconds.
    approx : bool or int, optional
        If ``False``, no approximation is applied. If ``True``, values are
        approximated using a default precision. If an integer is provided,
        it specifies the approximation precision.
    tex : bool, optional
        If ``True``, format the output for LaTeX typesetting.

    Returns
    -------
    str
        Human-readable representation of the time duration.
    """
    if approx == True:
        approx = 2
    sep   = "" if not tex else r"~\rm{"
    begin = "" if not tex else ""
    end   = "" if not tex else "}"
    def simplify(v):
        if not approx: return v
        #else: return float(int(v*10))/10
        v = float(('%.'+str(approx-1)+'e')%v)
        return v if int(v) != v else int(v)
        
    if v>3600*24*365: return begin+str(simplify(v/(3600*24*365))) + sep+"y"+end
    if v>3600*24    : return begin+str(simplify(v/(3600*24)))     + sep+"d"+end
    if v>3600       : return begin+str(simplify(v/(3600)))        + sep+"h"+end
    if v>60         : return begin+str(simplify(v/(60)))          + sep+"m"+end
    else            : return begin+str(simplify(v))               + sep+"s"+end
    
def time2strdetail(v):
    """
    Convert a time duration to a detailed human-readable string.

    The function decomposes a time duration given in seconds into years,
    days, hours, minutes, and seconds, and returns a space-separated
    string including all non-zero components.

    Parameters
    ----------
    v : float
        Time duration in seconds.

    Returns
    -------
    str
        Detailed human-readable representation of the time duration.
    """
    r = ""
    if v>3600*24*365:
        r += str(int(v/(3600*24*365))) +"y "
        v -= int(v/(3600*24*365))*3600*24*365
    if v>3600*24:
        r += str(int(v/(3600*24))) +"d "
        v -= int(v/(3600*24))*3600*24
    if v>3600:
        r += str(int(v/(3600))) +"h "
        v -= int(v/(3600))*3600
    if v>60:
        r += str(int(v/(60))) +"m "
        v -= int(v/(60))*60
    if v>0:
        r += str(int(v)) +"s "
    return r
    
def str2time(s):
    """
    Convert a human-readable time string to a duration in seconds.

    The function parses a string consisting of a numerical value followed
    by a single-character time unit and converts it to seconds.

    Parameters
    ----------
    s : str
        Time duration expressed as a string with a unit suffix
        (``y``, ``d``, ``h``, ``m``, or ``s``).

    Returns
    -------
    float
        Time duration converted to seconds.
    """
    v = float(s[:-1])
    if s[-1] == "y": return v*3600*24*365
    if s[-1] == "d": return v*3600*24
    if s[-1] == "h": return v*3600
    if s[-1] == "m": return v*60
    if s[-1] == "s": return v*1
    print("Error - str2time -",s)
    exit()
    
def int_with_zero(i, n, zero="0"):
    """
    Format an integer with leading characters to reach a fixed width.

    The function converts an integer to a string and prepends the specified
    character until the resulting string has a total length of ``n``.

    Parameters
    ----------
    i : int
        Integer value to be formatted.
    n : int
        Desired total length of the output string.
    zero : str, optional
        Character used for left-padding. Default is ``"0"``.

    Returns
    -------
    str
        String representation of the integer padded to length ``n``.
    """
    nro = str(i)
    return zero*(n-len(nro))+nro

def get_c(i,imax, reversed=False, no_dark=False):
    """
    Compute an interpolated color from a predefined color scale.

    The function maps an index within a given range to a color taken from
    a fixed RGB color palette. Linear interpolation is used to ensure a
    smooth color transition across the full index range.

    Parameters
    ----------
    i : int
        Index of the current element.
    imax : int
        Total number of elements defining the color scale range.
    reversed : bool, optional
        If ``True``, reverse the color ordering.
    no_dark : bool, optional
        If ``True``, exclude darker colors from the palette.

    Returns
    -------
    numpy.ndarray
        RGB color array with values normalized to the range [0, 1].
    """
    if reversed :
        i = imax-1-i
    l_c = np.array([(40.,40.,222.), (0.,0.,85.), (40.,205.,205.), (20.,114.,0.), (205.,205.,0.), (255.,75.,0.), (85.,0.,0.), (222.,40.,40.)])
    if no_dark:
        l_c = np.array([(40.,40.,222.), (40.,205.,205.), (20.,114.,0.), (205.,205.,0.), (255.,75.,0.), (222.,40.,40.)])
    l_c /= 255.
    avancement = (i/(imax-1.) *(len(l_c)-1)) if (imax>1) else 0.
    if int(avancement) == avancement:
        return l_c[int(avancement)]
    else:
        return l_c[int(avancement)] + (avancement-int(avancement)) * (l_c[int(avancement)+1]-l_c[int(avancement)])

def dash(i,imax):
    if i==0:
        return (1e9,1e-9)
    return (4,i*4)

def as_nrj(value):
    """
    Format an energy value using appropriate units.

    The function converts an energy value expressed in mega-electronvolts
    into a human-readable string using scaled units (MeV, keV, eV, or meV),
    depending on its magnitude.

    Parameters
    ----------
    value : float
        Energy value expressed in mega-electronvolts.

    Returns
    -------
    str
        Human-readable representation of the energy with appropriate units.
    """
    if value > 1e-0: return ("%0.1f"%value)+" MeV"
    if value > 1e-3: return ("%0.1f"%(value*1e3))+" keV"
    if value > 1e-6: return ("%0.1f"%(value*1e6))+" eV"
    if value > 1e-9: return ("%0.1f"%(value*1e9))+" meV"
    return str(value)

def set_nice_ax(ax, x="", y="", powmodulo=None):
    """
    Configure axis tick formatting for publication-quality plots.

    The function applies custom tick formatters to Matplotlib axes to
    improve readability, supporting scientific notation and energy-unit
    formatting. It can be applied to a single axis or to a list/array of
    axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes or list
        Axis or collection of axes to be formatted.
    x : str, optional
        Formatting mode for the x-axis. Supported values are ``"pow"``
        for scientific notation and ``"MeV"`` for energy-unit formatting.
    y : str, optional
        Formatting mode for the y-axis. Supported values are ``"pow"``
        for scientific notation and ``"MeV"`` for energy-unit formatting.
    powmodulo : tuple of int, optional
        Tuple controlling which powers of ten are displayed when using
        scientific notation. The first element defines the modulo, and
        the second defines the offset.

    Returns
    -------
    None
        The axis object is modified in place.
    """
    if type(ax) == type(np.zeros((1))): ax = list(ax)
    if type(ax) == list:
        map(lambda a: set_nice_ax(a,x=x,y=y), ax)
        return
    def format_func_MeV(value, tick_number):
        if value == 0   : return tex("0")
        if value == 1e-0: return tex("MeV")
        if value == 1e-3: return tex("keV")
        if value == 1e-6: return tex("eV")
        if value == 1e-9: return tex("meV")
        if int(np.log10(value)) == np.log10(value): return ""
        return value
    def format_func_pow(value, tick_number):
        nb1, nb2 = ('%e' % Decimal(value)).split("e")
        if float(nb1)==1 and powmodulo is not None:
            if ((int(nb2)-powmodulo[1]) % powmodulo[0]) != 0: return ""
        if "+0"in nb2: nb2 = nb2.replace("+0","+")
        if "-0"in nb2: nb2 = nb2.replace("-0","-")
        nb2 = nb2.replace("+","")
        while nb1[-1]=="0": nb1 = nb1[:-1]
        if nb1[-1]=="."   : nb1 = nb1[:-1]
        if nb1 == "1"     : nb1=""
        if nb1 == "-1."   : nb1="-"
        if nb1 == "0": return tex("0")
        if len(nb1)>4: return ""
        if len(nb1)>0: return tex(nb1+r"\,{\scriptscriptstyle\times}10^{"+nb2+"}")
        return tex("10^{"+nb2+"}")
    if x=="pow"  : ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func_pow))
    if y=="pow"  : ax.yaxis.set_major_formatter(plt.FuncFormatter(format_func_pow))
    if x=="MeV"  :
        ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func_MeV))
        ax.set_xticks([10.**int(i) for i in np.arange(-10,2)])
    if y=="MeV"  :
        ax.yaxis.set_major_formatter(plt.FuncFormatter(format_func_MeV))
        ax.set_yticks([10**int(i) for i in np.arange(-10,2)])
    if x not in ["pow","MeV"] and y not in ["pow","MeV"]:
        print("ERROR - set_nice_ax", x,y,"not in",["pow","MeV"])
        exit()

def tex(s):
    """
    Format a string for LaTeX math rendering using roman font.

    The function wraps the input string in a LaTeX ``\\mathrm{}`` math
    expression, replacing spaces with non-breaking spaces. If the string
    is already formatted as a ``\\mathrm`` expression, it is returned
    unchanged.

    Parameters
    ----------
    s : object
        Input value to be converted to a LaTeX-formatted string.

    Returns
    -------
    str
        LaTeX-formatted string suitable for use in Matplotlib or TeX output.
    """
    if r"$\mathrm{" in s: return s
    return r"$\mathrm{"+str(s).replace(r" ",r"~")+r"}$"

def sec_2_str(s):
    """
    Convert a time duration in seconds to a compact human-readable string.

    The function expresses a time duration given in seconds using the most
    appropriate unit (seconds, minutes, hours, days, or years) and formats
    the value with fixed decimal precision.

    Parameters
    ----------
    s : float
        Time duration in seconds.

    Returns
    -------
    str
        Human-readable representation of the time duration.
    """
    if s<60:           return str("%.3f"%s)           +" s"
    if s<60*60:        return str("%.3f"%(s/60))      +" m"
    if s<60*60*24:     return str("%.3f"%(s/60/60))   +" h"
    if s<60*60*24*365: return str("%.3f"%(s/60/60/24))+" d"
    return str(s/60/60/24/365)+" y"

def print_vec(vec, s=15):
    return " ".join(map(lambda v:str(v)+" " + " "*(s-len(str(v)+" ")),vec))


def dup(l):
    """
    Duplicate each element of an iterable.

    The function creates a new array in which each element of the input
    iterable appears twice in the same order.

    Parameters
    ----------
    l : iterable
        Input iterable whose elements are to be duplicated.

    Returns
    -------
    numpy.ndarray
        Array containing duplicated elements.
    """
    r = []
    for v in l:
        r += [v,v]
    return np.array(r)

def dup_piquet(l):
    """
    Duplicate elements of an iterable with trimmed endpoints.

    The function duplicates each element of the input iterable and returns
    the resulting list with the first and last elements removed. This
    operation is useful for constructing stepwise or piecewise-constant
    sequences.

    Parameters
    ----------
    l : iterable
        Input iterable whose elements are to be duplicated.

    Returns
    -------
    list
        List containing duplicated elements with endpoints removed.
    """
    l = list(l)
    r = []
    for v in l:
        r += [v,v]
    return r[1:-1]

def dupx(l, pos="left", log=False):
    """
    Generate a duplicated coordinate array with optional extrapolation.

    The function extends a sequence by extrapolating values at one or both
    ends, duplicates each element, and trims the resulting array. This is
    typically used for constructing stepwise coordinates for plotting,
    optionally in logarithmic space.

    Parameters
    ----------
    l : iterable
        Input sequence of numerical values.
    pos : str, optional
        Position where extrapolation is applied. Supported values are
        ``"left"``, ``"right"``, or ``"middle"`` (including common aliases).
    log : bool, optional
        If ``True``, perform the operation in logarithmic (base-10) space.

    Returns
    -------
    numpy.ndarray
        Array of duplicated and extrapolated values.
    """
    if len(l)==1:
        return l+[l[0]+1]
    if log:    l = np.log10(np.array(l))
    l = list(l)
    if pos in ["left","gauche","l","g"]:
        l = l + [2*l[-1] - l[-2]]
    if pos in ["right","droite","r","d"]:
        l = [2*l[0] - l[1]] + l
    if pos in ["middle","milieu","mid","m"]:
        l = np.array(l)
        l = list(0.5*(l[1:]+l[:-1]))
        l = [2*l[0] - l[1]] + l + [2*l[-1] - l[-2]]
    r = []
    for v in l:
        r += [v,v]
    if log:    r = 10**np.array(r)
    return np.array(r)[1:-1]


def formule2val(text):
    """
    Evaluate a mathematical expression and return its numerical value.

    The function executes a Python expression provided as a string in a
    separate Python process and converts the resulting output to a
    floating-point value. This allows evaluation of simple mathematical
    formulas defined as text.

    Parameters
    ----------
    text : str
        String representing a valid Python expression that evaluates to
        a numerical value.

    Returns
    -------
    float
        Numerical result of the evaluated expression.
    """
    import traceback
    s = "python3 -c print("+text+")"
    try:
        r = float(subprocess.Popen(s.split(), stdout=subprocess.PIPE).communicate()[0])
    except Exception:
        print("#"*50)
        print("ERROR - formule2val - "+s)
        print("here is the traceback:")
        print(traceback.print_exc())
        exit()
    return r





def gen_dose_rate_fct_old(l_irradiation,time_zero,pos="BertholdCR_arret",log=False):
    print("#"*100+"coucou")
    if pos=="BertholdCR_arret":
        fact = 1.
    elif pos=="BertholdCR_attente":
        fact = 0.240
    elif pos=="lid_attente":
        fact = 0.006
    else:
        print("ERROR - gen_dose_rate_fct - pos",pos,"not in <BertholdCR_arret, BertholdCR_attente, lid_attente>")
        exit()
    def fct(x):
        #param = [1.8367498386316123e-05,0.00012299307547309054,6.392976909445525e-07,1.4060412106102535e-05]
        #param = [0.0018012578836661428,0.002325086566619239,0.0003129105608273616,0.0005380502325996562,7.993956229841799e-05,0.00014659109761208918,7.657444960992908e-06,2.461705194449664e-05,1.524776800760012e-07,2.4614905404731693e-05,1.3769839492151543e-07,2.461689673676992e-05,1.521005552669318e-08,2.463475145343631e-05]
        param = [2.476048978190557e-07,1.7395601198834934e-06,2.4067507006424388e-06,1.8354024341238288e-05,1.4010846694047595e-05,6.094018286948987e-05,9.038082539756923e-05,0.0001854683290889316,0.0003690046091058582,0.0006530714381857627,0.002239347947673143,0.0028626126487732812]

        x = np.array(x)
        v = x*0
        for (puiss, duree, begin_of_irradiation) in l_irradiation:        # loop on the irradiations
            t0b = (begin_of_irradiation-time_zero).total_seconds()
            t1b = t0b + duree
            #print("         ",t0b, t1b)
            for iparam in range(int(len(param)/2)):                        # loop on the fit order
                ai,li = param[2*iparam], param[2*iparam+1]
                for i in range(len(x)):                                    # 1J decay rate = sum_i a_i*exp(-l_i*t),
                    t1b_loc = max(min(t1b,x[i]),t0b)                    # so the convolution from t0 to t1 is:
                    if x[i]>t0b:
                        v[i] += puiss*ai/li * (np.exp(-li*(x[i]-t1b_loc)) - np.exp(-li*(x[i]-t0b)))
        v *= fact
        return v if not log else np.log(v)
    return fct




    
    
