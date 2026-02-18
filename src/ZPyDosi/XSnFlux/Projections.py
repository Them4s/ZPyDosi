import numpy as np
############################################################################################################
######################################################################################## merge/project lists

def get_interpol(l_e, l_v, e):
    """
    Linearly interpolate a value at a given energy.

    The function performs a linear interpolation of values defined on an
    energy grid. It locates the interval in ``l_e`` that contains the target
    energy and interpolates the corresponding value from ``l_v``.

    Parameters
    ----------
    l_e : array-like
        Monotonically increasing sequence of energy values.
    l_v : array-like
        Values corresponding to each energy in ``l_e``.
    e : float
        Energy at which the value is interpolated.

    Returns
    -------
    float
        Interpolated value at energy ``e``.
    """
    ie = 0
    while l_e[ie+1]<e:
        ie += 1
    e1, e2 = l_e[ie], l_e[ie+1]
    avt = (e-e1)/(e2-e1)
    return avt*l_v[ie+1]+(1-avt)*l_v[ie]

def fusion_x(l_x1, l_x2):
    """
    Merge two sequences of values into a sorted list of unique elements.

    The function concatenates two input sequences, sorts the combined list,
    and removes duplicate consecutive values to produce a unique, ordered
    sequence.

    Parameters
    ----------
    l_x1 : array-like
        First sequence of values.
    l_x2 : array-like
        Second sequence of values.

    Returns
    -------
    list
        Sorted list containing the unique elements from both input sequences.
    """
    l_x = sorted(list(l_x1)+list(l_x2))
    i=0
    while i < len(l_x)-1:
        if l_x[i] == l_x[i+1]:    l_x.pop(i)
        else:            i += 1
    return l_x
    
def include_in_mesh(l_e1, l_e2, l_v2):
    """
    Interpolate values onto a merged energy mesh.

    The function merges two energy grids, ``l_e1`` and ``l_e2``, and computes
    a new set of values corresponding to ``l_v2`` interpolated onto the merged
    grid. Values outside the interpolation range are extrapolated using the
    nearest available value.

    Parameters
    ----------
    l_e1 : array-like
        First energy grid to be included in the merged mesh.
    l_e2 : array-like
        Second energy grid associated with the values ``l_v2``.
    l_v2 : array-like
        Values defined on the energy grid ``l_e2``.

    Returns
    -------
    tuple
        Tuple ``(new_l_e2, new_l_v2)`` where:

        - ``new_l_e2`` is the merged and sorted energy grid,
        - ``new_l_v2`` is the array of values interpolated onto ``new_l_e2``.
    """
    new_l_e2 = fusion_x(l_e1, l_e2)
    new_l_v2 = []
    i2 = 0
    for e in new_l_e2:
        if   e==l_e2[i2]:
            new_l_v2 += [l_v2[i2]]
        else:
            while i2+2<len(l_e2) and l_e2[i2+1]<e:
                i2 += 1
            if i2 == len(l_e2)-1:
                new_l_v2 += [l_v2[-1]]
            else:
                avt = (e - l_e2[i2]) / (l_e2[i2+1] - l_e2[i2])
                #avt = (np.log10(e) - np.log10(l_e2[i2])) / (np.log10(l_e2[i2+1]) - np.log10(l_e2[i2]))
                new_l_v2 += [avt*l_v2[i2+1]+(1-avt)*l_v2[i2]]
    return np.array(new_l_e2), np.array(new_l_v2)

def include_in_mesh_piquet_interval(l_e1, l_e2, l_v2):
    """
    Map interval (stepwise) values onto a merged energy mesh.

    The function merges two energy grids, ``l_e1`` and ``l_e2``, and assigns
    to each interval in the merged grid the value from ``l_v2`` corresponding
    to the interval of ``l_e2`` that contains the left edge. This implements
    a piecewise-constant (histogram-like) mapping rather than linear
    interpolation.

    Parameters
    ----------
    l_e1 : array-like
        First energy grid to be included in the merged mesh.
    l_e2 : array-like
        Energy grid defining the intervals associated with ``l_v2``.
    l_v2 : array-like
        Interval values defined over the bins of ``l_e2`` (typically length
        ``len(l_e2) - 1``).

    Returns
    -------
    tuple
        Tuple ``(new_l_e2, new_l_v2)`` where:

        - ``new_l_e2`` is the merged and sorted energy grid,
        - ``new_l_v2`` contains the piecewise-constant values assigned to
          each interval of ``new_l_e2`` (length ``len(new_l_e2) - 1``).
    """
    new_l_e2 = fusion_x(l_e1, l_e2)
    new_l_v2 = []
    i2 = 0
    for e in new_l_e2[:-1]:
        while i2+2<len(l_e2) and l_e2[i2+1]<=e:
            i2 += 1
        new_l_v2 += [l_v2[i2]]
    return np.array(new_l_e2), np.array(new_l_v2)


