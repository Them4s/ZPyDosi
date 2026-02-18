# All CSV related Class and function
from ..Common.ExcelSheet import *
from ..Common.utils_general import *
import numpy as np

class CsvSeeker: 
    '''
    Class to store and read .CSV data
    '''
    # def get(self, case, key, data_type=None):
    # def get_list(self, case, sec,key, data_type=None, optional=True, deep=False, nb_version=0):
    # def get_in_list(self, case, sec, name, key_name, data, data_type=None, deep=False, nb_version=0, nb_version_key=0):
    # def get_line_starting_with(self, start):
    
    def __init__(self, path_csv_data):
        '''
        Docstring for __init__
        
        :param self: CsvSeeker object
        :param path_csv_data: path to the csv file
        '''
        self.path_csv_data = path_csv_data
        
    def get(self, case, key, data_type=None, default="forbiden_key", all_line=False):
        '''
        Load a single line or element table from CSV

        :param self: CsvSeeker object
        :param case: Identifier of the group constaining the table to be loaded in the csv
        :param key: Identifier of the table to be loaded with the "case" group
        :param data_type: Optinal, data_type for formatting
        :param default: Optinal, Default output if key not found.
        :param all_line: if False only load the first element after "key" in the line, else load all elements
        
        :return: data_type value or array
        '''
        #if ".xlsx" in path_csv:
        #    xlsx_2_csv_lines(path_csv)
        #    exit()
    
        #lines = list(map(lambda l:l.replace(",",";").replace("\n",""), open(self.path_csv_data).readlines()))
        lines = get_csv_lines(self.path_csv_data)
        while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != case:
            lines.pop(0)
        if len(lines)==0:
            self._err("get_csv - case "+case+" not found")
        while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != key:
            lines.pop(0)
        if len(lines)==0:
            if default != "forbiden_key":
                return default
            self._err("get_csv - key "+key+" not found")
        if not all_line:
            return convtype(data_type, lines[0].replace(",",";").split(";")[1])
        else:
            return np.array(lmap(lambda v: convtype(data_type, v), lines[0].replace(",",";").split(";")))
            
    def get_list(self, case, sec,key, data_type=None, optional=True, deep=False, nb_version=0): # , void_value="dontusethis"
        '''
        Load a column from a table within a CSV
        
        :param self: CsvSeeker object
        :param case: Identifier of the group constaining the table to be loaded in the csv
        :param sec: Identifier of the table to be loaded with the "case" group
        :param key: Identifier of the column to be loaded with the "sec" table
        :param data_type: Optional, data_type for formatting
        :param optional: if true return None if "key" note found
        :param deep: force to read the csv file until the last line, overiding the table end detection 
        :param nb_version: addtional inidcator in the case the "sec" table having multiple columns named "key"

        :return: data_type value or array
        '''
        lines = get_csv_lines(self.path_csv_data)
        while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != case:
            lines.pop(0)
        if len(lines)==0:
            self._err("data_get_csv_list - case - "+str(case)+" not found")
        while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != sec:
            lines.pop(0)
        if len(lines)==0:
            self._err("data_get_csv_list - sec - "+str(sec)+" not found")
        if key not in lines[0]:
            if optional: return None
            else:        self._err("data_get_csv_list - key <"+str(key)+"> not in available list ["+ ",".join(lines[0])+"]")
        l_key = lines[0].replace("\n","").replace(",",";").split(";")
        pos = l_key.index(key)
        while nb_version>0:
            if key not in l_key[pos+1:]:
                if optional: return None
                else:        self._err("data_get_csv_list - key <"+str(key)+"> version <"+str(nb_version)+"> not in available list ["+ ",".join(lines[0])+"]")
            pos = pos+1 + l_key[pos+1:].index(key)
            nb_version  -= 1
        lines.pop(0)
        l_data = []
        def not_finish(l):
            t1 = len(l.replace(",",";").split(";")[0])==0
            t2 = len(l.replace(",",";").split(";"))>1
            #t3 = len(l.replace(",",";").split(";")[pos])>0 or void_value != "dontusethis"            # old: 1 - new: pos
            t3 = len(l.replace(",",";").split(";")[1])>0
            return t1 and t2 and t3
        while len(lines)>0 and (not_finish(lines[0]) or deep):
            v = lines[0].replace("\n","").replace(",",";").split(";")[pos]
            #if len(v)==0 : v=void_value
            while len(v)>0 and v[-1]==" ": v=v[:-1]
            l_data += [v]
            lines.pop(0)
        #if key=="order":
        #    print(l_data)
        #    print(lines[0], not_finish(lines[0]) )
        #    exit()
        return np.array(list(map(lambda v: convtype(data_type, v), l_data)))
    
    def get_in_list(self, case, sec, name, key_name, data, data_type=None, deep=False, nb_version=0, nb_version_key=0):
        '''
        load a single value witin a table in a csv file
        
        :param self: CsvSeeker object
        :param case: Identifier of the group constaining the table to be loaded in the csv
        :param sec: Identifier of the table to be loaded with the "case" group
        :param name: Identifier of the column listing the names of each line of the table the table "sec" table
        :param key_name: Identifier of the the line containing the value to be loaded within the "name" column
        :param data: Identifier of the column containing the value to be loaded within the "sec" table
        :param data_type: Optional, data_type for formatting
        :param deep: force to read the csv file until the last line, overiding the table end detection 
        :param nb_version: addtional inidcator in the case of the "sec" table having multiple columns named "data"
        :param nb_version_key: addtional inidcator in the case of the sec" having multiple line named "key_name"

        :return:  data_type
        '''
        l_name = list(self.get_list(case, sec,name, deep=deep))
        l_data = list(self.get_list(case, sec,data, data_type, deep=deep, nb_version=nb_version))
        
        #print(list(self.get_list(case, sec,name, deep=deep)))
        #print(list(self.get_list(case, sec,data, data_type, deep=deep, nb_version=nb_version)))
        #print(list(self.get_list("generic", "source_description","period")))
        #exit()
        if key_name not in l_name:
            sp=key_name.split("-")
            if "-".join([sp[i][:3] if i==1 else sp[i] for i in range(len(sp))]) in l_name:
                key_name="-".join([sp[i][:3] if i==1 else sp[i] for i in range(len(sp))])
        if key_name not in l_name:
            for iname in range(len(l_name)):
                if "*" in l_name[iname]:
                    if key_name.startswith(l_name[iname].replace("*","")):
                        l_name[iname] = key_name
        if key_name not in l_name:
            self._err("data_get_csv_in_list - ask for <"+key_name+"> not in ["+",".join(l_name)+"]")
        
        id_col = l_name.index(key_name)
        while nb_version_key>0:
            if key_name not in l_name[id_col+1:]:
                self._err("get_in_list - ask for <"+key_name+"> version <"+str(nb_version_key)+"> not in ["+",".join(l_name)+"]")
            id_col = l_name[id_col+1:].index(key_name)
            nb_version_key  -= 1
        return l_data[id_col]
    
    def get_line_starting_with(self, start, default="forbiden_key"):
        '''
        return all cells of a line within csv file
        
        :param self: CsvSeeker object
        :param start: Identifier of the the line containing the value to be loaded within the csv file
        :param default: Optinal, Default output if key not found.
        
        :retrun: list of string
        '''
        
        #if ".xlsx" in path_csv:
        #        xlsx_2_csv_lines(path_csv)
        #        exit()
        
    
        #lines = lmap(lambda l:l.replace(",",";"), open(self.path_csv_data).readlines())
        lines = get_csv_lines(self.path_csv_data)
        
        while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != start:
            lines.pop(0)
        if len(lines) == 0:
            if default != "forbiden_key":
                return default
            else:
                self._err("get_line_starting_with - "+start)
        return lines[0].replace(",",";").split(";")
    
    def _err(self, txt):
        print("ERROR - CsvSeeker - "+txt)
        exit()


