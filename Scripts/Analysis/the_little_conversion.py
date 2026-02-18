
from utils_p5 import *
from cnf import *
import subprocess

for p in [  'hpge_data/raw/data/Fu/Calibration~PETALE/Ba_300920_24h_2016_1344_top.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/2020_10_06_10_02_44_FU_T_Cs134-2020.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/2020_10_06_18_18_41_FU_T_Zn65-2020.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/Co57_2020_10_05_10_29_18_FU_T.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/Co60_011020_24h_2016_1360_top.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/Cs137_021020_5h_2019_1351_top.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/Eu_290920_24h_2010_1847_top.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/Mn_0210_20_18h_2016_1791_top.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/Na_011020_6h_2016_1144_top.CNF',
            'hpge_data/raw/data/Fu/Calibration~PETALE/FURGGEN_BKG_191020_90h.CNF',
          ]:
    c = read_cnf_file(p.replace("~"," "), 'TRUE')
    d, mo, y, h, mi, s = c["Start time"].replace("-"," ").replace(":"," ").replace(",","").split()
    start = y+"_"+mo+"_"+d
    time  = h+"_"+mi+"_"+s
    time_meas = str(int(c["Real time"]))+"s"
    dead_time = str(round((c["Real time"]-c["Live time"])/c["Real time"], 4))
    print(str(d)+"/"+str(mo)+"/"+str(y)+" "+str(h)+":"+str(mi)+":"+str(s)+" "+str(y)+"_"+str(mo)+"_"+str(d)+"_"+str(h)+"_"+str(mi)+"_"+str(s)+" "+str(round(c["Real time"],4)))
