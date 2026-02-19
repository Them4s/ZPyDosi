'''
Produce automatically the petale geometry with the dosimeters
'''

from ZPyDosi.Common.utils_general import lmap
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.DosiFunctions.Dictionaries import d_matdosi_2_data
from scipy.optimize import curve_fit
from os.path import expanduser
import numpy as np
from random import gauss
from numpy.random import rand
import matplotlib.pyplot as plt
home = expanduser("~")



print("#"*50)
pert_position = get_param_vari("pert_position" , bool, "false")
larger_dosi = get_param_vari("larger_dosi" , bool, "false") #larger dosi for uncertainty propagation on position. (include al dosimeter positions
do_voxel = get_param_vari("do_voxel" , bool, "True")
one_block = get_param_vari("one_block" , bool, "False") #Create one cell with all voxel or one per voxel
lattice_mod = get_param_vari("lattice_mod" , bool, "True") # Voxelize using serpent lattice
do_plot = get_param_vari("do_plot" , bool, "True") # Voxelize using serpent lattice
save = get_param_vari("save" , str, "") # place the case at the real experimental position
print("#"*50)

path_csv_data  = get_param_vari("csv_data",  str)
path_csv_dosi  = get_param_vari("csv_dosi",  str)
case_csv       = get_param_vari("case",     str)
ref_mat=case_csv[3:5]
path_to_reflector_data=home+"/Link_to_analysis/plaque_3D/data/"
print ("#"*50)

data = DataIrrad(path_csv_data, path_csv_dosi, [case_csv], remove_data=False, load_petale_position=True)
name_petale_list=[]
l_path_vox=[]
name_air=""
name_supl = ""


if len(data.l_mat)<1:
    print("No Dosimeter data detected\n Creating critical experiments geometry")
    Crit_mode=True
else:
    Crit_mode=False


def do_for_all(fun,X,s): #apply fun to all element of X
    A=np.zeros(X.shape)
    for ind, x in np.ndenumerate(X):
        A[ind]=fun(x,s) if np.isscalar(s) else fun(x,s[ind[0],ind[1]]) 
    return A

#f_sig = 1.
def sample_g(v,s): return gauss(v, s)
# def sample_d(v,s): return gauss(v, s/np.sqrt(6)) # door meas. uncertainty, at 6 if not well known, 9 if can be aproximate as a gaussian
def sample_d(v,s): return v+s*(rand()*2-1) # uniform
# def sample_u(v,s): # door meas. uncertainty with limits
    # val=gauss(v, s/np.sqrt(6)) 
    # val = max([val,v-s]) if val < v else min([val,v+s])
    # return val
def sample_u(v,s): return v+s*(rand()*2-1)
#def sample_up(v,s): return v+s*rand()
if False:
    def sample_g(v,s):  return v + s
    def sample_u(v,s):  return v + s
    #def sample_up(v,s): return v + s
if False:
    def sample_g(v,s):  return v - s
    def sample_u(v,s):  return v - s
    #def sample_up(v,s): return v
if False:
    def sample_g(v,s):  return v
    def sample_u(v,s):  return v
    #def sample_up(v,s): return v + 0.5*s
if not pert_position:
    def sample_g(v,s):  return v
    def sample_u(v,s):  return v
    def sample_d(v,s):  return v
    #def sample_up(v,s): return v
################################################################################################# FREE PARAMETERS
# porte dosi            - plan 33
#   largeur y            : 29.8 (+0/-0.01)
#   hauteur z            : 30.0                                # todo : hauteur des plaques utilise a la place...
#   epaisseur x            : 0.15
#   zone dosi x            : 0.05
#   smiley dosi x        : 0.05
# couvercle            - plan 14
#   epaisseur z            : 2.0
# casier            - plan 12
#   ep plaque x            : 1.0                                # todo : pas d incertitude sur le plan...
#   ep plaque y            : 0.8 (+0.002/-0)                        # todo : oui en mm c'est bien 0.02 d incertitude...
#   ep plaque ac rainures y    : 1.0
#   large inter x        : 17.7 (+0.01/-0)
#   large inter rainures y    : 29.8+(+0.01/-0)
#   ep rainure x        : 0.16 (+0.01/-0)
#   ep inter rainures        : 2.01 (+0.01/-0)









nb, lz = 8, 30.0                                      # number and size of the petales

diff_z=30.0083430-30.0


# convention pour les dimentions:
# dim_name_axis(_sig)
dim_prtdosi_y,   dim_prtdosi_y_sig    = 29.795, 0.005
dim_prtdosi_x                = 0.15
dim_epbox_x                = 1.0
dim_epbox_y                = 1.0
dim_epbox_z                = 2.0 
#dim_epbox_z                = 2.0 -diff_z/2
dim_sillon_y,    dim_sillon_y_sig    = 0.199 , 0.001                        # de 1-0.8 a 1-0.802 = 0.2 a 0.198
dim_intbox_x,    dim_intbox_x_sig    = 17.705, 0.005
dim_intbox_y,    dim_intbox_y_sig    = 29.805, 0.005                     # attention, c est sans la hauteur rainures
dim_eprainure_x, dim_eprainure_x_sig    = 0.165, 0.005
dim_rainure2rainure_x            = 2.015+0.165                         # todo : pb topo sur le cumul des incertitudes
dim_dist_plate_lid, dim_dist_plate_lid_sig = 3.2, 0.005                # space for the support bracket
dist_dosi = 3.

dim_support_plate_x=16.0
dim_support_plate_y=40.2
dim_support_plate_z=1.5
dist_support_holes_x=7.15

rot_angle = "0"

sig_e_cale= 0.005 if pert_position else 0
#wedge dosimeter holder
e_cale_pdosi_x=sample_d(16.4,sig_e_cale)
e_cale_pdosi_y=sample_d(21.0,sig_e_cale)
e_cale_pdosi_y_edge=sample_d(0.2,sig_e_cale)
e_cale_pdosi_z=0.2+(1.5*30*(7*158+20))/(e_cale_pdosi_x*10)/(e_cale_pdosi_y*10)/10 +7620/(e_cale_pdosi_x*10)/(e_cale_pdosi_y*10)/10 #th+pdosi+peigne 
e_cale_edge_x=sample_d(16.4,sig_e_cale)
# e_cale_edge_y=11480/(e_cale_edge_x*10)/(17+e_cale_pdosi_z*10)/10 #cale + peigne
# e_cale_edge_z=1.7+e_cale_pdosi_z #peigne
e_cale_edge_y=sample_d(0.3,sig_e_cale)
e_cale_edge_z=1.7+e_cale_pdosi_z #peigne
dist_cale_pdosi_lid=1.7
e_craddle_al=0.4 # thickness of the craddle sheets
#scotch
e_scotch=0.01

if True:
    dim_rainure2rainure_x        = 2.025+0.165                         # todo : pb topo sur le cumul des incertitudes
    
if False:
    dim_intbox_y, dim_intbox_y_sig = 29.80+0.8, 0.00
    dim_sillon_y, dim_sillon_y_sig = 0.2 , 0.000
    
def amplifie(v,s,sens, fact=10):    # sens : True si l incertitude va vers le haut
    print("uncertainty increase: ",v,s, end=" -> ")
    v = v-s if sens else v+s
    s *= fact
    v = v+s if sens else v-s
    print(v,s)
    return v,s



dim_intbox_y = sample_u(dim_intbox_y, dim_intbox_y_sig)

dim_maxrainure_y             = dim_sillon_y +    dim_sillon_y_sig





l_sampled_eprainure_x = np.array([sample_u(dim_eprainure_x, dim_eprainure_x_sig) for i in range(nb+1)])
l_x_mid_rainure = np.arange(nb+1) * dim_rainure2rainure_x + l_sampled_eprainure_x/2 
tmp_borne_sup_rainure = l_x_mid_rainure[:-1] + l_sampled_eprainure_x[:-1]/2
tmp_borne_inf_rainure = l_x_mid_rainure[1:] - l_sampled_eprainure_x[1:]/2
l_sampled_sillon_x = tmp_borne_inf_rainure-tmp_borne_sup_rainure
l_x_mid_sillon = (tmp_borne_inf_rainure+tmp_borne_sup_rainure)/2 + dim_epbox_x
l_x_mid_rainure += dim_epbox_x

#exit()
#angle_vert = "-2"

#rad_circ_dosi    = 5.2                                        # dosimeter on a circle of diameter rad_circ_dosi
rad_circ_dosi    = 3.0*2**0.5                                        # dosimeter on a circle of diameter rad_circ_dosi
pos_dosi_sigma  = 0.01

if False : #old
    trans_z        = sample_u(50., 0.01)                            # z position of petale
else:
    trans_z=0.
e_plate,       e_plate_sig   = 2.01, 0.001


box_x_int_size = l_sampled_sillon_x.sum() + l_sampled_eprainure_x.sum()
box_x_ext_size = box_x_int_size+2*dim_epbox_x

box_y_int_size = dim_intbox_y + 2*dim_maxrainure_y
print(box_y_int_size)
box_y_ext_size = dim_intbox_y + 2*dim_epbox_y
box_z_int_size = lz
#box_z_ext_size = box_z_int_size+2*(dim_epbox_z-diff_z/2)
box_z_ext_size = box_z_int_size+2*dim_epbox_z

if False:                                                                           # TODO : un joli truc qui reconnait le type de reflecteur (Fe/Ni/Cr/SS) et adapte les dimentions
    e_rod_petale_bas_droite = 2.400-1.900
    e_rod_petale_haut_droite = 2.446-1.900
    e_rod_petale_vert = (e_rod_petale_bas_droite + e_rod_petale_haut_droite)/2

    e_rod_petale_haut_gauche = (2.552-1.900)
    e_rod_petale_hori = (e_rod_petale_haut_gauche + e_rod_petale_haut_droite)/2
else:

    e_rod_petale_bas_droite = 2.470-1.900
    e_rod_petale_haut_droite = 2.469-1.900
    e_rod_petale_vert = (e_rod_petale_bas_droite + e_rod_petale_haut_droite)/2

    e_rod_petale_haut_gauche = (2.600-1.900)
    e_rod_petale_hori = (e_rod_petale_haut_gauche + e_rod_petale_haut_droite)/2



dist_inter_meas_hori = 2.917 * 2**0.5 * 3
off_set_lateral = 0.0                                # offset, valeur positive -> en direction de la CI

#print (e_rod_petale_vert, e_rod_petale_hori)
#exit()

                                   
print("coucou",e_cale_edge_y)


angle_vert = np.arcsin(-(e_rod_petale_bas_droite  - e_rod_petale_vert)/(box_z_ext_size      /2))/(2*np.pi)*360  # a ajuster en fonction de la distance reelle entre les points de mesure
angle_hori = np.arcsin(-(e_rod_petale_haut_droite - e_rod_petale_hori)/(dist_inter_meas_hori/2))/(2*np.pi)*360

if True:
    angle_vert = 0
    angle_hori = 0


print("angle_vert", angle_vert)
print("angle_hori", angle_hori)


e_rod_petale = (e_rod_petale_vert + e_rod_petale_hori)/2
e_rod_petale = e_rod_petale_vert - (e_rod_petale_haut_droite-e_rod_petale_hori)




mat_petal, mat_interval, mat_boite, mat_protec = "mat_petale", "mat_port_dosi", "mat_boite","Al6012"    # choose the material composition name /"Air" "mat_protec"
if Crit_mode:
    mat_interval = "Air_PETALE"
mode_replace_mat = False                                    # activate the mode to replace the experiment by water (to update before use)
name_mat_replacement,mat_replacement = "toto_mat", "-0.9983 rgb 51 153 255 moder lwtr 1001 1001g0.0300c 0.6665 1002g0.0300c 0.0001 8016g0.0300c 0.3334"
if mode_replace_mat:
    mat_petal, mat_interval, mat_boite, mat_protec = name_mat_replacement,name_mat_replacement,name_mat_replacement,name_mat_replacement
'''list_dosi = [                                            # list of dosimeters
    ("Au", [(791970, [102   ])]),
    ("Ni", [(280580, [103   ])]),
    #("Ti", [(220460, [103   ]),(220480,[103])]),
    ("Fe", [(260540, [103   ]),(260560,[103])]),
    #("Mg", [(120240, [103   ])]),
    ("In", [(491150, [102,11004])]),    # 51
    #("Ag", [(471090, [102   ])]),        # 12102
    #("Co", [(270590, [102   ])]),
    #("Rh", [(451030, [11004])]),        # 51
    #("Vn", [(230510, [107])]),
    ("Al", [(130270, [107])]),
    #("Cu", [(290630, [102   ]),(290650,[102])]),
    ##("Mn", []),
]'''
'''list_dosi = [
    ("In", [(491150, [102,11004])]),    # 51
    ("In", [(491150, [102,11004])]),    # 51
    ("In", [(491150, [102,11004])]),    # 51
]'''


################################################################################################# DO NOT TOUCH PARAMETERS
pas_reseau_umet, radius_clad_ext = 2.917, 0.9675
################################################################################################# choose the material composition name


d_dosi_general = {
    "Ni":{"den":-8.908, "rgb":"181 182 181",   "compo":"28058g0.0300c 0.680769  28060g0.0300c 0.262234   28061g0.0300c 0.011399  28062g0.0300c 0.036345  28064g0.0300c 0.0092560"},
    "Ti":{"den":-4.510, "rgb":"182 175 169",   "compo":"22046g0.0300c 0.0825  22047g0.0300c 0.0744  22048g0.0300c 0.7372  22049g0.0300c 0.0541  22050g0.0300c 0.0518"}, # (3)  (2)  (3)  (2) (2)
    "Fe":{"den":-7.874, "rgb":"83  89  93 ",   "compo":"26054g0.0300c 0.05845 26056g0.0300c 0.91754 26057g0.0300c 0.02119 26058g0.0300c 0.00282        "}, # (35) (36) (20) (4)
    "Mg":{"den":-1.738, "rgb":"233 238 235",   "compo":"12024g0.0300c 0.7899  12025g0.0300c 0.1000  12026g0.0300c 0.1101                    "}, # (4)  (1)  (3)
    "In":{"den":-7.31 , "rgb":"119 136 153",   "compo":"49113g0.0300c 0.0429  49115g0.0300c 0.9571                            "}, # +-5% +-5%
    "Cu":{"den":-8.96 , "rgb":"184 115 51 ",   "compo":"29063g0.0300c 0.6915  29065g0.0300c 0.3085                            "}, # (15) (15)
    "Ag":{"den":-10.50, "rgb":"0   71  171",   "compo":"47107g0.0300c 0.51839 47109g0.0300c 0.48161                            "}, # (8)  (8)
    "Au":{"den":-19.3 , "rgb":"255 215 1  ",   "compo":"79197g0.0300c 1                                        "},
    "Co":{"den":-8.90 , "rgb":"0   71  171",   "compo":"27059g0.0300c 1                                         "},
    "Rh":{"den":-12.41, "rgb":"0   71  171",   "compo":"45103g0.0300c 1                                         "},
    "Vn":{"den":-6.0,   "rgb":"0   71  171",   "compo":"23050g0.0300c 0.0025  23051g0.0300c 0.9975                             "},
    "Al":{"den":-2.6989,"rgb":"0   71  171",   "compo":"13027g0.0300c 1                                         "},
    #"Mn":{"den":-7.47 ,"rgb":"36  45  54 ", "e_dosi":0.01, "compo":"25055g0.0300c 1                                        "},
}
# TODO : merger avec le dico general de utils_p4



