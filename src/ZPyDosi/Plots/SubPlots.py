from ..Common.utils_general import get_aff_size
import numpy as np
variable_cachee_pas_bien = 0
def my_sub6(fig,i,j,p, mg=0.2,md=0.05, mb=0.15, mh=0.05, 
        list_rx=[0.5,0.25,0.25], list_ry=[0.5,0.25,0.25],
        list_sy=None, list_sx=None, list_idx_none=[],
        force_all_axes=False, auto_x=True, auto_y=True,
        list_idx_out_auto=[]):
    """
    Create a custom grid of axes inside a Matplotlib figure with fine control over layout.

    This function builds a (potentially non-uniform) grid of axes using
    ``fig.add_axes``. The grid is defined by relative width/height ratios
    for columns/rows and optional spacing ratios between them. Individual
    cells can be disabled. Optionally, x/y limits can be synchronized across
    rows/columns (or across all axes) via Matplotlib callback hooks.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure in which the axes will be created.
    i : int
        Number of "blocks" vertically in the global figure layout (used to
        position the panel indexed by ``p``).
    j : int
        Number of "blocks" horizontally in the global figure layout (used to
        position the panel indexed by ``p``).
    p : int
        Index of the block within the ``i``*``j`` global layout where this
        custom axes grid will be placed.
    mg : float, optional
        Left margin (relative figure units) allocated to the grid region.
    md : float, optional
        Right margin (relative figure units) allocated to the grid region.
    mb : float, optional
        Bottom margin (relative figure units) allocated to the grid region.
    mh : float, optional
        Top margin (relative figure units) allocated to the grid region.
    list_rx : list of float, optional
        Relative width ratios for columns in the local grid.
    list_ry : list of float, optional
        Relative height ratios for rows in the local grid.
    list_sy : list of float, optional
        Relative vertical spacing ratios between rows. If ``None``, uses zeros.
    list_sx : list of float, optional
        Relative horizontal spacing ratios between columns. If ``None``, uses zeros.
    list_idx_none : list, optional
        List of grid indices to disable (cells are created but made invisible).
        Indices are interpreted as tuples of the form ``(iy, ix)``.
    force_all_axes : bool, optional
        If ``True``, synchronize limits across all axes when auto synchronization
        is enabled.
    auto_x : bool, optional
        If ``True``, connect callbacks to propagate x-limits across axes.
    auto_y : bool, optional
        If ``True``, connect callbacks to propagate y-limits across axes.
    list_idx_out_auto : list, optional
        List of indices excluded from auto limit synchronization. Supports
        wildcard-like tuples using ``"*"``, e.g. ``(ix, "*")`` or ``("*", iy)``.

    Returns
    -------
    numpy.ndarray
        2D array of Matplotlib axes with shape ``(n_cols, n_rows)`` corresponding
        to the constructed local grid.
    """
    mg /= len(list_rx)
    md /= len(list_rx)
    #list_ry = list(reversed(list_ry))
    list_ry = list(list_ry)
    list_rx = list(list_rx)
    if list_sy is None: list_sy = [0.]*(len(list_ry)-1)
    if list_sx is None: list_sx = [0.]*(len(list_rx)-1)
    list_sy = list(reversed(list_sy))+[0]
    list_sx = list(list_sx)+[0]
    sumtoty = sum(np.array(list_ry)) + sum(np.array(list_sy))
    sumtotx = sum(np.array(list_rx)) + sum(np.array(list_sx))
    list_ry = 1.*np.array(list_ry) / sumtoty
    list_rx = 1.*np.array(list_rx) / sumtotx
    list_sy = 1.*np.array(list_sy) / sumtoty
    list_sx = 1.*np.array(list_sx) / sumtotx
    fx, fy = 1./j, 1./i
    y_dispo = 1-mh-mb
    list_dy = y_dispo * list_ry
    list_dys = y_dispo * list_sy
    x_dispo = 1-md-mg
    list_dx = x_dispo * list_rx
    list_dxs = x_dispo * list_sx
    y0 = mb
    list_list_ax = [ [None for toto in range(len(list_dy))] for titi in range(len(list_dx))]
    prev_dys = 1.
    for iy, dy in enumerate(list_dy):
        dys = list_dys[iy]
        list_ax = []
        prev_dxs = 1.
        x0 = mg
        for ix, dx in enumerate(list_dx):
            dxs = list_dxs[ix]
            ax = fig.add_axes((    fx*(p%j)            + fx*x0,    # left
                        fy*((i-1)-int(p/j)) + fy*y0,    # bottom
                        fx*(dx),            # delta horizontal
                        fy*(dy)))            #
            
            ax.tick_params(axis='both', labelsize=get_aff_size("s_tick")-6)
            #if prev_dys == 0 and (iy-1,ix) not in list_idx_none: ax.tick_params(axis='x',labelbottom='off') # which='both',bottom='off',top='off
            if prev_dys == 0 or (ix,iy) in list_idx_none:
                ax.tick_params(axis='x',labelbottom='off') # which='both',bottom='off',top='off
            if prev_dxs == 0: ax.tick_params(axis='y',labelleft='off')  # which='both',bottom='off',top='off
            list_list_ax[ix][iy] = ax
            if (iy,ix) in list_idx_none:
                ax.set_frame_on(False)
                ax.axes.get_yaxis().set_visible(False)
                ax.axes.get_xaxis().set_visible(False)
            prev_dxs = dxs
            x0 += dx+dxs
        prev_dys = dys
        y0 += dy+dys
        #list_list_ax += [list_ax]
    for iy, dy in enumerate(list_dy):
        for ix, dx in enumerate(list_dx):
            def find(obj):
                for i in range(len(list_dx)):
                    for j in range(len(list_dy)):
                        if obj == list_list_ax[i][j]:
                            return i,j
            if auto_x:
                def on_xlims_change(axes):
                    global variable_cachee_pas_bien
                    my_x, my_y = find(axes)
                    variable_cachee_pas_bien += 1
                    if variable_cachee_pas_bien == 1:
                        for j in range(len(list_dy)):
                            if not force_all_axes:
                                if (my_x,j) not in list_idx_out_auto and (my_x,"*") not in list_idx_out_auto and ("*",j) not in list_idx_out_auto:
                                    list_list_ax[my_x][j].set_xlim(axes.get_xlim())
                            else:
                                for i in range(len(list_dx)):
                                    if (i,j) not in list_idx_out_auto:
                                        list_list_ax[i][j].set_xlim(axes.get_xlim())
                    variable_cachee_pas_bien -= 1
                list_list_ax[ix][iy].callbacks.connect('xlim_changed', on_xlims_change)
            if auto_y:
                def on_ylims_change(axes):
                    global variable_cachee_pas_bien
                    my_x, my_y = find(axes)
                    variable_cachee_pas_bien += 1
                    if variable_cachee_pas_bien == 1:
                        for i in range(len(list_dx)):
                            if not force_all_axes:
                                if (i,my_y) not in list_idx_out_auto and ("*",my_y) not in list_idx_out_auto and (i,"*") not in list_idx_out_auto:
                                    list_list_ax[i][my_y].set_ylim(axes.get_ylim())
                            else:
                                for j in range(len(list_dy)):
                                    if (i,j) not in list_idx_out_auto:
                                        list_list_ax[i][j].set_ylim(axes.get_ylim())
                    variable_cachee_pas_bien -= 1
                    
                    #axes[0].set_yticks(map(lambda i:(i+0.5)*n, range(nb_split)))
                    #axes[0].set_yticklabels(map(lambda n:"", names))
                    
                list_list_ax[ix][iy].callbacks.connect('ylim_changed', on_ylims_change)
    return np.array(list_list_ax)


