from ..Common.utils_general import *
import numpy as np
# https://www-nds.iaea.org/IRDFFtest/IRDFF_v1-05.pdf -> IRDFF covar
# p722 https://books.google.ch/books?id=oa8gh4wA1nUC&pg=PA722&lpg=PA722&dq=48Ti+neutron+dosimeter+efficiency&source=bl&ots=73JeIhUCu_&sig=AsZkFv0EMwsZU9Ka_M9PSGvrEII&hl=fr&sa=X&ved=2ahUKEwi1ueDDqdvdAhUCCuwKHUPbDmYQ6AEwBHoECAUQAQ#v=onepage&q=48Ti%20neutron%20dosimeter%20efficiency&f=false
# https://nucleonica.com/Application/ReducedDecaySchemes/Na24_TXT.htm
# Rh p 265 https://books.google.fr/books?id=_OPFCgAAQBAJ&pg=PA266&lpg=PA266&dq=rhodium+dosimeter&source=bl&ots=BmGXLoQcit&sig=ACfU3U334Hio2i8HadGLVwSNVGWfn_0b0A&hl=fr&sa=X&ved=2ahUKEwiHtuCJzuXpAhXjDWMBHbv9BTMQ6AEwAnoECAgQAQ#v=onepage&q=rhodium%20dosimeter&f=false
# Rh https://www.lib4ri.ch/archive/nebis/PSI_Berichte_000478272/PSI-Bericht_11-04.pdf
h,d,y,m = 3600, 3600*24, 3600*24*365,60                            # time units

