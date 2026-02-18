from ..Common.utils_general import lmap, formule2val, time2str
from ..Common.CsvSeeker import CsvSeeker
from ..Common.ExcelSheet import ExcelSheet
from ..Stats.Stats import cor_sig_to_cov
from ..EfficiencyCalibration.EfficiencyCalibration import EfficiencyCalibration
from ..Serpent2_utils.sss2_utils import get_sss_res
from ..Prints.PrintnSave import aff, load_dict_from_file, aff_list, aff_decription_s_v_cov
from ..DosiFunctions.Dictionaries import d_spectro, d_mt2name
from ..DosiFunctions.Functions import get_at_density, mass_rad_mat_2_ep
import numpy as np
import datetime
from os.path import expanduser
from scipy.optimize import curve_fit
import hashlib
import os 
import sys
class DataIrrad:
    '''
    Container for the iradiation data from a csv/xlsx file prior
    and during to analysis
    
    This class reads structured CSV/xlsx input describing dosimeters charateristics,
    positions, and HPGe detector configurations. The parsed data are
    stored as attributes for later use in geometry handling, simulations,
    or analysis workflows, uncertainty propagation.
    '''
    def __init__(self, path_csv_data, path_csv_dosi, lcase_csv,
            use_sqrt_for_meas_sig=False,
            load_hpge_eff=False,
            load_sss_results=False,
            load_sss_spectrum=False,
            load_ndup=False,
            load_ndup_nuis=False,
            load_up_pos=False,
            load_moni=True,
            load_petale_position=False, 
            remove_data=True,
            group_order=0,                      # exponent for the grouping of spectra
            keff_only=False,
            load_Factor=False,
            load_ratio=True,
            unique_only=False       #For activity plotting
            ):                   #To load only the keff values not the dosimeters, used for analysis of critical experiments
        """
        Initialize the DataIrrad object containing all informations 
        necessary to the analysis.

        Parameters
        ----------
        path_csv_data : str
            Path to the csv/xlsx file containing the information related to the irradiations
            and/or measurements of dosimeters  
        path_csv_dosi : str
            Path to the csv/xlsx file containing the geometrical charectiristics of dosimeters
        lcase_csv : list of string
            List of experiments identifier to be loaded in the Object
        use_sqrt_for_meas_sig : bool, optional, default is False
            If True: override the counts uncertainties tabulated in "path_csv_data" 
            and replace it by the square root of the counts
        load_hpge_eff: bool, optional, default is False
            If True: load the detector efficiency data from a location specified in "path_csv_data"
        load_sss_results : bool, optional, default is False
            If True: load dosimeters simulation tallies from a location specified in "path_csv_data"
        load_sss_spectrum : bool, optional, default is False
            If True: load in dosimeter spectra from a location specified in "path_csv_data"
        load_ndup : bool, optional, default is False
            If True: load prepropagated dosimetry nuclear data uncertainties saved in a "nducup_out" folder
            The prepropagation is done with the "nducup.py" script
        load_ndup_nuis : bool, optional, default is False
            If True: load prepropagated core nuclear data uncertainties saved in a "ndupnuis_out" folder
            The prepropagation is done with the "nducup_nuis.py" script
        load_up_pos : bool, optional, default is False
            If True: load prepropagated positional uncertainties saved in a "up_pos_out" folder
            The prepropagation is done with the "up_pos.py" script
        load_moni : bool, optional default is True
            If True: load the irradiation monitor history from a location specified in "path_csv_data"
        load_petale_position : bool, optional, default is False
            PETALE specific, 
            If True: load the PETALE case position measurment data 
        remove_data : bool, optional, default is True
            If True all dosimeter data flagged by a "x" in the experiments' "order" columns in "path_csv_data"
        group_order : int, optional, default is 0
            Exponent for the aggregation (summation) of spectral data (e.g., spectra or multigroup tallies)
            in order to reduce the RAM usage.
            The number of energy group summed together is 2^group_order.
            By default 2^0=1 thus nos aggregation is performed 
        keff_only : bool, optional, default is False 
            If True, no dosimeter data are loaded, only the keff from simulations data and monitors histories
        load_Factor: bool, optional, default is False
            If True: load the values from the the experiments' "factor" columns in "path_csv_data"
        load_ratio : bool, optional, default is True
            If True: load the precalculated efficiency ratios from the "Ratio" folder
        unique_only: bool, optional, default is False
            If True: keep only one entry of dosimeters measured on multiple spectrometers 

        Returns
        -------
        None
            The object is initialized in place.
        """
        data_csv = CsvSeeker(path_csv_data)
        dosi_csv = CsvSeeker(path_csv_dosi)
        #self.data_csv = data_csv
        #self.dosi_csv = dosi_csv
        #self.path_csv_data = path_csv_data
        self.path_csv_dosi = path_csv_dosi
        
        self.l_name            = []
        self.l_compo_plate    = []
        self.l_iso          = []
        self.l_mt          = []
        self.l_path_case    = []
        self.l_ymd        = []
        self.l_hms        = []
        self.l_hpge_id        = []
        self.l_hpge_pos        = []
        self.l_time_in_hpge_raw    = []
        self.l_time_in_hpge    = []
        self.l_factor        = []
        self.l_counts_v        = []
        self.l_counts_s        = []
        self.l_deadtime        = []
        self.l_pos_name        = []
        self.l_pos_rel_barre    = []
        self.l_pos_reel        = []
        self.l_case_csv        = []
        self.l_data_other    = []
        self.l_irrad_time_start    = []
        self.l_irrad_time_stop     = []
        self.l_sss_path        = []
        self.l_NDlib           = []
        self.l_compo_plate_full_name = []
        self.l_Activ_Energy    = []
        if load_sss_results:
            self.l_power_per_src_n   =[]
            self.l_power_per_src_n_s =[]
            self.l_sss_keff   =[]
            self.l_sss_keff_s =[]
        self.l_sss_path_nuis        = []
        self.l_sss_pos_nuis         = []
        self.l_sss_path_pos        = []
        self.l_sss_pos_pos         = []
        self.l_up_pos_name        = []
        self.l_calib_path    = []
        self.l_calib_ratio_v    = []
        self.l_calib_ratio_s    = []
        self.m_calib_ratio_cov    = []
        self.l_calib_ratio_key    = []
        self.l_monitor_path    = []
        self.l_monitor_calib    = []
        self.l_planned_power_and_time = []
        self.l_order = []
        self.l_meas_order = []
        self.l_water_lvl_cm     = []
        self.CR_north_cm        = []
        self.CR_south_cm        = []
        self.l_water_lvl_cm_ign = []
        self.hh_mm_ss_start=[]
        self.l_irrad_HH_start=[]
        self.l_irrad_HH_stop =[] 
        self.gr_order = int(group_order)
        self.keff_only=keff_only
        self.l_dead_time_param = { #Key: Dead_t_load
                                "v1":{"tau":data_csv.get_list("monitors","monitors","tau [s]",data_type=float)[0], "tau_s" :data_csv.get_list("monitors","monitors","tau sig [s]",data_type=float)[0]},
                                "v2":{"tau":data_csv.get_list("monitors","monitors","tau [s]",data_type=float)[1], "tau_s" :data_csv.get_list("monitors","monitors","tau sig [s]",data_type=float)[1]}}
        print("loading:")
        for case_csv in lcase_csv:
            print(case_csv)
            l_name_tmp         = list(data_csv.get_list(case_csv, "dosimeters","name"           ))
            l_hpge_id_tmp         = list(data_csv.get_list(case_csv, "dosimeters","hpge_id"        ))
            l_hpge_pos_tmp         = list(data_csv.get_list(case_csv, "dosimeters","hpge_pos"        ))
            l_iso_tmp          = list(data_csv.get_list(case_csv, "dosimeters","iso"         ))
            l_mt_tmp           = list(data_csv.get_list(case_csv, "dosimeters","mt"          ))
            self.l_name        += l_name_tmp
            self.l_hpge_id        += l_hpge_id_tmp
            self.l_hpge_pos        += l_hpge_pos_tmp
            self.l_iso        += l_iso_tmp
            self.l_mt        += l_mt_tmp
            self.l_time_in_hpge_raw    += list(data_csv.get_list(case_csv, "dosimeters","time_in_hpge"        ))
            self.l_order        += list(data_csv.get_list(case_csv, "dosimeters","order"        ))
            if data_csv.get_list(case_csv, "dosimeters","prio_1") is not None:
                l1 = list(data_csv.get_list(case_csv, "dosimeters","prio_1"        ))
                l2 = list(data_csv.get_list(case_csv, "dosimeters","prio_2"        ))
                l3 = list(data_csv.get_list(case_csv, "dosimeters","prio_3"        ))
                self.l_meas_order    += lmap(lambda i: float(l1[i])*1e12+float(l2[i])*1e6+float(l3[i]), range(len(l1)))
            else:
                self.l_meas_order += [0] * len(l_name_tmp)
            self.l_ymd        += list(data_csv.get_list(case_csv, "dosimeters","y_m_d"        ))
            self.l_hms        += list(data_csv.get_list(case_csv, "dosimeters","h_m_s"        ))
            if load_Factor:
                self.l_factor        += list(data_csv.get_list(case_csv, "dosimeters","Factor"        , float))
            else:
                self.l_factor        += [1]*len(list(data_csv.get_list(case_csv, "dosimeters","Factor"        , float)))
            self.l_counts_v        += list(data_csv.get_list(case_csv, "dosimeters","counts"        , float))
            self.l_counts_s        += list(data_csv.get_list(case_csv, "dosimeters","counts_sig"        , float))
            #print(self.l_counts_v)
            #print(self.l_counts_s)
            #exit()
            self.l_deadtime        += list(data_csv.get_list(case_csv, "dosimeters","dead_time"        , float))
            self.l_pos_name        += list(data_csv.get_list(case_csv, "dosimeters","pos_barre"        ))
            self.l_pos_rel_barre    += lmap(lambda s: formule2val(s),list(data_csv.get_list(case_csv, "dosimeters","pos [cm]"))) # , str
            tmp_l_pos_reel         =list(data_csv.get_list(case_csv, "dosimeters","pos_reel [cm]"    , str))
            warning_displayed = False
            for ip, p in enumerate(tmp_l_pos_reel):
                if p=="":
                    warning_displayed = True
                    pos_barre =  lmap(lambda s: formule2val(s),list(data_csv.get_list(case_csv, "dosimeters","pos [cm]")))[ip]
                    pos_name  =  data_csv.get_list(case_csv, "dosimeters","pos_barre")[ip]
                    fct = data_csv.get_in_list(data_csv.get(case_csv,"data_other"), "dim_barre", "name",pos_name,"fct_pos")
                    pos_reel = formule2val(fct.replace("x",str(pos_barre)))
                    print("ERROR - pos_reel not given for "+aff(self.l_name[ip],10)+" - on rod "+aff(pos_name,4)+" at "+aff(str(pos_barre)+" cm",10)+", the computed absolute one is: "+str(pos_reel))
                    tmp_l_pos_reel[ip] = str(pos_reel)
            if warning_displayed:
                self._err("please correct the csv file")
            self.l_pos_reel        += lmap(lambda s: formule2val(s),tmp_l_pos_reel)
            
            nb_new_dosi = len(data_csv.get_list(case_csv, "dosimeters","name"))
            
            self.l_compo_plate    += [data_csv.get(case_csv, "compo_plate", default=None)]*int(max([1,nb_new_dosi]))
            self.l_compo_plate_full_name    += [data_csv.get(case_csv, "compo_plate", default=None).replace("Ni","Nickel").replace("Cr","Chromium").replace("Fe","Iron").replace("SS","304L")]*int(max([1,nb_new_dosi]))
            self.l_path_case    += [data_csv.get(case_csv, "sss_path")]*int(max([1,nb_new_dosi]))
            self.l_case_csv        += [case_csv]*int(max([1,nb_new_dosi]))
            tmp_data_other           = data_csv.get(case_csv,"data_other")
            self.l_data_other    += [tmp_data_other]*int(max([1,nb_new_dosi]))
        
            self.l_irrad_time_start    += nb_new_dosi*[datetime.datetime(*map(lambda s:int(s), (data_csv.get(case_csv, "date")+"_"+data_csv.get(case_csv,"time_start_irrad")).split("_")))]
            self.l_irrad_time_stop     += nb_new_dosi*[datetime.datetime(*map(lambda s:int(s), (data_csv.get(case_csv, "date")+"_"+data_csv.get(case_csv,"time_stop_irrad")).split("_")))]
            self.l_irrad_HH_start    += nb_new_dosi*[datetime.datetime(*map(lambda s:int(s), (data_csv.get(case_csv, "date")+"_"+data_csv.get(case_csv,"time_start_irrad")).split("_"))).strftime("%H:%M:%S")]
            self.l_irrad_HH_stop     += nb_new_dosi*[datetime.datetime(*map(lambda s:int(s), (data_csv.get(case_csv, "date")+"_"+data_csv.get(case_csv,"time_stop_irrad")).split("_"))).strftime("%H:%M:%S")]
            
            self.l_sss_path        += [data_csv.get(case_csv, "sss_path")] *int(max([1,nb_new_dosi]))
            if len(data_csv.get(case_csv, "sss_path").split("/"))>6:
                self.l_NDlib       += [data_csv.get(case_csv, "sss_path").split("/")[5]] *int(max([1,nb_new_dosi]))
            else:
                self.l_NDlib       += [" "] *int(max([1,nb_new_dosi]))
            # print(self.l_NDlib)
            if True:
                path, pos = data_csv.get(case_csv, "sss_path_nduc",data_type=str,default="NoPath NoPos").split()
                self.l_sss_path_nuis        += [path] *int(max([1,nb_new_dosi]))
                self.l_sss_pos_nuis         += [pos]  *int(max([1,nb_new_dosi]))
            if True:
                path, pos = data_csv.get(case_csv, "sss_path_up_pos",data_type=str,default="NoPath NoPos").split()
                self.l_sss_path_pos        += [path] *int(max([1,nb_new_dosi]))
                self.l_sss_pos_pos         += [pos]  *int(max([1,nb_new_dosi]))
                if "C" in pos: 
                    self.l_up_pos_name        += [n.replace("_3","_1").replace("_5","_1")  for n in list(data_csv.get_list(case_csv, "dosimeters","pos_barre"        ))]
                else:
                    self.l_up_pos_name        += [n.replace("_3","_1").replace("_5","_1").replace("C","all")  for n in list(data_csv.get_list(case_csv, "dosimeters","pos_barre"        ))]
            tmp_data_lnamehpge = list(data_csv.get_list(tmp_data_other, "hpge","name"))
            tmp_data_lposhpge  = list(data_csv.get_list(tmp_data_other, "hpge","pos"))
            tmp_data_lpathhpge = list(data_csv.get_list(tmp_data_other, "hpge","path"))
            
            self.l_mat        = lmap(lambda name: name.split("-")[0], self.l_name)
            if load_ratio:
                self.d_ratio=load_dict_from_file(filename="Ratio/8d88ffabf2b0a63016e3c408c2cc58c8")       
                # self.d_ratio=load_dict_from_file(filename="Ratio/"+self.get_key_for_ratio())       
                ratio_key= self.d_ratio.keys()
                for (name_dosi, name,pos, iso, mt) in zip(l_name_tmp, l_hpge_id_tmp,l_hpge_pos_tmp, l_iso_tmp, l_mt_tmp):    # get the calibration
                    def get_data(name, pos, namehpge,idposhpge,key):
                        for ihpgecalib in range(len(tmp_data_lnamehpge)):
                            idhpge, poshpge = tmp_data_lnamehpge[ihpgecalib], tmp_data_lposhpge[ihpgecalib]
                            #print(name, pos, v,s,key, idhpge, poshpge, idhpge==name and poshpge==pos)
                            if idhpge==name and poshpge==pos:
                                self.l_calib_path      += [tmp_data_lpathhpge[ihpgecalib]]
                                tmploc="_".join([iso,mt,str(namehpge)])
                                print(tmploc)
                                if tmploc in ratio_key and idposhpge!="p13":
                                    self.l_calib_ratio_v   += [self.d_ratio["_".join([iso,mt,namehpge])]]
                                    self.l_calib_ratio_s   += [self.d_ratio["_".join([iso,mt,namehpge,iso,mt,namehpge])]**0.5]
                                else:
                                    self.l_calib_ratio_v   += [1]
                                    self.l_calib_ratio_s   += [0]

                                if key is not None: key += "_"+name+"_"+pos+"_"+str(d_spectro[(iso, mt)]["keV"])
                                self.l_calib_ratio_key += [key]
                                return True
                        return False
                #print("#"*40)
                #print("coucou",name_dosi)
                    if not get_data(name, pos, 1.,0.,None):
                        l_key_ratio_eff = dosi_csv.get_in_list("name", "name", "name", name_dosi, "ratio_eff", deep=True).replace("/"," ").split()
                        key_ratio_eff = l_key_ratio_eff[0]
                        ok = False
                        #print(name_dosi,l_key_ratio_eff)
                        #print("loop",key_ratio_eff)
                        for ikey, name_key_available in enumerate(dosi_csv.get_list("ratio_eff", "ratio_eff", "name")):
                            if name_key_available == key_ratio_eff:
                                nrj       = dosi_csv.get_list("ratio_eff", "ratio_eff", "energy [keV]")[ikey]
                                pos_other = dosi_csv.get_list("ratio_eff", "ratio_eff", "pos_other"   )[ikey]
                                pos_ref   = dosi_csv.get_list("ratio_eff", "ratio_eff", "pos_ref"     )[ikey]
                                ratio_val = dosi_csv.get_list("ratio_eff", "ratio_eff", "ratio_val"   )[ikey]
                                ratio_sig = dosi_csv.get_list("ratio_eff", "ratio_eff", "ratio_sig"   )[ikey]
                                name_hpge_ref, pos_hpge_ref = pos_ref.split("_")
                                hpge_id,hpge_id_pos=pos_other.split("_")
                                #print((iso, mt))
                                #print(nrj, pos_other, pos_ref,d_spectro[(iso, mt)]["keV"],float(nrj), pos_other.split("_") == [name,pos], abs(d_spectro[(iso, mt)]["keV"]-float(nrj))<2)
                                if pos_other.split("_") == [name,pos] and abs(d_spectro[(iso, mt)]["keV"]-float(nrj))<2:
                                    #print("->",key_ratio_eff, name_key_available, nrj, pos_other, pos_ref, name, pos, pos_other.split("_") == [name,pos] )
                                    if get_data(name_hpge_ref, pos_hpge_ref, hpge_id, hpge_id_pos, key_ratio_eff+"_"+pos_other):
                                        ok = True
                                        break
                        if not ok:
                            self._err("no hpge HPGe calibration or efficiency ratio found for <"+name_dosi+"> in HPGe <"+name+"> at position <"+pos+"> for iso <"+str(iso)+"> and mt <"+str(mt)+">")
            
            
            if load_moni:
                #tmp_moni_path = data_csv.get(case_csv, "moni_path")
                tmp_moni_path = data_csv.get(case_csv, "monitor_path")
                ye,mo,da,ho,mi,se,voie,dw = tmp_moni_path.split("/")[-1].split("_")[:8]
                tmp_l_data_monitor_voie  = list(data_csv.get_list(tmp_data_other, "monitors", "channel",        str))
                tmp_l_data_monitor_calib = list(data_csv.get_list(tmp_data_other, "monitors", "calibration [count/J]",    float))
                id_voie = tmp_l_data_monitor_voie.index(voie)
                self.l_monitor_path    += [tmp_moni_path]*int(max([1,nb_new_dosi]))
                self.l_monitor_calib    += [tmp_l_data_monitor_calib[id_voie]]*int(max([1,nb_new_dosi]))
                dt=datetime.datetime(*lmap(lambda s: int(s),tmp_moni_path.split("//")[0].split("/")[-1].split("_")[0:6]))
                self.hh_mm_ss_start += [dt.strftime("%H:%M:%S")]*int(max([1,nb_new_dosi]))
            self.l_water_lvl_cm     += (np.array([data_csv.get_list(case_csv, "water_lvl [mm]", "dev_irrad", float)[0]] *int(max([1,nb_new_dosi]))) / 10       ).tolist()
            self.CR_north_cm        += (np.array([data_csv.get_list(case_csv, "Control_rod_height [mm]", "BABS NO", float)[0]] *int(max([1,nb_new_dosi]))) / 10).tolist()
            self.CR_south_cm        += (np.array([data_csv.get_list(case_csv, "Control_rod_height [mm]", "BABS SE", float)[0]] *int(max([1,nb_new_dosi]))) / 10).tolist()
            self.l_water_lvl_cm_ign += (np.array([data_csv.get_list(case_csv, "water_lvl [mm]", "inus_irrad", float)[0]] *int(max([1,nb_new_dosi])))    / 10  ).tolist()
            # if self.l_water_lvl_cm_ign[-1] != None:
                # self.l_water_lvl_cm_ign /= 10
        print("loaded")
        
        self.l_time_in_hpge = lmap(lambda s: float(s[:-1]) * {"s":1, "m":60, "h":3600, "d":3600*24}[s[-1]],self.l_time_in_hpge_raw)
        
        
        
        
        
        self.l_pos_name_tex = []
        for s in self.l_pos_name:
            if "_" not in s:
                self.l_pos_name_tex += [s]
            elif len(s.split("_"))==2 and s.startswith("P"):
                s1,s2 = s.split("_")
                self.l_pos_name_tex += [s1+"_{"+s2+"}"]
            elif len(s.split("_"))==3:
                s1,s2,s3 =s.split("_")
                self.l_pos_name_tex += [s1+"^{"+s2+"}"+"_{"+s3+"}"]
            else:
                self._err("format in <pos_barre>, suppose to find something like <C>,<CR>,<P_fe_3>... but found: "+ s)
        
        self.nb_dosi = len(self.l_name)
        self.l_zz        = lmap(lambda iso: iso[:-4], self.l_iso)
        def fct_remove_0(s):                                    # useful functions
            while s[0] == "0" : s = s[1:]
            return s
        self.l_aaa        = lmap(lambda i: fct_remove_0(self.l_iso[i][:-1].replace(self.l_zz[i],"",1)), range(self.nb_dosi))
        self.l_mat_with_iso = [r"^{"+s1+r"}"+s2 for (s1,s2) in zip(self.l_aaa,self.l_mat)]
        self.l_at_den    = lmap(lambda i: get_at_density(self.l_mat[i],self.l_iso[i][:-1]), range(self.nb_dosi))
        self.l_key_irdff_iaea= lmap(lambda i: self.l_mat[i]+self.l_aaa[i]+d_mt2name[self.l_mt[i]], range(self.nb_dosi))
        
        self.l_masse    = np.array(lmap(lambda name: float(dosi_csv.get_in_list("name", "name", "name", name, "weight",        deep=True)), self.l_name))
        self.l_diam        = np.array(lmap(lambda name: float(dosi_csv.get_in_list("name", "name", "name", name, "diameter [cm]", deep=True)), self.l_name))
        
        self.l_radius    = self.l_diam / 2
        self.l_thickness = np.array(lmap(lambda i:mass_rad_mat_2_ep(self.l_masse[i], self.l_radius[i], self.l_mat[i]), range(self.nb_dosi)))
        
        
        self.l_volume   = (np.pi*self.l_radius**2)*self.l_thickness
        
        self.l_at_den     = np.array(lmap(lambda i: get_at_density(self.l_mat[i],self.l_iso[i][:-1]),    range(self.nb_dosi)))
        self.l_half_time  = np.array(lmap(lambda i: d_spectro[(self.l_iso[i], self.l_mt[i])]["halftime"],    range(self.nb_dosi)))
        self.l_gamma_nrj  = np.array(lmap(lambda i: d_spectro[(self.l_iso[i], self.l_mt[i])]["keV"],    range(self.nb_dosi)))
        self.l_gamma_inten= np.array(lmap(lambda i: d_spectro[(self.l_iso[i], self.l_mt[i])]["inten"],    range(self.nb_dosi)))
        self.l_reaction_txt= np.array(lmap(lambda i: d_spectro[(self.l_iso[i], self.l_mt[i])]["txt"],    range(self.nb_dosi)))

        self.l_hpge_time     = lmap(lambda i: datetime.datetime(*map(lambda s:int(s), (self.l_ymd[i]+"_"+self.l_hms[i]).split("_"))), range(self.nb_dosi))
        self.l_hpge_time_out = lmap(lambda i: self.l_hpge_time[i]+datetime.timedelta(seconds=self.l_time_in_hpge[i]), range(self.nb_dosi))
        
        if use_sqrt_for_meas_sig:
            self.l_counts_s = np.array(self.l_counts_v)**0.5
        
        self.l_barre_name    = lmap(lambda i: data_csv.get_in_list(self.l_data_other[i], "dim_barre", "name",self.l_pos_name[i],"name"),    range(self.nb_dosi))
        self.l_barre_fct_pos = lmap(lambda i: data_csv.get_in_list(self.l_data_other[i], "dim_barre", "name",self.l_pos_name[i],"fct_pos"),    range(self.nb_dosi))
        
        
        self.l_auto_abs      = np.ones(self.nb_dosi)
        self.l_auto_abs_s    = np.zeros(self.nb_dosi)
        self.m_autoabs_cov   = np.zeros([self.nb_dosi,self.nb_dosi])
        
        for idosi in range(self.nb_dosi):
            found = False
            if False:
                nb_col = len(filter(lambda s:s=="auto_abs_val", dosi_csv.get_line_starting_with("name")))
                for iver in range(nb_col):
                    nrj_in_csv = dosi_csv.get_in_list("name", "name", "name", self.l_name[idosi], "auto_abs_nrj [keV]", deep=True, nb_version=iver)
                    if nrj_in_csv != "" and abs(float(nrj_in_csv) - self.l_gamma_nrj[idosi])<2:
                        self.l_auto_abs[idosi]   = dosi_csv.get_in_list("name", "name", "name", self.l_name[idosi], "auto_abs_val", deep=True, nb_version=iver)
                        self.l_auto_abs_s[idosi] = dosi_csv.get_in_list("name", "name", "name", self.l_name[idosi], "auto_abs_sig", deep=True, nb_version=iver)
                        found = True
                if not found:
                    print("WARNING - no auto absorption for dosimeter "+self.l_name[idosi]+" at energy",self.l_gamma_nrj[idosi])
            else:
                key_alias = dosi_csv.get_in_list("name", "name", "name", self.l_name[idosi], "ratio_eff", deep=True)
                if key_alias != "":
                    val, sig = 1., 0.
                    for ikey, name_key_available in enumerate(dosi_csv.get_list("auto_abs_et_geom", "auto_abs_et_geom", "name")):
                        if name_key_available == key_alias:
                            nrj = dosi_csv.get_list("auto_abs_et_geom", "auto_abs_et_geom", "energy [keV]")[ikey]
                            if abs(d_spectro[(self.l_iso[idosi], self.l_mt[idosi])]["keV"]-float(nrj)) < 2:
                                val = dosi_csv.get_list("auto_abs_et_geom", "auto_abs_et_geom", "val")[ikey]
                                sig = dosi_csv.get_list("auto_abs_et_geom", "auto_abs_et_geom", "sig")[ikey]
                                if val=="-":
                                    thickness   = float(dosi_csv.get_list("auto_abs_et_geom", "auto_abs_et_geom", "fct_thickness")[ikey])
                                    absoption   = float(dosi_csv.get_list("auto_abs_et_geom", "auto_abs_et_geom", "fct_abs")[ikey])
                                    absoption_s = float(dosi_csv.get_list("auto_abs_et_geom", "auto_abs_et_geom", "fct_abs_sig")[ikey])
                                    lambda_abs  = -np.log(absoption)/thickness
                                    lambda_abs_s= absoption_s/(absoption*thickness)
                                    val = np.exp(-lambda_abs * self.l_thickness[idosi])
                                    sig = lambda_abs_s*self.l_thickness[idosi] * np.exp(-lambda_abs * self.l_thickness[idosi])
                                    
                    self.l_auto_abs  [idosi] = float(val)
                    self.l_auto_abs_s[idosi] = float(sig)
                else:
                    self.l_auto_abs  [idosi] = 1.
                    self.l_auto_abs_s[idosi] = 0.
                
                if self.l_auto_abs[idosi] == 1:
                    print("WARNING - no autoabsorption factor for", key_alias, "no autoabsorption is assumed")
                if   self.l_mat[idosi] == "Fe" and self.l_aaa[idosi]=="58"  and self.l_mt[idosi]=="102"  : self.l_Activ_Energy+=["Unknown"]
                elif self.l_mat[idosi] == "In" and self.l_aaa[idosi]=="115" and self.l_mt[idosi]=="102"  : self.l_Activ_Energy+=["1.7 eV"]
                elif self.l_mat[idosi] == "Au" and self.l_aaa[idosi]=="197" and self.l_mt[idosi]=="102"  : self.l_Activ_Energy+=["5.7 eV"]
                elif self.l_mat[idosi] == "In" and self.l_aaa[idosi]=="115" and self.l_mt[idosi]=="11004": self.l_Activ_Energy+=["2.0 MeV"]
                elif self.l_mat[idosi] == "Ni" and self.l_aaa[idosi]=="58"  and self.l_mt[idosi]=="103"  : self.l_Activ_Energy+=["3.6 MeV"]
                elif self.l_mat[idosi] == "Fe" and self.l_aaa[idosi]=="54"  and self.l_mt[idosi]=="103"  : self.l_Activ_Energy+=["4.1 MeV"]
                elif self.l_mat[idosi] == "Fe" and self.l_aaa[idosi]=="56"  and self.l_mt[idosi]=="103"  : self.l_Activ_Energy+=["7.6 MeV"]
                elif self.l_mat[idosi] == "Al" and self.l_aaa[idosi]=="27"  and self.l_mt[idosi]=="107"  : self.l_Activ_Energy+=["8.7 MeV"]
        for i in range(len(self.l_auto_abs)) :            #small trick for the cov with 100% correlation as one sim per material
            for j in range(len(self.l_auto_abs)) :    
                if self.l_iso[i]==self.l_iso[j]:
                    self.m_autoabs_cov[i][j]=self.l_auto_abs_s[i]*self.l_auto_abs_s[j]
                    
        #self.l_auto_abs  = np.array(map(lambda name: float(dosi_csv.get_in_list("name", "name", "name", name, "auto_abs",     deep=True)), self.l_name))
        #self.l_auto_abs_s= np.array(map(lambda name: float(dosi_csv.get_in_list("name", "name", "name", name, "auto_abs_sig", deep=True)), self.l_name))
        
        #self.data_csv.get_list(self.l_data_other[i], "hpge","pos"))
        
        self.d_hpge_calib   = {}
        
        if load_ndup:
            self._load_ndup()
        if load_ndup_nuis:
            self._load_ndup_nuis()
        if load_up_pos:
            self._load_up_pos()
        
        for att in [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self,a))]:
            if type(getattr(self, att)) == list:
                setattr(self, att, np.array(getattr(self, att)))

        if remove_data or unique_only:
            self._remove_commented(remove_data,unique_only =unique_only)
        if load_petale_position: # will need changes when Rex finalized
            self.l_petale_face_meas = []
            self.l_petale_side_meas = []
            self.l_petale_height_meas = []
            self.l_petale_meas_pos_h = []
            self.l_petale_meas_pos_lat = [] #lateral position of the measurment relatively the the centre one
            self.l_petale_meas_rod_d = []
            self.l_petale_deflection_rod = []
            self.do_case_position()
                
        if load_sss_results:
            self._load_sss_results(load_sss_spectrum)
        ###################
        #for att in [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self,a))]:
        #    if type(getattr(self, att)) == list:
        #        setattr(self, att, np.array(getattr(self, att)))
        #
        #self._remove_commented()
        #self.aff_description()
        #exit()
        ###################
        if load_hpge_eff:
            self._load_hpge_efficiency()

        for att in [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self,a))]:
            if type(getattr(self, att)) == list:
                setattr(self, att, np.array(getattr(self, att)))
        #self._remove_commented()
        
        #self.aff_description()
        #exit()
    
    def do_case_position(self):
        '''
        Iinitialise PETALE specific case position parameters. 
        '''
        home = expanduser("~")
        mat_csv=ExcelSheet(home+"/Link_to_analysis/Casier_position/Data2.xlsx")
        
        def get_case_position(case_csv,mat_csv): #only for Cr and Ni, get the position from the excel sheet
            if "Cr" in case_csv:
                start_line_pos=2    #Potentially to be modified
                start_line_side=10
            elif "Ni" in case_csv:
                start_line_pos=14   #Potentially to be modified    
                start_line_side=start_line_pos
            else:
                print("Error: Unknown case for load_petale_position")
                print(case_csv)
                exit()
            start_column_face=3
            start_column_side=7
            start_column_meas_height=11
            start_column_height=16
            start_line_rod=8
            start_column_rod=11
            tmp_side = []
            tmp_face = []
            tmp_height = []
            tmp_meas_height = []
            tmp_diam_rod = []
            tmp_deflection_rod = []
            
            for i_repet in range(3): #all measurment repetition face
                tmp_f_m_face = []
                for i_h in range(3): #height laoding
                    tmp_f_l_face = []
                    for i_lat in range(3): #lateral loading
                        tmp_f_l_face += [float(mat_csv.get(start_line_pos + i_repet*4 + i_h,start_column_face+i_lat))]
                    tmp_f_m_face += [tmp_f_l_face]
                tmp_face +=[tmp_f_m_face]
            
            for i_h in range(3): #height laoding
                tmp_s_l_face = []
                for i_lat in range(2): #lateral loading
                    print(start_line_pos + i_h,start_column_side+i_lat)
                    tmp_s_l_face += [float(mat_csv.get(start_line_side + i_h,start_column_side+i_lat))]
                tmp_side += [tmp_s_l_face]
                
            
            
            for i_h in range(2): #height laoding
                tmp_h_l_face = []
                for i_lat in range(3): #lateral loading
                    tmp_h_l_face += [float(mat_csv.get(2  + i_h,start_column_height+i_lat))]
                tmp_height += [tmp_h_l_face]
            
            
            for i_h in range(3): #height laoding
                tmp_mh_l_face = []
                for i_lat in range(3): #lateral loading
                    tmp_mh_l_face += [float(mat_csv.get(2  + i_h,start_column_meas_height+i_lat))]
                tmp_meas_height += [tmp_mh_l_face]
            
            
            for i_h in range(5): #height laoding
                tmp_d_l_rod = []
                for i_lat in range(6): #rod loading
                    tmp_d_l_rod += [float(mat_csv.get(start_line_rod +  i_h,start_column_rod+i_lat))]
                tmp_diam_rod += [tmp_d_l_rod]
                
            for i_h in range(6): #rod laoding
                tmp_def_l_rod = []
                for i_lat in range(3): #lateral loading
                    tmp_def_l_rod += [float(mat_csv.get(start_line_rod+1 + i_lat,start_column_rod+6+i_h)/2)]
                tmp_deflection_rod += [tmp_def_l_rod]
            
            return tmp_face, tmp_side, tmp_height, tmp_meas_height, tmp_diam_rod, tmp_deflection_rod
        
        if ("Cr" in self.l_compo_plate[0]):
            tmp_face, tmp_side, tmp_height, tmp_meas_height, tmp_diam_rod, tmp_deflection_rod = get_case_position("expCr",mat_csv)        
        elif ("Ni" in self.l_compo_plate[0]):
            tmp_face, tmp_side, tmp_height, tmp_meas_height, tmp_diam_rod, tmp_deflection_rod = get_case_position("expNi",mat_csv)
        else :
            tmp_face_Cr, tmp_side_Cr, tmp_height_Cr, tmp_meas_height_Cr, tmp_diam_rod_Cr, tmp_deflection_rod_Cr = get_case_position("expCr",mat_csv)
            tmp_face_Ni, tmp_side_Ni, tmp_height_Ni, tmp_meas_height_Ni, tmp_diam_rod_Ni, tmp_deflection_rod_Ni = get_case_position("expNi",mat_csv)
            masseCr = 103784 #mass in g
            masseNi = 128596 #mass in g
            masseRef= 114051 if "SS" in self.l_compo_plate[0] else 113736

            def f_lin(X,a,b):
                s=[]
                if not np.isscalar(X):
                    for x in X:
                        s += [a*x + b]
                    return s
                else :
                    return a*X + b
            #problem à venir très certainement   
            fit_face   = list(map(lambda X,Y: list(map(lambda x,y: curve_fit(f_lin,[masseCr]*3+[masseNi]*3,x+y)[0],X,Y)),tmp_face_Cr,tmp_face_Ni))
            fit_side   = list(map(lambda X,Y: list(map(lambda x,y: curve_fit(f_lin,[masseCr,masseNi],[x,y])[0],X,Y)),tmp_side_Cr,tmp_side_Ni))
            fit_height = list(map(lambda X,Y: list(map(lambda x,y: curve_fit(f_lin,[masseCr,masseNi],[x,y])[0],X,Y)),tmp_height_Cr,tmp_height_Ni))
            coef_face   = np.array(fit_face)
            coef_side   = np.array(fit_side)
            coef_height = np.array(fit_height)
            tmp_face   = [list(map(lambda C: list(map(lambda c: f_lin(masseRef,*c),C)),coef_face  ))]*3
            tmp_side   = list(map(lambda C: list(map(lambda c: f_lin(masseRef,*c),C)),coef_side  ))
            tmp_height = list(map(lambda C: list(map(lambda c: f_lin(masseRef,*c),C)),coef_height))
            tmp_meas_height = tmp_meas_height_Cr
            tmp_diam_rod = tmp_diam_rod_Cr
            tmp_deflection_rod = tmp_deflection_rod_Cr
        
        def f_quad(X,a,b,c):
            s=[]
            for x in X:
                s += [a*x*x + b*x + c]
            return s
        def f_fit(X): 
            # print(X)
            return curve_fit(f_quad,[679,595,409],X)[0]
        fit_defl  = list(map(lambda X: f_fit(X),tmp_deflection_rod))#manually place position may be replace in the future 
        fit_defl = np.array(fit_defl)
        # print(fit_defl)
        coef_defl = np.array(fit_defl)
        tmp_defl   = list(map(lambda C: f_quad([679,529,409],*C), coef_defl  ))
        for it in range(len(tmp_deflection_rod)) : tmp_deflection_rod[it][1]=tmp_defl[it][1]
        if len(set(self.l_case_csv))>1:
            print("Warning - use of \"PETALE position\" with multiple cases, not tested")
            self.l_petale_face_meas      += [tmp_face]
            self.l_petale_side_meas      += [tmp_side]
            self.l_petale_height_meas    += [tmp_height]
            self.l_petale_meas_pos_h     += [tmp_meas_height]
            tmp_pitch=29.17              
            self.l_petale_meas_pos_lat   += [[-3*np.sqrt(2)*tmp_pitch,0,3*np.sqrt(2)*tmp_pitch]]
            self.l_petale_meas_rod_d     += [tmp_diam_rod]
            self.l_petale_deflection_rod += [tmp_deflection_rod]
        else:
            self.l_petale_face_meas      = tmp_face
            self.l_petale_side_meas      = tmp_side
            self.l_petale_height_meas    = tmp_height
            self.l_petale_meas_pos_h     = tmp_meas_height
            tmp_pitch=29.17              
            self.l_petale_meas_pos_lat   = [-3*np.sqrt(2)*tmp_pitch,0,3*np.sqrt(2)*tmp_pitch]
            self.l_petale_meas_rod_d     = tmp_diam_rod
            self.l_petale_deflection_rod = tmp_deflection_rod
            
    def linearity_loss_corrected_tka(self, tka,id_voie="v1",dwell_time=1.): # key : linearity_corr
        """
        Correct measured count rates for linearity loss due to detector dead time.

        The method applies a dead-time correction to a time-channel analysis (TKA)
        spectrum using a non-paralyzable dead-time model. Input data can be
        provided either as a numerical array or as a path to a file containing
        the spectrum.

        Parameters
        ----------
        tka : array-like or str
            Measured count rates per channel, or path to a file containing the
            spectrum data.
        id_voie : str or int, optional
            Identifier of the acquisition channel. Accepted values are ``"v1"``
            or ``"v2"`` (or their integer equivalents ``1`` and ``2``).
        dwell_time : float or str, optional
            Acquisition dwell time per channel. If provided as a string, it must
            represent a numerical value.

        Returns
        -------
        numpy.ndarray
            Dead-time–corrected count rates per channel.
        """
        if "d" in dwell_time : dwell_time = dwell_time[1:]
        elif isinstance(dwell_time, str): 
            print("Error - in linearity_loss_corrected_tka dwell tim should be a \"float\"")
            exit()
        dwell_time=float(dwell_time)
        true_counts=[]
        if isinstance(tka,str): #check if the path is given instead of the array
            tka=open(tka).readlines()[2:]
        tka=lmap(lambda s : float(s), tka)
        tka=np.array(tka)
        #print(tka)
        if id_voie==1 or id_voie=="1": id_voie= "v1" 
        if id_voie==2 or id_voie=="2": id_voie= "v2" 
        if id_voie not in ["v1","v2"] :
            print("ERROR : in function \"linearity_loss_corrected\" please enter \"v1\" or  \"v2\" as monitor id.")
            exit()
        tau=self.l_dead_time_param[id_voie]["tau"]
        #print(tau)
        true_counts=np.divide(tka,1-np.multiply(tka,tau/dwell_time))
        return true_counts        

    def _remove_commented(self,remove_data,unique_only=False):
        '''
        Remove the dosimeters marked by a "x", in the "order" column of the original csv file, from the object.
        '''
        #print("remove")
        #l_keep = []
        l_delete = []
        #o_inside = map(lambda order: "o" in order, self.l_order)
        #if True in o_inside:
        # l_delete = [i for i,order in enumerate(self.l_order) if "o" not in order]
        if remove_data:
            l_delete = [i for i,order in enumerate(self.l_order) if "x" in order]
        if unique_only:
            l_delete += [i for i,order in enumerate(self.l_name) if i!=0 and order in self.l_name[:i]]
        l_delete=np.unique(l_delete)
        #print(self.l_order)
        #print(l_delete)
        #exit()
        if len(l_delete)>0:
            for att in [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self,a))]:
                val = getattr(self, att)
                if type(val) == np.ndarray:
                    new_val = []
                    if val.shape == (self.nb_dosi,):
                        setattr(self, att, np.delete(val, l_delete, axis=0))
                    elif val.shape == (self.nb_dosi,self.nb_dosi):
                        val = np.delete(val, l_delete, axis=0)
                        val = np.delete(val, l_delete, axis=1)
                        setattr(self, att, val)
                    else:
                        if len(val)>0:
                            self._err("_remove_commented, "+att+" shape do not fit: "+str(val.shape)+"!="+str(self.nb_dosi)+"\n"+str(val))
            self.nb_dosi -= len(l_delete)
        #self.l_order = np.array(map(lambda s:0 if s.replace("o","")=="" else int(s.replace("o","")), self.l_order))
        
        if False:
            l_reorder = np.arange(self.nb_dosi)
            for i in range(self.nb_dosi):
                for j in range(self.nb_dosi)[:-1]:
                
                    def comp(v1,v2):
                        if v1>v2:  return 1
                        if v1==v2: return 0
                        return -1
                    rev, stop = False, False
                    for l in [self.l_mat,self.l_aaa,self.l_mt,self.l_pos_name]:
                        if not stop:
                            inv = comp(l[l_reorder[j]],l[l_reorder[j+1]])
                            if inv == 1:
                                rev, stop = True, True
                            if inv == -1:
                                stop = True
                    if rev:
                        l_reorder[[j,j+1]] = l_reorder[[j+1,j]]
        else:
            l_ordering = []
            for i in range(self.nb_dosi):
                mini = 0
                if self.l_pos_name[i] == "R":  mini = 0.2
                if self.l_pos_name[i] == "CR": mini = 0.1
                if self.l_pos_name[i] == "C":  mini = 0.0
                
                if   self.l_mat[i] == "Fe" and self.l_aaa[i]=="58"  and self.l_mt[i]=="102"  : l_ordering+=[-1+mini]
                elif self.l_mat[i] == "In" and self.l_aaa[i]=="115" and self.l_mt[i]=="102"  : l_ordering+=[0+mini]
                elif self.l_mat[i] == "Au" and self.l_aaa[i]=="197" and self.l_mt[i]=="102"  : l_ordering+=[1+mini]
                elif self.l_mat[i] == "In" and self.l_aaa[i]=="115" and self.l_mt[i]=="11004": l_ordering+=[2+mini]
                elif self.l_mat[i] == "Ni" and self.l_aaa[i]=="58"  and self.l_mt[i]=="103"  : l_ordering+=[3+mini]
                elif self.l_mat[i] == "Fe" and self.l_aaa[i]=="54"  and self.l_mt[i]=="103"  : l_ordering+=[4+mini]
                elif self.l_mat[i] == "Fe" and self.l_aaa[i]=="56"  and self.l_mt[i]=="103"  : l_ordering+=[5+mini]
                elif self.l_mat[i] == "Al" and self.l_aaa[i]=="27"  and self.l_mt[i]=="107"  : l_ordering+=[6+mini]
                else:
                    print("Warning - DataIrrad - ordering unknown for -",self.l_mat[i],self.l_aaa[i],self.l_mt[i])
                    l_ordering+=[7]
            #l_reorder = map(lambda (i,o):i, sorted(enumerate(l_ordering), key=lambda (i,o):o))
            l_reorder = lmap(lambda i_o:i_o[0], sorted(enumerate(l_ordering), key=lambda i_o:i_o[1]))
        for att in [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self,a))]:
            val = getattr(self, att)
            if type(val) == np.ndarray:
                new_val = []
                if val.shape == (self.nb_dosi,):
                    setattr(self, att, val[l_reorder])
                elif val.shape == (self.nb_dosi,self.nb_dosi):
                    setattr(self, att, val[l_reorder,:][:,l_reorder])
                else:
                    if len(val)>0:
                        self._err("_remove_commented, "+att+" shape do not fit: "+str(val.shape))
    
    def get_key_for_ndup(self):
        """
        Generate a unique hash key for processed propagated dosimetry nuclear data uncertainties table file.

        The method builds a deterministic string from internal configuration
        attributes and computes an MD5 hash. The resulting key can be used to
        uniquely identify a specific table file.

        Returns
        -------
        str
            MD5 hexadecimal hash string representing the corresponding table file path.
        """
        txt  = " ".join(self.l_name)
        txt += " ".join(self.l_mat)
        txt += " ".join(self.l_sss_path)
        txt += " ".join(self.l_key_irdff_iaea)
        return hashlib.md5(bytes(txt, 'utf-8')).hexdigest()
    
    def get_key_for_ndup_nuis(self):
        """
        Generate a unique hash key for processed propagated corenuclear data uncertainties table file.

        The method builds a deterministic string from internal configuration
        attributes and computes an MD5 hash. The resulting key can be used to
        uniquely identify a specific table file.

        Returns
        -------
        str
            MD5 hexadecimal hash string representing the corresponding table file path.
        """
        txt  = " ".join(self.l_name)
        txt += " ".join(self.l_mat)
        txt += " ".join(self.l_sss_path_nuis)
        txt += " ".join(self.l_sss_pos_nuis)
        txt += " ".join(self.l_key_irdff_iaea)
        #print("coucou", hashlib.md5(bytes(txt, 'utf-8')).hexdigest(), self.l_sss_path_nuis)
        #exit()
        return hashlib.md5(bytes(txt, 'utf-8')).hexdigest()
        
    def get_key_for_up_pos(self):
        """
        Generate a unique hash key for processed propagated positionnal uncertainties table file.

        The method builds a deterministic string from internal configuration
        attributes and computes an MD5 hash. The resulting key can be used to
        uniquely identify a specific table file.

        Returns
        -------
        str
            MD5 hexadecimal hash string representing the corresponding table file path.
        """
        txt  = " ".join(self.l_name)
        txt += " ".join(self.l_mat)
        txt += " ".join(self.l_sss_path_pos)
        txt += " ".join(self.l_sss_pos_pos)
        txt += " ".join(self.l_key_irdff_iaea)
        return hashlib.md5(bytes(txt, 'utf-8')).hexdigest()
    
    def get_key_for_ratio(self):
        """
        Generate a unique hash key for efficiency ratios table file.

        The method builds a deterministic string from internal configuration
        attributes and computes an MD5 hash. The resulting key can be used to
        uniquely identify a specific table file.

        Returns
        -------
        str
            MD5 hexadecimal hash string representing the corresponding table file path.
        """
        txt  = " ".join(self.l_name)
        txt += " ".join(self.l_mat)
        txt += "_efficacité"
        return hashlib.md5(bytes(txt, 'utf-8')).hexdigest()

    def get_hpge_calib(self, path):
        """
        Retrieve or load an HPGe efficiency calibration.

        The method returns a cached HPGe efficiency calibration object if it
        has already been loaded. Otherwise, it loads the calibration from the
        specified path, stores it internally, and returns the new instance.

        Parameters
        ----------
        path : str
            Path to the HPGe efficiency calibration file.

        Returns
        -------
        object
            EfficiencyCalibration object associated with the given path.
        """
        if path in self.d_hpge_calib:
            return self.d_hpge_calib[path]
        print("load EfficiencyCalibration",path)
        self.d_hpge_calib[path] = EfficiencyCalibration(path)
        #self.d_hpge_calib[key] = EfficiencyCalibrationG2K(path)
        return self.d_hpge_calib[path]


    def _load_hpge_efficiency(self):
        '''
        load and initialise the HPGe efficiency values, uncertainties, and correlations for all
        dosimeters of the object 
        '''
        print("load_hpge_efficiency")
        for calib_path in self.l_calib_path:
            if calib_path != self.l_calib_path[0]:
                #self._err("no unceratinty propagation implemented between different efficiency calibration")
                print("#########################################################################################")
                print("Warning - no unceratinty propagation implemented between different efficiency calibration")
        if True:
            #calib = self.get_hpge_calib(self.l_calib_path[0])            # get the calibration
            #lval,mcov = calib.get_lval_mcov(self.l_gamma_nrj)            # get the eff and cov
            
            lval = np.zeros(self.nb_dosi)
            mcov = np.zeros((self.nb_dosi,self.nb_dosi))
            for calib_path in set(self.l_calib_path):
                l_id_dosi = self.l_calib_path == calib_path
                m_id_dosi = l_id_dosi.reshape((self.nb_dosi, 1)).dot(l_id_dosi.reshape((1, self.nb_dosi)))
                #print(m_id_dosi)
                lval_sub, mcov_sub = self.get_hpge_calib(calib_path).get_lval_mcov(self.l_gamma_nrj[l_id_dosi])
                lval[l_id_dosi] = lval_sub
                mcov[m_id_dosi] = mcov_sub.reshape(mcov[m_id_dosi].shape)
                #print(mcov[[list(l_id_dosi)]*self.nb_dosi])
                #print(lval)
                #print(mcov)
            
            # l_ratio_eff_v   = np.array(self.l_calib_ratio_v)             # get the ratio efficiency
            m_ratio_eff_cov = np.zeros((len(self.l_calib_ratio_s),len(self.l_calib_ratio_s)))      
            for i in range(len(self.l_calib_ratio_s)):
                    if self.l_hpge_pos[i]!="p13":
                        iso1,mt1,hpge1=self.l_iso[i], self.l_mt[i],self.l_hpge_id[i]
                        for j in range(len(self.l_calib_ratio_s)):
                            if self.l_hpge_pos[j]!="p13":
                                iso2,mt2,hpge2=self.l_iso[j], self.l_mt[j],self.l_hpge_id[j]
                                if "_".join([iso1,mt1,hpge1,iso2,mt2,hpge2]) in self.d_ratio.keys(): 
                                    m_ratio_eff_cov[i,j]=self.d_ratio["_".join([iso1,mt1,hpge1,iso2,mt2,hpge2])]
            self.m_calib_ratio_cov = m_ratio_eff_cov
            # lval, mcov = cov_mult((lval, mcov),(l_ratio_eff_v, m_ratio_eff_cov))    # combine the eff and the ratio
            # print(l_ratio_eff_v)
            # print(np.diag(mcov)**0.5)

            self.l_eff_gamma     = lval
            self.m_eff_gamma_cov = mcov
            self.l_eff_gamma_s   = np.diag(self.m_eff_gamma_cov)**0.5
            
            """
            self.l_eff_gamma     = lval 
            self.m_eff_gamma_cov = mcov
            self.l_eff_gamma_s   = np.diag(self.m_eff_gamma_cov)**0.5
            
            for i_calib, calib_path in enumerate(self.l_calib_path):
                if calib_path != self.l_calib_path[0]:
                    v,s = self.get_hpge_calib(calib_path).get_eff_sig(self.l_gamma_nrj[i_calib])
                    self.l_eff_gamma[i_calib]   = v
                    self.l_eff_gamma_s[i_calib] = s
                    for i in range(self.nb_dosi):
                        #for j in range(self.nb_dosi):
                        self.m_eff_gamma_cov[i,i_calib] = 0
                        self.m_eff_gamma_cov[i_calib,i] = 0
                    self.m_eff_gamma_cov[i_calib,i_calib] = s**2
            """
                    
            '''
            calib = self.get_hpge_calib(self.l_calib_path[0])            # get the calibration
            lval,mcov = calib.get_lval_mcov(self.l_gamma_nrj)            # get the eff and cov
            
            l_ratio_eff_v   = np.array(self.l_calib_ratio_v)             # get the ratio efficiency
            l_ratio_eff_s   = np.array(self.l_calib_ratio_s)
            m_ratio_eff_cor = np.diag(np.ones(len(self.l_calib_ratio_s)))        # 100% correlated for the same key
            monolist_ratio_key = filter(lambda k: k is not None, list(set(self.l_calib_ratio_key)))
            for key in monolist_ratio_key:
                l_id_key = list(filter(lambda i: self.l_calib_ratio_key[i] == key, range(self.nb_dosi)))
                for i in l_id_key:
                    for j in l_id_key:
                        m_ratio_eff_cor[i,j] = 1
            m_ratio_eff_cov = cor_sig_to_cov(m_ratio_eff_cor, l_ratio_eff_s)    # get the cov from sig and cor
            lval, mcov = cov_mult((lval, mcov),(l_ratio_eff_v, m_ratio_eff_cov))    # combine the eff and the ratio
            
            self.l_eff_gamma     = lval
            self.m_eff_gamma_cov = mcov
            self.l_eff_gamma_s   = np.diag(self.m_eff_gamma_cov)**0.5
            
            for i_calib, calib_path in enumerate(self.l_calib_path):
                if calib_path != self.l_calib_path[0]:
                    v,s = self.get_hpge_calib(calib_path).get_eff_sig(self.l_gamma_nrj[i_calib])
                    self.l_eff_gamma[i_calib]   = v
                    self.l_eff_gamma_s[i_calib] = s
                    for i in range(self.nb_dosi):
                        #for j in range(self.nb_dosi):
                        self.m_eff_gamma_cov[i,i_calib] = 0
                        self.m_eff_gamma_cov[i_calib,i] = 0
                    self.m_eff_gamma_cov[i_calib,i_calib] = s**2'''
        
        else:
            l_calib = 1
        
        #self.l_eff_gamma *= 1.1
        #exit()
        
  ###########################################################
    def _load_sss_results(self, load_sss_spectrum):
        """
        Load simulation results from a text files in the "<input_path>_mat_sss_2_of/" folder

        The methods reads the simulation input to identify the tallies identifier and other parameters from
        and then load the tallies and other results (keff, spectrum, etc...) 

        Parameters
        ----------
        load_sss_spectrum : bool
            If Trure the tallies neutron spectra are also loaded

        Returns
        -------
        None
            The tallies and other simulation results are initialised within the object
        """
        print("load_sss_results")
        print(self.nb_dosi)
        def i2den_irdff(i):
            lines = open(self.l_sss_path[i]+".out").readlines()                            # step 1: get de atomic density
            while self.l_iso[i][:-1]+".34y" not in lines[-1]:
                lines.pop(len(lines)-1)
            return float(lines[-1].split()[3])
        one = "" if os.path.isfile(self.l_sss_path[0]) else "1"
        # print(self.l_sss_path[0])
        # print("one :",one)
        #exit()
        mode_vr = "mat_matrix_rr" in "".join(open(self.l_sss_path[0]+one).readlines())
        if False: # To use _det0.m + get_sss_out_det need new definition

            self.l_c_raw   = np.array(lmap(lambda i : get_sss_out(self.l_sss_path[i]+"_det0.m", "DETdos_"+self.l_name[i]+"_"+self.l_iso[i]+"_"+self.l_mt[i]+"_rr")[-2] , range(self.nb_dosi)))
            self.l_cs_raw  = np.array(lmap(lambda i : get_sss_out(self.l_sss_path[i]+"_det0.m", "DETdos_"+self.l_name[i]+"_"+self.l_iso[i]+"_"+self.l_mt[i]+"_rr")[-1] , range(self.nb_dosi)))
            if None in list(self.l_c_raw):
                for iv, v in enumerate(self.l_c_raw):
                    if v is None:
                        print("No result in the sss calculation for",self.l_name[iv])
                self._err("_load_sss_results")
            self.l_cs_raw *= self.l_c_raw
            
            self.l_at_den_irdff = np.array(lmap(lambda i:i2den_irdff(i), range(self.nb_dosi)))
        
            print(aff_list("irdff/calc den-1 [%]", (self.l_at_den_irdff/self.l_at_den-1)*100))
        
            self.l_c  = self.l_c_raw *self.l_at_den_irdff
            self.l_cs = self.l_cs_raw*self.l_at_den_irdff
            if load_sss_spectrum:
                self.ll_fv    = []
                self.ll_fs    = []
                for idosi in range(self.nb_dosi):
                    def get_sss_out_det(a,b) #dummy
                    return a,b
                    l_fv_tmp, l_fs_tmp = get_sss_out_det(self.l_path_case[idosi]+"_det0.m", "dos_"+self.l_name[idosi]+"_spectrum")
                    l_fs_tmp = np.array(l_fs_tmp) * np.array(l_fv_tmp)
                    l_fe_tmp1, l_fe_tmp2 = get_sss_out_det(self.l_path_case[idosi]+"_det0.m", "dos_"+self.l_name[idosi]+"_spectrumE", 0, 1)
                    self.l_fe = l_fe_tmp1 + [l_fe_tmp2[-1]]
                    self.ll_fv += [l_fv_tmp]
                    self.ll_fs += [l_fs_tmp]
                
        elif not self.keff_only:
            self.l_c = []
            self.l_cs = []
            
            #load_sss_spectrum = True
            if load_sss_spectrum:
                self.ll_fv    = []
                self.ll_fs    = []
                nb_nrj = int(int(open(self.l_sss_path[0]+one+"_mat_sss_2_of/perspectra").readline().split()[-1])/(2**self.gr_order))
                E1,E2 = 1e-10, 20.
                self.l_fe = 10**(((np.log10(E2)-np.log10(E1)) * np.array(range(nb_nrj+1))*1./(nb_nrj)) + np.log10(E1))
                dleth = (np.log(20.)-np.log(1e-10))/nb_nrj
            for idosi in range(self.nb_dosi):
                one = "" if os.path.isfile(self.l_sss_path[idosi]) else "1" #reset of "one" necessary in the case of treatment of multiple irrad at once in the case one irrad hasnt a tmp"" file but only tmp1
                l_sub_pathes=[]
                if os.path.isfile(self.l_sss_path[idosi]+"1"): # Key:parallel_sim, Modification in order to allow to parform parallel simulation as well as add ulterior sim for better stat
                    l_sub_pathes+=[self.l_sss_path[idosi]+one]
                    ident=2 if one=="1" else 1
                    while os.path.isfile(self.l_sss_path[idosi]+str(ident)):
                        l_sub_pathes+=[self.l_sss_path[idosi]+str(ident)]
                        ident+=1
                else:
                    l_sub_pathes+=[self.l_sss_path[idosi]]
                ident=0
                ncycle=[]
                lines = open(l_sub_pathes[0]).readlines()
                while "mat_matrix_rr" not in lines[0]:#recherche les detecteurs
                    lines.pop(0)
                lines.pop(0)
                id_l, val, sig = 0, None, None
                
                dosi_name, dosi_iso, dosi_mt = self.l_name[idosi], self.l_iso[idosi], self.l_mt[idosi] #identifie les detecteurs
                if len(dosi_name.split("-")[1])>3:
                    sp=dosi_name.split("-")
                    dosi_name="-".join([sp[i][:3] if i==1 else sp[i] for i in range(len(sp))])
                trouve = False
                while len(lines[0].split())>0 and lines[0].split()[0] == "idet" and not trouve:
                    name, iso, mt = lines[0].split()[1:] # mat_dosi_Au-R4 791970    102
                    
                    if name.replace("mat_dosi_","")==dosi_name and iso==dosi_iso and mt==dosi_mt: #recupere les detecteurs presents dans le xlsx.
                        print(name)
                        #print lines[0].split()[1].replace("mat_dosi_","")
                        ncycle=[]
                        tmp_l_c = []
                        tmp_l_cs = []
                        if len(l_sub_pathes)>1:
                          for l_sub_path in l_sub_pathes : # Key:parallel_sim, Modification in order to allow to perform parallel simulation as well, add to ulterior sim for better stat
                            ncycle.append(float(get_sss_res(l_sub_path+"_res.m", "CYCLE_IDX")))
                            # print(id_l)
                            tmp_l_c  += [float(open(l_sub_path+"_mat_sss_2_of/rr_vec"    ).readlines()[1+id_l].split()[0])]
                            tmp_l_cs += [float(open(l_sub_path+"_mat_sss_2_of/rr_vec_sig").readlines()[1+id_l].split()[0])]
                        # self.l_c  += [np.dot(tmp_l_c,ncycle)/sum(ncycle)]
                        # self.l_cs  +=  [np.sqrt(sum(np.power(np.multiply(tmp_l_cs,np.power(ncycle,1.5)),2)))/sum(np.power(ncycle,1.5))]
                          self.l_c  += [np.sum(np.divide(tmp_l_c,np.power(tmp_l_cs,2)))/np.sum(np.divide(1,np.power(tmp_l_cs,2)))] # Key:parallel_sim, Modification in order to allow to parform parallel simulation as well, add to ulterior sim for better stat
                          self.l_cs  +=  [np.divide(1,np.sqrt(np.sum(np.divide(1,np.power(tmp_l_cs,2)))))]
                        else:
                          self.l_c  += [float(open(self.l_sss_path[idosi]+"_mat_sss_2_of/rr_vec"    ).readlines()[1+id_l].split()[0])]
                          self.l_cs += [float(open(self.l_sss_path[idosi]+"_mat_sss_2_of/rr_vec_sig").readlines()[1+id_l].split()[0])]
                        if load_sss_spectrum:
                            #print(open(l_sub_path+"_mat_sss_2_of/perspectra"    ).readlines()[5+id_l*4])
                          if len(l_sub_pathes)>1:  
                            print("COUCOU1")
                            ncycle=[]
                            tmp_l_fv = []
                            tmp_l_fs = []
                            for l_sub_path in l_sub_pathes :# Key:parallel_sim, Modification in order to allow to parform parallel simulation as well, add to ulterior sim for better stat
                                ncycle.append(get_sss_res(l_sub_path+"_res.m", "CYCLE_IDX"))
                                nb_per = int(open(l_sub_path+"_mat_sss_2_of/perspectra"    ).readline().split()[1])
                                tmp_l_fv += [lmap(lambda lv: sum(lv),np.reshape(lmap(lambda v:float(v)/dleth, open(l_sub_path+"_mat_sss_2_of/perspectra"    ).readlines()[1+(id_l+1)*(nb_per+1)].split()),(-1,2**self.gr_order)))]
                                tmp_l_fs += [lmap(lambda lv: sum(lv),np.reshape(lmap(lambda v:float(v)/dleth, open(l_sub_path+"_mat_sss_2_of/perspectra_sig").readlines()[1+(id_l+1)*(nb_per+1)].split()),(-1,2**self.gr_order)))]
                            #print(np.transpose(tmp_l_fv).shape)
                            tmp_mean_fv = []
                            tmp_mean_fs = []
                            # mat_val=np.matmul(np.transpose(tmp_l_fv),ncycle)
                            # mat_val=np.multiply(np.transpose(tmp_l_fv),np.power(np.divide(1,np.transpose(tmp_l_fs)),2))
                            weights=np.divide(ncycle,np.sum(ncycle))
                            for i in range(len(np.transpose(tmp_l_fv))) : # Key: weighted_arithmetic Modification of the calculation for mean and variance of flux to the inverse-variance weighting method
                                tmp_mean_fv += [np.sum(np.divide(np.transpose(tmp_l_fv)[i],np.power(np.transpose(tmp_l_fs)[i],2)))/np.sum(np.power(np.divide(1,np.transpose(tmp_l_fs)[i]),2))]
                                # tmp_mean_fs += [np.sqrt(sum(np.power(np.multiply(np.transpose(tmp_l_fs)[i],np.power(ncycle,1.5)),2)))/sum(np.power(ncycle,1.5))]
                                # tmp_mean_fs += [np.sqrt(sum(np.power(np.multiply(np.transpose(tmp_l_fs)[i],weights),2)))]
                                tmp_mean_fs += [np.divide(1,np.sqrt(np.sum(np.power(np.divide(1,np.transpose(tmp_l_fs)[i]),2))))]  
                                
                            self.ll_fv  += [tmp_mean_fv]
                            self.ll_fs  += [tmp_mean_fs]
                            #print(len(np.transpose(tmp_l_fv)))
                            #print(self.ll_fv)
                          else:
                            l_sub_path=l_sub_pathes[0]
                            nb_per = int(open(self.l_sss_path[idosi]+"_mat_sss_2_of/perspectra"    ).readline().split()[1])
                            self.ll_fv  += [lmap(lambda v:float(v)/dleth, open(self.l_sss_path[idosi]+"_mat_sss_2_of/perspectra"    ).readlines()[1+(id_l+1)*(nb_per+1)].split())]
                            self.ll_fs  += [lmap(lambda v:float(v)/dleth, open(self.l_sss_path[idosi]+"_mat_sss_2_of/perspectra_sig").readlines()[1+(id_l+1)*(nb_per+1)].split())]
                            if True:
                                print("COUCOU2")
                                print(self.l_name[idosi], end="\t")
                                # compute average energy on interacting neutron
                                l_rr = np.array(lmap(lambda lv: sum(lv),np.reshape(lmap(lambda v:float(v)/dleth, open(l_sub_path+"_mat_sss_2_of/rrperspectra"    ).readlines()[1+(id_l+1)*(nb_per+1)].split()),(-1,2**self.gr_order))))
                                
                                l_leth = np.log10(self.l_fe)
                                print(10**(np.sum((l_leth[1:]+l_leth[:-1])/2 * l_rr) / np.sum(l_rr)), end="\t")
                                
                                for i in range(len(l_rr))[1:]: l_rr[i] += l_rr[i-1]
                                l_rr /= (l_rr[-1]+1e-15)
                                #for lim in [0.1,0.25,0.5,0.75]:
                                for lim in [0.5]:
                                    i = 0
                                    while l_rr[i]<l_rr[-1]*lim: i += 1
                                    print(self.l_fe[i],end="\t")
                                print()
                                # print(self.l_fe * l_rr)
                        #s = sum(map(lambda v:float(v), open(l_sub_path+"_mat_sss_2_of/rrperspectra"    ).readlines()[5+id_l*4].split()))
                        trouve = True
                    lines.pop(0)
                    id_l += 1
                if not trouve :
                    self._err("error 404 pas trouve de dosi demande dans le calcul sss - "+str((dosi_name, dosi_iso, dosi_mt)))
        
        #exit()
        cor = np.zeros((self.nb_dosi, self.nb_dosi))
        d_calc2lnro = {}
        for idosi in range(self.nb_dosi):
            name, iso, mt, path_sss = self.l_name[idosi], self.l_iso[idosi], self.l_mt[idosi], self.l_path_case[idosi]
            if (name, iso, mt, path_sss) not in d_calc2lnro:
                d_calc2lnro[(name, iso, mt, path_sss)] = []
            d_calc2lnro[(name, iso, mt, path_sss)] += [idosi]
        
        for key, l in d_calc2lnro.items():
            #print key, l
            for i in l:
                for j in l:
                    cor[i,j] = 1
        # print(cor)
        # print(self.l_cs)
        
        self.l_power_per_src_n   = np.array(lmap(lambda i : get_sss_res(self.l_sss_path[i]+"_res.m", "TOT_POWER")[0] , range(max([1,self.nb_dosi]))))
        self.l_power_per_src_n_s = np.array(lmap(lambda i : get_sss_res(self.l_sss_path[i]+"_res.m", "TOT_POWER")[1] , range(max([1,self.nb_dosi]))))
        self.l_sss_keff   = np.array(lmap(lambda i : float(open(self.l_sss_path[i]+"_mat_sss_2_of/keff_perspectra"    ).readlines()[1].split()[0]), range(max([1,self.nb_dosi]))))
        self.l_sss_keff_s = np.array(lmap(lambda i : float(open(self.l_sss_path[i]+"_mat_sss_2_of/keff_perspectra_sig"    ).readlines()[1].split()[0]), range(max([1,self.nb_dosi]))))
        # self.l_sss_keff   = np.array(lmap(lambda i : get_sss_res(self.l_sss_path[i]+"_res.m", "IMP_KEFF")[0] , range(max([1,self.nb_dosi]))))
        # self.l_sss_keff_s = np.array(lmap(lambda i : get_sss_res(self.l_sss_path[i]+"_res.m", "IMP_KEFF")[1] , range(max([1,self.nb_dosi]))))
        if not self.keff_only: self.m_c = cor_sig_to_cov(cor, np.array(self.l_cs))
 ####################################################################       
        
    def _load_ndup(self):
        '''
        Initialize the dosimetry nuclear data uncertainties and correlations attributes by reading a table in a preprocessed file.
        The processed files are produced with the "nducup.py" script
        '''
        path_ndup = "nducup_out/out_"+self.get_key_for_ndup()
        if not os.path.isfile(path_ndup):
            print("looking for:",path_ndup)
            print("ERROR - no nuclear data uncertaity propagation on the dosimeter rr founded...")
            print("        please run first:")
            print("#"*50)
            print("python3.9 $petale_analysis/python/irrad/nducup13_WIP.py "+" ".join(sys.argv[1:]))
            print("#"*50+"\n")
            exit()
        
        lines = open(path_ndup).readlines()
        self.l_ndup_rr    =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))        # stdv     3.83306223191e-12 2.13702492392e-12
        self.l_ndup_sig    =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))        # stdv     3.83306223191e-12 2.13702492392e-12
        
        lines.pop(0)                                        # stdv_rel
        lines.pop(0)                                        # cor
        self.m_ndup_cor     = np.array(lmap(lambda line: lmap(lambda s:float(s),line.split()) , lines))# 1.0 0.999848959412 ... \n 0.999848959412 1.0           ...
        self.m_ndup_cov     = cor_sig_to_cov(self.m_ndup_cor, self.l_ndup_sig)
    
        self.l_ndup_rel_rr  = np.ones(self.nb_dosi)
        self.l_ndup_rel_sig = self.l_ndup_sig/self.l_ndup_rr
        self.m_ndup_rel_cov = cor_sig_to_cov(self.m_ndup_cor, self.l_ndup_rel_sig)
    
    
    def _load_ndup_nuis(self):
        '''
        Initialize the core nuclear data uncertainties and correlations attributes by reading a table in a preprocessed file.
        The processed files are produced with the "nducup_nuis.py" script
        '''
        
        path_ndup = "ndupnuis_out/out_"+self.get_key_for_ndup_nuis()
        if not os.path.isfile(path_ndup):
            print("looking for:",path_ndup)
            print("ERROR - no nuclear data uncertaity propagation on the reactor xs founded...")
            print("        please run first:")
            print("#"*50)
            print("python3.9 $petale_analysis/python/irrad/nducup_nuis3.py    "+" ".join(sys.argv[1:]))
            print("#"*50+"\n")
            exit()
        
        lines = open(path_ndup).readlines()
        self.l_ndupnuis_rr    =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))        # stdv     3.83306223191e-12 2.13702492392e-12
        self.l_ndupnuis_sig    =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))        # stdv     3.83306223191e-12 2.13702492392e-12
        
        lines.pop(0)                                        # stdv_rel
        lines.pop(0)                                        # cor
        self.m_ndupnuis_cor     = np.array(lmap(lambda line: lmap(lambda s:float(s),line.split()) , lines))# 1.0 0.999848959412 ... \n 0.999848959412 1.0           ...
        self.m_ndupnuis_cov     = cor_sig_to_cov(self.m_ndupnuis_cor, self.l_ndupnuis_sig)
    
        self.l_ndupnuis_rel_rr  = np.ones(self.nb_dosi)
        self.l_ndupnuis_rel_sig = self.l_ndupnuis_sig/self.l_ndupnuis_rr
        self.m_ndupnuis_rel_cov = cor_sig_to_cov(self.m_ndupnuis_cor, self.l_ndupnuis_rel_sig)
    
    def _load_up_pos(self):
        '''
        Initialize the positional uncertainties and correlations attributes by reading a table in a preprocessed file.
        The processed files are produced with the "up_pos.py" script
        '''
        
        path_uppos = "up_pos_out/out_"+self.get_key_for_up_pos()
        if not os.path.isfile(path_uppos):
            print("looking for:",path_uppos)
            print("ERROR - no postion unceratinty file founded...")
            print("        please run first:")
            print("#"*50)
            print("python ~/Link_to_analysis/python/irrad/up_pos_2_WIP.py    jolimat=True    "+" ".join(sys.argv[1:]))
            print("#"*50+"\n")
            exit()
        
        lines = open(path_uppos).readlines()
        self.l_uppos_rr    =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))       
        self.l_uppos_sig    =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))      
        
        lines.pop(0)                                        # stdv_rel
        lines.pop(0)                                        # cor
        self.m_uppos_cor     = np.array(lmap(lambda line: lmap(lambda s:float(s),line.split()) , lines))#
        self.m_uppos_cov     = cor_sig_to_cov(self.m_uppos_cor, self.l_uppos_sig)
    
        self.l_uppos_rel_rr  = np.ones(self.nb_dosi)
        self.l_uppos_rel_sig = self.l_uppos_sig/self.l_uppos_rr
        self.m_uppos_rel_cov = cor_sig_to_cov(self.m_uppos_cor, self.l_uppos_rel_sig)
        
        
    def _err(self, txt):
        print("ERROR - DataIrrad - "+txt)
        exit()
        
    def aff_description(self):
        '''
        Print a description of the dosimeters with their related attributes in the DataIrrad object as a text table 
        '''
        print(aff_list("l_name",                    self.l_name))
        print(aff_list("l_weight",                  self.l_masse))
        print(aff_list("l_radius",                  self.l_radius))
        print(aff_list("l_thickness",               self.l_thickness))
        print(aff_list("l_hpge_id",                 self.l_hpge_id))
        print(aff_list("l_hpge_pos",                self.l_hpge_pos))
        print(aff_list("l_pos_reel",                self.l_pos_reel))
        print(aff_list("l_hpge_time",               self.l_hpge_time))
        print(aff_list("time_to_hpge [h]",          map(lambda i: (self.l_hpge_time[i]-self.l_irrad_time_stop[i]).total_seconds()/3600. , range(self.nb_dosi))))
        print(aff_list("l_time_in_hpge [h]",        self.l_time_in_hpge/3600.))
        print(aff_list("l_measure",                 self.l_counts_v))
        print(aff_list("l_measure_s rel [%]",       self.l_counts_s/(self.l_counts_v+1e-100)*100))
        print(aff_list("l_deadtime [%]",            self.l_deadtime*100))
        print(aff_list("l_auto_abs",                self.l_auto_abs))
        print(aff_list("l_auto_abs_s rel [%]",      self.l_auto_abs_s/self.l_auto_abs*100))
        print(aff_list("l_iso",                     self.l_iso))
        print(aff_list("l_mt",                      self.l_mt))
        print(aff_list("l_half_time",               map(lambda v:time2str(v),self.l_half_time)))
        print(aff_list("gamma energy [keV]",        self.l_gamma_nrj))
        print(aff_list("l_inten",                   self.l_gamma_inten))
        print(aff_list("l_order",                   self.l_order))
        
        if "l_eff_gamma" in self.__dict__:
            if np.max(np.abs(self.l_calib_ratio_v-1))>0:
                print(aff_list("l_calib_ratio_v",    self.l_calib_ratio_v))
                print(aff_list("l_calib_ratio_s",    self.l_calib_ratio_s))
                print(aff_list("l_calib_ratio_key",    self.l_calib_ratio_key))
            
            
            aff_decription_s_v_cov("eff_gamma", (self.l_eff_gamma, self.m_eff_gamma_cov))
            #print aff_list("l_eff_gamma",            self.l_eff_gamma)
            #print aff_list("l_eff_gamma_s rel [%]",        self.l_eff_gamma_s/self.l_eff_gamma*100)
            #print aff_mat ("m_eff_gamma_cor",        cov_to_sig_cor(self.m_eff_gamma_cov)[1])
        if "l_c_raw" in self.__dict__:
            print(aff_list("l_c_raw",            self.l_c_raw))
            print(aff_list("l_den",                self.l_at_den_irdff))
            print(aff_list("l_c",                self.l_c))
            print(aff_list("l_cs rel [%]",            self.l_cs/self.l_c*100))
        
        if "l_ndup_rel_rr" in self.__dict__:
            aff_decription_s_v_cov("l_ndup_rel_rr", (self.l_ndup_rel_rr, self.m_ndup_rel_cov))
        if "l_uppos_rel_rr" in self.__dict__:
            aff_decription_s_v_cov("l_uppos_rel_rr", (self.l_uppos_rel_rr, self.m_uppos_rel_cov))
        
        if "l_ndupnuis_rel_rr" in self.__dict__:
            aff_decription_s_v_cov("l_ndupnuis_rel_rr", (self.l_ndupnuis_rel_rr, self.m_ndupnuis_rel_cov))
        









    
