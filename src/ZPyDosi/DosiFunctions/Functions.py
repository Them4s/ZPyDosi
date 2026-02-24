from ..Prints.PrintnSave import aff
from ..Common.utils_general import lmap
from .Dictionaries import d_matdosi_2_data
import numpy as np
from math import pi
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
d_iso2mass = None
mode_irdff_only = False

def _init_d_iso2mass(path_xsdata):
    """
    Initialize the isotope-to-mass lookup dictionary.

    The function reads isotope mass data from the cross-section data source
    and populates a global dictionary mapping isotope identifiers to their
    atomic masses. When multiple entries for the same isotope are found,
    consistency checks are performed and execution is stopped if significant
    discrepancies are detected.

    Returns
    -------
    None
        The global isotope-to-mass dictionary is initialized in place.
    """
    global d_iso2mass
    d_iso2mass = {}
    warn = False
    for iso_complete, mass in map(lambda l: (l.split()[0], float(l.split()[5])),open(path_xsdata).readlines()):            # get the mass from the xsdata
        iso, temp_key = iso_complete[:-4], iso_complete[-4:]
        if not mode_irdff_only or ".34y" == temp_key:  # avoid IRDFF
            if iso in d_iso2mass and abs(mass/d_iso2mass[iso]-1)>1e-4:
                print ("warning - "+aff(iso)+aff(d_iso2mass[iso], l=11, rev=True)+"!= "+aff(mass, l=11, rev=True)+"rel diff: "+aff(d_iso2mass[iso]/mass,l=14))
                warn = True
            d_iso2mass[iso] = mass
    if warn:
        exit()

def get_iso2mass(iso,path_xsdata):
    if d_iso2mass is None: _init_d_iso2mass(path_xsdata)
    return d_iso2mass[iso]

def get_massic_fraction(iso, compo,path_xsdata,suffix="g0.0300c"):
    """
    Compute the mass fraction of a given isotope in a composition.

    The function evaluates the mass fraction of a specified isotope from a
    text composition description by combining isotopic fractions with
    corresponding atomic masses.

    Parameters
    ----------
    iso : str
        Isotope identifier whose mass fraction is to be computed.
    compo : str
        Composition string containing alternating isotope identifiers and
        numerical fractions.

    Returns
    -------
    float
        Mass fraction of the specified isotope within the composition.
    """
    if d_iso2mass is None: _init_d_iso2mass(path_xsdata)
    l_iso_e = compo.split()[::2]
    l_iso_f = lmap(lambda v:float(v), compo.split()[1::2])
    pos = l_iso_e.index(iso+suffix)
    return l_iso_f[pos]*d_iso2mass[l_iso_e[pos][:5]] / sum(lmap(lambda i: l_iso_f[i] * d_iso2mass[l_iso_e[i][:5]],range(len(l_iso_e))))


def get_at_density(mat, iso, path_xsdata):
    """
    Compute the atomic density of an isotope in a material.

    The function calculates the atomic density of a given isotope within a
    specified material using the material composition, density, and the
    isotope atomic mass. The result is expressed in atoms per barn·centimeter.

    Parameters
    ----------
    mat : str
        Material identifier used to retrieve composition and density data.
    iso : str
        Isotope identifier whose atomic density is to be computed.

    Returns
    -------
    float
        Atomic density of the isotope in units of atoms per barn·centimeter.
    """
    at_per_g = 6.022140857e23 / get_iso2mass(iso, path_xsdata)                    # at/g
    mass_frac = get_massic_fraction(iso, d_matdosi_2_data[mat]["compo"], path_xsdata)
    density = d_matdosi_2_data[mat]["den"]
    return at_per_g * mass_frac * density*1e-24                    # at/(barn.cm)


def mass_rad_mat_2_ep(masse, rad, mat):
    """
    Compute the thickness of a material from its mass and radius.

    The function calculates the equivalent thickness of a cylindrical
    material sample given its mass, radius, and material density.

    Parameters
    ----------
    masse : float
        Mass of the material sample in grams.
    rad : float
        Radius of the cylindrical sample in centimeters.
    mat : str
        Material identifier used to retrieve the material density.

    Returns
    -------
    float
        Equivalent thickness of the material in centimeters.
    """
    surf = pi*rad**2            # cm^2
    den  = d_matdosi_2_data[mat]['den']    # g/cm^3
    vol  = masse/den            # cm^3
    return vol/surf                # cm
    
