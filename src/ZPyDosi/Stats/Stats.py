############################################################################################################
############################################################################################## variance & co
from ..Common.utils_general import *
import numpy as np

def imoyvar_list(l_v, l_w = None):
    """
    Compute the weighted mean and standard deviation of a list of values.

    The function evaluates the weighted average and the corresponding
    weighted standard deviation for a set of values. If no weights are
    provided, all values are assumed to have equal weight.

    Parameters
    ----------
    l_v : array-like
        Sequence of numerical values.
    l_w : array-like, optional
        Sequence of weights associated with ``l_v``. If ``None``, unit
        weights are used.

    Returns
    -------
    tuple
        Tuple ``(mean, std)`` where ``mean`` is the weighted mean of the
        values and ``std`` is the weighted standard deviation.
    """
    if l_w is None: l_w = np.zeros(len(l_v))+1.
    l_v, l_w = np.array(l_v), np.array(l_w)
    sum_w = sum(l_w)
    moy = sum(l_v*l_w)/sum_w
    var = (sum((l_v-moy)**2*l_w)/sum_w)**0.5
    return moy, var

def imoyvar(l_l_v, l_w = None, do_jackknife=False):# en realité ça retourne les std ;)
    """
    Compute the weighted mean and standard deviation of vector-valued samples.

    The function operates on a list of vectors and computes the weighted mean
    and pointwise weighted standard deviation across samples. Optionally, a
    jackknife estimate of the standard deviation can also be computed.

    Notes
    -----
    Despite the name, the function returns standard deviations (square roots
    of variances), not variances.

    Parameters
    ----------
    l_l_v : array-like
        List (or array) of vectors with identical length. Each element
        represents one sample.
    l_w : array-like, optional
        Weights associated with each sample. If ``None``, all samples are
        equally weighted.
    do_jackknife : bool, optional
        If ``True``, compute an additional jackknife estimate of the standard
        deviation.

    Returns
    -------
    tuple
        If ``do_jackknife`` is ``False``, returns ``(mean, std)`` where:

        - ``mean`` is the weighted mean vector,
        - ``std`` is the weighted standard deviation vector.

        If ``do_jackknife`` is ``True``, returns ``(mean, std, jk_std)`` where
        ``jk_std`` is the jackknife-estimated standard deviation vector.
    """
    t = len(l_l_v[0])
    nxs = len(l_l_v)
    sum_w = nxs if l_w is None else sum(l_w[:nxs])
    moy = np.zeros(t)
    for x in range(nxs):
        w = 1 if l_w is None else l_w[x]
        moy += np.array(l_l_v[x]) * w / sum_w
    var = np.zeros(t)
    for x in range(nxs):
        w = 1 if l_w is None else l_w[x]
        var += (np.array(l_l_v[x])-moy)**2 * w / sum_w
    var = var**0.5
    if not do_jackknife:
        return moy, var # en realité ça retourne les std ;)
    else:    
        l_var = np.array([nxs*var**2 - (nxs-1)*imoyvar(np.array(l_l_v)[np.arange(len(l_l_v))!=num])[1]**2 for num in range(nxs)])
        jkk_var = np.var(l_var,axis=0)/nxs
        return moy, var, jkk_var**0.5 # en realité ça retourne les std ;)

    
def sig2covdiag(sig):
    """
    Construct a diagonal covariance matrix from standard deviations.

    The function converts a vector of standard deviations into a diagonal
    covariance matrix by squaring each element and placing it on the
    diagonal.

    Parameters
    ----------
    sig : array-like
        Vector of standard deviations.

    Returns
    -------
    numpy.ndarray
        Diagonal covariance matrix corresponding to ``sig``.
    """
    return np.diag(sig)**2

def cor_sig_to_cov(cor, std):
    """
    Convert a correlation matrix and standard deviations to a covariance matrix.

    The function computes the covariance matrix from a correlation matrix
    and a vector of standard deviations using the relation
    ``cov[i, j] = cor[i, j] * std[i] * std[j]``.

    Parameters
    ----------
    cor : array-like
        Correlation matrix.
    std : array-like
        Vector of standard deviations corresponding to the variables.

    Returns
    -------
    numpy.ndarray
        Covariance matrix constructed from ``cor`` and ``std``.
    """
    cov  = cor * 1.
    cov *= std[:, None]
    cov *= std[None, :]
    return cov
    