_dict_path_csv_2_lines = {}

def get_csv_lines(path):
    '''
    Return a list of all lines within a .csv or .xlsx file.
    The cells are separated by ";"
    
    :param path: path of the file
    :return: list of string
    '''
    global _dict_path_csv_2_lines
    #print("coucou", path)
    if path in _dict_path_csv_2_lines:
        return _dict_path_csv_2_lines[path]+[]
    if ".csv" in path:
        lines = lmap(lambda l:l.replace(",",";"), open(path).readlines())
    elif ".xlsx" in path:
        #wb = xlrd.open_workbook(path)
        #sheet = wb.sheet_by_index(0)
        input = ExcelSheet(path)
        i = 1
        lines =[]
        def xlsx_cell_2_str(v):
            if v is None:
                return ""
            if type(v) == float and int(v) == v:
                v = int(v)
            return str(v)
        #for i in range(sheet.nrows):
        for i in range(input.get_nb_row()):
            #lines += [";".join(lmap(lambda j:xlsx_cell_2_str(sheet.cell_value(i, j)), range(sheet.ncols)))+"\n"]
            lines += [";".join(lmap(lambda j:xlsx_cell_2_str(input.get(i, j)), range(input.get_nb_col())))+"\n"]
            #if "Co57" in lines[-1]:
            #if i<120:
            #    print(lines[-1])
    else:
        print("ERROR - unregognized format -",path)
        exit()
    _dict_path_csv_2_lines[path] = lines+[]
    return lines
    