def projet_vec_interpol(l_e1, l_e2, l_v2):
    """
    Project values defined on one mesh onto another mesh by linear interpolation.

    The function interpolates a vector ``l_v2`` defined on the mesh ``l_e2``
    onto the target mesh ``l_e1``. Boundary handling is performed to ensure
    the source mesh covers the target mesh: if needed, the source mesh is
    extended at the ends with zero-valued padding. Near-equal endpoints are
    snapped to avoid numerical mismatches.

    Parameters
    ----------
    l_e1 : array-like
        Target mesh (monotonically increasing) on which values are requested.
    l_e2 : array-like
        Source mesh (monotonically increasing) associated with ``l_v2``.
    l_v2 : array-like
        Values defined on the source mesh ``l_e2``. Expected to be compatible
        with linear interpolation between successive points.

    Returns
    -------
    numpy.ndarray
        Values of ``l_v2`` linearly interpolated onto the target mesh ``l_e1``.
    """
    l_e1, l_e2, l_v2 = map(lambda t:list(t), [l_e1, l_e2, l_v2])
    if abs(l_e2[0] /(l_e1[0] +1e-20)-1)<1e-10: l_e2[0]  = l_e1[0]
    if abs(l_e2[-1]/(l_e1[-1]+1e-20)-1)<1e-10: l_e2[-1] = l_e1[-1]
    if l_e1[0]<l_e2[0]:
        l_e2 = [l_e1[0],l_e2[0]]+l_e2
        l_v2 = [0,0]+l_v2
    if l_e1[-1]>l_e2[-1]:
        l_e2 = l_e2+[l_e2[-1],l_e1[-1]]
        l_v2 = l_v2+[0,0]
    #if l_e2[-1]>l_e1[-1]:
    #    idlim = len(l_e2)-1
    #    while l_e2[idlim]>l_e1[-1]: idlim -= 1
    #    l_e2, l_v2 = l_e2[:idlim], l_v2[:idlim]
    if l_e1[0]<l_e2[0] or l_e1[-1]>l_e2[-1]:
        print ("Error -  projet_vec_interpol - boundary larger than targer: from " +str([l_e2[0],l_e2[-1]]) +" to "+str([l_e1[0],l_e1[-1]]))
        exit()
    new_l_v2 = []
    ie2 = 0
    for e in l_e1:
        while ie2+3<len(l_e2) and l_e2[ie2+1]< e: ie2 += 1
        avt = (e-l_e2[ie2])/(l_e2[ie2+1]-l_e2[ie2])
        new_l_v2 += [l_v2[ie2] * (1-avt) + l_v2[ie2+1]*avt]
    return np.array(new_l_v2)

def projet_vec_intervals_from_continus(l_e1, l_e2, l_v2):

    """
    Project continuous values onto target intervals by averaging over bins.

    The function maps a continuous function sampled at points ``(l_e2, l_v2)``
    onto a target interval mesh ``l_e1`` (interpreted as bin edges). For each
    target interval, it computes the average value of the continuous function
    over that interval using trapezoidal integration.

    Boundary handling ensures the source domain covers the target domain. If
    needed, the source mesh can be extended at the lower boundary with
    zero-valued padding. The source sampling is first augmented so that all
    target edges exist in the source mesh.

    Parameters
    ----------
    l_e1 : array-like
        Target interval edges (monotonically increasing). Output values are
        computed for intervals ``[l_e1[k], l_e1[k+1]]``.
    l_e2 : array-like
        Source sampling points (monotonically increasing).
    l_v2 : array-like
        Values of the continuous quantity at the points ``l_e2``. Must have
        the same length as ``l_e2``.

    Returns
    -------
    numpy.ndarray
        Array of length ``len(l_e1) - 1`` containing the average value of the
        continuous function over each target interval.
    """
    if len(l_e2) != len(l_v2):
        print ("Error -  projet_vec_intervals_from_continus: not the same size for l_e2 and l_v2")
        1/0
        exit()
    if abs(l_e2[0] /(l_e1[0] +1e-20)-1)<1e-10: l_e1[0]  = l_e2[0]
    if abs(l_e2[-1]/(l_e1[-1]+1e-20)-1)<1e-10: l_e1[-1] = l_e2[-1]
    if l_e1[0]<l_e2[0]:
        l_e2 = [l_e1[0], l_e2[0]]+list(l_e2)
        l_v2 = [0,0]+list(l_v2)
    if l_e1[0]<l_e2[0] or l_e1[-1]>l_e2[-1]:
        print (l_e2[:10])
        print ("Error -  projet_vec_intervals_from_continus - target boundary smaller than origin: from " +str([l_e2[0],l_e2[-1]]) +" to "+str([l_e1[0],l_e1[-1]]))
        1/0
        exit()
    l_e2, l_v2 = include_in_mesh(l_e1, l_e2, l_v2)
    l_v1 = []
    i1, i2 = 0, 0
    while l_e2[i2] != l_e1[i1] : i2 += 1
    accu_v, accu_e = 0, 0
    for e1 in l_e1[1:]:
        while l_e2[i2]!=e1:
            de = l_e2[i2+1]-l_e2[i2]
            accu_v += 0.5*(l_v2[i2]+l_v2[i2+1])*de
            accu_e += de
            i2 += 1
        l_v1 += [accu_v/accu_e]
        accu_v, accu_e = 0, 0
    del l_e2
    del l_v2
    return np.array(l_v1)