def cov_to_sig_cor(cov, err=1e-100):
    """
    Convert a covariance matrix to standard deviations and correlation matrix.

    The function extracts the standard deviations from the diagonal of the
    covariance matrix and computes the corresponding correlation matrix.
    A small regularization term can be added to avoid division by zero.

    Parameters
    ----------
    cov : array-like
        Covariance matrix.
    err : float, optional
        Small regularization value added to denominators to prevent division
        by zero.

    Returns
    -------
    tuple
        Tuple ``(std, cor)`` where:

        - ``std`` is a vector of standard deviations,
        - ``cor`` is the corresponding correlation matrix.
    """
    std = np.sqrt(np.diag(cov))
    cor  = cov*1.
    cor /= (std[:, None]+err)
    cor /= (std[None, :]+err)
    return std, cor

def cov_sum(mean1_cov1, mean2_cov2):
    """
    Combine two independent mean–covariance pairs by summation.

    The function adds two mean vectors and their corresponding covariance
    matrices, assuming the two quantities are statistically independent.

    Parameters
    ----------
    mean1_cov1 : tuple
        Tuple ``(mean1, cov1)`` where ``mean1`` is a mean vector and
        ``cov1`` is its covariance matrix.
    mean2_cov2 : tuple
        Tuple ``(mean2, cov2)`` where ``mean2`` is a mean vector and
        ``cov2`` is its covariance matrix.

    Returns
    -------
    tuple
        Tuple ``(mean, cov)`` representing the summed mean vector and
        summed covariance matrix.
    """
    (mean1,cov1), (mean2,cov2) = mean1_cov1, mean2_cov2
    return mean1+mean2 , cov1 + cov2

def cov_inv(mean_cov,err = 1e-100):
    """
    Compute the inverse of a mean–covariance pair under element-wise inversion.

    The function applies an element-wise inversion to the mean vector and
    propagates the covariance accordingly using first-order error propagation.
    A small regularization term can be added to denominators to avoid division
    by zero.

    Parameters
    ----------
    mean_cov : tuple
        Tuple ``(mean, cov)`` where ``mean`` is a vector of mean values and
        ``cov`` is the corresponding covariance matrix.
    err : float, optional
        Small regularization value added to denominators to prevent division
        by zero.

    Returns
    -------
    tuple
        Tuple ``(mean_inv, cov_inv)`` where:

        - ``mean_inv`` is the element-wise inverse of the mean vector,
        - ``cov_inv`` is the propagated covariance matrix of the inverted mean.
    """
    mean, cov = mean_cov
    return 1./mean, (cov/((mean**2)[:, None]+err)) / ((mean**2)[None, :]+err)

def cov_mult(mean1_cov1, mean2_cov2):
    """
    Multiply two independent mean–covariance pairs.

    The function computes the element-wise product of two mean vectors and
    propagates their uncertainties assuming statistical independence between
    the two quantities. Covariance propagation follows first-order error
    propagation for products.

    Parameters
    ----------
    mean1_cov1 : tuple
        Tuple ``(mean1, cov1)`` where ``mean1`` is a mean vector and
        ``cov1`` is its covariance matrix.
    mean2_cov2 : tuple
        Tuple ``(mean2, cov2)`` where ``mean2`` is a mean vector and
        ``cov2`` is its covariance matrix.

    Returns
    -------
    tuple
        Tuple ``(mean, cov)`` where:

        - ``mean`` is the element-wise product of ``mean1`` and ``mean2``,
        - ``cov`` is the propagated covariance matrix of the product.
    """
    (mean1,cov1), (mean2,cov2) = mean1_cov1, mean2_cov2
    return mean1*mean2, (cov1*mean2[:, None])*mean2[None,:] + (cov2*mean1[:, None])*mean1[None,:]
    #return mean1*mean2, abs((cov1*mean2[:, None])*mean2[None,:]) + abs((cov2*mean1[:, None])*mean1[None,:])