def get_csv(path_csv, key, case, data_type=None):
    '''
    get a value within a csv
    
    :param path_csv: Path to the csv
    :param key: Identifier of the line line containing the data within the "case" table
    :param case: Identifier of the subtable within the file 
    :param data_type: type of data for formatting
    
    :return: single element of the file
    '''
    #if ".xlsx" in path_csv:
    #    xlsx_2_csv_lines(path_csv)
    #    exit()
    #lines = map(lambda l:l.replace(",",";"), open(path_csv).readlines())
    lines = get_csv_lines(path_csv)
    while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != case: lines.pop(0)
    if len(lines)==0:
        print("ERROR 404 - get_csv - case", case,"not found")
        exit()
    while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != key: lines.pop(0)
    if len(lines)==0:
        print("ERROR 404 - get_csv - key", key,"not found")
        exit()
    return convtype(data_type, lines[0].replace(",",";").split(";")[1])

def get_csv_dosi_data(path_csv, name, key):
    """
    Extract a numerical value associated with a given name and key from a CSV file.

    The function reads a CSV file, locates the header row containing the column
    names, determines the position of the requested key, and then searches for
    the row corresponding to the specified name. The value at the intersection
    of the name row and key column is returned as a float.

    Parameters
    ----------
    path_csv : str
        Path to the CSV file containing the data.
    name : str
        Identifier used to select the desired row in the CSV file.
    key : str
        Column name whose value should be extracted.

    Returns
    -------
    float
        The value associated with the specified name and key.
    """
    #if ".xlsx" in path_csv:
    #    xlsx_2_csv_lines(path_csv)
    #    exit()
    #lines = map(lambda l:l.replace(",",";"), open(path_csv).readlines())
    lines = get_csv_lines(path_csv)
    while "name" != lines[0].replace(",",";").split(";")[0]:
        lines.pop(0)
    pos_key = lines[0].replace("\n","").replace(",",";").split(";").index(key)
    
    while len(lines)>0 and name != lines[0].replace(",",";").split(";")[0]:
        lines.pop(0)
    if len(lines)==0:
        print("Error - get_csv_dosi_data -",path_csv,"-", name,"-", key)
        1/0
        exit()
    return float(lines[0].replace("\n","").replace(",",";").split(";")[pos_key])

def get_csv_list(path_csv, key1,key2, case, data_type=None, optional=True):
    """
    Extract a list of values from a CSV file for a given case and keys.

    The function scans a CSV file to locate a section identified by a case name,
    then finds a header row corresponding to ``key1`` and extracts all subsequent
    values associated with ``key2``. The extracted values are optionally cast to
    a specified data type and returned as a NumPy array.

    Parameters
    ----------
    path_csv : str
        Path to the CSV file containing the data.
    key1 : str
        Primary key identifying the header row to search for.
    key2 : str
        Secondary key identifying the column whose values should be extracted.
    case : str
        Case identifier used to locate the relevant data block in the CSV file.
    data_type : type, optional
        Target type used to convert the extracted values.
        If ``None``, no explicit type conversion is applied.
    optional : bool, optional
        If ``True``, return ``None`` when ``key2`` is not found instead of stopping
        execution.

    Returns
    -------
    numpy.ndarray or None
        Array containing the extracted values converted to ``data_type``.
        Returns ``None`` if the key is optional and not found.
    """
    #if ".xlsx" in path_csv:
    #    xlsx_2_csv_lines(path_csv)
    #    exit()
    #
    #lines = map(lambda l:l.replace(",",";"), open(path_csv).readlines())
    lines = get_csv_lines(path_csv)
    
    while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != case: lines.pop(0)
    if len(lines)==0:
        print("ERROR 404 - get_csv_list - case", case,"not found")
        exit()
    while len(lines)>0 and lines[0].replace(",",";").split(";")[0] != key1: lines.pop(0)
    if len(lines)==0:
        print("ERROR 404 - get_csv_list - key", key2,"not found")
        exit()
    #print lines[0].replace("\n","").replace(",",";").split(";")
    if key2 not in lines[0] and optional:
        return None
    pos = lines[0].replace("\n","").replace(",",";").split(";").index(key2)
    lines.pop(0)
    l_data = []
    while len(lines[0].replace(",",";").split(";")[0])==0 and len(lines[0].replace(",",";").split(";"))>1 and len(lines[0].replace(",",";").split(";")[1])>0:
        l_data += [lines[0].replace("\n","").replace(",",";").split(";")[pos]]
        lines.pop(0)
    return np.array(lmap(lambda v: convtype(data_type, v), l_data))