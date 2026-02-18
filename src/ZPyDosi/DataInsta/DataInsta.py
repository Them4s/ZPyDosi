from ..Common.utils_general import *
from ..Common.CsvSeeker import *
from ..Prints.PrintnSave import *
import numpy as np
class DataInsta:
    """
    Container for instrumentation and geometry data loaded from CSV files.

    This class reads structured CSV input describing bar geometries,
    hole positions, and HPGe detector configurations. The parsed data are
    stored as attributes for later use in geometry handling, simulations,
    or analysis workflows.
    """
    def __init__(self, path_csv_data, case_csv):
        """
        Load instrumentation data from a CSV configuration.

        The initializer parses a CSV file using a given case identifier and
        extracts geometric parameters for bars, hole positions defined through
        parametric formulas, and HPGe detector metadata.

        Parameters
        ----------
        path_csv_data : str
            Path to the CSV file containing the instrumentation data.
        case_csv : str
            Case identifier used to select the relevant data block in the CSV.
        """
        data_csv = CsvSeeker(path_csv_data)
        data_other = data_csv.get(case_csv, "data_other")
        
        self.l_name              = list(data_csv.get_list(data_other, "dim_barre","name",          str))
        self.l_width             = list(data_csv.get_list(data_other, "dim_barre","width [cm]",       float))
        self.l_thickness         = list(data_csv.get_list(data_other, "dim_barre","thickness [cm]",      float))
        self.l_h_min             = list(data_csv.get_list(data_other, "dim_barre","h_min [cm]",       float))
        self.l_h_max             = list(data_csv.get_list(data_other, "dim_barre","h_max [cm]",       float))
        self.l_hole_width        = list(data_csv.get_list(data_other, "dim_barre","hole_width [cm]",      float))
        self.l_hole_thickness    = list(data_csv.get_list(data_other, "dim_barre","hole_thickness [cm]",  float))
        self.l_centrage          = list(data_csv.get_list(data_other, "dim_barre","centrage",          float))
        self.l_fct_pos             = list(data_csv.get_list(data_other, "dim_barre","fct_pos",          str))
        hole_tmp                  = list(data_csv.get_list(data_other, "dim_barre","pos_hole",          str))
        
        print(hole_tmp)
        
        def get_pos(nom_barre, pos):
            id_pos = list(self.l_name).index(nom_barre)
            fct = self.l_fct_pos[id_pos]
            fct = fct.replace("x",str(pos))
            return formule2val(fct)
        self.l_pos_hole = []
        for iname, name in enumerate(self.l_name):
            if hole_tmp[iname] != None :
                vec_tmp = lmap(lambda v:float(v), hole_tmp[iname].replace("/","_").replace("-","_").split("_"))
                vec     = lmap(lambda v:get_pos(name,v), vec_tmp)
                print(aff_list("l_pos_hole input "+name, vec_tmp))
                print(aff_list("l_pos_hole "      +name, vec))
                self.l_pos_hole += [vec]
            else:   self.l_pos_hole += [[-100,200]]

        self.l_hpge_name             = list(data_csv.get_list(data_other, "hpge","name"))
        self.l_hpge_pos             = list(data_csv.get_list(data_other, "hpge","pos"))
        self.l_hpge_path             = list(data_csv.get_list(data_other, "hpge","path"))
        
        self.d_hpge_calib   = {}

    '''def get_hpge_calib_path(self, name, pos):
        key = (name,pos)
        if key in self.d_hpge_calib:
            return self.d_hpge_calib[key]
        l_pos_path = filter(lambda i: self.l_hpge_name[i]==name and self.l_hpge_pos[i]==pos, range(len(self.l_hpge_name)))
        if len(l_pos_path) == 0 or len(l_pos_path)>1:
            self._err("get_hpge_calib_path - "+str(len(l_pos_path))+"choice(s) from"+str(name)+" "+str(pos))
        print "load EfficiencyCalibration",name,pos, data_hpge_path[l_pos_path[0]]
        self.d_hpge_calib[key] = EfficiencyCalibration(self.l_hpge_path[l_pos_path[0]])
        #d_hpge_calib[key] = EfficiencyCalibrationG2K(data_hpge_path[l_pos_path[0]])
        return self.d_hpge_calib[key]'''
        
    def _err(self, txt):
        """
        Report an error and stop execution.

        Parameters
        ----------
        txt : str
            Error message describing the failure condition.
        """
        print("ERROR - DataInsta - "+txt)
        exit()