def ep_rad_mat_2_masse(ep, rad, mat):
    """
    Compute the mass of a material from its thickness and radius.

    The function calculates the mass of a cylindrical material sample given
    its thickness, radius, and material density.

    Parameters
    ----------
    ep : float
        Thickness of the material sample in centimeters.
    rad : float
        Radius of the cylindrical sample in centimeters.
    mat : str
        Material identifier used to retrieve the material density.

    Returns
    -------
    float
        Mass of the material sample in grams.
    """
    surf = pi*rad**2            # cm^2
    den  = d_matdosi_2_data[mat]['den']    # g/cm^3
    vol  = surf*ep                # cm^3
    return vol*den                # g




def _weight_2_selfshielding(weight, l_e, l_na, l_a, plot=False):
    """
    Estimate the self-shielding factor as a function of material weight.

    The function fits an empirical model to the ratio of attenuated to
    non-attenuated quantities as a function of energy, and evaluates the
    resulting fit at a given material weight. An optional diagnostic plot
    can be produced to visualize the fit quality.

    Parameters
    ----------
    weight : float
        Material weight at which the self-shielding factor is evaluated.
    l_e : array-like
        Energy values used for the fit.
    l_na : array-like
        Reference (non-attenuated) values corresponding to ``l_e``.
    l_a : array-like
        Attenuated values corresponding to ``l_e``.
    plot : bool, optional
        If ``True``, display a diagnostic plot of the fitted model and
        stop execution.

    Returns
    -------
    float
        Estimated self-shielding factor evaluated at the given weight.
    """
    #def my_fct(x, a, b, c):  return a*np.exp(b*x) + c
    def my_fct(x, a, b,c,d): return a*np.exp(-b*x)+c*x+d
    popt, ipcov =  curve_fit(my_fct, l_e, l_a/l_na)
    def my_fct(x, a, b,c,d,e): return a*np.exp(-b*x)+c*np.exp(-d*x)+e
    popt, ipcov =  curve_fit(my_fct, l_e, l_a/l_na,p0=list(popt[:2])+[0,0,0])
    if plot:
        fig2 = plt.figure(2, figsize=(16,5))
        ax = plt.subplot(1,1,1)
        ax.plot(l_e, l_a/l_na,"o")
        l_e2=np.arange(0,l_e[-1],l_e[-1]/1000)
        ax.plot(l_e2, my_fct(l_e2,*popt))
        #ax.set_xscale('log')
        #ax.set_yscale('log')
        plt.show()
        exit()
    return my_fct(weight,*popt)

def weight_2_selfshielding_Au_15mm(weight, plot=False):
    """
    Compute the self-shielding factor for a 15 mm in diameter gold sample.

    The function evaluates the self-shielding correction factor as a
    function of sample weight for a gold (Au) geometry with a fixed
    diameter of 15 mm. The correction is derived from precomputed
    attenuated and non-attenuated reference data.

    Parameters
    ----------
    weight : float
        Sample weight at which the self-shielding factor is evaluated.
    plot : bool, optional
        If ``True``, display a diagnostic plot of the fitted model and
        stop execution.

    Returns
    -------
    float
        Self-shielding correction factor for the given sample weight.
    """
    l_e  = np.array( [0]+[0.0005,0.001,0.002,0.004,0.008,0.016,0.032,0.064,0.128,0.256])                    # masse
    l_na = np.array( [1]+[4.95E-07,1.02E-06,2.11E-06,4.12E-06,8.70E-06,1.65E-05,3.33E-05,6.29E-05,1.22E-04,2.32E-04])    # without abs
    l_a  = np.array( [1]+[4.81E-07,9.69E-07,1.96E-06,3.81E-06,7.02E-06,1.33E-05,2.37E-05,3.93E-05,6.78E-05,1.13E-04])    # with abs
    return _weight_2_selfshielding(weight, l_e, l_na, l_a, plot=plot)