def projet_vec_intervals_from_integrated(l_e1, l_e2, l_v2, sum_e=False):
    """
    Project piecewise-constant interval data onto a target interval mesh.

    The function maps interval values defined on a source mesh ``l_e2`` onto a
    target mesh ``l_e1`` (both interpreted as bin edges). The source values
    ``l_v2`` are assumed to be piecewise-constant over each interval
    ``[l_e2[k], l_e2[k+1]]``. For each target interval, the function computes
    the length-weighted average of the source interval values over the target
    interval.

    The source mesh is first augmented so that all target edges exist in the
    source mesh, enabling exact accumulation over aligned sub-intervals.

    Parameters
    ----------
    l_e1 : array-like
        Target interval edges (monotonically increasing). Output values are
        computed for intervals ``[l_e1[k], l_e1[k+1]]``.
    l_e2 : array-like
        Source interval edges (monotonically increasing).
    l_v2 : array-like
        Source interval values. Must satisfy ``len(l_v2) == len(l_e2) - 1``.
    sum_e : bool, optional
        Deprecated option. If ``True``, the function exits with an error.

    Returns
    -------
    numpy.ndarray
        Array of length ``len(l_e1) - 1`` containing the projected interval
        values on the target mesh.
    """
    if sum_e:
        print ('Error - projet_vec_intervals_from_integrated - sum_e - deprecated')
        exit()
    if len(l_e2)-1 != len(l_v2):
        print ("Error - projet_vec_intervals_from_integrated: len(l_e2) is supposed to be len(l_v2)+1")
        1/0
        exit()
    if abs(l_e2[0] /(l_e1[0] +1e-20)-1)<1e-10: l_e1[0]  = l_e2[0]
    if abs(l_e2[-1]/(l_e1[-1]+1e-20)-1)<1e-10: l_e1[-1] = l_e2[-1]
    if l_e1[0]<l_e2[0] or l_e1[-1]>l_e2[-1]:
        print ("Error -  projet_vec_intervals_from_integrated - target boundary smaller than origin: from " +str([l_e2[0],l_e2[-1]]) +" to "+str([l_e1[0],l_e1[-1]]))
        1/0
        exit()
    l_e2, l_v2 = include_in_mesh_piquet_interval(l_e1, l_e2, l_v2)
    l_v1 = []
    i1, i2 = 0, 0
    while l_e2[i2] != l_e1[i1] : i2 += 1
    accu_v, accu_e = 0, 0
    for e1 in l_e1[1:]:
        while l_e2[i2]!=e1:
            de = l_e2[i2+1]-l_e2[i2]
            accu_v += l_v2[i2]*de
            accu_e += de
            i2 += 1
        l_v1 += [accu_v/accu_e if not sum_e else accu_v]
        accu_v, accu_e = 0, 0
    return np.array(l_v1)

#print projet_vec_intervals_from_integrated([0,1,2,3,4,5], [0,2.5,5], [1,1], sum_e=True)
#exit()

if False: # check
    print (projet_vec_interpol                 ([0,3.2,5] , [0,1,2,3,4,5], [0,   1,    2,    3,    4,   5]))
    print (projet_vec_intervals_from_continus  ([0,3.2,5] , [0,1,2,3,4,5], [0,   1,    2,    3,    4,   5]))
    print (projet_vec_intervals_from_integrated([0,3.2,5] , [0,1,2,3,4,5], [  0.5, 1.5,  2.5,  3.5,  4.5  ]))
    print ((0.5+1.5+2.5+3.5*0.2)/3.2)
    #print projet_vec_intervals_from_integrated([0,3.2,5] , [0,1,2,3,4,5], [  0.5, 1.5,  2.5,  3.5,  4.5  ], sum_e=True)
    print ((0.5+1.5+2.5+3.5*0.2))
    exit()