#d_mat_plate = {             # old density computed from dimension and mass
#    "Ni":{"den":-8.888, "rgb":"100 100 100",   "compo":"28058g0.0300c 0.6827  28060g0.0300c 0.261   28061g0.0300c 0.0113  28062g0.0300c 0.0359  28064g0.0300c 0.0091"},
#    "Fe":{"den":-7.862, "rgb":"100 100 100",   "compo":"26054g0.0300c 0.05845 26056g0.0300c 0.91754 26057g0.0300c 0.02119 26058g0.0300c 0.00282        "}, # (35) (36) (20) (4)
#    "SS":{"den":-7.897,   "rgb":"100 100 100",   "compo":"24052g0.0300c -0.14206 24053g0.0300c -0.0152 24050g0.0300c -0.00274 28058g0.0300c -0.087138 \
#      28060g0.0300c -0.033565 28062g0.0300c -0.004666 28061g0.0300c -0.002631 \
#      12024g0.0300c -0.00008 12025g0.0300c -0.00001 12026g0.0300c -0.00001 \
#      25055g0.0300c -0.019 14028g0.0300c -0.0054 14029g0.0300c -0.0003 \
#      14030g0.0300c -0.0002 26054g0.0300c -0.03916 26056g0.0300c -0.63204 \
#      26057g0.0300c -0.0158"},
#    "Cr":{"den":-7.178,  "rgb":"100 100 100",   "compo":"24050g0.0300c 0.04345 24052g0.0300c 0.83789 24053g0.0300c 0.09501 24054g0.0300c 0.02365"},
#    }



d_mat_plate = {             # density computed from dimension and mass
    "Ni":{"den":-8.888, "rgb":"100 100 100",   "compo":"6000g0.0300c    -0.0001   14028g0.0300c    -0.000459368   14029g0.0300c    -2.41588E-05   14030g0.0300c    -1.64737E-05   25055g0.0300c    -0.0009   26054g0.0300c    -2.82278E-05   26056g0.0300c    -0.000459508   26057g0.0300c    -1.08018E-05   26058g0.0300c    -1.46272E-06   28058g0.0300c    -0.670626951   28060g0.0300c    -0.267220248   28061g0.0300c    -0.011810834   28062g0.0300c    -0.038276384   28064g0.0300c    -0.010065582"},
    "Fe":{"den":-7.862, "rgb":"100 100 100",   "compo":"5010g0.0300c    -5.50665E-07   5011g0.0300c    -2.44934E-06   6000g0.0300c    -0.00003   7014g0.0300c    -4.98039E-05   7015g0.0300c    -1.96139E-07   13027g0.0300c    -0.00004   14028g0.0300c    -3.67494E-05   14029g0.0300c    -1.9327E-06   14030g0.0300c    -1.31789E-06   16032g0.0300c    -2.55875E-05   16033g0.0300c    -2.07868E-07   16034g0.0300c    -1.20019E-06   16036g0.0300c    -4.41551E-09   19039g0.0300c    -2.78811E-05   19040g0.0300c    -3.57913E-09   19041g0.0300c    -2.1153E-06   23050g0.0300c    -2.44826E-08   23051g0.0300c    -9.97552E-06   24050g0.0300c    -6.6779E-06   24052g0.0300c    -0.000133919   24053g0.0300c    -1.54777E-05   24054g0.0300c    -3.92538E-06   25055g0.0300c    -0.0005   26054g0.0300c    -0.056385577   26056g0.0300c    -0.917875709   26057g0.0300c    -0.021576898   26058g0.0300c    -0.002921816   27059g0.0300c    -0.00002   28058g0.0300c    -0.000107515   28060g0.0300c    -4.28409E-05   28061g0.0300c    -1.89352E-06   28062g0.0300c    -6.13649E-06   28064g0.0300c    -1.61372E-06   29063g0.0300c    -6.85035E-05   29065g0.0300c    -3.14965E-05   33075g0.0300c    -0.00001   41093g0.0300c    -0.00001   42092g0.0300c    -4.17344E-06   42094g0.0300c    -2.68662E-06   42095g0.0300c    -4.69905E-06   42096g0.0300c    -4.99871E-06   42097g0.0300c    -2.90811E-06   42098g0.0300c    -7.46563E-06   42100g0.0300c    -3.06843E-06   50112g0.0300c    -1.8344E-07   50114g0.0300c    -1.2646E-07   50115g0.0300c    -6.56244E-08   50116g0.0300c    -2.83836E-06   50117g0.0300c    -1.5118E-06   50118g0.0300c    -4.8115E-06   50119g0.0300c    -1.71976E-06   50120g0.0300c    -6.58392E-06   50122g0.0300c    -9.50684E-07   50124g0.0300c    -1.20844E-06"}, # (35) (36) (20) (4)
    "SS":{"den":-7.897, "rgb":"100 100 100",   "compo":"6000g0.0300c    -0.00013   7014g0.0300c    -0.000896469   7015g0.0300c    -3.53051E-06   13027g0.0300c    -0.00004   14028g0.0300c    -0.003858688   14029g0.0300c    -0.000202934   14030g0.0300c    -0.000138379   16032g0.0300c    -7.58149E-05   16033g0.0300c    -6.15906E-07   16034g0.0300c    -3.55612E-06   16036g0.0300c    -1.3083E-08   19039g0.0300c    -0.000204462   19040g0.0300c    -2.6247E-08   19041g0.0300c    -1.55122E-05   22046g0.0300c    -1.58382E-06   22047g0.0300c    -1.45896E-06   22048g0.0300c    -1.4769E-05   22049g0.0300c    -1.10623E-06   22050g0.0300c    -1.08202E-06   24050g0.0300c    -0.007763057   24052g0.0300c    -0.155680814   24053g0.0300c    -0.017992872   24054g0.0300c    -0.004563257   25055g0.0300c    -0.0154   26054g0.0300c    -0.039884175   26056g0.0300c    -0.64925673   26057g0.0300c    -0.015262356   26058g0.0300c    -0.002066738   27059g0.0300c    -0.0004   28058g0.0300c    -0.05725192   28060g0.0300c    -0.022812791   28061g0.0300c    -0.0010083   28062g0.0300c    -0.003267683   28064g0.0300c    -0.000859306   29063g0.0300c    -0.000274014   29065g0.0300c    -0.000125986   41093g0.0300c    -0.00007   42092g0.0300c    -5.56459E-05   42094g0.0300c    -3.58217E-05   42095g0.0300c    -6.2654E-05   42096g0.0300c    -6.66494E-05   42097g0.0300c    -3.87749E-05   42098g0.0300c    -9.95418E-05   42100g0.0300c    -4.09124E-05   50112g0.0300c    -6.42041E-07   50114g0.0300c    -4.4261E-07   50115g0.0300c    -2.29686E-07   50116g0.0300c    -9.93427E-06   50117g0.0300c    -5.29129E-06   50118g0.0300c    -1.68403E-05   50119g0.0300c    -6.01915E-06   50120g0.0300c    -2.30437E-05   50122g0.0300c    -3.3274E-06   50124g0.0300c    -4.22955E-06"},
    "Cr":{"den":-7.178, "rgb":"100 100 100",   "compo":"6000g0.0300c    -0.00004   8016g0.0300c    -0.000189496   8017g0.0300c    -7.651E-08   8018g0.0300c    -4.27584E-07   13027g0.0300c    -0.00001   14028g0.0300c    -9.18735E-06   14029g0.0300c    -4.83175E-07   14030g0.0300c    -3.29473E-07   16032g0.0300c    -9.47686E-06   16033g0.0300c    -7.69882E-08   16034g0.0300c    -4.44515E-07   16036g0.0300c    -1.63537E-09   24050g0.0300c    -0.041720587   24052g0.0300c    -0.836667197   24053g0.0300c    -0.096698142   24054g0.0300c    -0.024524074   26054g0.0300c    -5.64556E-06   26056g0.0300c    -9.19015E-05   26057g0.0300c    -2.16037E-06   26058g0.0300c    -2.92544E-07   28058g0.0300c    -6.71971E-06   28060g0.0300c    -2.67756E-06   28061g0.0300c    -1.18345E-07   28062g0.0300c    -3.83531E-07   28064g0.0300c    -1.00858E-07   29063g0.0300c    -6.85035E-06   29065g0.0300c    -3.14965E-06   74180g0.0300c    -1.17262E-08   74182g0.0300c    -2.62256E-06   74183g0.0300c    -1.42442E-06   74184g0.0300c    -3.06604E-06   74186g0.0300c     -2.87526E-06"},
    }


d_mat_dim = { # doubt on Fe
    "FeA":{"ly":30.00169925	,"lz":30.0034825,"lx":2.0084, "path_vox":path_to_reflector_data+"fe/FE01sss_geom"},
    "FeB":{"ly":30.00274975	,"lz":29.9996925,"lx":2.0087, "path_vox":path_to_reflector_data+"fe/FE02sss_geom"},
    "FeC":{"ly":30.00536925	,"lz":30.003665	,"lx":2.0091, "path_vox":path_to_reflector_data+"fe/FE03sss_geom"},
    "FeD":{"ly":30.0017165	,"lz":30.0013035,"lx":2.0085, "path_vox":path_to_reflector_data+"fe/FE04sss_geom"},
    "FeE":{"ly":30.006507	,"lz":30.00468	,"lx":2.0097, "path_vox":path_to_reflector_data+"fe/FE05sss_geom"},
    "FeF":{"ly":30.0063065	,"lz":30.0032825,"lx":2.0081, "path_vox":path_to_reflector_data+"fe/FE06sss_geom"},
    "FeG":{"ly":30.00386275	,"lz":30.006179	,"lx":2.0085, "path_vox":path_to_reflector_data+"fe/FE07sss_geom"},
    "FeH":{"ly":30.00293075	,"lz":30.001774	,"lx":2.0092, "path_vox":path_to_reflector_data+"fe/FE10sss_geom"},
    "SSA":{"ly":30.0012255,"lz":30.001712,"lx":2.0020924, "path_vox":path_to_reflector_data+"ss/SS01sss_geom"},
    "SSB":{"ly":30.0041255,"lz":30.002701,"lx":2.0026534, "path_vox":path_to_reflector_data+"ss/SS02sss_geom"},
    "SSC":{"ly":30.0031488,"lz":30.002277,"lx":2.0046810, "path_vox":path_to_reflector_data+"ss/SS03sss_geom"},
    "SSD":{"ly":30.0029813,"lz":30.002075,"lx":2.0062302, "path_vox":path_to_reflector_data+"ss/SS04sss_geom"},
    "SSE":{"ly":30.0043188,"lz":30.003277,"lx":2.0085556, "path_vox":path_to_reflector_data+"ss/SS05sss_geom"},
    "SSF":{"ly":30.0012735,"lz":30.002089,"lx":2.0055335, "path_vox":path_to_reflector_data+"ss/SS06sss_geom"},
    "SSG":{"ly":30.0032905,"lz":30.003751,"lx":2.0030366, "path_vox":path_to_reflector_data+"ss/SS07sss_geom"},
    "SSH":{"ly":30.0042342,"lz":30.004586,"lx":2.0107494, "path_vox":path_to_reflector_data+"ss/SS08sss_geom"},
    "NiC":{"ly":30.001616,"lz":30.0018815,"lx":2.0127   , "path_vox":path_to_reflector_data+"ni/NI02sss_geom"},
    "NiB":{"ly":29.999899,"lz":30.000569 ,"lx":2.0084   , "path_vox":path_to_reflector_data+"ni/NI03sss_geom"},
    "NiD":{"ly":29.998748,"lz":29.998282 ,"lx":2.0121   , "path_vox":path_to_reflector_data+"ni/NI04sss_geom"},             #29.998282 
    "NiE":{"ly":29.99833 ,"lz":29.99791	,"lx":2.0105    , "path_vox":path_to_reflector_data+"ni/NI05sss_geom"},             #29.99791	 
    "NiA":{"ly":30.001688,"lz":30.0008145,"lx":2.0051   , "path_vox":path_to_reflector_data+"ni/NI06sss_geom"},
    "NiG":{"ly":30.002214,"lz":30.0016835,"lx":2.0072   , "path_vox":path_to_reflector_data+"ni/NI07sss_geom"},
    "NiH":{"ly":30.00012 ,"lz":30.0001955,"lx":2.0082   , "path_vox":path_to_reflector_data+"ni/NI08sss_geom"},
    "NiF":{"ly":30.001275,"lz":30.0018165,"lx":2.0118   , "path_vox":path_to_reflector_data+"ni/NI09sss_geom"},
    "CrC":{"ly":30.00501725,"lz":30.0070485,"lx":2.0109 , "path_vox":path_to_reflector_data+"cr/CR01sss_geom"},
    "CrB":{"ly":30.00383975,"lz":30.0060675,"lx":2.0082 , "path_vox":path_to_reflector_data+"cr/CR02sss_geom"},
    "CrA":{"ly":30.00400125,"lz":30.0026575,"lx":2.0046 , "path_vox":path_to_reflector_data+"cr/CR03sss_geom"},
    "CrD":{"ly":30.00670700,"lz":30.0053305,"lx":2.0062 , "path_vox":path_to_reflector_data+"cr/CR04sss_geom"},
    "CrE":{"ly":30.00873975,"lz":30.0074360,"lx":2.0090 , "path_vox":path_to_reflector_data+"cr/CR05sss_geom"},
    "CrF":{"ly":30.00400825,"lz":30.0049260,"lx":2.0043 , "path_vox":path_to_reflector_data+"cr/CR06sss_geom"},
    "CrG":{"ly":30.00645675,"lz":30.0083430,"lx":2.0074 , "path_vox":path_to_reflector_data+"cr/CR07sss_geom"},
    "CrH":{"ly":30.00548300,"lz":30.0043090,"lx":2.0090 , "path_vox":path_to_reflector_data+"cr/CR08sss_geom"},
}



