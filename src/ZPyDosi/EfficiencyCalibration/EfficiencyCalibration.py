from ..Common.utils_general import *
from ..Stats.Stats import *
import numpy as np
class EfficiencyCalibrationG2K:
    ''' Class to compute and store efficiency calibration of the Genie-2000 software'''
    def __init__(self, key):
        #self.param = [0.179,  -25.017, 15.102, -3.579, 0.378,  -0.015  ]
        #self.param = [0.1791, -25.02,  15.10 , -3.579, 0.3775, -0.01491]
        self.param = [0.1791, -25.017, 15.102, -3.579, 0.3775, -0.01491]
        self.raw_data_e = np.array([121.78,  244.69,  344.27,  411.11,  443.98,  778.89,  867.32,  964.01,  1085.78, 1112.02, 1407.95])
        self.raw_data_v = np.array([0.00483, 0.00370, 0.00291, 0.00256, 0.00240, 0.00159, 0.00147, 0.00136, 0.00126, 0.00124, 0.00103])
        
    def get_eff(self, e):
        if type(e) == float : e=np.array([e])
        log_e = np.log(e)
        log_e_n = np.zeros(len(e)) + 1
        log_eff = np.zeros(len(e))
        for p in self.param:
            log_eff += log_e_n*p
            log_e_n *= log_e
        return np.exp(log_eff)
    def get_eff_sig(self, e):
        return self.get_eff(e)[0], 0
    def get_lval_mcov(self, l_e):
        lval = self.get_eff(l_e)
        return lval, np.zeros((len(lval),len(lval)))

#gamma energy [keV]       846.7638          1368.626          411.802           336.241           411.802           834.848           834.848           
#l_inten                  0.9885            0.999934          0.9562            0.459             0.9562            0.99976           0.99976           
#l_calib_ratio_v          1.0               1.0               1.0               1.0               1.0               1.0               33.9362           
#l_calib_ratio_s          0.0               0.0               0.0               0.0               0.0               0.0               0.6043            
#l_calib_ratio_key        None              None              None              None              None              None              Fe_RX_L1          
#l_eff_gamma              0.00140882056652  0.00097034339668  0.00240281767887  0.00281464359963  0.00240281767887  0.00142305679133  0.0482931398819   


class EfficiencyCalibration:
    '''
    Container for the Efficiency calibration of HPGE.

    The class reads and stores the information from txt file produced by the spectrum_calib.py
    including the efficiency curve and covariance data
    '''
    def __init__(self, path):
        """
        Initialize the EfficiencyCalibration object containing all informations 
        necessary to the analysis.

        Parameters
        ----------
        path : str
            Path to the txt file containing the efficiency curve and covariance data
        
        Returns
        -------
        None
            The object is initialized in place.
        """
        lines = open(os.path.expandvars(path)).readlines()
        self.raw_data_e  =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))           #
        self.raw_data_v  =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))           #
        self.raw_data_s  =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))           #
        self.nrj         =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))        # nrj     121.7817         123.069218819     ...
        self.eff         =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))        # eff     0.00489937793846   0.00490226768176  ...
        self.eff_sig     =  np.array(lmap(lambda s:float(s), lines.pop(0).split()[1:]))        # stdv     1.64991437579e-05  1.60173859944e-05 ...
        self.eff_sig_rel =  self.eff_sig/self.eff
        lines.pop(0)                                        # stdv_rel 0.00336759971677   0.00326734218411  ...
        lines.pop(0)                                        # corr
        self.cor     = np.array(lmap(lambda line: lmap(lambda s:float(s),line.split()) , lines))    # 1.0                0.99100048643 ... \n 0.99100048643      1.0           ...
        self.cov     = cor_sig_to_cov(self.cor, self.eff_sig)
        self.cov_rel = cor_sig_to_cov(self.cor, self.eff_sig_rel)
    def get_eff_sig(self, e):
        '''
        Returns the efficiency and uncerrtainty values at energy for the energy e

        Parameters
        ----------
        e : float [keV]
            energy for which the efficiency is evaluated
        
        Returns
        -------
        (eff,sig): (float,float)
            tuple of the evaluated efficiency and uncertainty
        '''
        tmp = list(self.nrj>e)
        if True in tmp:    ie =  tmp.index(True)- 1
        else:        ie = len(self.nrj)-2
        f = (e-self.nrj[ie])/(self.nrj[ie+1]-self.nrj[ie])
        return (1-f)*self.eff[ie] + f*self.eff[ie+1] , (1-f)*self.eff_sig[ie] + f*self.eff_sig[ie+1]
    def get_lval_mcov(self, l_e):
        '''
        Returns the efficiency and covariance matrix for a list of energies

        Parameters
        ----------
        l_e : list of float  [keV]
            energies for which the efficiency and covariance matrix are returns
        
        Returns
        -------
        (l_eff,m_cov): (ndarray,ndarray)
            tuple of the evaluated efficiencies and covariances for the energy of interest
        '''
        l_v = np.zeros(len(l_e))
        m_cov = np.zeros((len(l_e), len(l_e)))
        for i in range(len(l_e)):
            l_v[i] = self.get_eff_sig(l_e[i])[0]
            for j in range(len(l_e)):
                m_cov[i,j] = self.get_cov(l_e[i], l_e[j])
        return l_v, m_cov
    
    def pos(self, l,v):
        """
        Find the index of the largest element smaller than a given value.

        The method searches a sorted sequence and returns the index of the
        last element that is strictly less than the specified value. A
        binary-search-like strategy is used for efficiency.

        Parameters
        ----------
        l : sequence
            Sorted sequence of comparable values.
        v : object
            Value to be located within the sequence.

        Returns
        -------
        int
            Index of the largest element in ``l`` that is smaller than ``v``.
        """
        #i1 = 0
        #while l[i1]<v:
        #    i1 += 1
        var=int(len(l)/2)
        i = 0
        while var>=1:
            while i+var<len(l) and l[i+var]<v:
                i += var
            var /= 2
            var=int(var/2)
        return i
    def get_cor(self, e1, e2):
        '''
        Returns the correlation between the efficiencies of 2 given energies

        Parameters
        ----------
        e1 : float [keV]
            First energy value

        e2 : float [keV]
            First energy value
        
        Returns
        -------
        cor: float
            Correlation between the efficiencies of the 2 given energies
        '''
        return self.cor[self.pos(self.nrj, e1),self.pos(self.nrj, e2)]
    def get_cov(self, e1, e2):
        '''
        Returns the covariance between the efficiencies of 2 given energies

        Parameters
        ----------
        e1 : float [keV]
            First energy value

        e2 : float [keV]
            First energy value
        
        Returns
        -------
        cor: float
            Covariance between the efficiencies of the 2 given energies
        '''
        return self.cov[self.pos(self.nrj, e1),self.pos(self.nrj, e2)]
    def get_cov_rel(self, e1, e2):
        '''
        Returns the relative covariance between the efficiencies of 2 given energies

        Parameters
        ----------
        e1 : float [keV]
            First energy value

        e2 : float [keV]
            First energy value 
        
        Returns
        -------
        cor: float
            Relative covariance between the efficiencies of the 2 given energies
        '''
        return self.cov_rel[self.pos(self.nrj, e1),self.pos(self.nrj, e2)]