def cov_l_mult(l_mean_cov):
    """
    Multiply a list of independent mean–covariance pairs.

    The function applies successive element-wise multiplications to a list
    of ``(mean, covariance)`` pairs, propagating uncertainties at each step
    under the assumption that all quantities are statistically independent.

    Parameters
    ----------
    l_mean_cov : list of tuple
        List of tuples ``(mean, cov)``, where each ``mean`` is a vector of
        mean values and each ``cov`` is the corresponding covariance matrix.

    Returns
    -------
    tuple
        Tuple ``(mean, cov)`` representing the element-wise product of all
        input means and the propagated covariance matrix.
    """
    head = cov_mult(l_mean_cov[0], l_mean_cov[1])
    if len(l_mean_cov)>2:
        return cov_l_mult([head]+l_mean_cov[2:])
    return head




if False:
    v,m = np.array([1,2]), np.array([[0.1, 0.05],[0.05,0.1]])
    aff_decription_s_v_cov("a",(v,m))
    aff_decription_s_v_cov("b",cov_inv((v,m)))
    exit()


def icovar_jkk(l_l_v, l_w=None, do_cor=False, do_jackknife=False, fast_jackknife=True, blabla=False, nb_jkk=None, fast=True):
    """
    Compute covariance (and optionally correlation) with optional jackknife uncertainty.

    The function computes the covariance matrix of a set of vector-valued
    samples, optionally using sample weights. It can also compute the
    corresponding correlation matrix. When requested, a jackknife procedure
    is applied to estimate the uncertainty (standard deviation) of the
    covariance (and correlation) estimates.

    Several options are provided to trade accuracy for speed, including an
    incremental/analytic leave-one-out update for the jackknife, optional
    subsampling of jackknife replicates, and vectorized updates.

    Parameters
    ----------
    l_l_v : array-like
        Array-like of shape ``(n_samples, n_dim)`` containing the sample
        vectors.
    l_w : array-like, optional
        Optional weights associated with samples. Passed to ``numpy.cov`` as
        ``aweights`` when computing the covariance.
    do_cor : bool, optional
        If ``True``, also compute and return the correlation matrix.
    do_jackknife : bool, optional
        If ``True``, compute a jackknife estimate of the uncertainty of the
        covariance estimate (and correlation estimate if ``do_cor`` is ``True``).
    fast_jackknife : bool, optional
        If ``True``, use a faster leave-one-out covariance update rather than
        recomputing covariance from scratch for each jackknife replicate.
    blabla : bool, optional
        If ``True``, print timing/debug information.
    nb_jkk : int, optional
        Number of jackknife replicates to use. If ``None``, use all samples.
        If larger than the number of samples, it is capped.
    fast : bool, optional
        If ``True``, use a vectorized leave-one-out update when performing the
        fast jackknife computation.

    Returns
    -------
    numpy.ndarray or tuple
        Depending on the options, returns:

        - If ``do_cor`` is ``False`` and ``do_jackknife`` is ``False``:
          ``cov``

        - If ``do_cor`` is ``True`` and ``do_jackknife`` is ``False``:
          ``(cov, cor)``

        - If ``do_cor`` is ``False`` and ``do_jackknife`` is ``True``:
          ``(cov, cov_jk_std)``

        - If ``do_cor`` is ``True`` and ``do_jackknife`` is ``True``:
          ``(cov, cor, cov_jk_std, cor_jk_std)``

        where ``cov_jk_std`` and ``cor_jk_std`` are jackknife-estimated
        standard deviations of the covariance and correlation matrices.
    """
    t0 = time.time()
    err = 1e-50
    l_l_v = np.array(l_l_v)
    cov = np.cov(l_l_v.T, aweights=l_w)
    moy = sum(l_l_v) / len(l_l_v)
    t1 = time.time()
    if do_cor:
        cor = cov*1.
        stddev = np.sqrt(np.diag(cov))
        cor /= (stddev[:, None]+err)
        cor /= (stddev[None, :]+err)
    t2 = time.time()
    if do_jackknife:
        if l_w is not None and sum(l_w) != len(l_w):
            new_l_l_v = []
            for i in range(len(l_w)):
                if rand()<l_w[i]:
                    new_l_l_v += [l_l_v[i]]
            l_l_v = np.array(new_l_l_v)
            print("only",len(l_l_v),"remainings")
            l_w = None
            loc_cov = np.cov(l_l_v.T, aweights=l_w)
            loc_moy = sum(l_l_v) / len(l_l_v)
            if do_cor:
                loc_cor = loc_cov*1.
                loc_stddev = np.sqrt(np.diag(loc_cov))
                loc_cor /= (loc_stddev[:, None]+err)
                loc_cor /= (loc_stddev[None, :]+err)
        else:
            loc_cov = cov
            loc_moy = moy
            if do_cor:
                loc_cor = cor
            
        if nb_jkk is None: nb_jkk = len(l_l_v)
        if nb_jkk > len(l_l_v): nb_jkk = len(l_l_v)
        def moy_without(idx):
            if not fast_jackknife:
                return icovar_jkk(l_l_v[np.arange(len(l_l_v))!=idx])
            else:
                tmp_cov = loc_cov*1.
                if not fast:
                    for i in range(len(tmp_cov)):
                        #tmp_cov[i,:] = (tmp_cov[i,:] * len(l_l_v) - (l_l_v[idx][i]-moy[i])*(l_l_v[idx][:]-moy[:])) / (len(l_l_v)-1)
                        for j in range(len(tmp_cov)):
                            tmp_cov[i,j] = (tmp_cov[i,j] * len(l_l_v) - (l_l_v[idx][i]-loc_moy[i])*(l_l_v[idx][j]-loc_moy[j])) / (len(l_l_v)-1)
                else:
                    #tmp_cov[:,:] = (tmp_cov[:,:] * len(l_l_v) - (l_l_v[idx][:,None]-moy[:,None])*(l_l_v[idx][None,:]-moy[None,:])) / (len(l_l_v)-1)
                    tmp_cov = (tmp_cov * len(l_l_v) - (l_l_v[idx][:,None]-loc_moy[:,None])*(l_l_v[idx][None,:]-loc_moy[None,:])) / (len(l_l_v)-1)
                return tmp_cov
        def moy_without_cor(idx):
            tmp_cor = moy_without(idx)
            tmp_stddev = np.sqrt(np.diag(tmp_cor)+err)
            tmp_cor /= (tmp_stddev[:, None]+err)
            tmp_cor /= (tmp_stddev[None, :]+err)
            return tmp_cor
        l_jkk = list(range(len(l_l_v)))
        while len(l_jkk) > nb_jkk: l_jkk.pop(int(rand()*len(l_jkk)))
        jackknife_cov_var = np.sum((moy_without(i)-loc_cov)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        #jackknife_cov_var = np.sum((dmoy_without(i))**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        if do_cor:
            jackknife_cor_var = np.sum((moy_without_cor(i)-loc_cor)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
    t3 = time.time()
    #print t3-t2
    if not do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s")
        return cov
    if do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s")
        return cov, cor
    if not do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and jkk in",t3-t2,"s")
        return cov, jackknife_cov_var**0.5
    if do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s and jkk in",t3-t2,"s")
        return cov, cor, jackknife_cov_var**0.5, jackknife_cor_var**0.5
    print("icovar_jkk - error")
    exit()
    
    
def icovar_jkk_w_nan(l_l_v, l_w=None, do_cor=False, do_jackknife=False, fast_jackknife=False, blabla=False, nb_jkk=None, fast=True):
    """
    Compute covariance (and optionally correlation) with optional jackknife uncertainty.
    Compatible with data set including NaNs. 

    The function computes the covariance matrix of a set of vector-valued
    samples, optionally using sample weights. It can also compute the
    corresponding correlation matrix. When requested, a jackknife procedure
    is applied to estimate the uncertainty (standard deviation) of the
    covariance (and correlation) estimates.

    Several options are provided to trade accuracy for speed, including an
    incremental/analytic leave-one-out update for the jackknife, optional
    subsampling of jackknife replicates, and vectorized updates.

    Parameters
    ----------
    l_l_v : array-like
        Array-like of shape ``(n_samples, n_dim)`` containing the sample
        vectors.
    l_w : array-like, optional Not supported yet
        Optional weights associated with samples. Passed to ``numpy.cov`` as
        ``aweights`` when computing the covariance.
    do_cor : bool, optional
        If ``True``, also compute and return the correlation matrix.
    do_jackknife : bool, optional
        If ``True``, compute a jackknife estimate of the uncertainty of the
        covariance estimate (and correlation estimate if ``do_cor`` is ``True``).
    fast_jackknife : bool, optional
        If ``True``, use a faster leave-one-out covariance update rather than
        recomputing covariance from scratch for each jackknife replicate.
    blabla : bool, optional
        If ``True``, print timing/debug information.
    nb_jkk : int, optional
        Number of jackknife replicates to use. If ``None``, use all samples.
        If larger than the number of samples, it is capped.
    fast : bool, optional
        If ``True``, use a vectorized leave-one-out update when performing the
        fast jackknife computation.

    Returns
    -------
    numpy.ndarray or tuple
        Depending on the options, returns:

        - If ``do_cor`` is ``False`` and ``do_jackknife`` is ``False``:
          ``cov``

        - If ``do_cor`` is ``True`` and ``do_jackknife`` is ``False``:
          ``(cov, cor)``

        - If ``do_cor`` is ``False`` and ``do_jackknife`` is ``True``:
          ``(cov, cov_jk_std)``

        - If ``do_cor`` is ``True`` and ``do_jackknife`` is ``True``:
          ``(cov, cor, cov_jk_std, cor_jk_std)``

        where ``cov_jk_std`` and ``cor_jk_std`` are jackknife-estimated
        standard deviations of the covariance and correlation matrices.
    """
    t0 = time.time()
    err = 1e-50
    if l_w:
        print("l_w not implemented in icovar_jkk_w_nan yet, exit")
        exit()
    l_l_v = np.array(l_l_v)
    cov = np.array(np.ma.cov(np.ma.masked_invalid(l_l_v.T)),dtype=np.float64)
    moy = np.nanmean(l_l_v,axis=0)
    t1 = time.time()
    if do_cor:
        cor = cov*1.
        stddev = np.sqrt(np.diag(cov))
        cor /= (stddev[:, None]+err)
        cor /= (stddev[None, :]+err)
    t2 = time.time()
    if do_jackknife:
        if l_w is not None and sum(l_w) != len(l_w):
            new_l_l_v = []
            # for i in range(len(l_w)):
                # if rand()<l_w[i]:
                    # new_l_l_v += [l_l_v[i]]
            # l_l_v = np.array(new_l_l_v)
            # print("only",len(l_l_v),"remainings")
            # l_w = None
            # loc_cov = np.cov(l_l_v.T, aweights=l_w)
            # loc_moy = sum(l_l_v) / len(l_l_v)
            # if do_cor:
                # loc_cor = loc_cov*1.
                # loc_stddev = np.sqrt(np.diag(loc_cov))
                # loc_cor /= (loc_stddev[:, None]+err)
                # loc_cor /= (loc_stddev[None, :]+err)
        else:
            loc_cov = cov
            loc_moy = moy
            if do_cor:
                loc_cor = cor
            
        if nb_jkk is None: nb_jkk = len(l_l_v)
        if nb_jkk > len(l_l_v): nb_jkk = len(l_l_v)
        def moy_without(idx):
            if not fast_jackknife:
                return icovar_jkk_w_nan(l_l_v[np.arange(len(l_l_v))!=idx])
            else:
                print("fast_jkk not allowed")
                exit()
            '''
                tmp_cov = loc_cov*1.
                if not fast:
                    for i in range(len(tmp_cov)):
                        #tmp_cov[i,:] = (tmp_cov[i,:] * len(l_l_v) - (l_l_v[idx][i]-moy[i])*(l_l_v[idx][:]-moy[:])) / (len(l_l_v)-1)
                        for j in range(len(tmp_cov)):
                            tmp_cov[i,j] = (tmp_cov[i,j] * len(l_l_v) - (l_l_v[idx][i]-loc_moy[i])*(l_l_v[idx][j]-loc_moy[j])) / (len(l_l_v)-1)
                else:
                    #tmp_cov[:,:] = (tmp_cov[:,:] * len(l_l_v) - (l_l_v[idx][:,None]-moy[:,None])*(l_l_v[idx][None,:]-moy[None,:])) / (len(l_l_v)-1)
                    tmp_cov = (tmp_cov * len(l_l_v) - (l_l_v[idx][:,None]-loc_moy[:,None])*(l_l_v[idx][None,:]-loc_moy[None,:])) / (len(l_l_v)-1)
                return tmp_cov
            '''
        def moy_without_cor(idx):
            tmp_cor = moy_without(idx)
            tmp_stddev = np.sqrt(np.diag(tmp_cor)+err)
            tmp_cor /= (tmp_stddev[:, None]+err)
            tmp_cor /= (tmp_stddev[None, :]+err)
            return tmp_cor
        l_jkk = list(range(len(l_l_v)))
        while len(l_jkk) > nb_jkk: l_jkk.pop(int(rand()*len(l_jkk)))
        jackknife_cov_var = np.sum((moy_without(i)-loc_cov)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        #jackknife_cov_var = np.sum((dmoy_without(i))**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
        if do_cor:
            jackknife_cor_var = np.sum((moy_without_cor(i)-loc_cor)**2.0 for i in l_jkk) * (len(l_l_v)/len(l_jkk)) * (len(l_l_v)-1.)/(len(l_l_v))
    t3 = time.time()
    #print t3-t2
    if not do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s")
        return cov
    if do_cor and not do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s")
        return cov, cor
    if not do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and jkk in",t3-t2,"s")
        return cov, jackknife_cov_var**0.5
    if do_cor and do_jackknife:
        if blabla: print("cov calculation in",t1-t0,"s and cor in",t2-t1,"s and jkk in",t3-t2,"s")
        return cov, cor, jackknife_cov_var**0.5, jackknife_cor_var**0.5
    print("icovar_jkk_w_nan - error")
    exit()

def weigted_cirmc_mean(Vec,l_w=None):
    """
    Compute the weighted circular mean and dispersion of angular data.

    The function evaluates the circular (angular) mean and an associated
    dispersion measure for a set of angles using complex exponentials.
    Weights can be applied to account for non-uniform importance of samples.

    Parameters
    ----------
    Vec : array-like
        Sequence of angular values (in radians).
    l_w : array-like, optional
        Weights associated with each angle. If ``None``, all angles are
        equally weighted.

    Returns
    -------
    tuple
        Tuple ``(mean, std)`` where:

        - ``mean`` is the weighted circular mean angle (in radians),
        - ``std`` is a circular dispersion measure derived from the
          magnitude of the mean resultant vector.
    """
    Vec=np.array(Vec)
    if l_w is None:
        l_w=np.ones(len(Vec))
    l_w=np.array(l_w)
    Aexp=np.exp(1j*Vec)
    W=sum(l_w)
    mean=np.angle(np.sum(l_w*Aexp)/W)
    std=np.sqrt(-2*np.log(np.abs(np.sum(l_w*Aexp)/W)))
    # print(Aexp)
    return mean, std

from scipy.stats import chi2

def weighted_mean(x, sigma):
    """Compute inverse-variance weighted mean and std."""
    w = 1.0 / sigma**2
    return np.sum(w * x) / np.sum(w), np.sqrt(1/(np.sum(w)))

def chi_squared(x, sigma, mu):
    """Compute chi^2 = sum [ (x_i - mu)^2 / sigma_i^2 ]."""
    return np.sum(((x - mu) ** 2) / sigma**2)

def consistency_test(x, sigma):
    """
    Performs the consistency test:
      - weighted mean
      - chi^2
      - p-value
      - reduced chi^2
    """
    x = np.asarray(x, dtype=float)
    sigma = np.asarray(sigma, dtype=float)
    if x.shape != sigma.shape:
        raise ValueError("x and sigma must have the same shape")
    
    N = x.size
    nu = N - 1

    mu_w, std_w = weighted_mean(x, sigma)
    chi2_stat = chi_squared(x, sigma, mu_w)
    p_value = 1.0 - chi2.cdf(chi2_stat, df=nu)
    chi2_red = chi2_stat / nu
    results={
        "weighted_mean": mu_w,
        "weighted_std": std_w,
        "chi2": chi2_stat,
        "degrees_of_freedom": nu,
        "p_value": p_value,
        "reduced_chi2": chi2_red
    }
    print(f"Weighted mean:         {-results['weighted_mean']:.5f}")
    print(f"Weighted std:          {-results['weighted_std']:.5f}")
    print(f"Chi-squared:           {results['chi2']:.2f}")
    print(f"Degrees of freedom:    {results['degrees_of_freedom']}")
    print(f"Reduced chi-squared:   {results['reduced_chi2']:.3f}")
    print(f"p-value:               {results['p_value']:.4f}")

    return results