# def den(dosi_mat):
#     val = -d_dosi[dosi_mat]["den"]
#     return val
    
#def radius_for_wgt(dosi_mat, masse):
#    return (masse/(den(dosi_mat)*d_dosi[dosi_mat]["e_dosi"]*pi))**0.5

#def get_wgt(dosi_mat):
#    return pi * d_dosi[dosi_mat]["l_dosi"]**2 * d_dosi[dosi_mat]["e_dosi"] * den(dosi_mat)

#def coord(r,ratio_angle):
#    #ratio_angle += 0.25
#    ratio_angle += 0.25/2
#    return r*np.cos(ratio_angle*2*pi) + sample_u(0,pos_dosi_sigma), r*np.sin(ratio_angle*2*pi) + sample_u(0,pos_dosi_sigma)

#def dist_coord(x1_y1,x2_y2):
#    (x1,y1),(x2,y2) = x1_y1,x2_y2
#    return ((x2-x1)**2+(y2-y1)**2)**0.5
    
def aff(o, n):
    return " "*(n-len(str(o))) + str(o)


def get_dosi_Pi_j(i,j):
    for nro, name in enumerate(data.l_pos_name):
        if name.startswith("P"):
            name_i, name_j = name[1:].split("_")
            if (str(i),str(j)) == (name_i,name_j):
                return {    "mat":data.l_mat[nro],
                            "name":data.l_name[nro],
                            "radius":data.l_radius[nro],
                            "th":data.l_thickness[nro],
                            "masse":data.l_masse[nro],
                            "den":data.l_masse[nro]/data.l_volume[nro]
                        }
    return None
'''
print(data.l_pos_name)
print(get_dosi_Pi_j(3,1))
print(get_dosi_Pi_j(3,2))
print(get_dosi_Pi_j(3,3))
print(get_dosi_Pi_j(3,4))
print(get_dosi_Pi_j(3,5))

exit()'''

#for elt, data in d_dosi.items():
#    print(elt, get_wgt(elt))


#n_dosi_circ = len(list_dosi)-1
#print ("nb dosi :",len(list_dosi), " in circle with 1+"+str(n_dosi_circ))
#if len(list_dosi)>2:
#    print ("rad_circ_dosi", rad_circ_dosi)
#    available_dist = dist_coord(coord(rad_circ_dosi,0), coord(rad_circ_dosi,1./n_dosi_circ))
#    print ("available_dist =", available_dist)
#    for (imat, imt) in list_dosi[1:]:
#        if d_dosi[imat]["l_dosi"]*2>available_dist:
#            print ("error:",imat, "dosimeter needs a space of",d_dosi[imat]["l_dosi"]*2)
#            exit()
#        if (d_dosi[imat]["l_dosi"]+d_dosi[list_dosi[0][0]]["l_dosi"])>rad_circ_dosi:
#            print ("error: ",d_dosi[imat]["l_dosi"],"+",d_dosi[list_dosi[0][0]]["l_dosi"],">",rad_circ_dosi)
#            exit()
#    print ("radius checked ok for all dosimeters")


######################################################################################### START INPUT GENERATION

list_xmin=[]
list_xmax=[]
list_ymin=[]
list_ymax=[]
list_zmin=[]
list_zmax=[]
for i in range(nb):  
    plate_letter="ABCDEFGH"[i]
    lz=d_mat_dim[ref_mat+plate_letter]["lz"]
    path_vox=d_mat_dim[ref_mat+plate_letter]["path_vox"]
    name_petale     = "s_petale_meta_"+str(i)
    name_air        = "s_petale_air2_"+str(i)
    name_sillon     = "s_petale_sillon_"+str(i)
    name_compl        = "s_petale_compl_"+str(i)
    name_petale_list.append(name_petale)
    l_path_vox.append(path_vox)
    if lattice_mod:
        f_vox=open(path_vox,"r")
        l_vox=f_vox.readlines()
        l_surf_raw=[]
        l_surf_cell=[]
        for line in l_vox:
            if "surf" in line: l_surf_raw += [line]
            elif "cell" in line: l_surf_cell += [line]
        z_min=[float(l_surf_raw[0].split()[7])] if float(l_surf_raw[0].split()[7])<0.1  else []
        for voxel in l_surf_raw:
            voxel=voxel.split()
            voxel[8] = float(voxel[8]) -lz/2 -np.mean(z_min)
            if lattice_mod:
                if "X0" in voxel[1] :
                   list_zmax+=[voxel[8]]
                if "X1" in voxel[1]:
                   list_zmax[-1]=voxel[8]

#corrections position des feuilles, cales different à gauche (0.8 mm) et à droite (0.5mm)
corr_sheets_cale=0.015
cales_width=0.13 #sum of the two cale width


overall_max_z=max(list_zmax)

print(overall_max_z)



#Correction des rotations du casier 
def f_lin(X,a,b):
    s=[]
    for x in X:
        s+=[(a)*x+b] # 1/a is more appropriate
    return s

#loading of petale position data
diam_rod     =np.array(data.l_petale_meas_rod_d[1:-1]) # rod_diameter 3x6
height_petale=np.array(data.l_petale_height_meas)
face_meas    =np.array(data.l_petale_face_meas)
side_meas    =np.array(data.l_petale_side_meas)
meas_pos_h   =np.array(data.l_petale_meas_pos_h    )
meas_pos_lat =np.array(data.l_petale_meas_pos_lat  )
rod_deflection =np.array(data.l_petale_deflection_rod  )*0  #just all 0 if no pert
s=0
sd=0
if pert_position: #random sampling on measured param
    s=0.01 #mm regle
    # sd=0.4 # deplacemnt estimé dans l'eau
    # sd=1 # deplacemnt estimé dans l'eau conservateur
    diam_rod     = do_for_all(sample_d,diam_rod     ,s)
    # print(height_petale,s)
    height_petale= do_for_all(sample_d,height_petale,s)
    face_meas    = do_for_all(sample_d,face_meas    ,s)
    side_meas    = do_for_all(sample_d,side_meas    ,s)
    meas_pos_h   = do_for_all(sample_d,meas_pos_h   ,s)
    meas_pos_lat = do_for_all(sample_d,meas_pos_lat ,s)
    rod_deflection =do_for_all(sample_d,rod_deflection ,np.array(data.l_petale_deflection_rod))


#cst distance value for surface def
d_min_casier=sample_d(0,sd) #Valeur de base 0 , peut changer avec la metro du casier
h_min_casier=box_z_ext_size/2 #distance between 0 and the bottom of the case for the cuboid definition (not the actual height), peut changer avec la metro du casier


diam_corr=np.transpose([(diam_rod[:,2*i]+diam_rod[:,2*i+1])/2 for i in range(3)])
rod_deflection =np.transpose([(rod_deflection[2*i,:]+rod_deflection[2*i+1,:])/2 for i in range(3)])
m_x_zx=np.add(np.subtract(face_meas,diam_corr),rod_deflection)  #list of absice values for fit zx 3x3x3
print("m_x_zx")
print(m_x_zx)
m_y_zy=side_meas  #list of absice values for fit zy 3x2
m_x_yx=np.add(np.subtract(face_meas,diam_corr),rod_deflection) #list of absice values for fit yx 3x3x3 

m_z_zx=np.r_['0,3',meas_pos_h,meas_pos_h,meas_pos_h]  #list of ordonne values for fit zx 3x3
m_z_zy=np.delete(meas_pos_h,1,axis=1)  #list of ordonne values for fit zy 3x3
m_y_yx=np.r_['0,2',meas_pos_lat,meas_pos_lat,meas_pos_lat]  #list of ordonne values for fit yx 3x1
m_y_yx=np.r_['0,3',m_y_yx,m_y_yx,m_y_yx]  #list of ordonne values for fit yx 3x1

# print(m_z_zx)
# print(m_z_zy)
# print(m_y_yx)

m_face_corr=0 # correction for the face inhomogeneity, to be 3x3x3
m_side_corr=0 # correction for the side inhomogeneity, to be 3x1


def x_plane(X,b,c,d): #X must be Nx(y,z)
    s=[]
    for x in X:
        s=[b*x[0]+c*x[1]+d]
    return s


def face_fit(vals_yz,vals_x):
    coef, coef_s=curve_fit(x_plane,vals_yz,vals_x,sigma=[0.05]*len(vals_x),p0=[0,0.01,0])
    return coef, coef_s 

tmp_pitch=29.17

vals_yz=[[-3*np.sqrt(2)*tmp_pitch,679],[0,679],[3*np.sqrt(2)*tmp_pitch,677.5],
         [-3*np.sqrt(2)*tmp_pitch,529],[0,529],[3*np.sqrt(2)*tmp_pitch,529],
         [-3*np.sqrt(2)*tmp_pitch,409],[0,409],[3*np.sqrt(2)*tmp_pitch,409]]*3

vals_y =[-3*np.sqrt(2)*tmp_pitch,0,3*np.sqrt(2)*tmp_pitch,
         -3*np.sqrt(2)*tmp_pitch,0,3*np.sqrt(2)*tmp_pitch,
         -3*np.sqrt(2)*tmp_pitch,0,3*np.sqrt(2)*tmp_pitch]*3



vals_z =[679,679,677.5,
         529,529,529,
         409,409,409]*3

print(np.mean(height_petale[1,:]))
# offset_x = -np.mean(m_x_zx[1,1,:]) #offset measured with respect to the expected position (careful of e_rod_petale)
offset_y = -np.mean((m_y_zy[:,1]-m_y_zy[:,0])/2) #offset measured with respect to the expected position 
offset_z = np.mean(height_petale[1,:])-27  #offset measured with respect to the expected position+correction for the geometry definition minus the distnave between the grid and the plate

cplane, cplane_s=face_fit(vals_yz,m_x_zx.flatten())

offset_x= x_plane([(offset_y,offset_z+abs(h_min_casier)*10)],*cplane)
print(offset_x)
print((offset_y,offset_z+abs(h_min_casier)*10))
print(vals_yz)
print(m_x_zx.flatten())
print(cplane)



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(m_x_zx.flatten(), vals_y, vals_z, s=50, color='k', marker='o', linewidth=None, alpha=1)
ax.set_xlabel("x")
# ax.plot_surface(X, Y, Z)
fig.tight_layout()

from skspatial.objects import Plane, Points # type: ignore 

l_point=[]
for i in range(len(vals_yz)):
    l_point+=[[m_x_zx.flatten()[i]]+vals_yz[i]]


points = Points(l_point)

plane = Plane.best_fit(points)
# print(points[:,1])

# plot_3d(
#     points.plotter(c='k', s=50, depthshade=False),
#     plane.plotter(alpha=0.2), lims_x=(-7, 7),lims_y=(-1, 1))
XY=Plane([0,0,350],[0,0,1])

inter_line=plane.intersect_plane(XY)
fig=plt.figure()
ax2=fig.add_subplot(111,projection="3d")
plane.plot_3d(ax2,alpha=0.2,lims_y=(-150,150))
points.plot_3d(ax2)
inter_line.plot_3d(ax2,-200,200,color="r")
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_zlim(350,700)
ax2.set_xlim(min(points[:,0])-0.1,max(points[:,0])+0.1)

coef=plane.cartesian()

offset_x= x_plane([(offset_y,offset_z+abs(h_min_casier)*10)],-coef[1]/coef[0],-coef[2]/coef[0],-coef[3]/coef[0])
offset_x=offset_x[0]
print(offset_x)

print("normal vector norm")
print(np.linalg.norm(coef[:-1]))
print("normal vector after 45 degree rotation")
mat = np.array([[np.cos(-np.pi/4),-np.sin(-np.pi/4),0],
                [np.sin(-np.pi/4),np.cos(-np.pi/4) ,0],
                [0               ,0                 ,1]])
print(mat.dot(coef[:-1]))


print("cos(angles)")
print(abs(coef[0])/np.sqrt(coef[0]*coef[0]+coef[1]*coef[1]+coef[2]*coef[2]))
print(abs(coef[1])/np.sqrt(coef[0]*coef[0]+coef[1]*coef[1]+coef[2]*coef[2]))
print(abs(coef[2])/np.sqrt(coef[0]*coef[0]+coef[1]*coef[1]+coef[2]*coef[2]))


if do_plot: plt.show()

# exit() # marche pas

offset_x =offset_x/10.# mm to cm
offset_y =offset_y/10. # mm to cm
offset_z =offset_z/10. +abs(h_min_casier)# mm to cm A verifier


m_y_zy= np.c_[-m_y_zy[:,0],m_y_zy[:,1]]  # correction due tu the measurment method which gives two y-axis of opposite direction

# mean_x0_z =[[np.mean(m_x_zx[:,2,:],axis=0).tolist()]*3]*3                       # get min value of first point to allow simultanate fitting
# mean_x0_y =[np.transpose([np.mean(m_x_zx[:,0,:],axis=1).tolist()]*3).tolist()]*3 # get min value of first point to allow simultanate fitting
# mean_y_z =[np.mean(m_y_zy,axis=0).tolist()]*3 # get mean value of first point to allow simultanate fitting

# print(mean_y_z)
l_x_zx = np.transpose(m_x_zx- m_face_corr,[2,0,1])
l_y_zy = (m_y_zy- m_side_corr).T
l_x_yx = np.transpose(m_x_yx- m_face_corr,[1,0,2])

# print(np.subtract(m_y_zy,mean_y_z))

l_z_zx = np.transpose(m_z_zx,[2,0,1])
l_z_zy = m_z_zy.T
l_y_yx = np.transpose(m_y_yx,[1,0,2])

# print(face_meas)
# print(np.transpose(face_meas,[2,0,1]))
# print(np.transpose(face_meas,[2,0,1]))
# print(np.transpose(face_meas,[1,0,2]))
# print(np.transpose(m_y_yx,[1,0,2]))
# print(np.transpose(m_z_zx,[2,0,1]))
# print(np.array(mean_x0_z))
# print(diam_corr)
# print(rod_deflection)
# print(m_x_zx)
print(m_x_zx)
print(m_y_zy)
# exit()
fitzx = np.mean(list(map(lambda X,Y : curve_fit(f_lin,X.flatten(),Y.flatten())[0][0],l_z_zx,-l_x_zx))) # sigma as no impact if same for all values
fitzy = np.mean(list(map(lambda X,Y : curve_fit(f_lin,X.flatten(),Y.flatten())[0][0],l_z_zy,l_y_zy))) # sigma as no impact if same for all values
fityx = np.mean(list(map(lambda X,Y : curve_fit(f_lin,X.flatten(),Y.flatten())[0][0],l_y_yx,-l_x_yx))) # sigma as no impact if same for all values



