from ..Common.utils_general import *
############################################################################################################
################################################################################################ matrix plot

def interval_joli(mini, maxi, nb=4):
    """
    Generate a set of nice for plotting interval values.

    The function computes a sequence of evenly spaced values spanning a
    specified range, with step sizes chosen to produce readable and
    well-distributed intervals. This is typically used for defining axis
    ticks or reference levels in plots.

    Parameters
    ----------
    mini : float
        Lower bound of the interval range.
    maxi : float
        Upper bound of the interval range.
    nb : int, optional
        Target number of intervals used to guide the step size selection.

    Returns
    -------
    list of float
        List of interval values covering the range from ``mini`` to ``maxi``.
    """
    delta =10.**(np.floor(np.log10(maxi-mini)))
    while (maxi-mini)/delta>nb*2 : delta *= 2
    while (maxi-mini)/delta<nb : delta /= 2
    pos = [mini - (mini-delta)%delta]

    def auto_round(v):
        d = 0
        while 10**(-d) > v/1e5 and round(v, d) != v:
            d += 1
        return round(v,d)
            
    while pos[-1]+delta<maxi:
        pos += [pos[-1]+delta]
    while pos[0]-delta>mini:
        pos = [pos[0]-delta] + pos
    if pos[0] < mini :
        pos = pos[1:]
    return list(map(lambda p: auto_round(p), pos))

def nice_nb(nb, mode_exp=False, log=False):
    """
    Format a number as a LaTeX-friendly string.

    The function converts a numerical value into a formatted LaTeX string,
    optionally using scientific notation or logarithmic interpretation.
    The output is intended for display in plots or mathematical text.

    Parameters
    ----------
    nb : float
        Numerical value to be formatted.
    mode_exp : bool, optional
        If ``True``, format the number using scientific notation.
    log : bool, optional
        If ``True``, interpret the input value as a base-10 logarithm and
        format the corresponding power of ten.

    Returns
    -------
    str
        LaTeX-formatted string representation of the number.
    """
    if log:
        mode_exp = True
        nb = 10**nb
    if mode_exp:
        v,e = (("%.1e"%nb) .replace("+0","+")).split("e")
        s = "$"+v+"e^{"+e+"}$"
        s = s.replace("0.0e^{+0}","0").replace("e^{-0","e^{-").replace("e^{+0","e^{+").replace(".0e","e").replace("e^{+}","e^{+0}")
    else:
        if int(nb) == nb:
            nb = int(nb)
        s = "$"+str(nb)+"$"
    return s

class MidpointNormalize(mpl.colors.Normalize):
    """
    Normalize values with a fixed midpoint for colormap scaling.

    This normalization maps values to the [0, 1] range while enforcing a
    specified midpoint to correspond to a fixed normalized value. It is
    commonly used to center diverging colormaps around a physically or
    visually meaningful reference value.
    """
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        """
        Initialize the normalization with a specified midpoint.

        Parameters
        ----------
        vmin : float, optional
            Lower bound of the normalization range.
        vmax : float, optional
            Upper bound of the normalization range.
        midpoint : float
            Data value that should be mapped to the central point of the
            colormap.
        clip : bool, optional
            If ``True``, values outside the range [vmin, vmax] are clipped.
        """
        self.midpoint = midpoint
        mpl.colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        """
        Normalize input values according to the midpoint-based scaling.

        Parameters
        ----------
        value : array-like
            Input data values to be normalized.
        clip : bool, optional
            Whether to clip values outside the normalization range.

        Returns
        -------
        numpy.ma.MaskedArray
            Normalized values mapped to the [0, 1] interval.
        """
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.05, 1]
        return np.ma.masked_array(np.interp(value, x, y))


