# from ..Common.utils_general import *
from ..Stats.Stats import *

def aff(v, l=10, rev=False):
    """
    Format a value as a fixed-width string.

    The function converts the input value to a string and pads it with spaces
    to obtain a fixed length. Integer values are converted directly, while
    floating-point values are formatted in scientific notation with fixed
    precision.

    Parameters
    ----------
    v : object
        Value to be formatted. Supported types include integers, floats,
        NumPy floats, and strings.
    l : int, optional
        Desired length of the output string.
    rev : bool, optional
        Alignment flag. Currently kept for compatibility but not used;
        output is always left-justified.

    Returns
    -------
    str
        Fixed-width string representation of the input value.
    """
    #v = str(v)+" "
    #return v+" "*(l-len(v)) if not rev else " "*(l-len(v))+v
    if type(v) == int           : v = str(v)
    if type(v) == float         : v = "%.4e"%v
    if type(v) == np.float64 : v = "%.4e"%v
    v = str(v)
    return v.ljust(l)

def aff_s_v(s, v, l1=25, l2=15):
    """
    Format a label-value pair as a fixed-width string.

    The function formats a string label and an associated value using
    fixed-width alignment and concatenates them. It is typically used
    for producing aligned textual output or tables.

    Parameters
    ----------
    s : object
        Label or descriptor to be formatted.
    v : object
        Value associated with the label.
    l1 : int, optional
        Field width for the label.
    l2 : int, optional
        Field width for the value.

    Returns
    -------
    str
        Concatenated fixed-width string containing the formatted label
        and value.
    """
    return aff(s,l=l1)+aff(v,l=l2)
    
def aff_s_v_vs(s, v, vs, l1=25, l2=15):
    """
    Format a label, value, and uncertainty as a fixed-width string.

    The function formats a label, a numerical value, and its associated
    uncertainty, and appends the relative uncertainty expressed as a
    percentage. The output is intended for aligned textual reports or
    tables.

    Parameters
    ----------
    s : object
        Label or descriptor to be formatted.
    v : object
        Central value.
    vs : object
        Uncertainty associated with ``v``.
    l1 : int, optional
        Field width for the label.
    l2 : int, optional
        Field width for the value and uncertainty fields.

    Returns
    -------
    str
        Fixed-width formatted string containing the label, value,
        uncertainty, and relative uncertainty in percent.
    """
    return aff(s,l=l1)+aff(v,l=l2)+"+- "+aff(vs,l=l2)+' ('+aff(vs/v*100)+"%)"

def mk_dir(l_path):
    if type(l_path) == str : l_path = l_path.split("/")
    pos = ""
    while len(l_path)>0:
        if not os.path.isdir(pos+l_path[0]):
            os.mkdir(pos+l_path[0])
        pos += l_path.pop(0)+"/"

txt_csv = ""

def export_csv(path):
    global txt_csv
    open(path,"w").write(txt_csv)

def aff_list(s, l_v, l1=25, l2=18):
    """
    Format a label and a list of values as a fixed-width string and log to CSV text.

    The function appends a semicolon-separated representation of the label and
    values to a global CSV text buffer, and returns a formatted fixed-width
    string suitable for aligned textual output.

    Parameters
    ----------
    s : object
        Label or descriptor associated with the list of values.
    l_v : iterable
        Iterable of values to be formatted and logged.
    l1 : int, optional
        Field width for the label.
    l2 : int, optional
        Field width for each value in the list.

    Returns
    -------
    str
        Fixed-width formatted string containing the label followed by the
        formatted list of values.
    """
    global txt_csv
    txt_csv += s+";"+";".join(map(lambda v: str(v), list(l_v)))+"\n"
    return aff(s,l=l1)+''.join(map(lambda v: aff(v,l=l2), list(l_v)))

def aff_t(l_v, l=18):
    """
    Format a sequence of values as a fixed-width concatenated string.

    The function applies fixed-width formatting to each element of the
    input sequence and concatenates the results into a single string.
    It is typically used for aligned tabular text output.

    Parameters
    ----------
    l_v : iterable
        Iterable of values to be formatted.
    l : int, optional
        Field width applied to each value.

    Returns
    -------
    str
        Concatenated fixed-width string representation of the input values.
    """
    return ''.join(map(lambda v: aff(v,l=l), list(l_v)))
    
def aff_mat(s, ll_v, l1=25, l2=18, size_max=None):
    """
    Format a 2D list (matrix) as aligned fixed-width text.

    The function formats a matrix-like structure into a multi-line string
    suitable for aligned textual display. Each row is formatted using
    fixed-width fields, optionally truncating the number of displayed
    rows and columns.

    Parameters
    ----------
    s : object
        Label associated with the first row of the matrix.
    ll_v : iterable of iterable
        2D iterable representing the matrix to be formatted.
    l1 : int, optional
        Field width for the row label.
    l2 : int, optional
        Field width for each matrix element.
    size_max : int, optional
        Maximum number of rows and columns to display. If ``None``, the
        full matrix is displayed.

    Returns
    -------
    str
        Multi-line fixed-width string representation of the matrix.
    """
    if size_max is None: size_max = len(ll_v)
    not_full = size_max<len(ll_v)
    s = aff_list(s, ll_v[0][:size_max], l1=l1, l2=l2)+("..." if not_full else "")+"\n"
    for l_v in ll_v[1:size_max]:
        #s += aff_list("", l_v[1:size_max], l1=l1, l2=l2)+"\n"
        s += aff_list("", l_v[:size_max], l1=l1, l2=l2)+"\n"
    return s[:-1]

size_max_aff_mat = int(1e5)