print(fitzx)
print(fitzy)
print(fityx)

alpha=np.arctan(1/fitzx)   if fitzx>0 else (np.pi+np.arctan(1/fitzx)) 
beta =np.arctan(1/fitzy)   if fitzy>0 else (np.pi+np.arctan(1/fitzy))
gamma=np.arctan(1/fityx)   if fityx>0 else (np.pi+np.arctan(1/fityx))

print("angle casier")
print(alpha*180/np.pi)
print(beta *180/np.pi)
print(gamma*180/np.pi)

phi=np.pi/2-alpha  #y-axis rotation
theta=np.pi/2-beta #x-axis rotation
nu=np.pi/2-gamma   #z-axis rotation
print("angle rota serpent")
print(phi)
print(theta)
print(nu)

dz_corr_zx=d_min_casier*np.sin(phi) #correction for the z translation if r!=0
dx_corr_zx=d_min_casier*(1-np.cos(phi)) #correction for the x translation if r!=0
dz_corr_zy=0 # zero cause definitions are centred along the x axis so no translation
dy_corr_zy=0 # zero cause definitions are centred along the x axis so no translation
dy_corr_yx=d_min_casier*np.sin(nu) #correction for the z translation if r!=0
dx_corr_yx=d_min_casier*(1-np.cos(nu)) #correction for the x translation if r!=0

#Serpent rotation linked correction (rotation with respectto the origin) 
Delta_x_corr=(dx_corr_zx+dx_corr_yx)
Delta_y_corr=(dy_corr_zy+dy_corr_yx)
Delta_z_corr=(dz_corr_zx+dz_corr_zy)


#Serpent inputs starts

bloc_surf_raw   = ["","",""]
bloc_surf_trans = ["","","",""]
bloc_surf_cell  = ["","",""]
bloc_mat = ""
bloc_det = "set mat_matrix_rr\n"