def make_cmap(colors, position=None, bit=False):
    """
    Create a custom Matplotlib colormap from a list of colors.

    The function builds a linear segmented colormap using specified RGB
    color values. Colors are interpolated linearly over the full range
    of the colormap.

    Parameters
    ----------
    colors : list of tuple
        List of RGB color tuples. Values are expected as integers in the
        range [0, 255].
    position : array-like, optional
        Positions of the colors within the colormap, normalized to [0, 1].
        If ``None``, colors are evenly spaced.
    bit : bool, optional
        Flag indicating whether color values are provided in 8-bit format.
        Currently kept for compatibility.

    Returns
    -------
    matplotlib.colors.LinearSegmentedColormap
        Generated Matplotlib colormap.
    """
    position = np.linspace(0,1,len(colors))
    cdict = {'red':[], 'green':[], 'blue':[]}
    bit_rgb = np.linspace(0,1,256)
    for i in range(len(colors)):
        colors[i] = (    bit_rgb[colors[i][0]],
                bit_rgb[colors[i][1]],
                bit_rgb[colors[i][2]])
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))
    return mpl.colors.LinearSegmentedColormap('my_colormap',cdict,1024)

def aff_mat4(lx, ly, mat, ax, orientation, titre, xlab, ylab,Cbar_label=None, cov=None, xlim=None, ylim=None,
        logz=None, logx=False, logy=False, minimaxi=None, midblanc=False, midgreen=False, minblanc=False, simple_scale=False,nb_leg=4,
        maxblanc=False, centered=False, smooth=None, pad=None, pcol=False,head_top=True, maskout=False):
    """
    Display a 2D matrix as a heatmap with configurable scaling, colormap, and colorbar.

    This function renders a matrix on a provided Matplotlib axis using either
    ``imshow`` or ``pcolormesh``. It supports linear or logarithmic color scaling,
    optional interpolation/smoothing onto a finer grid, customizable diverging
    colormaps (including white or green midpoints), and optional masking of values
    outside a specified range.

    If a covariance/correlation/uncertainty matrix is provided via ``cov``, the function can
    render two matrices in the same plot by displaying one triangle for ``mat``
    and the other triangle for ``cov`` (with additional handling for diagonal cells).

    Parameters
    ----------
    lx : array-like
        X-axis coordinates (bin edges or centers depending on rendering mode).
    ly : array-like
        Y-axis coordinates (bin edges or centers depending on rendering mode).
    mat : array-like
        2D matrix to display (e.g., data, response matrix, correlation matrix).
    ax : matplotlib.axes.Axes
        Target axis on which the plot is drawn.
    orientation : str or None
        Colorbar orientation for the main matrix when ``cov`` is None.
        Typically ``"vertical"`` or ``"horizontal"``. If falsy, no colorbar is added.
    titre : str
        Title/label used for colorbar labeling and some colormap choices (e.g. "ND").
    xlab : str
        X-axis label.
    ylab : str
        Y-axis label.
    Cbar_label : str, optional
        Label for the secondary colorbar when plotting ``cov`` alongside ``mat``.
    cov : array-like, optional
        Secondary matrix (often covariance/correlation/uncertainty) to overlay/display together
        with ``mat`` using triangular masking.
    xlim : tuple, optional
        X-axis limits.
    ylim : tuple, optional
        Y-axis limits.
    logz : bool, optional
        If ``True``, apply log10 scaling to ``mat`` values (zeros are masked).
    logx : bool, optional
        If ``True``, set the x-axis to logarithmic scale.
    logy : bool, optional
        If ``True``, set the y-axis to logarithmic scale.
    minimaxi : tuple, optional
        Tuple ``(vmin, vmax)`` used to fix the displayed range. If not provided,
        bounds are inferred from the data.
    midblanc : bool, optional
        If ``True``, use a colormap with a white midpoint (useful for diverging data).
    midgreen : bool, optional
        If ``True``, use a colormap with a green midpoint.
    minblanc : bool, optional
        If ``True``, use a colormap with a white minimum.
    simple_scale : bool, optional
        If ``True``, use a simpler blue→red (optionally via white/green) colormap.
    nb_leg : int, optional
        Target number of colorbar tick labels.
    maxblanc : bool, optional
        If ``True``, use a colormap with a white maximum.
    centered : bool, optional
        If ``True``, interpret coordinates as bin edges and compute bin centers
        (behavior depends on implementation branch).
    smooth : int, optional
        If provided, resample/interpolate the matrix onto a regular grid of size
        ``smooth`` for both axes.
    pad : float, optional
        Padding used for the colorbar placement.
    pcol : bool, optional
        If ``True``, use ``pcolormesh`` instead of ``imshow``.
    head_top : bool, optional
        Control for y-axis direction / header positioning (behavior depends on branch).
    maskout : bool, optional
        If ``True`` and ``minimaxi`` is provided, mask values outside ``minimaxi``.

    Returns
    -------
    None
        The plot is drawn on ``ax`` and modified in place.
    """
    lx = np.array(lx)*1.
    ly = np.array(ly)*1.
    
    if smooth is not None:
        #print lx
        if logx: lx = np.log10(lx)
        if logy: ly = np.log10(ly)
        lx = (lx[1:]+lx[:-1])/2
        ly = (ly[1:]+ly[:-1])/2
        #f = interp2d(lx+(lx[1]-lx[0])/2, ly+(ly[1]-ly[0])/2, mat, kind='linear') # linear cubic quintic
        f = interp2d(lx, ly, mat, kind='linear') # linear cubic quintic
        lx = np.linspace(lx[0], lx[-1], num=smooth)
        ly = np.linspace(ly[0], ly[-1], num=smooth)
        mini,maxi = np.min(mat), np.max(mat)
        mat = f(lx,ly)
        mat[np.where(mat>maxi)] = maxi
        mat[np.where(mat<mini)] = mini
        if logx: lx = 10**lx
        if logy: ly = 10**ly

    minlim = (255,255,255) if minblanc else (150,150,255)
    maxlim = (255,255,255) if maxblanc else (255,150,150)
    midlim = [(255,255,255)] if midblanc else []
    cmap = make_cmap([minlim, (40,40,222), (0,0,85), (40,255,255), (20,114,0)]+ midlim +[(255,255,0), (255,75,0), (85,0,0), (222,40,40), maxlim])
    if titre=="ND" :
        cmap = make_cmap([minlim, (150,150,255), (40,40,222), (0,0,85), (40,255,255), (20,114,0)]+ midlim +[(255,255,0), (255,75,0), (85,0,0), (222,40,40), maxlim])
    
    #if minblanc=True and blabla="ND" =cmap = make_cmap([minlim, minlim, (40,40,222), (0,0,85), (40,255,255), (20,114,0), midlim ,(255,255,0), (255,75,0), (85,0,0), (222,40,40), maxlim, (40,40,222), (0,0,85), (40,255,255), (20,114,0)]+ midlim +[(255,255,0), (255,75,0), (85,0,0), (222,40,40), maxlim])
    #cmap = make_cmap([minlim, (40,40,222), (0,0,85), (40,255,255)]+ midlim +[(255,75,0), (85,0,0), (222,40,40), maxlim])
    #print midlim
    #exit()
    
    if False:
        rm,gm,bm = 50,255,50
        if midblanc:
            rm,gm,bm = 255,255,255
        r=[    0,    0,    0,    rm,    255,    255,    205    ]
        g=[    0,    0,    255,    gm,    255,    0,    0    ]
        b=[    205,    255,    255,    bm,    0,    0,    0    ]
        
        #r=[170,0  ,0  ,40 ,50 ,255,120,255,150,255,255]
        #g=[170,0  ,0  ,255,100,255,100,255,0  ,0  ,170]
        #b=[255,255,150,255,120,255,50 ,40 ,0  ,0  ,170]
        
        cmap = make_cmap(map(lambda i:(r[i],g[i],b[i]), range(len(r))))
    if True:
        #echl_raw = make_cmap([(170,170,255), ( 0, 0,255), (0,0,150), (40,255,255), (50,100,120), (20, 255,20 ), (120,100,50), (255,255,40), (150,0,0), (255,0, 0 ), (255,170,170)])
        echl_raw = make_cmap([(170,170,255), ( 0, 0,255), (0,0,150), (40,255,255),                (50,120,50),                (255,255,40), (150,0,0), (255,0, 0 ), (255,170,170)])
        
        echl_mid = make_cmap([(170,170,255), ( 0, 0,255), (0,0,150), (40,255,255), (50,100,120), (255,255,255), (120,100,50), (255,255,40), (150,0,0), (255,0, 0 ), (255,170,170)])
        echl_mid = make_cmap([( 0, 0,220),(40,205,255), (255,255,255), (255,205,40), (220,0, 0 )])
        echl_mid = make_cmap([( 0, 0,255), (0,0,150), (40,255,255), (50,100,120), (255,255,255), (120,100,50), (255,255,40), (150,0,0), (255,0, 0 )])
        echl_mid = make_cmap([( 0, 0,255), (0,150,255), (40,255,255), (255,255,255),(255,255,40), (255,150,0), (255,0, 0 )])

        echl_min = make_cmap([(255,255,255), ( 0, 0,255), (0,0,150), (40,255,255), (50,100,120), (20, 255,20 ), (120,100,50), (255,255,40), (150,0,0), (255,0, 0 ), (255,170,170)])
        echl_midg  = make_cmap([( 0, 0,220),(40,205,255), (0,200,0), (255,205,40), (220,0, 0 )])

        cmap = echl_raw
        if midblanc:
            cmap = echl_mid
        if minblanc:
            cmap = echl_min
        if midgreen:
            cmap = echl_midg
            
        
    if simple_scale:
        #echl_raw = make_cmap([(170,170,255), ( 0, 0,255), (0,0,150), (40,255,255), (50,100,120), (20, 255,20 ), (120,100,50), (255,255,40), (150,0,0), (255,0, 0 ), (255,170,170)])
        
        red,green,blue,white = map(lambda c:np.array(c), [(255,0,0), (0,255,0),(0,0,255),(255,255,255)])
        
        cmap = make_cmap([blue,red])
        if midblanc: cmap = make_cmap([blue,white,red])
        if minblanc: cmap = make_cmap([white,blue,red])
        if midgreen: cmap = make_cmap([blue,green,red])
        if minblanc and midgreen: cmap = make_cmap([white,blue,green,red])
        
    if logz:
        mat = np.ma.masked_array(mat, mask = mat==0)
    if minimaxi is not None and maskout:
        mat = np.ma.masked_array(mat, mask = (mat>minimaxi[1])+(mat<minimaxi[0]))
    
    taille = len(mat)
    nx,ny = mat.shape
    if logz:
        mat = np.log10(mat)
    if minimaxi is not None:
        mini, maxi = minimaxi
    else:
        mini, maxi = np.min(mat), np.max(mat)+1e-10
    if midblanc and not logz:
        mini, maxi = -(max(abs(mini),abs(maxi))), (max(abs(mini),abs(maxi)))
    pos = interval_joli(mini, maxi, nb=nb_leg)
    pos2 = interval_joli(0, 1, nb=nb_leg)
    if False:
        cs = plt.contour(mat, pos, smoothing=2., linewidths=1.5, extent=(0,len(lx),0,len(ly)), colors='k')
        fmt = {}
        for v in pos:
            fmt[v] = nice_nb(v, False)
        plt.clabel(cs,colors='black', inline=True,  fontsize=22, fmt=fmt) #inline_spacing=0,
    if centered:
        '''if not logx:    center_x = (lx[1:]+lx[:-1])/2.
        else:         center_x = 10**(np.log10(lx[1:])+np.log10(lx[:-1]))/2.
        if not logy:    center_y = (ly[1:]+ly[:-1])/2.
        else:        center_y = 10**(np.log10(ly[1:])+np.log10(ly[:-1]))/2.'''
    else:
        center_x = lx
        center_y = ly
    head_top = False
    if pcol:
        if not head_top and cov is None:
            im = ax.pcolormesh(center_x, center_y, mat,cmap=cmap, vmin=mini, vmax=maxi) # , shading='gouraud'
        elif cov is None:
            im = ax.pcolormesh(center_x, center_y, mat,cmap=cmap, vmin=mini, vmax=maxi) # , shading='gouraud'
            ax.invert_yaxis()
            #plt.gca().invert_yaxis()
            
            #im = ax.pcolormesh(center_x, center_y, mat[::-1],cmap=cmap, vmin=mini, vmax=maxi) # , shading='gouraud'
        else:
            n=len(mat)
            mat_masked = np.ma.masked_array(mat, mask=np.tril(np.ones_like(mat), k=0))
            cov_masked = np.ma.masked_array(cov, mask=np.triu(np.ones_like(cov), k=0))
            cmap1=cmap
            cmap2='Greys'




            if titre=="ND" :
                norm=MidpointNormalize(midpoint=0.5)
                im2 = ax.pcolormesh(center_x, center_y,cov_masked,cmap=cmap2, vmin=0, vmax=1)
                im1 = ax.pcolormesh(center_x, center_y,mat_masked,cmap=cmap1, vmin=mini, vmax=maxi)
                # ax.invert_yaxis()
            else:
                norm=None
                im2 = ax.pcolormesh(center_x, center_y,cov_masked,cmap=cmap2, vmin=0, vmax=1)
                im1 = ax.pcolormesh(center_x, center_y,mat_masked,cmap=cmap1, vmin=mini)
                # ax.invert_yaxis()

            from matplotlib.patches import Polygon  # type: ignore # False alert with Pylance
            from matplotlib.cm import ScalarMappable  # type: ignore # False alert with Pylance
            from matplotlib.colors import Normalize  # type: ignore # False alert with Pylance

            smA = ScalarMappable(Normalize(vmin=mini, vmax=maxi), cmap=cmap1)
            smB = ScalarMappable(Normalize(vmin=0, vmax=1), cmap=cmap2)



            # now draw the half‐cells on the diagonal
            for i in range(n):
                # upper‐right triangle (A) in cell (i,i)
                tri_up = Polygon(
                    [(i+0.5, i+0.5), (i+0.5+1, i+0.5+1), (i+0.5+1, i+0.5)],
                    facecolor=smA.to_rgba(mat[i, i]),
                    edgecolor='none'
                )
                ax.add_patch(tri_up)

                # lower‐left triangle (B)
                tri_lo = Polygon(
                    [(i+0.5, i+0.5),(i+0.5, i+0.5+1), (i+0.5+1, i+0.5+1)],
                    facecolor=smB.to_rgba(cov[i, i]),
                    edgecolor='none'
                )
                ax.add_patch(tri_lo)

            pad = 0.05
            cbar = plt.colorbar(im1, ax=ax, format='%.1e',  orientation="vertical", aspect=30, pad=pad,fraction=0.036) #, pad=0.01) fraction=0.046
            cbar.set_ticks(pos)
            cbar.set_ticklabels(list(map(lambda p: nice_nb(p, mode_exp=False, log=logz),pos)))
            cbar.ax.tick_params(labelsize=get_aff_size("s_tick")*0.8-6)
            if titre is not None and len(titre)>0:
                cbar.set_label(tex(titre), rotation=90, size=get_aff_size("s_leg"))       
            pad =(0.15 if len(xlab)>0 else 0.01)
            cbar = plt.colorbar(im2, ax=ax, format='%.1e', orientation="horizontal", aspect=30, pad=pad,fraction=0.046) #, pad=0.01) fraction=0.046
            cbar.set_ticks(pos2)
            cbar.set_ticklabels(list(map(lambda p: nice_nb(p, mode_exp=False, log=logz),pos2)))
            cbar.ax.tick_params(labelsize=get_aff_size("s_tick")*0.8-6)
            if Cbar_label is not None and len(titre)>0:
                cbar.set_label(tex(Cbar_label), rotation=0, size=get_aff_size("s_leg"))




    elif cov is None:
        if titre=="ND" :
            im = ax.imshow(mat,cmap=cmap, vmin=mini, vmax=maxi, norm=MidpointNormalize(midpoint=0.5), interpolation='nearest')
        else:
            im = ax.imshow(mat,cmap=cmap, vmin=mini, vmax=maxi, interpolation='nearest')
        
        #im = ax.imshow(mat,cmap=cmap, vmin=mini, vmax=maxi, interpolation='nearest', extent=[lx[0],lx[-1],ly[0],ly[-1]])
    else:
        n=len(mat)
        mat_masked = np.ma.masked_array(mat, mask=np.tril(np.ones_like(mat), k=0))
        cov_masked = np.ma.masked_array(cov, mask=np.triu(np.ones_like(cov), k=0))
        cmap1=cmap
        cmap2='Greys'




        if titre=="ND" :
            norm=MidpointNormalize(midpoint=0.5)
            im = ax.imshow(mat_masked,cmap=cmap1, vmin=mini, vmax=maxi,extent=[0,n,0,n], norm=norm, interpolation='nearest')
            im = ax.imshow(cov_masked,cmap=cmap2, vmin=0, vmax=1,extent=[0,n,0,n], norm=None, interpolation='nearest')
        else:
            norm=None
            im = ax.imshow(mat_masked,cmap=cmap1, vmin=mini, vmax=maxi,extent=[0,n,0,n], interpolation='nearest')
            im = ax.imshow(cov_masked,cmap=cmap2, vmin=0, vmax=1,extent=[0,n,0,n], interpolation='nearest')

        from matplotlib.patches import Polygon  # type: ignore # False alert with Pylance
        from matplotlib.cm import ScalarMappable  # type: ignore # False alert with Pylance
        from matplotlib.colors import Normalize  # type: ignore # False alert with Pylance
        smA = ScalarMappable(Normalize(vmin=mini, vmax=maxi), cmap=cmap1)
        smB = ScalarMappable(Normalize(vmin=0, vmax=1), cmap=cmap2)



        # now draw the half‐cells on the diagonal
        for i in range(n):
            # upper‐right triangle of the square at (i,i)
            verts_up = [(i,   i+1),
                        (i+1, i+1),
                        (i+1, i  )]
            tri_up = Polygon(verts_up,
                            facecolor=smA.to_rgba(mat[i,i]),
                            edgecolor='none')
            ax.add_patch(tri_up)

            # lower‐left triangle of the square at (i,i)
            verts_lo = [(i,   i),
                        (i,   i+1),
                        (i+1, i  )]
            tri_lo = Polygon(verts_lo,
                            facecolor=smB.to_rgba(cov[i,i]),
                            edgecolor='none')
            ax.add_patch(tri_lo)


    #plt.show()
    #exit()
    ax.axis('tight')
    ax.set_xlabel(tex(xlab), size=get_aff_size("s_xylabel")-8)
    ax.set_ylabel(tex(ylab), size=get_aff_size("s_xylabel")-8)
    ax.tick_params(labelsize=get_aff_size("s_tick")-6)
    if orientation and cov is None:
        if pad is None: pad = 0.05 if orientation == "vertical" else (0.15 if len(xlab)>0 else 0.01)
        cbar = plt.colorbar(im, ax=ax, format='%.1e',  orientation=orientation, aspect=30, pad=pad) #, pad=0.01) fraction=0.046
        cbar.set_ticks(pos)
        cbar.set_ticklabels(list(map(lambda p: nice_nb(p, mode_exp=False, log=logz),pos)))
        cbar.ax.tick_params(labelsize=get_aff_size("s_tick")*0.8-6)
        if titre is not None and len(titre)>0:
            cbar.set_label(tex("Correlation"), rotation=0, size=get_aff_size("s_xylabel")-8)
            # cbar.set_label(tex(titre), rotation=0, size=get_aff_size("s_leg"))
    if xlim: ax.set_xlim(xlim)
    if ylim: ax.set_ylim(ylim)
    if logx: ax.set_xscale('log')
    if logy: ax.set_yscale('log')