def aff_decription_s_v_cov(s, v_cov, size_max=size_max_aff_mat):
    """
    Display and log a vector with its covariance-derived uncertainties
    and correlations.

    The function prints a formatted summary of a vector and its associated
    covariance matrix, including absolute uncertainties, relative
    uncertainties in percent, and (if non-diagonal) the correlation matrix.
    Selected information is also appended to a global CSV text buffer.

    Parameters
    ----------
    s : str
        Description or label associated with the vector and covariance data.
    v_cov : tuple
        Tuple ``(v, cov)`` where ``v`` is a vector of values and ``cov`` is
        the corresponding covariance matrix.
    size_max : int, optional
        Maximum size used when displaying the correlation matrix. Larger
        matrices are truncated for readability.

    Returns
    -------
    None
        Information is printed to standard output and logged to the global
        CSV buffer.
    """
    global txt_csv
    v,cov = v_cov
    print("#"*25)
    print("#",s)
    txt_csv += s+"\n"
    print(aff_list("vec",        v                ))
    print(aff_list("sig",        cov_to_sig_cor(cov)[0]        ))
    print(aff_list("sig rel [%]",     cov_to_sig_cor(cov)[0]/v*100    ))
    cor = cov_to_sig_cor(cov)[1]
    if np.max(np.abs(cor-np.diag(np.diag(cor))))>1e-15:
        #print aff_mat("cov",         cov,            )
        print(aff_mat("cor [%]",     cor*100        , size_max=size_max))

def aff_decription_s_v_cov_as_C_over_E(s, v_cov, size_max=size_max_aff_mat):
    """
    Display and log C/E-style residuals with covariance information.

    The function prints a formatted summary of a vector interpreted as
    C/E (calculated over experimental) values together with its covariance
    matrix. It reports deviations from unity in percent, absolute
    uncertainties in percent, normalized residuals, and (if non-diagonal)
    the correlation matrix. Selected information is also appended to a
    global CSV text buffer.

    Parameters
    ----------
    s : str
        Description or label associated with the C/E data.
    v_cov : tuple
        Tuple ``(v, cov)`` where ``v`` is the vector of C/E values and
        ``cov`` is the corresponding covariance matrix.
    size_max : int, optional
        Maximum size used when displaying the correlation matrix. Larger
        matrices are truncated for readability.

    Returns
    -------
    None
        Information is printed to standard output and logged to the global
        CSV buffer.
    """
    global txt_csv
    v,cov = v_cov
    print("#"*25)
    print("#",s)
    txt_csv += s+"\n"
    print(aff_list("vec [%]",    (v-1)*100            ))
    #print aff_list("sig ",        cov_to_sig_cor(cov)[0]        )
    print(aff_list("sig [%]",    cov_to_sig_cor(cov)[0]*100    ))
    print(aff_list("residual",    (v-1)/cov_to_sig_cor(cov)[0]    ))
    cor = cov_to_sig_cor(cov)[1]
    if np.max(np.abs(cor-np.diag(np.diag(cor))))>1e-15:
        #print aff_mat("cov",         cov             )
        print(aff_mat("cor [%]",     cor*100 ,size_max=size_max))


def get_key_for_GRAPE_RR(input_path_name):
    """
    Generate a unique hash key for a GRAPE path.

    The function computes an MD5 hash from the given input path name.
    The resulting key can be used as a compact, deterministic identifier
    for caching or indexing GRAPE related data.

    Parameters
    ----------
    input_path_name : str
        Input path or name used to generate the hash key.

    Returns
    -------
    str
        MD5 hexadecimal hash string derived from the input path name.
    """
    return hashlib.md5(bytes(input_path_name, 'utf-8')).hexdigest()

def get_key_for_BLOOM_Sim(input_path_name):
    """
    Generate a unique hash key for a BLOOM path.

    The function computes an MD5 hash from the given input path name.
    The resulting key can be used as a compact, deterministic identifier
    for caching or indexing GRAPE BLOOM related data.

    Parameters
    ----------
    input_path_name : str
        Input path or name used to generate the hash key.

    Returns
    -------
    str
        MD5 hexadecimal hash string derived from the input path name.
    """
    return hashlib.md5(bytes("BLOOM"+input_path_name, 'utf-8')).hexdigest()

def get_key_for_SAFFRON_signal(input_path_name,dwell_time):
    """
    Generate a unique hash key for a SAFFRON path.

    The function computes an MD5 hash from the given input path name.
    The resulting key can be used as a compact, deterministic identifier
    for caching or indexing SAFFRON-related data.

    Parameters
    ----------
    input_path_name : str
        Input path or name used to generate the hash key.

    Returns
    -------
    str
        MD5 hexadecimal hash string derived from the input path name.
    """
    return hashlib.md5(bytes("SAFFRON"+input_path_name+str(dwell_time), 'utf-8')).hexdigest()
    

import json
def save_dict_to_file(d: dict, filename: str) -> None:
    """
    Save a dictionary to a JSON file.

    The function serializes the given dictionary into JSON format and writes
    it to the specified file. Keys are sorted and the output is indented to
    improve readability.

    Parameters
    ----------
    d : dict
        Dictionary to be saved.
    filename : str
        Path to the output JSON file.

    Returns
    -------
    None
        The dictionary is written to disk.
    """
    with open(filename, 'w') as f:
        json.dump(d, f, sort_keys=True, indent=4)

def load_dict_from_file(filename: str) -> dict:
    """
    Load a dictionary from a JSON file.

    The function reads a JSON-formatted file from disk and deserializes its
    contents into a Python dictionary.

    Parameters
    ----------
    filename : str
        Path to the JSON file to be read.

    Returns
    -------
    dict
        Dictionary loaded from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)