def create_plate(i, pos_x, large_x):
    plate_letter="ABCDEFGH"[i]
    path_vox=d_mat_dim[ref_mat+plate_letter]["path_vox"]
    print()
    print()
    sample_sillon_y_gauche = sample_u(dim_sillon_y, dim_sillon_y_sig)
    sample_sillon_y_droite = sample_u(dim_sillon_y, dim_sillon_y_sig)
    
    # print(sample_sillon_y_gauche, sample_sillon_y_droite)
    decalage_y_sillon_a_sillon = (sample_sillon_y_droite-sample_sillon_y_gauche)/2 # incertitude sur la profondeur des scillions
    name_separator1, name_separator2="","" 
    if True:
        name_separator1, name_separator2 = "s_petale_sep_"+str(i), "s_petale_sep_"+str(i+1)
    if not do_voxel : 
        name_petale     = "s_petale_meta_"+str(i)
        ly=d_mat_dim[ref_mat+plate_letter]["ly"]
        lz=d_mat_dim[ref_mat+plate_letter]["lz"]
    else:#import of the voxelized reflector
        f_vox=open(path_vox,"r")
        l_vox=f_vox.readlines()
        l_surf_raw=[]
        l_surf_cell=[]
        for line in l_vox:
            if "surf" in line: l_surf_raw += [line]
            elif "cell" in line: l_surf_cell += [line]
        ref_union="("+l_surf_raw[0].split()[1]
        x_min=[float(l_surf_raw[0].split()[3])] if float(l_surf_raw[0].split()[3])<0.1  else []
        x_max=[float(l_surf_raw[0].split()[4])] if float(l_surf_raw[0].split()[4])>1.9 else []
        y_min=[float(l_surf_raw[0].split()[5])] if float(l_surf_raw[0].split()[5])<0.1  else []
        y_max=[float(l_surf_raw[0].split()[6])] if float(l_surf_raw[0].split()[6])>29.9 else []
        z_min=[float(l_surf_raw[0].split()[7])] if float(l_surf_raw[0].split()[7])<0.1  else []
        z_max=[float(l_surf_raw[0].split()[8])] if float(l_surf_raw[0].split()[8])>29.9 else []
        for voxel in l_surf_raw[1:]:
            ref_union+=" "+voxel.split()[1]
            if float(voxel.split()[3])<0.1 : x_min+=[float(voxel.split()[3])] 
            if float(voxel.split()[4])>1.9: x_max+=[float(voxel.split()[4])] 
            if float(voxel.split()[5])<0.1 : y_min+=[float(voxel.split()[5])] 
            if float(voxel.split()[6])>29.9: y_max+=[float(voxel.split()[6])] 
            if float(voxel.split()[7])<0.1 : z_min+=[float(voxel.split()[7])] 
            if float(voxel.split()[8])>29.9: z_max+=[float(voxel.split()[8])] 
        
        ref_union+=")"
        name_petale     = "s_petale_meta_"+str(i)
    name_air        = "s_petale_air2_"+str(i)
    name_sillon     = "s_petale_sillon_"+str(i)
    
    
    if not do_voxel: sampled_e_plate        = sample_u(d_mat_dim[ref_mat+plate_letter]["lx"], e_plate_sig)
    else:
        sampled_e_plate        =sample_u(np.mean(x_max)-np.mean(x_min), e_plate_sig)
        ly=np.mean(y_max)-np.mean(y_min)
        lz=np.mean(z_max)-np.mean(z_min)
    if pert_position:
        sampled_declage_plaque_portedosi  = sample_u(0,(large_x-sampled_e_plate)/2)
    else:
        sampled_declage_plaque_portedosi = tmp_disp[i] #to avoid steel superposition with pdosi
    sampled_declage_plaque_box = sample_u(corr_sheets_cale,(dim_intbox_y + sample_sillon_y_gauche + sample_sillon_y_droite -(np.max(y_max)-np.min(y_min)) -cales_width)/2)
    # print(sampled_declage_plaque_box)
    global l_max_x_sheets
    global l_min_x_sheets
    
    
    # print(sampled_e_plate)
    if do_voxel: print(np.mean(x_min))
    if False:
        sens = 1 if i%2==0 else -1
        sens = 0
        sampled_declage_plaque_box = sens*(dim_intbox_y + sample_sillon_y_gauche + sample_sillon_y_droite -(np.max(y_max)-np.min(y_min)))/2    # WARNING
        print("coucou", sampled_declage_plaque_box)
        print(dim_intbox_y , sample_sillon_y_gauche , sample_sillon_y_droite  , ly)
    
    if not do_voxel : 
        print("Voxelization obliged in petale_23 and later: exit")
        exit()
        l_max_x_sheets+=[-(pos_x-sampled_e_plate/2)-(trans_x+sampled_declage_plaque_portedosi)]
        l_min_x_sheets+=[-(pos_x+sampled_e_plate/2)-(trans_x+sampled_declage_plaque_portedosi)]
    
        bloc_surf_raw[0]  += "surf "+name_sillon+" cuboid -"+str(pos_x+large_x/2)            +"  -"+str(pos_x-large_x/2)            +" -"+str(box_y_int_size/2)    +" "+str(box_y_int_size/2)+" -"+str(lz/2)+" "+str(lz/2)+"\n"
        bloc_surf_trans[0]+= "strans "+name_sillon+" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
        bloc_surf_cell[0] += "cell c_"+name_sillon[2:]+" u_refl "+mat_boite+" -"+name_sillon+" "+name_air+" \n" # -s_petale_box2
        
        bloc_surf_raw[2]  += "surf   "+name_air       +" cuboid -"+str(pos_x+large_x/2) +"  -"+str(pos_x-large_x/2)         +" -"+str(dim_intbox_y/2+sample_sillon_y_gauche)    +" "+str(dim_intbox_y/2+sample_sillon_y_droite)+" -"+str(lz/2)+" "+str(lz/2)+"\n"
        bloc_surf_trans[2]+= "strans "+name_air       +" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
        bloc_surf_cell[2] += "cell   c_"+name_air[2:] +" u_refl Air_PETALE -"+name_air +" "+name_petale+" -"+name_sillon+" \n"# -s_petale_box2 +" "+name_aira+" "+name_airb
       
        bloc_surf_raw[2]  += "surf "+name_petale   +" cuboid -"+str(pos_x+sampled_e_plate/2)         +"  -"+str(pos_x-sampled_e_plate/2)         +" -"+str(ly/2)    +" "+str(ly/2)+" -"+str(lz/2)+" "+str(lz/2)+"\n"
        bloc_surf_trans[2]+= "strans "+name_petale+" "+str(0+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
        bloc_surf_cell[2] += "cell c_"+name_petale[2:]   +" u_refl "+mat_petal   +" -"+name_petale +" \n"# -s_petale_box2
        print(trans_x,sampled_declage_plaque_portedosi,pos_x,sampled_e_plate/2)
        if lz > 30:
            global name_supl
            name_supl += " "+name_petale
    else:
        if not lattice_mod:    
            bloc_surf_raw[0]  += "surf "+name_sillon+" cuboid -"+str(pos_x+large_x/2)            +"  -"+str(pos_x-large_x/2)            +" -"+str(box_y_int_size/2)    +" "+str(box_y_int_size/2)+" -"+str(box_z_int_size/2)+" "+str(box_z_int_size/2)+"\n"
            bloc_surf_trans[0]+= "strans "+name_sillon+" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
            bloc_surf_cell[0] += "cell c_"+name_sillon[2:]+" u_refl "+mat_boite+" -"+name_sillon+" "+ref_union+" "+name_air+" \n" # -s_petale_box2
            
            # bloc_surf_raw[2]  += "surf   "+name_air       +" cuboid -"+str(pos_x+large_x/2) +"  -"+str(pos_x-large_x/2)         +" -"+str(dim_intbox_y/2+sample_sillon_y_gauche)    +" "+str(dim_intbox_y/2+sample_sillon_y_droite)+" -"+str(lz/2)+" "+str(lz/2)+"\n"
            bloc_surf_raw[2]  += "surf   "+name_air       +" cuboid -"+str(pos_x+large_x/2) +"  -"+str(pos_x-large_x/2)         +" -"+str(dim_intbox_y/2+sample_sillon_y_gauche)    +" "+str(dim_intbox_y/2+sample_sillon_y_droite)+" -"+str(box_z_int_size/2)+" "+str(box_z_int_size/2)+"\n"
            # bloc_surf_raw[2]  += "surf   "+name_air       +" cuboid -"+str(pos_x+large_x/2) +"  -"+str(pos_x-large_x/2)         +" -"+str(box_y_int_size/2)    +" "+str(box_y_int_size/2)+" -"+str(30/2)+" "+str(30/2)+"\n"
            # print("surf   "+name_air       +" cuboid -"+str(pos_x+large_x/2) +"  -"+str(pos_x-large_x/2)         +" -"+str(dim_intbox_y/2+sample_sillon_y_gauche)    +" "+str(dim_intbox_y/2+sample_sillon_y_droite)+" -"+str(lz/2)+" "+str(lz/2)+"\n")
            bloc_surf_trans[2]+= "strans "+name_air       +" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
            bloc_surf_cell[2] += "cell   c_"+name_air[2:] +" u_refl Air_PETALE -"+name_air +" "+ref_union+" -"+name_sillon+" \n"# -s_petale_box2 +" "+name_aira+" "+name_airb
        list_xmin=[]
        list_xmax=[]
        list_ymin=[]
        list_ymax=[]
        list_zmin=[]
        list_zmax=[]
        list_univers=[]
        # print(y_min)
        # print(ly)
        for voxel in l_surf_raw:
            if ((float(voxel.split()[-2])<0)or(float(voxel.split()[-1])>30)) and (not lattice_mod):name_supl+=" "+voxel.split()[1]
            voxel=voxel.split()
            voxel[3] = float(voxel[3]) -(+pos_x+sampled_e_plate/2+np.mean(x_min)) 
            voxel[4] = float(voxel[4]) -(+pos_x+sampled_e_plate/2+np.mean(x_min)) 
            voxel[5] = float(voxel[5]) +(-ly/2-np.mean(y_min)) 
            voxel[6] = float(voxel[6]) +(-ly/2-np.mean(y_min)) 
            voxel[7] = float(voxel[7]) -lz/2 -np.mean(z_min) 
            voxel[8] = float(voxel[8]) -lz/2 -np.mean(z_min)
            if lattice_mod:
                if "X0" in voxel[1] :
                   list_xmin+=[voxel[3]]
                   list_xmax+=[voxel[4]]
                   list_ymin+=[voxel[5]]
                   list_ymax+=[voxel[6]]
                   list_zmin+=[voxel[7]]
                   list_zmax+=[voxel[8]]
                   list_univers+=[voxel[1][2:7]+voxel[1][9:]]
                if "X2" in voxel[1]:
                   list_xmax[-1]=voxel[4]
                   # print(voxel[4])
                if "X1" in voxel[1]:
                   list_ymin[-1]=voxel[5]
                   list_ymax[-1]=voxel[6]
                   list_zmin[-1]=voxel[7]
                   list_zmax[-1]=voxel[8]
                # print(list_ymin)
            else:
                voxel=lmap(lambda i:str(i),voxel)
                voxel= " ".join(voxel)
                # bloc_surf_raw[2]  += voxel 
                bloc_surf_raw[2]  += voxel+"\n" 
                # bloc_surf_trans[2]+= "strans "+voxel.split()[1]+" -"+str(trans_x+sampled_declage_plaque_portedosi+dim_prtdosi_x+pos_x+sampled_e_plate/2+np.mean(x_min)+0.0075)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box-ly/2-np.mean(y_min)+0.1)+" "+str(trans_z-lz/2 -np.mean(z_min))+" 0 0 "+rot_angle+"\n" #The pos_x, +1 and -15 are recentering the plate as the voxels are defined from (0,0,0) to (lx,ly,lz) instead of (px-lx/2,ly/2,lz/2) to (px+lx/2,ly/2,lz/2)
                bloc_surf_trans[2]+= "strans "+voxel.split()[1]+" -"+str(trans_x+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n" #The pos_x, +1 and -15 are recentering the plate as the voxels are defined from (0,0,0) to (lx,ly,lz) instead of (px-lx/2,ly/2,lz/2) to (px+lx/2,ly/2,lz/2)
                # if plate_letter=="D":print(trans_x,sampled_declage_plaque_portedosi,pos_x,1)                                            #+min(x_min) +dim_prtdosi_x
        if one_block: 
            bloc_surf_cell[2] += "cell c_"+name_petale[2:]   +" u_refl "+mat_petal   +" -"+ref_union +" \n"# Create only one cell
            if pert_position:print("Warning: perturbation compatibility with this mod not tested")
            l_max_x_sheets+=[-np.inf]
            l_min_x_sheets+=[np.inf]
        elif lattice_mod:
            
            l_max_x_sheets+=[max(list_xmax)+(sampled_declage_plaque_portedosi)]
            l_min_x_sheets+=[min(list_xmin)+(sampled_declage_plaque_portedosi)]
            print("disp: %f" %(sampled_declage_plaque_portedosi))
            bloc_surf_cell[2] += "lat l_"+l_surf_raw[0].split()[1][2:7]+" 11 "+str(-(pos_x))+" 0 0  1 11 11 3 3.3 3.3"
            
            for i in range(11):
              for j in range(11):
                I=str(i)
                J=str(j)
                bloc_surf_cell[2] += " "+l_surf_raw[0].split()[1][2:7]+"Y"+J+"Z"+I
                             
            bloc_surf_cell[2] +="\n"
            bloc_surf_trans[3]+= "utrans l_"+l_surf_raw[0].split()[1][2:7]+" "+str(sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
            
            bloc_surf_raw[0]  += "surf "+name_sillon+" cuboid -"+str(pos_x+large_x/2)            +"  -"+str(pos_x-large_x/2)            +" -"+str(box_y_int_size/2)    +" "+str(box_y_int_size/2)+" -"+str(box_z_int_size/2)+" "+str(overall_max_z+1)+"\n"
            bloc_surf_trans[0]+= "strans "+name_sillon+" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
            bloc_surf_cell[0] += "cell c_"+name_sillon[2:]+" u_refl "+mat_boite+" -"+name_sillon+" "+name_petale+" "+name_air+" \n" # -s_petale_box2
            
            bloc_surf_raw[2]  += "surf   "+name_air       +" cuboid -"+str(pos_x+large_x/2) +"  -"+str(pos_x-large_x/2)         +" -"+str(dim_intbox_y/2+sample_sillon_y_gauche)    +" "+str(dim_intbox_y/2+sample_sillon_y_droite)+" -"+str(box_z_int_size/2+1)+" "+str(overall_max_z+1)+"\n"
            bloc_surf_trans[2]+= "strans "+name_air       +" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
            bloc_surf_cell[2] += "cell   c_"+name_air[2:] +" u_refl Air_PETALE -"+name_air +" "+name_petale+" "+name_separator1+" "+name_separator2+" -"+name_sillon+"  \n"# -s_petale_box2 +" "+name_aira+" "+name_airb
            # print(min(list_xmin), -(pos_x+large_x/2))
            # print(max(list_xmax), -(pos_x-large_x/2))
            
            bloc_surf_raw[2]  += "surf "+name_petale   +" cuboid "+str(min(list_xmin))         +"  "+str(max(list_xmax))         +" "+str(min(list_ymin))    +" "+str(max(list_ymax))+" "+str(min(list_zmin))+" "+str(max(list_zmax))+"\n"
            bloc_surf_trans[2]+= "strans "+name_petale+" "+str(0+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
            bloc_surf_cell[2] += "cell c_"+name_petale[2:]   +" u_refl fill=l_"+l_surf_raw[0].split()[1][2:7]+" -"+name_petale +" "+name_separator1+" "+name_separator2+" \n"# Create only one cell
            it=0
            for xmin,xmax,ymin,ymax,zmin,zmax,uni in zip(list_xmin,list_xmax,list_ymin,list_ymax, list_zmin, list_zmax, list_univers):
                bloc_surf_raw[2] +="surf px1_"+uni+" px "+str(xmin+pos_x)+" \n"
                # bloc_surf_trans[2] +="strans px1_"+uni+" -"+str(trans_x+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                bloc_surf_raw[2] +="surf px2_"+uni+" px "+str(xmax+pos_x)+" \n"
                # bloc_surf_trans[2] +="strans px2_"+uni+" -"+str(trans_x+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                
                cell_def_in="cell c_"+uni+" "+uni+" mat_petale " + " px1_"+uni+" -px2_"+uni
                cell_def_out1="cell c_"+uni+"1_A "+uni+" Air_PETALE " + " -px1_"+uni
                cell_def_out2="cell c_"+uni+"2_A "+uni+" Air_PETALE " +" px2_"+uni
                cell_def_out3=""
                cell_def_out4=""
                cell_def_out5=""
                cell_def_out6=""
                # print(ymin)
                if ymin < -ly/2+0.1:
                    it+=1
                    bloc_surf_raw[2] +="surf py1_"+uni+" py "+str(ymin)+" \n"
                    # bloc_surf_trans[2] +="strans py1_"+uni+" -"+str(trans_x+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                    cell_def_in+=" py1_"+uni
                    cell_def_out3+="cell c_"+uni+"3_A "+uni+" Air_PETALE " + " px1_"+uni+" -px2_"+uni +" -py1_"+uni
                if ymax > ly/2-0.1:
                    it+=1
                    bloc_surf_raw[2] +="surf py2_"+uni+" py "+str(ymax)+" \n"
                    # bloc_surf_trans[2] +="strans py2_"+uni+" -"+str(trans_x+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                    cell_def_in+=" -py2_"+uni
                    cell_def_out4+="cell c_"+uni+"4_A "+uni+" Air_PETALE " + " px1_"+uni+" -px2_"+uni +" py2_"+uni
                if zmin < -lz/2+0.1:
                    it+=1
                    bloc_surf_raw[2] +="surf pz1_"+uni+" pz "+str(zmin)+" \n"
                    # bloc_surf_trans[2] +="strans pz1_"+uni+" -"+str(trans_x+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                    cell_def_in+=" pz1_"+uni
                    cell_def_out5+="cell c_"+uni+"5_A "+uni+" Air_PETALE " + " px1_"+uni+" -px2_"+uni +" -pz1_"+uni
                    if cell_def_out3: cell_def_out5+= " py1_"+uni
                    if cell_def_out4: cell_def_out5+= " -py2_"+uni
                if zmax > lz/2-0.1:
                    it+=1
                    bloc_surf_raw[2] +="surf pz2_"+uni+" pz "+str(zmax)+" \n"
                    # bloc_surf_trans[2] +="strans pz2_"+uni+" -"+str(trans_x+sampled_declage_plaque_portedosi)+" "+str(decalage_y_sillon_a_sillon+sampled_declage_plaque_box)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                    cell_def_in+=" -pz2_"+uni
                    cell_def_out6+="cell c_"+uni+"6_A "+uni+" Air_PETALE " + " px1_"+uni+" -px2_"+uni +" pz2_"+uni
                    if cell_def_out3: cell_def_out6+= " py1_"+uni
                    if cell_def_out4: cell_def_out6+= " -py2_"+uni
                    
                bloc_surf_cell[2] += cell_def_in +" \n"
                bloc_surf_cell[2] += cell_def_out1+" \n"
                bloc_surf_cell[2] += cell_def_out2+" \n"
                if cell_def_out3: bloc_surf_cell[2] += cell_def_out3+" \n"
                if cell_def_out4: bloc_surf_cell[2] += cell_def_out4+" \n"
                if cell_def_out5: bloc_surf_cell[2] += cell_def_out5+" \n"
                if cell_def_out6: bloc_surf_cell[2] += cell_def_out6+" \n"
            # print(it)
        else:
            l_max_x_sheets+=[-np.inf]
            l_min_x_sheets+=[np.inf]
            if pert_position:print("Warning: perturbation compatibility with this mod not tested")
            for c_voxel in l_surf_cell:
                bloc_surf_cell[2] += c_voxel
        # print(dim_prtdosi_x+np.mean(x_min)+0.0075)
        # print(dim_prtdosi_x,np.mean(x_min),0.0075)
        # print(trans_x,sampled_declage_plaque_portedosi,dim_prtdosi_x,pos_x,sampled_e_plate/2,np.mean(x_min),0.0075)
    
    # if lz > 30:
        # global name_supl
        # name_supl += " "+name_petale
    
    
    
    
    
'''
        dim_prtdosi_y,   dim_prtdosi_y_sig    = 29.75, 0.005
        dim_prtdosi_x                = 0.15
        dim_epbox_x                = 1.0
        dim_epbox_y                = 1.0
        dim_epbox_z                = 2.0
        dim_sillon_y,    dim_sillon_y_sig    = 0.19 , 0.01
        dim_intbox_x,    dim_intbox_x_sig    = 17.75, 0.005
        dim_intbox_y,    dim_intbox_y_sig    = 29.85, 0.005                         # attention, c est sans la hauteur rainures
        dim_eprainure_x, dim_eprainure_x_sig    = 0.165, 0.005
        dim_rainure2rainure_x                      = 2.015+0.165                         # todo : pb topo sur le cumul des incertitudes

        l_sampled_eprainure_x = np.array([sample_u(dim_eprainure_x, dim_eprainure_x_sig) for i in range(nb+1)])
        l_x_mid_rainure = np.arange(nb+1) * dim_rainure2rainure_x
        tmp_borne_sup_rainure = l_x_mid_rainure[:-1] + l_sampled_eprainure_x[:-1]/2
        tmp_borne_inf_rainure = l_x_mid_rainure[1:] - l_sampled_eprainure_x[1:]/2
        l_sampled_sillon_x = tmp_borne_inf_rainure-tmp_borne_sup_rainure
        l_x_mid_sillon = (tmp_borne_inf_rainure+tmp_borne_sup_rainure)/2
'''

def create_sep(i, pos_x, large_x):
    global bloc_mat, bloc_det
    
    if pert_position:
        sampled_prtdosi_y = sample_u(dim_prtdosi_y, dim_prtdosi_y_sig)
    
        sampled_declage_portedosi_plaque  = sample_u(0,(large_x - dim_prtdosi_x)/2)-tmp_thic[i]/2
        sampled_declage_portedosi_rainure = sample_u(0,(dim_intbox_y - sampled_prtdosi_y)/2)
    else:
        sampled_prtdosi_y=dim_prtdosi_y
        sampled_declage_portedosi_plaque=-tmp_thic[i]/2
        sampled_declage_portedosi_rainure=0
    
    imp_biaisage = 5+i*0.6
    name_separator  = "s_petale_sep_"+str(i)
    name_air        = "s_petale_air_"+str(i)
    name_rainure    = "s_petale_rainure_"+str(i)
    name_pdosi      = "s_petale_pdosi_"+str(i)
    name_petale1     =""
    name_petale2     =""
    if i>0 :
        plate_letter="ABCDEFGH"[i-1]
        lz1=d_mat_dim[ref_mat+plate_letter]["lz"] if not do_voxel else 30.0
        name_petale1 += " s_petale_meta_"+str(i-1)
    else : 
        lz1=30.0
    if i<8 :
        plate_letter="ABCDEFGH"[i]
        lz2=d_mat_dim[ref_mat+plate_letter]["lz"] if not do_voxel else 30.0
        name_petale2 += " s_petale_meta_"+str(i)
    else :
        lz2=30.0
    rainure_corr=(name_petale1+" "+name_petale2) if pert_position else ""
    
    
    l_name_dosi, l_mat_dosi, l_name_all_places = [], [], []
    if not larger_dosi:
        for j in range(5):
            d_dosi = get_dosi_Pi_j(i+1,j+1)
            l_name_all_places += ["s_petale_hole_dos_"+str(i+1)+"_"+str(j+1)]
            if d_dosi is not None:
                l_name_dosi += ["s_petale_dos_"+str(i+1)+"_"+str(j+1)+"_"+d_dosi["mat"]]
                l_mat_dosi  += ["mat_dosi_"+str(i+1)+"_"+str(j+1)+"_"+d_dosi["mat"]]
    else:
        j=0
        d_dosi = get_dosi_Pi_j(i+1,j+1)
        name_dosi = "s_petale_dos_"+str(i+1)+"_"+str(j+1)+"_"+d_dosi["mat"]
        l_name_all_places += [name_dosi]
    
    
    
    bloc_surf_raw[0]  += "surf "+name_rainure+" cuboid -"+str(pos_x+large_x/2)            +"  -"+str(pos_x-large_x/2)            +" -"+str(box_y_int_size/2)    +" "+str(box_y_int_size/2)+" -"+str(lz1/2)+" "+str(overall_max_z+1)+"\n"
    bloc_surf_trans[0]+= "strans "+name_rainure+" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
    bloc_surf_cell[0] += "cell c_"+name_rainure[2:]+" u_refl "+mat_boite+" -"+name_rainure+" "+name_air+" "+rainure_corr+" \n" # -s_petale_box2
    
    bloc_surf_raw[0]  += "surf "+name_air+" cuboid -"+str(pos_x+large_x/2)            +"  -"+str(pos_x-large_x/2)            +" -"+str(dim_intbox_y/2)    +" "+str(dim_intbox_y/2)+" -"+str(box_z_int_size/2+1)+" "+str(overall_max_z+1)+"\n"
    bloc_surf_trans[0]+= "strans "+name_air+" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
    bloc_surf_cell[0] += "cell c_"+name_air[2:]+" u_refl Air_PETALE -"+name_air+" "+name_petale1+" "+name_petale2+" "+name_separator+" -"+name_rainure+"  \n"#
    
    bloc_surf_raw[0]  += "surf "+name_pdosi+" cuboid -"+str(pos_x+dim_prtdosi_x/2)            +"  -"+str(pos_x-dim_prtdosi_x/2)            +" -"+str(sampled_prtdosi_y/2)    +" "+str(sampled_prtdosi_y/2)+" -"+str(lz1/2)+" "+str(lz2/2)+"\n"
    bloc_surf_trans[0]+= "strans "+name_pdosi+" "+str(sampled_declage_portedosi_plaque)+" "+str(sampled_declage_portedosi_rainure)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
    bloc_surf_cell[0] += "cell c_"+name_pdosi[2:]+" u_pdosi_"+str(i)+" "+mat_interval+" -"+name_pdosi+" "+" ".join(l_name_all_places)   +" \n"#-s_petale_box2 +" ".join(l_name_dosi)
    
    
    global l_max_x_pdosi
    global l_min_x_pdosi
    l_max_x_pdosi+=[-(pos_x-dim_prtdosi_x/2)+(sampled_declage_portedosi_plaque)]
    l_min_x_pdosi+=[-(pos_x+dim_prtdosi_x/2)+(sampled_declage_portedosi_plaque)]
    l_name_supp_space=[]
    l_name_scotch=[]
    supp_space=0 #suplementary space due to the clip disks beeing larger than intended
    eff_e_scotch=0
    if not larger_dosi:
        for j in range(5):
            d_dosi = get_dosi_Pi_j(i+1,j+1)
            name_hole_dosi = "s_petale_hole_dos_"+str(i+1)+"_"+str(j+1)
            
            if   j+1 == 1: xy = "0 0"
            elif j+1 == 2: xy = "-"+str(dist_dosi)+" " +str(dist_dosi)
            elif j+1 == 3: xy = "-"+str(dist_dosi)+" -"+str(dist_dosi)
            elif j+1 == 4: xy = "" +str(dist_dosi)+" -"+str(dist_dosi)
            elif j+1 == 5: xy = "" +str(dist_dosi)+" " +str(dist_dosi)
                
            if d_dosi is not None:
                name_dosi = "s_petale_dos_"+str(i+1)+"_"+str(j+1)+"_"+d_dosi["mat"]
                #mat_dosi  = "mat_dosi_"+str(i+1)+"_"+str(j+1)+"_"+d_dosi["mat"]
                mat_dosi  = "mat_dosi_"+d_dosi["name"]
                bloc_surf_raw[1]  += "surf "+name_dosi +" cylx "+xy+" "+str(d_dosi["radius"])+" -"+str(pos_x-0.025+d_dosi["th"])   +"  -"+str(pos_x-0.025)+"\n"
                bloc_surf_trans[1]+= "strans "+name_dosi +" "+str(sampled_declage_portedosi_plaque)+" "+str(sampled_declage_portedosi_rainure)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                
                loc_imp_biaisage = str(imp_biaisage) if "Au" not in name_dosi else str(imp_biaisage+2)
                bloc_surf_cell[1] += "cell c_"+name_dosi[2:]     +" u_pdosi_"+str(i)+" imp "+aff(loc_imp_biaisage,3)+" "+mat_dosi +" -"+name_dosi   +" \n"# -s_petale_box2
                
            
                bloc_surf_raw[1]  += "surf "+name_hole_dosi +" cylx "+xy+" "+str(1.5)+" -"+str(pos_x+0.075)   +"  -"+str(pos_x-0.025)+"\n"
                bloc_surf_trans[1]+= "strans "+name_hole_dosi +" "+str(sampled_declage_portedosi_plaque)+" "+str(sampled_declage_portedosi_rainure)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                
                name_clip_dosi = "s_petale_clip_dos_"+str(i+1)+"_"+str(j+1)
                bloc_surf_raw[1]  += "surf "+name_clip_dosi +" cylx "+xy+" "+str(1.5)+" -"+str(pos_x-0.025+d_dosi["th"]+0.05)   +"  -"+str(pos_x-0.025+d_dosi["th"])+"\n" # for simplicity sake we avoid all kind of extrusion
                bloc_surf_trans[1]+= "strans "+name_clip_dosi +" "+str(sampled_declage_portedosi_plaque)+" "+str(sampled_declage_portedosi_rainure)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                bloc_surf_cell[1] += "cell c_"+name_clip_dosi[2:]     +" u_pdosi_"+str(i)+" mat_clip -"+name_clip_dosi   +" \n"# -s_petale_box2
                print("th",d_dosi["th"])

                bloc_surf_cell[1] += "cell c_"+name_hole_dosi[2:]     +" u_pdosi_"+str(i)+" Air_PETALE -"+name_hole_dosi +" "+name_clip_dosi+" "+name_dosi +" \n"# -s_petale_box2
                tmp_supp_space=(d_dosi["th"]+0.05)-(dim_prtdosi_x-0.05)
                # tmp_supp_space=(d_dosi["th"]+0.05-dim_prtdosi_x/2-0.025)
                if tmp_supp_space>supp_space: 
                    supp_space=tmp_supp_space
                    print("supp_space",supp_space)
                if tmp_supp_space>0:
                    l_name_supp_space+=[name_clip_dosi]
                if "Au" not in  d_dosi["name"]: #space for the scoth definition
                     eff_e_scotch=e_scotch
                     
                if not mode_replace_mat:
                    bloc_mat += "mat "+aff(mat_dosi,18)+" "+aff("-"+str(d_dosi["den"]),10)+"   "+d_dosi_general[d_dosi["mat"]]["compo"]+"\n"
                    for iso, l_mt in d_matdosi_2_data[d_dosi["mat"]]["iso"]:
                        for mt in l_mt:
                            bloc_det += "    idet "+mat_dosi+ "  "+str(iso)+"  "+str(mt)+"\n"
                else:
                    bloc_mat += "mat "+aff(mat_dosi,18)+" "+mat_replacement+" \n"
            else:
                bloc_surf_raw[1]  += "surf "+name_hole_dosi +" cylx "+xy+" "+str(1.5)+" -"+str(pos_x+0.075)   +"  -"+str(pos_x-0.025)+"\n"
                bloc_surf_trans[1]+= "strans "+name_hole_dosi +" "+str(sampled_declage_portedosi_plaque)+" "+str(sampled_declage_portedosi_rainure)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
                bloc_surf_cell[1] += "cell c_"+name_hole_dosi[2:]     +" u_pdosi_"+str(i)+" Air_PETALE -"+name_hole_dosi   +" \n"# -s_petale_box2
    else:
        d_dosi = get_dosi_Pi_j(i+1,j+1)
        if   j+1 == 1: xy = "0 0"
        elif j+1 == 2: xy = "-"+str(dist_dosi)+" " +str(dist_dosi)
        elif j+1 == 3: xy = "-"+str(dist_dosi)+" -"+str(dist_dosi)
        elif j+1 == 4: xy = "" +str(dist_dosi)+" -"+str(dist_dosi)
        elif j+1 == 5: xy = "" +str(dist_dosi)+" " +str(dist_dosi)
        name_dosi = "s_petale_dos_"+str(i+1)+"_"+str(j+1)+"_"+d_dosi["mat"]
        mat_dosi  = "mat_dosi_"+d_dosi["name"]
        bloc_surf_raw[1]  += "surf "+name_dosi +" cylx "+xy+" "+str(10)+" -"+str(pos_x+dim_prtdosi_x/2)   +"  -"+str(pos_x-dim_prtdosi_x/2)+"\n"
        bloc_surf_trans[1]+= "strans "+name_dosi +" "+str(sampled_declage_portedosi_plaque)+" "+str(sampled_declage_portedosi_rainure)+" "+str(trans_z)+" 0 0 "+rot_angle+"\n"
        
        loc_imp_biaisage = str(imp_biaisage) if "Au" not in name_dosi else str(imp_biaisage+2)
        bloc_surf_cell[1] += "cell c_"+name_dosi[2:]     +" u_pdosi_"+str(i)+" imp "+aff(loc_imp_biaisage,3)+" "+mat_dosi +" -"+name_dosi   +" \n"# -s_petale_box2
        bloc_mat += "mat "+aff(mat_dosi,18)+" "+aff("-"+str(d_dosi["den"]),10)+"   "+d_dosi_general[d_dosi["mat"]]["compo"]+"\n"
        for iso, l_mt in d_matdosi_2_data[d_dosi["mat"]]["iso"]:
            for mt in l_mt:
                bloc_det += "    idet "+mat_dosi+ "  "+str(iso)+"  "+str(mt)+"\n"
        
    bloc_surf_cell[0] += "cell c_Air_pdosi_"+str(i)+"  u_pdosi_"+str(i)+" Air_PETALE   "+name_pdosi+" "+" ".join(l_name_supp_space)+" "+" ".join(l_name_scotch)+"  \n"#
    
    bloc_surf_raw[0]  += "surf "+name_separator+" cuboid "+str(-pos_x-dim_prtdosi_x/2+sampled_declage_portedosi_plaque-(supp_space+eff_e_scotch))            +"  "+str(-pos_x+dim_prtdosi_x/2+sampled_declage_portedosi_plaque)            +" -"+str(dim_intbox_y/2)    +" "+str(dim_intbox_y/2)+" -"+str(box_z_int_size/2)+" "+str(box_z_int_size/2)+"\n"
    bloc_surf_trans[0]+= "strans "+name_separator+" "+str(0)+" 0 "+str(trans_z)+" 0 0 "+rot_angle+"\n"
    # bloc_surf_cell[0] += "cell c_"+name_air[2:]+" u_refl Air_PETALE -"+name_air+" "+name_separator+" -s_petale_box2"+" -"+name_rainure+"\n"#
    bloc_surf_cell[0] += "cell c_"+name_separator[2:]+" u_refl fill=u_pdosi_"+str(i)+" -"+name_separator+" \n"#
    # l_max_x_pdosi[-1]=max([l_max_x_pdosi[-1],pos_x+large_x/2+supp_space+eff_e_scotch-trans_x+sampled_declage_portedosi_plaque])#making there is no overlap with the plates
    l_min_x_pdosi[-1]-=(supp_space+eff_e_scotch)#making there is no overlap with the plates
    
    
    
#e_by_sep = e_rainure
First_it=True
l_min_x_sheets=[0,0,0]
l_max_x_sheets=[0,0,0]
l_min_x_pdosi =[0,0,0]
l_max_x_pdosi =[0,0,0]
tmp_thic=np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.]) # displace slightly pdos if necessary to avoid superposition (only if not pert)
tmp_disp=np.array([0.,0.,0.,0.,0.,0.,0.,0.]) # displace slightly ref. if necessary to avoid superposition (only if not pert and steel ref.)
try_number=0
while (First_it or any((np.array(l_min_x_pdosi[:-1])-np.array(l_max_x_sheets))<0) or any((np.array(l_min_x_sheets)-np.array(l_max_x_pdosi[1:]))<0) or (l_max_x_sheets[0]>-(d_min_casier+dim_epbox_x))):
    #if not First_it:
    #    for i in range(1,nb):
    #            l_x_mid_rainure[i]=(l_min_x_sheets[i-1]+l_max_x_sheets[i])/2
    print("Samplin try number",try_number)
    if not First_it: # correction from old model due to the clip dosimeter being larger than intended
      print("max pdosi [%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f]" % tuple(l_max_x_pdosi[1:] ) )
      print("min sheet [%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f]" % tuple(l_min_x_sheets    ) )
      print("max sheet [%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f]" % tuple(l_max_x_sheets    ) )
      print("min pdosi [%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f,%.5f]" % tuple(l_min_x_pdosi[:-1]) )
      print(l_max_x_pdosi[0],-(d_min_casier+dim_epbox_x))
      print((np.array(l_min_x_pdosi[:-1])-np.array(l_max_x_sheets))<0)
      print((np.array(l_min_x_sheets)-np.array(l_max_x_pdosi[1:]))<0)
      print(l_max_x_sheets[0]>-(d_min_casier+dim_epbox_x))
      if try_number==1: # correction from old model due to the clip dosimeter being larger than intended
          if not pert_position:
              tmp_thic=dim_prtdosi_x-(np.array(l_max_x_pdosi)-np.array(l_min_x_pdosi))
              #
              # l_x_mid_rainure += tmp_thic/2
              if "Fe" in case_csv : tmp_thic[4] +=0.002
              if "SS" in case_csv and "al" not in case_csv: 
                  tmp_thic[4] +=0.0025
                  tmp_thic[7] +=0.002*2
                  tmp_disp[6] =0.003
              elif "SS" in case_csv and "al"  in case_csv:
                  tmp_thic[3] -= 0.003
                  tmp_thic[4] += 0.004
                  tmp_thic[7] += 0.005
                  tmp_disp[6] = 0.003
                  tmp_disp[2] = 0.003
                  tmp_disp[7] = -0.001
              print(tmp_thic)
              print(tmp_disp)
      elif not pert_position:
          exit()
      
    First_it=False
    bloc_surf_raw   = ["","",""]
    bloc_surf_trans = ["","","",""]
    bloc_surf_cell  = ["","",""]
    bloc_mat = ""
    bloc_det = "set mat_matrix_rr\n"
    

    trans_x = (14*pas_reseau_umet)/2**0.5+radius_clad_ext            # translation of the box (before rotation)
    # trans_x = (14*pas_reseau_umet)/2**0.5+radius_clad_ext + e_rod_petale            # translation of the box (before rotation)
    #trans_x = (14*pas_reseau_umet)/2**0.5+radius_clad_ext             # translation of the box (before rotation)
    #e_fond = e_protec if protec_fond else 0.                        # additional B4C behind the expriment
    
    # box surf creation: outside / protection / inside
    bloc_surf_raw[0]   += "surf s_petale_box cuboid -"+str((14*pas_reseau_umet)/2**0.5+radius_clad_ext+25)+" -"+str((14*pas_reseau_umet)/2**0.5+radius_clad_ext+0.01)+" -"+str(box_y_ext_size/2+5)+" "+str(box_y_ext_size/2+5)+" -"+str(h_min_casier+3)+" "+str(100-offset_z)+"\n"
    bloc_surf_raw[0]   += "surf s_petale_box_out cuboid -"+str(box_x_ext_size-d_min_casier)+" -"+str(d_min_casier)+" -"+str(box_y_ext_size/2)+" "+str(box_y_ext_size/2)+" -"+str(h_min_casier)+" "+str(box_z_ext_size/2+dim_dist_plate_lid)+"\n"
    bloc_surf_raw[0]   += "surf s_petale_box_in cuboid -"+str(box_x_int_size+d_min_casier+dim_epbox_x)+" -"+str(d_min_casier+dim_epbox_x)+" -"+str(box_y_int_size/2)+" "+str(box_y_int_size/2)+" -"+str(box_z_int_size/2)+" "+str(box_z_int_size/2+dim_dist_plate_lid)+"\n"
    bloc_surf_raw[0]   += "surf s_petale_box_refl cuboid -"+str(box_x_int_size+d_min_casier+dim_epbox_x)+" -"+str(d_min_casier+dim_epbox_x)+" -"+str(box_y_int_size/2)+" "+str(box_y_int_size/2)+" -"+str(box_z_int_size/2)+" "+str(overall_max_z)+"\n"
    # bloc_surf_raw[0]   += "surf s_air_under_lid cuboid -"+str(box_x_int_size+d_min_casier+dim_epbox_x)+" -"+str(d_min_casier+dim_epbox_x)+" -"+str(box_y_int_size/2)+" "+str(box_y_int_size/2)+" "+str(overall_max_z)+" "+str(box_z_int_size/2+dim_dist_plate_lid)+"\n"
    bloc_surf_raw[0]   += "surf  s_dummy_ion_chamber cylz  -8.6  36.35   2.75 26.95  117.3 \n"                           #dummy north ion chamber

    bloc_surf_trans[0] += "strans s_petale_box_out "+str(0)+" 0 "+str(0)+" 0 0 "+rot_angle+"\n"
    bloc_surf_trans[0] += "strans s_petale_box_in "+str(0)+" 0 "+str(0)+" 0 0 "+rot_angle+"\n"
    bloc_surf_trans[0] += "strans s_petale_box_refl "+str(0)+" 0 "+str(0)+" 0 0 "+rot_angle+"\n"
    # bloc_surf_trans[0] += "strans s_air_under_lid "+str(0)+" 0 "+str(0)+" 0 0 "+rot_angle+"\n"
    
    # box cellule creation
    bloc_surf_cell[0]  += "cell c_petale_tmp   0  fill=4   -s_petale_box s_dummy_ion_chamber \n"
    bloc_surf_raw[0]   += "nest n_under_lid \n"
    bloc_surf_raw[0]   += "   Air_PETALE cuboid -"+str(box_x_int_size/2+d_min_casier+dim_epbox_x+e_cale_pdosi_x/2)+" -"+str(box_x_int_size/2+d_min_casier+dim_epbox_x-e_cale_pdosi_x/2)+" -"+str(e_cale_pdosi_y/2-e_cale_pdosi_y_edge)+" "+str(e_cale_pdosi_y/2-e_cale_pdosi_y_edge)+" "+str(box_z_int_size/2+dim_dist_plate_lid-dist_cale_pdosi_lid)+" "+str(box_z_int_size/2+dim_dist_plate_lid)+"\n"
    bloc_surf_raw[0]   += "   "+mat_interval+" cuboid -"+str(box_x_int_size/2+d_min_casier+dim_epbox_x+e_cale_pdosi_x/2)+" -"+str(box_x_int_size/2+d_min_casier+dim_epbox_x-e_cale_pdosi_x/2)+" -"+str(e_cale_pdosi_y/2)+" "+str(e_cale_pdosi_y/2)+" "+str(box_z_int_size/2+dim_dist_plate_lid-dist_cale_pdosi_lid-e_cale_pdosi_z)+" "+str(box_z_int_size/2+dim_dist_plate_lid)+"\n"
    bloc_surf_raw[0]   += "   mat_support_bracket cuboid -"+str(box_x_int_size/2+d_min_casier+dim_epbox_x+e_cale_pdosi_x/2)+" -"+str(box_x_int_size/2+d_min_casier+dim_epbox_x-e_cale_pdosi_x/2)+" -"+str(e_cale_pdosi_y/2+e_cale_edge_y)+" "+str(e_cale_pdosi_y/2+e_cale_edge_y)+" "+str(box_z_int_size/2+dim_dist_plate_lid-dist_cale_pdosi_lid-e_cale_pdosi_z)+" "+str(box_z_int_size/2+dim_dist_plate_lid)+"\n"
    bloc_surf_raw[0]   += "   Air_PETALE \n"
    bloc_surf_trans[0] += "utrans n_under_lid "+str(0)+" 0 "+str(0)+" 0 0 "+rot_angle+"\n"
   
    #supporting plate
    bloc_surf_raw[0]   += "surf s_petale_support_main cuboid "+str(d_min_casier-box_x_ext_size/2-(dist_support_holes_x))+" "+str(d_min_casier-box_x_ext_size/2+(dim_support_plate_x-dist_support_holes_x))+" -"+str(dim_support_plate_y/2)+" "+str(dim_support_plate_y/2)+" "+str(-h_min_casier-dim_support_plate_z)+" "+str(-h_min_casier)+"\n"
    # bloc_surf_raw[0]   += "surf s_support_cuboid cuboid -"+str(dist_support_holes_x)+" "+str(dim_support_plate_x-dist_support_holes_x)+" -"+str(dim_support_plate_y/2)+" "+str(dim_support_plate_y/2)+" "+str(-h_min_casier-dim_support_plate_z)+" "+str(-h_min_casier)+"\n"
    bloc_surf_raw[0]   += "surf s_support_plane_1 px 0  \n"
    # bloc_surf_raw[0]   += "surf s_support_plane_1 px "+str(abs(np.cos(30*np.pi/180)*(dim_support_plate_x-dist_support_holes_x) +np.sin(30*np.pi/180)*(dim_support_plate_y-2*np.tan(60)*80)/2)/10) +"  \n"
    bloc_surf_raw[0]   += "surf s_support_plane_2 px 0  \n"
    # bloc_surf_raw[0]   += "surf s_support_plane_2 px "+str(abs(np.cos(30*np.pi/180)*(dim_support_plate_x-dist_support_holes_x) +np.sin(30*np.pi/180)*(dim_support_plate_y-2*np.tan(60)*80)/2)/10) +" \n"
    bloc_surf_trans[0] += "strans s_petale_support_main "+str(0)+" 0 "+str(0)+" 0 0 " +rot_angle+"\n"
    # bloc_surf_trans[0] += "strans s_support_cuboid "+str(0)+" 0 "+str(0)+" 0 0 " +rot_angle+"\n"
    bloc_surf_trans[0] += "strans s_support_plane_1 "+str(0)+" 0 "+str(0)+" 0 0 -30 \n"
    bloc_surf_trans[0] += "strans s_support_plane_2 "+str(0)+" 0 "+str(0)+" 0 0  30 \n"
    #craddle
    bloc_surf_raw[0]   += "surf s_craddle_N_out cuboid "+str(-d_min_casier-box_x_ext_size/2-dist_support_holes_x)+" "+str(-d_min_casier-box_x_ext_size/2+(dim_support_plate_x/2-dist_support_holes_x))                        +"  "+str(dim_support_plate_y/2-4)+" "+str(dim_support_plate_y/2)                           +" "+str(-h_min_casier)+" "+str(-h_min_casier+64.45)+"\n"
    bloc_surf_raw[0]   += "surf s_craddle_N_in cuboid "+str(-d_min_casier-box_x_ext_size/2+e_craddle_al-dist_support_holes_x)+" "+str(-d_min_casier-box_x_ext_size/2-e_craddle_al+(dim_support_plate_x/2-dist_support_holes_x))+"  "+str(dim_support_plate_y/2-4+e_craddle_al)+" "+str(dim_support_plate_y/2-e_craddle_al) +" "+str(-h_min_casier)+" "+str(-h_min_casier+64.45)+"\n"
    bloc_surf_raw[0]   += "surf s_craddle_S_out cuboid "+str(-d_min_casier-box_x_ext_size/2-dist_support_holes_x)+" "+str(-d_min_casier-box_x_ext_size/2+(dim_support_plate_x/2-dist_support_holes_x))                        +" -"+str(dim_support_plate_y/2)+" -"+str(dim_support_plate_y/2-4)                          +" "+str(-h_min_casier)+" "+str(-h_min_casier+64.45)+"\n"
    bloc_surf_raw[0]   += "surf s_craddle_S_in cuboid "+str(-d_min_casier-box_x_ext_size/2+e_craddle_al-dist_support_holes_x)+" "+str(-d_min_casier-box_x_ext_size/2-e_craddle_al+(dim_support_plate_x/2-dist_support_holes_x))+" -"+str(dim_support_plate_y/2-e_craddle_al)+" -"+str(dim_support_plate_y/2-4+e_craddle_al)+" "+str(-h_min_casier)+" "+str(-h_min_casier+64.45)+"\n"
    bloc_surf_trans[0] += "strans s_craddle_N_out "+str(0)+" 0 "+str(0)+" 0 0 " +rot_angle+"\n"
    bloc_surf_trans[0] += "strans s_craddle_N_in  "+str(0)+" 0 "+str(0)+" 0 0 " +rot_angle+"\n"
    bloc_surf_trans[0] += "strans s_craddle_S_out "+str(0)+" 0 "+str(0)+" 0 0 " +rot_angle+"\n"
    bloc_surf_trans[0] += "strans s_craddle_S_in  "+str(0)+" 0 "+str(0)+" 0 0 " +rot_angle+"\n"
   
   
    try_number+=1
    l_min_x_sheets=[]
    l_max_x_sheets=[]
    l_min_x_pdosi =[]
    l_max_x_pdosi =[]
    for i in range(nb):                                    # loop over the plates
        create_plate(i, l_x_mid_sillon[i],  l_sampled_sillon_x[i])
        create_sep  (i, l_x_mid_rainure[i], l_sampled_eprainure_x[i])
        #pos_x += dx_pet+lx
        
    create_sep(nb, l_x_mid_rainure[nb], l_sampled_eprainure_x[nb])

#position info for manual check
print("position info:")
print("max pdosi",l_max_x_pdosi[1:] )
print("min sheet",l_min_x_sheets)
print("max sheet",l_max_x_sheets)
print("min pdosi",l_min_x_pdosi[:-1] )
print(l_max_x_pdosi[0],-(d_min_casier+dim_epbox_x))
print((np.array(l_min_x_pdosi[:-1])-np.array(l_max_x_sheets))<0)
print((np.array(l_min_x_sheets)-np.array(l_max_x_pdosi[1:]))<0)
print(l_max_x_sheets[0]>-(d_min_casier+dim_epbox_x))

if not mode_replace_mat:
    '''l_mat_done = []
    for idosi, dosi in enumerate(list_dosi):
        mat = dosi[0]
        if mat not in l_mat_done:
            bloc_mat += "mat "+aff(mat,18)+" "+aff(d_dosi[mat]["den"],10)+"   "+d_dosi[mat]["compo"]+" \n"
            l_mat_done += [mat]'''
    # old
    # bloc_mat += "mat "+aff("mat_boite", 18)+" "+aff("-2.702",10)+" dmax 0.1  rgb 152 151 152 13027g0.0300c -0.98000 14028g0.0300c -0.00551  14029g0.0300c -0.00029  14030g0.0300c -0.00020 26054g0.0300c -0.00017 26056g0.0300c -0.00276  26057g0.0300c -0.00006  26058g0.0300c -0.00001 29063g0.0300c -0.00068  29065g0.0300c -0.00032  25055g0.0300c -0.00100 12024g0.0300c -0.00468  12025g0.0300c -0.00062  12026g0.0300c -0.00071 24050g0.0300c -0.00002  24052g0.0300c -0.00042 24053g0.0300c -0.00005  24054g0.0300c -0.00001 22046g0.0300c -7.92e-5  22047g0.0300c -7.30e-5  22048g0.0300c -7.38e-4 22049g0.0300c -5.53e-5  22050g0.0300c -5.40e-5 30064g0.0300c -0.000707360697088 30066g0.0300c -0.000423756019262 30067g0.0300c -6.29901398762e-05 30068g0.0300c -0.000296262325155 30070g0.0300c -9.63081861958e-06\n"
    # CEA Bilan matiere Al 5083-O 
    bloc_mat += "mat "+aff("mat_boite", 20)+" "+aff("-2.65912",10)+" dmax 0.1  rgb 152 151 152  12024g0.0300c    -0.037026244    12025g0.0300c    -0.004883048    12026g0.0300c    -0.005590709    13027g0.0300c    -0.938562    14028g0.0300c    -0.00183747    14029g0.0300c    -9.6635E-05    14030g0.0300c    -6.58946E-05    22046g0.0300c    -1.02948E-05    22047g0.0300c    -9.48326E-06    22048g0.0300c    -9.59983E-05    22049g0.0300c    -7.1905E-06    22050g0.0300c    -7.03311E-06    24050g0.0300c    -3.04679E-05    24052g0.0300c    -0.000611005    24053g0.0300c    -7.06172E-05    24054g0.0300c    -1.79096E-05    25055g0.0300c    -0.0066    26054g0.0300c    -0.00020324    26056g0.0300c    -0.003308455    26057g0.0300c    -7.77733E-05    26058g0.0300c    -1.05316E-05    28058g0.0300c    -5.91334E-05    28060g0.0300c    -2.35625E-05    28061g0.0300c    -1.04144E-06    28062g0.0300c    -3.37507E-06    28064g0.0300c    -8.87546E-07    29063g0.0300c    -0.000232912    29065g0.0300c    -0.000107088    30064g0.0300c    -0.000216362    30066g0.0300c    -0.000125831    30067g0.0300c    -1.86108E-05    30068g0.0300c    -8.62596E-05    30070g0.0300c    -2.93594E-06 \n"
    bloc_mat += "mat Air_PETALE -5.058e-005  dmax 0.1  rgb 250 250 250  7014g0.0300c   4e-005      8016g0r0.0300c          1e-005      1001g0r0.0300c    5.79913e-007      1002g0r0.0300c        8.7e-011 \n"
      # CEA Bilan matière Al 1050
    bloc_mat += "mat "+aff("mat_port_dosi", 20)+" "+aff("-2.69914",10)+" dmax 0.1  rgb 122 121 122 12024g0.0300c    -7.795E-06    12025g0.0300c    -1.02801E-06    12026g0.0300c    -1.17699E-06    13027g0.0300c    -0.9965    14028g0.0300c    -0.001378103    14029g0.0300c    -7.24763E-05    14030g0.0300c    -4.9421E-05    22046g0.0300c    -8.71102E-06    22047g0.0300c    -8.0243E-06    22048g0.0300c    -8.12293E-05    22049g0.0300c    -6.08427E-06    22050g0.0300c    -5.95109E-06    25055g0.0300c    -0.00004    26054g0.0300c    -0.00010162    26056g0.0300c    -0.001654228    26057g0.0300c    -3.88866E-05    26058g0.0300c    -5.2658E-06    29063g0.0300c    -6.85035E-06    29065g0.0300c    -3.14965E-06    30064g0.0300c    -1.44241E-05    30066g0.0300c    -8.38876E-06    30067g0.0300c    -1.24072E-06    30068g0.0300c    -5.75064E-06    30070g0.0300c    -1.95729E-07     \n"
    # corrected clip density
    bloc_mat += "mat "+aff("mat_clip", 20)+" "+aff("-2.428353",10)+" dmax 0.1  rgb 102 101 102  12024g0.0300c    -2.3385E-05    12025g0.0300c    -3.08403E-06    12026g0.0300c    -3.53097E-06    13027g0.0300c    -0.99577    14028g0.0300c    -0.001001421    14029g0.0300c    -5.26661E-05    14030g0.0300c    -3.59126E-05    22046g0.0300c    -7.1272E-06    22047g0.0300c    -6.56534E-06    22048g0.0300c    -6.64604E-05    22049g0.0300c    -4.97804E-06    22050g0.0300c    -4.86907E-06    24050g0.0300c    -4.17369E-07    24052g0.0300c    -8.36994E-06    24053g0.0300c    -9.67359E-07    24054g0.0300c    -2.45336E-07    25055g0.0300c    -0.00005    26054g0.0300c    -0.000140574    26056g0.0300c    -0.002288348    26057g0.0300c    -5.37932E-05    26058g0.0300c    -7.28436E-06    29063g0.0300c    -6.85035E-06    29065g0.0300c    -3.14965E-06    30064g0.0300c    -4.32724E-05    30066g0.0300c    -2.51663E-05    30067g0.0300c    -3.72217E-06    30068g0.0300c    -1.72519E-05    30070g0.0300c    -5.87187E-07    82204g0.0300c    -1.37808E-07    82206g0.0300c    -2.39555E-06    82207g0.0300c    -2.20743E-06    82208g0.0300c    -5.25921E-06    \n"
    # old den of clip but due to real shape 10% correction needed 
    # bloc_mat += "mat "+aff("mat_clip", 20)+" "+aff("-2.69817",10)+" dmax 0.1  rgb 102 101 102  12024g0.0300c    -2.3385E-05    12025g0.0300c    -3.08403E-06    12026g0.0300c    -3.53097E-06    13027g0.0300c    -0.99577    14028g0.0300c    -0.001001421    14029g0.0300c    -5.26661E-05    14030g0.0300c    -3.59126E-05    22046g0.0300c    -7.1272E-06    22047g0.0300c    -6.56534E-06    22048g0.0300c    -6.64604E-05    22049g0.0300c    -4.97804E-06    22050g0.0300c    -4.86907E-06    24050g0.0300c    -4.17369E-07    24052g0.0300c    -8.36994E-06    24053g0.0300c    -9.67359E-07    24054g0.0300c    -2.45336E-07    25055g0.0300c    -0.00005    26054g0.0300c    -0.000140574    26056g0.0300c    -0.002288348    26057g0.0300c    -5.37932E-05    26058g0.0300c    -7.28436E-06    29063g0.0300c    -6.85035E-06    29065g0.0300c    -3.14965E-06    30064g0.0300c    -4.32724E-05    30066g0.0300c    -2.51663E-05    30067g0.0300c    -3.72217E-06    30068g0.0300c    -1.72519E-05    30070g0.0300c    -5.87187E-07    82204g0.0300c    -1.37808E-07    82206g0.0300c    -2.39555E-06    82207g0.0300c    -2.20743E-06    82208g0.0300c    -5.25921E-06    \n"
    bloc_mat += "mat "+aff("mat_support_bracket", 20)+" "+aff("-2.67912",10)+" dmax 0.1  rgb 72 71 72  12024g0.0300c   -0.024242446    12025g0.0300c   -0.003197111    12026g0.0300c   -0.003660443    13027g0.0300c   -0.96021    14028g0.0300c   -0.002113091    14029g0.0300c   -0.00011113    14030g0.0300c   -7.57788E-05    22046g0.0300c   -1.18787E-05    22047g0.0300c   -1.09422E-05    22048g0.0300c   -0.000110767    22049g0.0300c   -8.29673E-06    22050g0.0300c   -8.11512E-06    24050g0.0300c   -2.46248E-05    24052g0.0300c   -0.000493826    24053g0.0300c   -5.70742E-05    24054g0.0300c   -1.44748E-05    25055g0.0300c   -0.0016    26054g0.0300c   -0.000197595    26056g0.0300c   -0.003216554    26057g0.0300c   -7.56129E-05    26058g0.0300c   -1.02391E-05    29063g0.0300c   -0.00019866    29065g0.0300c   -0.00009134    30064g0.0300c   -0.000125009    30066g0.0300c   -7.27026E-05    30067g0.0300c   -1.07529E-05    30068g0.0300c   -4.98389E-05    30070g0.0300c   -1.69632E-06        \n"
    bloc_mat += "mat "+aff("mat_support_plate", 20)+" "+aff("-2.65896",10)+" dmax 0.1  rgb 72 71 72  12024g0.0300c    -0.034297994    12025g0.0300c    -0.004523244    12026g0.0300c    -0.005178762    13027g0.0300c    -0.94225    14028g0.0300c    -0.002480585    14029g0.0300c    -0.000130457    14030g0.0300c    -8.89578E-05    22046g0.0300c    -1.90059E-05    22047g0.0300c    -1.75076E-05    22048g0.0300c    -0.000177228    22049g0.0300c    -1.32748E-05    22050g0.0300c    -1.29842E-05    23050g0.0300c    -4.40687E-07    23051g0.0300c    -0.000179559    24050g0.0300c    -0.000041737    24052g0.0300c    -0.00083699    24053g0.0300c    -0.000096736    24054g0.0300c    -2.4534E-05    25055g0.0300c    -0.0049    26054g0.0300c    -0.000186303    26056g0.0300c    -0.00303275    26057g0.0300c    -7.12922E-05    26058g0.0300c    -9.65396E-06    28058g0.0300c    -6.04774E-05    28060g0.0300c    -2.4098E-05    28061g0.0300c    -1.06511E-06    28062g0.0300c    -3.45178E-06    28064g0.0300c    -9.07718E-07    29063g0.0300c    -0.000356218    29065g0.0300c    -0.000163782    30064g0.0300c    -0.00034618    30066g0.0300c    -0.00020133    30067g0.0300c    -2.97773E-05    30068g0.0300c    -0.000138015    30070g0.0300c    -4.6975E-06    31069g0.0300c    -5.94205E-05    31071g0.0300c    -4.05795E-05    \n"
    bloc_mat += "mat "+aff("mat_craddle", 20)+" "+aff("-2.69907",10)+" dmax 0.1  rgb 72 71 72  12024g0.0300c    -0.003897499    12025g0.0300c    -0.000514005    12026g0.0300c    -0.000588496    13027g0.0300c    -0.98783    14028g0.0300c    -0.003950561    14029g0.0300c    -0.000207765    14030g0.0300c    -0.000141673    22046g0.0300c    -9.89889E-06    22047g0.0300c    -9.11852E-06    22048g0.0300c    -9.2306E-05    22049g0.0300c    -6.91394E-06    22050g0.0300c    -6.7626E-06    24050g0.0300c    -8.34737E-07    24052g0.0300c    -1.67399E-05    24053g0.0300c    -1.93472E-06    24054g0.0300c    -4.90673E-07    25055g0.0300c    -0.00021    26054g0.0300c    -0.00012138    26056g0.0300c    -0.001975883    26057g0.0300c    -4.64479E-05    26058g0.0300c    -6.2897E-06    29063g0.0300c    -0.000133582    29065g0.0300c    -6.14182E-05    30064g0.0300c    -8.17368E-05    30066g0.0300c    -4.75363E-05    30067g0.0300c    -7.03076E-06    30068g0.0300c    -3.2587E-05    30070g0.0300c    -1.10913E-06    \n"
    
    bloc_mat += "mat "+aff("mat_protec",20)+" "+aff("-8.65",10)+" dmax 0.1 rgb 0 153 0 48106g0.0300c 1.25 48108g0.0300c 0.89 48110g0.0300c 12.49 48111g0.0300c 12.80 48112g0.0300c 24.13 48113g0.0300c 12.22 48114g0.0300c 28.73 48116g0.0300c 7.49\n"
else:
    bloc_mat += "mat "+name_mat_replacement+" "+mat_replacement+" \n"
'''
det = "set mat_matrix_rr\n"
for idosi, (dosi, l_iso2lmt) in enumerate(list_dosi):
    for iso, l_mt in l_iso2lmt:
        for mt in l_mt:
            for n in range(nb+1):
                det += "    idet  mat_dosi_"+str(n)+"_"+str(idosi)+"_"+str(dosi) + "  "+str(iso)+"  "+str(mt)+"\n"
'''

if angle_vert<0: angle_vert += 360
bloc_trans_final = ""
for line in "".join(bloc_surf_trans).split("\n"):
    if len(line)>0:
        name = line.split()[1]
        bloc_trans_final += line.split()[0]+" "+name+" 0 0 0 "+str(theta*180/np.pi)+" "+str(phi*180/np.pi)+" "+str(nu*180/np.pi)+" \n"
        bloc_trans_final += line+"\n"
        #bloc_trans_final += "strans "+name+" 0 "+str(off_set_lateral)+" 0 0 "+str(angle_vert)+" 0"+"\n"
        if angle_vert != 0 or angle_hori != 0 :
            bloc_trans_final += line.split()[0]+" "+name+" 0 "+str(off_set_lateral)+" 0 0 0 "+"%.10f"%(angle_hori)+"\n"
            # bloc_trans_final += line.split()[0]+" "+name+" 0 "+str(off_set_lateral)+" 0 0 "+"%.10f"%(angle_vert)+" "+"%.10f"%(angle_hori)+"\n"
        #bloc_trans_final += "strans "+name+" 0 0 0 0 0 0"+"\n"
    else:
        bloc_trans_final += "\n"
# bloc_trans_final += "utrans u_craddle -"+str(dim_support_plate_x-dist_support_holes_x)+" "+str(0)+" "+str(0)+" 0 0 0 \n" 
bloc_trans_final += "utrans u_support "+str(dim_support_plate_y/2*np.tan(30*np.pi/180)+(dim_support_plate_x/2-dist_support_holes_x)-box_x_ext_size/2)+" "+str(0)+" "+str(0)+" 0 0 0 \n" 
bloc_trans_final += "utrans 4 "+str(-offset_x-Delta_x_corr-trans_x)+" "+str(offset_y-Delta_y_corr)+" "+str(offset_z-Delta_z_corr)+" 0 0 0 \n" 
bloc_trans_final += "utrans u_core 0 0 0 0 0 -45 \n" 
bloc_trans_final += "utrans 0 0 0 0 0 0  45 \n" 
bloc_trans_final += "strans s_petale_box -"+str(0)+" 0 "+str(offset_z)+" 0 0 "+rot_angle+"\n" 
bloc_trans_final += "strans s_dummy_ion_chamber 0 0 0 0 0 -45 \n" 
bloc_surf_cell[0]  += "cell c_petale_box_out 4 fill=u_craddle s_petale_box_out \n" 
bloc_surf_cell[0]  += "cell c_petale_box1 4 "+mat_boite+" s_petale_box_in -s_petale_box_out \n" 
bloc_surf_cell[0]  += "cell c_petale_box_refl 4 fill=u_refl -s_petale_box_refl \n" 
bloc_surf_cell[0]  += "cell c_air_under_lid 4 fill=n_under_lid -s_petale_box_in s_petale_box_refl \n" 
#support plate
bloc_surf_cell[0]  += "cell c_petale_support_plate u_craddle fill u_support -s_petale_support_main \n" 
bloc_surf_cell[0]  += "cell c_support_plate_in u_support mat_support_plate  -s_support_plane_1 -s_support_plane_2 \n" 
bloc_surf_cell[0]  += "cell c_support_plate_out u_support H2O s_support_plane_1:s_support_plane_2 \n" 
#craddle (could perhaps be further optimize)
bloc_surf_cell[0]  += "cell c_craddle_water u_craddle H2O s_petale_support_main s_craddle_N_out s_craddle_S_out\n" 
bloc_surf_cell[0]  += "cell c_craddle_N_out u_craddle mat_craddle -s_craddle_N_out s_craddle_N_in \n" 
bloc_surf_cell[0]  += "cell c_craddle_N_in  u_craddle Air_PETALE -s_craddle_N_in  \n" 
bloc_surf_cell[0]  += "cell c_craddle_S_out u_craddle mat_craddle -s_craddle_S_out s_craddle_S_in \n" 
bloc_surf_cell[0]  += "cell c_craddle_S_in  u_craddle Air_PETALE -s_craddle_S_in \n" 
out  = "#"*40+"\n"*2
out += "".join(bloc_surf_raw)
out += bloc_trans_final
out += "".join(bloc_surf_cell)
out += "\n"+bloc_mat+"\n"
# out += bloc_det+"\n"
# out += "\n"+"#"*40+"\n"

#print out
open("auto_geom"+save+".out","w").write(out)
print ("--> see auto_geom.out")

#print(bloc_trans_final)
#print(bloc_mat)

print()
print(box_y_int_size)


print("offset_x, -Delta_x, -trans_x",offset_x,-Delta_x_corr,-trans_x)
print(f"p_x={-(offset_x+trans_x-offset_y)*np.cos(np.pi/4)}cm, p_y={(offset_x+trans_x+offset_y)*np.sin(np.pi/4)}cm, p_x={(offset_z)}cm")
"""
set mat_matrix_rr 
    idet mat_dosi_0     491150  102
    idet mat_dosi_1     491150  102
    idet mat_dosi_2     491150  102
    idet mat_dosi_3     491150  102
    idet mat_dosi_4     491150  102
    idet mat_dosi_5     491150  102
    idet mat_dosi_6     491150  102
    idet mat_dosi_7     491150  102
    idet mat_dosi_8     491150  102
    idet mat_dosi_0     491150  51
    idet mat_dosi_1     491150  51
    idet mat_dosi_2     491150  51
    idet mat_dosi_3     491150  51
    idet mat_dosi_4     491150  51
    idet mat_dosi_5     491150  51
    idet mat_dosi_6     491150  51
    idet mat_dosi_7     491150  51
    idet mat_dosi_8     491150  51
    """




'''
fm204  (1)                                            $ Flux and total fission
       (1 59 102) (1 64 103) (1 109 12102)            $ Thermal reactions
       (1 115 102) (1 197 102)                        $ Thermal reactions
       (1 24 103) (1 46 103) (1 51 107) (1 54 103)    $ Fast reactions
       (1 56 103) (1 58 103) (1 103 11004) (1 115 11004)  $ Fast reactions
       (1 235 -6) (1 238 -6) (1 239 -6) (1 237 -6)    $ Fission reactions
       (1 238 102) (1 237 102)                        $ Capture reactions
c    Materials for tally
c    -------------------
c
c    Thermal reactions
c    Co-59
m59   27059.10y 1 
c    Zn-64
m64   30064.10y 1 
c    Ag-109
m109  47109.10y 1 
c    In-115
m115  49115.10y 1 
c    gold for foils
m197  79197.10y 1 
c
c    Fast reactions
c    Mg-24
m24  12024.10y 1
c    Ti-46
m46   22046.10y 1
c    V-51
m51   23051.10y 1
c    Fe-54
m54   26054.10y 1
c    Fe-56
m56   26056.10y 1
c    Ni-58
m58   28058.10y 1
c    Rh-103
m103  45103.10y 1
c
c    Fissile/fertile materials
c    uranium 235 
m235  92235.71c 1 
c    neptunium 237 
m237  93237.71c 1 
c    uranium 238 
m238  92238.71c 1 
c    plutonium 239 
m239  94239.71c 1 

'''

