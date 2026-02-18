###########################################################################################################
############################################################################################ get param input
from .utils_general import *
import numpy as np
def_forbiden = "hfispdg"
def _get_param(nom, defaut=def_forbiden):
    """
    Retrieve a command-line parameter value.

    The function searches the command-line arguments for a parameter of the
    form ``<nom>=<value>`` and returns the associated value. If the parameter
    is not found, a default value may be returned if provided; otherwise,
    execution is stopped with an error message.

    Parameters
    ----------
    nom : str
        Name of the command-line parameter to retrieve.
    defaut : object, optional
        Default value returned if the parameter is not found.
        If set to ``def_forbiden``, the parameter is considered mandatory.

    Returns
    -------
    str or object
        Value associated with the specified parameter, or the default value
        if provided.
    """
    for param in sys.argv[1:]:
            if param[:len(nom)]==nom and param[len(nom)] == "=":
                    return param[len(nom)+1:]
    if defaut != def_forbiden:
            return defaut
    print("ERROR - please, provide parameter: "+nom)
    exit()

def _aff_input_param(nom, r):
    if type(r) == list:
        r = " ".join(map(lambda v:str(v), r))
    print("# "+nom+" "*(10-len(nom))+" "+str(r))
    

def get_param_vari(nom, itype, defaut=def_forbiden, aff=True):
    """
    Retrieve and convert a command-line parameter value.

    This function obtains a command-line parameter of the
    form ``<nom>=<value>`` converts the retrieved value to
    the specified type, and optionally displays the
    parameter and its value.

    Parameters
    ----------
    nom : str
        Name of the command-line parameter to retrieve.
    itype : type
        Target type used to convert the parameter value.
    defaut : object, optional
        Default value returned if the parameter is not provided.
        If set to ``def_forbiden``, the parameter is considered mandatory.
    aff : bool, optional
        If ``True``, display the parameter name and value after retrieval.

    Returns
    -------
    object
        Parameter value converted to the specified type.
    """
    r = convtype(itype, _get_param(nom, defaut))
    if aff:
        _aff_input_param(nom, r)
    return r


def get_param_list(nom, itype, defaut=def_forbiden, sep="/"):
    """
    Retrieve and convert a list-valued command-line parameter.

    The function reads a command-line parameter of the form
    ``<nom>=<v1><sep><v2><sep>...`` and converts each element to the specified
    type. The resulting list is optionally empty if no value is provided.

    Parameters
    ----------
    nom : str
        Name of the command-line parameter to retrieve.
    itype : type
        Target type used to convert each element of the list.
    defaut : object, optional
        Default value returned if the parameter is not provided.
        If set to ``def_forbiden``, the parameter is considered mandatory.
    sep : str, optional
        Separator used to split the parameter value into elements.

    Returns
    -------
    list or object
        List of values converted to ``itype``, or the default value if provided.
    """
    r = _get_param(nom, defaut)
    if r is not None:
        if r=="": r=[]
        elif type(r)==type("hello"): r = map(lambda v:convtype(itype, v), r.split(sep))
    _aff_input_param(nom, r)
    return r

def get_param_str(nom, defaut=def_forbiden):
    r = _get_param(nom, defaut=defaut)
    _aff_input_param(nom, r)
    return r
def get_param_int(nom, defaut=def_forbiden):
    r = int(_get_param(nom, defaut=defaut))
    _aff_input_param(nom, r)
    return r
def get_param_float(nom, defaut=def_forbiden):
    r = float(_get_param(nom, defaut=defaut))
    _aff_input_param(nom, r)
    return r
def get_param_bool(nom, defaut=def_forbiden):
    r = _get_param(nom, defaut=defaut).lower() in "true yes t y 1".split()
    _aff_input_param(nom, r)
    return r
def get_param_l_str(nom, defaut=def_forbiden, sep="/"):
    r = _get_param(nom, defaut).split(sep)
    _aff_input_param(nom, r)
    return r
def get_param_l_int(nom, defaut=def_forbiden, sep="/"):
    r = map(lambda v:int(v), _get_param(nom, defaut).split(sep))
    _aff_input_param(nom, r)
    return r
def get_param_l_float(nom, defaut=def_forbiden, sep="/"):
    r = _get_param(nom, defaut)
    if r is not None:
        r = map(lambda v:float(v), r.split(sep))
    _aff_input_param(nom, r)
    return r