''' Dictionary with genral spectrometry data of dosimetry isotopes '''
d_spectro = {
    ("791970" ,"102"): {"halftime":2.6943*d,  "keV":411.80205,"eff":0.04,  "inten":0.9562     ,"txt":"$^{197}$Au(n,g)" }, #197Au(n,g)198Au(b)          (h2 i-)
    ("280580" ,"103"): {"halftime":70.86*d,   "keV":810.7602, "eff":0.02,  "inten":0.9944     ,"txt":"$^{58}$Ni(n,p)" }, #58Ni(n,p)58Co           (h6 i-)    # https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc=58CO&unc=nds    https://www.nucleonica.com/Application/ReducedDecaySchemes/Co58_TXT.htm
    ("280620" ,"102"): {"halftime":101.2*y,   "keV":17.425,   "eff":0.02,  "inten":1.         ,"txt":"         " },                     
    ("220460" ,"103"): {"halftime":83.79*d,   "keV":889.23,      "eff":0.015, "inten":0.99984 ,"txt":"$^{46}$Ti(n,p)" }, #46Ti(n,p)46Sc           (4)
    ("220480" ,"103"): {"halftime":43.67*h,   "keV":984.,      "eff":0.02,  "inten":1.        ,"txt":"$^{48}$Ti(n,p)" }, #48Ti(n,p)48Sc           (9)    # eff inten to check !!
    ("260540" ,"102"): {"halftime":2.744*y,   "keV":5.899,    "eff":0.02,  "inten":0.162      ,"txt":"         " },                       
    ("260540" ,"103"): {"halftime":312.20*d,  "keV":834.848,  "eff":0.02,  "inten":0.999760   ,"txt":"$^{54}$Fe(n,p)" }, #54Fe(n,p)54Mn           (h20 i10)    # https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc=54MN&unc=nds
    ("260560" ,"103"): {"halftime":2.5789*h,  "keV":846.7638, "eff":0.02,  "inten":0.9885     ,"txt":"$^{56}$Fe(n,p)" }, #56Fe(n,p)56Mn           (h1 i-)    # https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc=56MN&unc=nds    https://www.nucleonica.com/Application/ReducedDecaySchemes/Mn56_TXT.htm
    ("260580" ,"102"): {"halftime":44.494*d,  "keV":1099.245, "eff":0.02,  "inten":0.5661     ,"txt":"$^{58}$Fe(n,g)" }, #58Fe(n,g)59Fe
    ("120240" ,"103"): {"halftime":14.9590*h, "keV":1368.,      "eff":0.015, "inten":0.9995   ,"txt":"$^{24}$Mg(n,p)" }, #24Mg(n,p)24Na           (12)
    ("491150" ,"102"): {"halftime":54.29*m,   "keV":1293.54,  "eff":0.015, "inten":0.848      ,"txt":"$^{115}$In(n,g)" }, #115In(n,g-b)116In* 116Sn    (h17 i12)    # https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc=116In&unc=nds    https://www.nucleonica.com/Application/ReducedDecaySchemes/In116_TXT.htm
    ("491150" ,"51" ): {"halftime":4.486*h,   "keV":336.241,  "eff":0.05,  "inten":0.459      ,"txt":"$^{115}$In(n,n')" }, #115In(n,n')115In*          (h4  i1)    # https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc=115IN&unc=nds
    ("471090" ,"102"): {"halftime":249.950*d, "keV":885.,      "eff":0.02,  "inten":0.732     ,"txt":"$^{10}$9Ag(n,g)" }, #109Ag(n,g)110Ag*          (24)
    ("270590" ,"102"): {"halftime":5.2713*y,  "keV":1332.,      "eff":0.015, "inten":0.9998   ,"txt":"$^{59}$Co(n,g)" }, #59Co(n,g)Co60           (8)
    #("451030" ,"51"):  {"halftime":56.12*m,   "keV":39.76,      "eff":0.1,   "inten":1.      ,"txt":"$^{10}$3Rh(n,n')" }, #103Rh(n,n')103Rh*
    ("451030" ,"51"):  {"halftime":56.12*m,   "keV":39.76,      "eff":0.1,   "inten":0.00068  ,"txt":"$^{103}$Rh(n,n')" }, #103Rh(n,n')103Rh*
    ("230510" ,"107"): {"halftime":43.67*h,   "keV":983.,      "eff":0.015, "inten":1.        ,"txt":"$^{51}$V(n,a)" }, #51V(n,a)Sc48
    ("130270" ,"107"): {"halftime":14.997*h,  "keV":1368.626, "eff":0.2,  "inten":0.999934    ,"txt":"$^{27}$Al(n,a)" }, #27Al(n,a)24Na                  (i 15)    # https://www.nndc.bnl.gov/nudat2/decaysearchdirect.jsp?nuc=24NA&unc=nds    https://nucleonica.com/Application/ReducedDecaySchemes/Na24_TXT.htm
    ("130270" ,"102"): {"halftime":2.2414*m,  "keV":1779.97,  "eff":0.2,  "inten":1.          ,"txt":"$^{27}$Al(n,g)" }, #27Al(n,g)28Al
    ("41093"  ,"51"):  {"halftime":16.13*y,   "keV":30.77,    "eff":0.1,   "inten":1.         ,"txt":"$^{93}$Nb(n,n')" }, #93Nb(n,n')93Nb*          (14)    (2)
}
# http://www.lnhb.fr/nuclear-data/module-lara/
#


# https://www-nds.iaea.org/IRDFFtest/IRDFF_v1-05.pdf -> IRDFF covar
d_lambda = {}
for key in d_spectro.keys():
    d_spectro[key]["lambda"] = np.log(2)/d_spectro[key]["halftime"]
    d_spectro[key]["MeV"] = d_spectro[key]["keV"]/1e3

d_spectro[('491150', '11004')] = d_spectro[('491150', '51')]
d_spectro[('451030', '11004')] = d_spectro[('451030', '51')]