def my_sub6_finalise(list_list_ax, x=True, y=True):
    """
    Finalize axis limits for a grid of sub-axes created by ``my_sub6``.

    The function inspects all line objects in the provided axes grid to
    determine global minimum and maximum data extents. It then applies
    consistent x- and/or y-limits across axes, with a small padding applied
    to the y-range to improve readability. A global guard variable is used
    to avoid feedback loops with limit-synchronization callbacks.

    Parameters
    ----------
    list_list_ax : array-like
        2D collection of Matplotlib axes (typically the output of ``my_sub6``).
    x : bool, optional
        If ``True``, synchronize x-limits across axes.
    y : bool, optional
        If ``True``, synchronize y-limits across axes.

    Returns
    -------
    None
        Axes limits are modified in place.
    """
    global variable_cachee_pas_bien
    variable_cachee_pas_bien = 1
    xmin,xmax = list_list_ax[0,0].get_xlim()
    ymin,ymax = list_list_ax[0,0].get_ylim()
    for j in range(len(list_list_ax[0])):
        for i in range(len(list_list_ax)):
            for line in list_list_ax[i,j].lines:
                xmin = min(xmin, min(line.get_xdata()))
                xmax = max(xmax, max(line.get_xdata()))
                ymin = min(ymin, min(line.get_ydata()))
                ymax = max(ymax, max(line.get_ydata()))
        ymin *= 1.04 if ymin<0 else 0.96
        ymax *= 1.04 if ymax>0 else 0.96
        
        for i in range(len(list_list_ax)):
            if x: list_list_ax[i,j].set_xlim([xmin,xmax])
            if y: list_list_ax[i,j].set_ylim([ymin,ymax])
    variable_cachee_pas_bien = 0

