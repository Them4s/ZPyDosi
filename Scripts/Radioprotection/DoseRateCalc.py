import numpy as np

def gen_dose_rate_fct(l_irradiation,time_zero,pos="BertholdCR_arret",log=False):
    """
    Generate a dose-rate function from irradiation history.

    This function builds and returns a callable that computes the dose rate
    as a function of time, based on a sequence of irradiation periods and
    a multi-exponential decay model. The resulting function accounts for
    convolution of radioactive decay during and after irradiation periods.

    Parameters
    ----------
    l_irradiation : list of tuple
        List of irradiation descriptions. Each element must be a tuple
        ``(puiss, duree, begin_of_irradiation)``, where ``puiss`` is the
        irradiation power, ``duree`` is the duration in seconds, and
        ``begin_of_irradiation`` is a datetime object marking the start
        of irradiation.
    time_zero : datetime.datetime
        Reference time used to define the origin of the time axis.
    pos : str, optional
        identifier used to select the decay parameters (detectot/position/reactor state).
        Supported values are ``"BertholdCR_arret"``, ``"BertholdCR_attente"``,
        and ``"lid_attente"``.
    log : bool, optional
        If ``True``, return the logarithm of the computed dose rate.

    Returns
    -------
    callable
        Function ``f(x)`` that computes the dose rate for a given array-like
        time input ``x`` expressed in seconds relative to ``time_zero``.
    """
    param, fact = None, 1
    
    #param_arret   = [1.2451364800533156e-07,8.318093191502471e-07,2.2042737323258074e-07,4.758921430151674e-06,2.593853897756098e-06,2.013179065086507e-05,1.55666838913216e-05,6.4658172636912e-05,9.936420603633325e-05,0.00019702638151941713,0.0004609425901585006,0.0007492392023653782,0.0031568948415931827,0.00393759471207397]
    #param_attente = [2.5335812589491014e-08,9.577028253967527e-07,2.2849843887766297e-07,1.1970105942663165e-05,1.6003083663493403e-06,4.994901691840768e-05,1.770541359426842e-06,4.994168677332405e-05,2.36746695531472e-05,0.00018944042878880202,9.860535326323562e-05,0.0007047097275239984,0.0006101259842882184,0.0031886596819304244]
    
    #param_arret   = [1.0109471672792641e-07,6.548177602477454e-07,2.1595648327485336e-07,3.7106017909241045e-06,2.631387785907707e-06,1.9978009084857362e-05,1.5206882175299968e-05,6.400485860886686e-05,0.00010316494373063211,0.00019820024531952003,0.00047441958229777295,0.0007696677079145239,0.0025669151923934123,0.0038414102956936032,0.01725290518660394,0.014369443132394728]
    #param_attente = [2.5094284150451363e-08,6.535974822819132e-07,4.509668544751526e-08,4.030848530334835e-06,8.198598756985005e-07,2.4291829720853755e-05,7.418536951193905e-07,5.913893189261338e-05,7.419288867511635e-06,9.5628362511231e-05,3.222022332385608e-05,0.0002810240306114093,0.0001503736665410727,0.0009998901187622219,0.0042699400813268245,0.007962640079772003]

    # modif du 10 sept, apres ajout des donnees de l arret long de l ete 2020
    param_arret = [7.631439062123619e-08,5.246032670309735e-07,1.870820064115664e-07,2.718852274243294e-06,2.055549279184006e-06,1.7348290422538165e-05,1.3035505715717224e-05,5.6738137516435025e-05,9.722797459137301e-05,0.0001858323531377628,0.0004443992503422421,0.0007222141243386814,0.0021718545585811587,0.003477246958533186,0.01582245967036667,0.013125507774425529]
    param_attente = [2.5094284150451363e-08,6.535974822819132e-07,4.509668544751526e-08,4.030848530334835e-06,8.198598756985005e-07,2.4291829720853755e-05,7.418536951193905e-07,5.913893189261338e-05,7.419288867511635e-06,9.5628362511231e-05,3.222022332385608e-05,0.0002810240306114093,0.0001503736665410727,0.0009998901187622219,0.0042699400813268245,0.007962640079772003]


    if pos=="BertholdCR_arret":
        param = param_arret
    elif pos=="BertholdCR_attente":
        param = param_attente
    elif pos=="lid_attente":
        fact = 0.025
        param = param_attente
    else:
        print("ERROR - gen_dose_rate_fct - pos",pos,"not in <BertholdCR_arret, BertholdCR_attente, lid_attente>")
        exit()
    def fct(x, param=param):
        x = np.array(x)
        v = x*0
        for (puiss, duree, begin_of_irradiation) in l_irradiation:        # loop on the irradiations
            t0b = (begin_of_irradiation-time_zero).total_seconds()
            t1b = t0b + duree
            #print("         ",t0b, t1b)
            for iparam in range(int(len(param)/2)):                        # loop on the fit order
                ai,li = param[2*iparam], param[2*iparam+1]
                for i in range(len(x)):                                    # 1J decay rate = sum_i a_i*exp(-l_i*t),
                    t1b_loc = max(min(t1b,x[i]),t0b)                    # so the convolution from t0 to t1 is:
                    if x[i]>t0b:
                        v[i] += puiss*ai/li * (np.exp(-li*(x[i]-t1b_loc)) - np.exp(-li*(x[i]-t0b)))
        v *= fact
        return v if not log else np.log(v)
    return fct