''' Dictionary with genral properties of dosimetry isotopes '''
d_matdosi_2_data = {
        "Ni":{"den":8.908, "rgb":"181 182 181", "iso":[(280580, [103   ])]         , "compo":"28058g0.0300c 0.680769  28060g0.0300c 0.262234   28061g0.0300c 0.011399  28062g0.0300c 0.036345  28064g0.0300c 0.0092560"},
        "Ti":{"den":4.510, "rgb":"182 175 169", "iso":[(220460, [103   ]),(220480,[103])], "compo":"22046g0.0300c 0.0825  22047g0.0300c 0.0744  22048g0.0300c 0.7372  22049g0.0300c 0.0541  22050g0.0300c 0.0518"},
        "Fe":{"den":7.874, "rgb":"83  89  93 ", "iso":[(260540, [103   ]),(260560,[103]),(260580,[102])], "compo":"26054g0.0300c 0.05845 26056g0.0300c 0.91754 26057g0.0300c 0.02119 26058g0.0300c 0.00282           "},
        "Mg":{"den":1.738, "rgb":"233 238 235", "iso":[(120240, [103   ])]         , "compo":"12024g0.0300c 0.7899  12025g0.0300c 0.1000  12026g0.0300c 0.1101                   "},
        "In":{"den":7.31 , "rgb":"119 136 250", "iso":[(491150, [102,11004])]         , "compo":"49113g0.0300c 0.0429  49115g0.0300c 0.9571                             "},
        "Ag":{"den":10.50, "rgb":"0   71  171", "iso":[(471090, [12102 ])]         , "compo":"47107g0.0300c 0.51839 47109g0.0300c 0.48161                            "},
        "Au":{"den":19.3 , "rgb":"255 215 1  ", "iso":[(791970, [102   ])]         , "compo":"79197g0.0300c 1                                        "},
        "Co":{"den":8.90 , "rgb":"0   71  171", "iso":[(270590, [102   ])]         , "compo":"27059g0.0300c 1                                        "},
        "Rh":{"den":12.41, "rgb":"0   71  171", "iso":[(451030, [11004 ])]         , "compo":"45103g0.0300c 1                                        "},
        "Vn":{"den":6.0,   "rgb":"0   71  171", "iso":[(230510, [107   ])]         , "compo":"23050g0.0300c 0.0025  23051g0.0300c 0.9975                             "},
        "Al":{"den":2.6989,"rgb":"0   71  171", "iso":[(130270, [107   ])]         , "compo":"13027g0.0300c 1                                           "},
}

''' dictionary for string reformating for printing'''
d_lib = {
    "JEFF-3.3":"J33",
    "JEFF-3.1.1":"J311",
    # "INDEN":"IN",
    # "INDEN_2022":"IN22",
    # "INDEN_12_23_02_24":"IN24",
    # "Full_JEFF-3.1.1":"J311",
    # "JEFF4T3":"J4T3",
    # "JEFF4T4":"J4T4"
    # "INDEN":"IN",
    "INDEN_2022":"IN22",
    "INDEN_12_23_02_24":"J40",
    "Full_JEFF-3.1.1":"J311",
    "JEFF4T3":"J40",
    "JEFF4T4":"J40"
}





dict_sssrea2mt  = {    'total xs':    '1',            'ela scatt xs':    '2',                   'inl scatt xs':    '4',
            'fission xs':    '18',           'nxn xs':    '16',                   'capture xs':    '102',
            'nubar total':    'Nu',           'chi prompt':   'Chi-p',               'chi delayed':    'Nu-d',
            'sab scatt xs':    'Sab','':    'Disap.','':    'Mu-bar'}

''' dictionary for string reformating from mt to txt '''
d_mt2name = {
    '1':  'tot',
    '2':  'el',
    '18': 'fiss',
    '102':'ng',
    '12102':'ng',
    '103':'np',
    '107':'na',
    '4':  "inel",
    '11004':  "inel",}

''' dictionary for string reformating from mt to tex '''
d_mt2tex = {
    '1':      r'\sigma_{n,tot}',
    '2':      r'\sigma_{n,el}',
    '18':     r'\sigma_{n,fiss}',
    '102':    r'\sigma_{n,\gamma}',
    '12102':  r'\sigma_{n,\gamma}',
    '103':    r'\sigma_{n,p}',
    '107':    r'\sigma_{n,\alpha}',
    '4':      r"\sigma_{n,n'_{tot}}",
    '11004':  r"\sigma_{n,n'_{tot}}",
    'chip':   r'\chi_p',
    'nu':     r'\nu',
    'nup':    r'\nu_p',
    'nud':    r'\nu_d',}

for i in range(91-51+1): d_mt2tex[str(i+51)] = "\sigma_{n,n'_{"+str(i+51)+"}}" # ,n_{'+str(i+51)+'
for i in range(200):     d_mt2tex["chip"+str(i/10.)] = r'\chi_p'+"^{"+str(i/10.)+"\,MeV}"
for i in range(20):      d_mt2tex["chip"+str(i)    ] = r'\chi_p'+"^{"+str(i)+"\,MeV}"