def get_lim(ax):
    """
    Compute data bounds from line objects in a Matplotlib axis.

    The function scans all line artists attached to the given axis and
    determines the minimum and maximum x and y values present in the data.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis whose line data are inspected.

    Returns
    -------
    tuple
        Tuple ``((xmin, xmax), (ymin, ymax))`` giving the data bounds
        extracted from the axis.
    """
    xmin,xmax,ymin,ymax  = 1e100,-1e100,1e100,-1e100
    for line in ax.lines:
        xmin = min(xmin, min(line.get_xdata()))
        xmax = max(xmax, max(line.get_xdata()))
        ymin = min(ymin, min(line.get_ydata()))
        ymax = max(ymax, max(line.get_ydata()))
    return (xmin, xmax),(ymin,ymax)



def aff_curve(ax, lx,ly,sly,c,a1,a2,linewidth=1, dashes=None, label=None, log_to_lin=False):
    """
    Plot a curve with a shaded uncertainty band on a Matplotlib axis.

    The function draws a central curve together with a surrounding band
    representing symmetric uncertainties. The uncertainty band is rendered
    using ``fill_between`` with configurable transparency. Optionally, data
    provided in logarithmic space can be converted back to linear space
    before plotting.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis on which the curve and uncertainty band are plotted.
    lx : array-like
        X-axis values.
    ly : array-like
        Central Y values of the curve.
    sly : array-like
        Symmetric uncertainties associated with ``ly``.
    c : color
        Color used for both the curve and the uncertainty band.
    a1 : float
        Alpha (transparency) value for the curve.
    a2 : float
        Alpha (transparency) value for the uncertainty band.
    linewidth : float, optional
        Line width of the curve.
    dashes : tuple or None, optional
        Dash pattern for the curve. If ``None``, a solid line is used.
    label : str, optional
        Label for the curve, used in legends.
    log_to_lin : bool, optional
        If ``True``, interpret ``ly`` and ``sly`` as logarithmic values and
        convert them to linear space before plotting.

    Returns
    -------
    None
        The curve and uncertainty band are drawn on ``ax`` in place.
    """
    lx,ly,sly = map(lambda l:np.array(l), [lx,ly,sly])
    if not log_to_lin :
        ax.fill_between(lx, ly-sly, ly+sly, facecolor=c, alpha=a2,linewidth=0.0, zorder = 0)
    else:
        ax.fill_between(lx, np.exp(ly-sly), np.exp(ly+sly), facecolor=c, alpha=a2,linewidth=0.0, zorder = 0)
        ly = np.exp(ly)
    if dashes is None:
        ax.plot(lx,ly, c=c, alpha=a1, linewidth=linewidth, zorder = 1, label=label)
    else:
        ax.plot(lx,ly, c=c, alpha=a1, linewidth=linewidth, dashes=dashes, zorder = 1, label=label)
