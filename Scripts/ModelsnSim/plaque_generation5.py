
# cd "$petale_analysis"/plaque_3D
# python3.9 ../python/sss_input/plaque_generation5.py

from ZPyDosi.Common.utils_general import lmap, get_aff_size, tex
from ZPyDosi.Common.ExcelSheet import ExcelSheet
from ZPyDosi.Plots.MatrixPlots import make_cmap, nice_nb, interval_joli
from ZPyDosi.Prints.PrintnSave import aff, aff_t
from ZPyDosi.Plots.SubPlots import my_sub6
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
l_mini, l_maxi, l_ave = [], [], []
Volumes=[]
def repeat(func,n, x):
    for i in range(n):
        x=func(x)
    return x
def rotate(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        for i in range(cols):
            temp = []
            for j in range(rows):
                temp.append(matrix[j][i])
            res.append(temp[::-1])
    
        return np.array(res)

def do_you_job(path, l_ax):
    print("#"*100)
    print(path)
    input = ExcelSheet(path)
    
    i = 0
    l_bloc = [
    (99,"X"),
    (99,"X"),
    (20,"Z"),
    (18,"Y"),
    (16,"Z"),
    (20,"Y"),
        ]
    
    l_x_grid = np.array(list(reversed([-8.0, -18.0])))
    l_y_grid = np.array(list(reversed([-1.5, -34.5, -67.5, -100.5, -133.5, -166.5, -199.5, -232.5, -265.5, -298.5])))
    l_z_grid = np.array(list(reversed([-1.5, -34.5, -67.5, -100.5, -133.5, -166.5, -199.5, -232.5, -265.5, -298.5])))
    
    
    #l_x_grid,l_y_grid,l_z_grid = map(lambda l: -1*l, [l_x_grid,l_y_grid,l_z_grid])
    l_x_grid += 20
    l_y_grid += 300
    l_z_grid += 300
    
    #print(l_z_grid)
    #exit()
    
    
    
    
    def get_pos(l,val):
        for iv, v in enumerate(l):
            if abs(v-val)<0.5:
                return iv
        return None
    
    data_X = np.zeros((2 ,10,10))+1e3*1
    data_Y = np.zeros((2 ,2 ,10))+1e3*1
    data_Z = np.zeros((2 ,10,2 ))+1e3*1
    
    nro_pt = 0
    for i in range(input.get_nb_row()):
        if input.get(i,2) == "X":
            #x,y,z = map(lambda j: -input.get(i+j,3), range(3))
            x,y,z = map(lambda j: input.get(i+j,3), range(3))
            x += 20
            y += 300
            z += 300
            if   abs(x-0  )<1: data_X[0, get_pos(l_y_grid, y), get_pos(l_z_grid, z)] = x
            elif abs(x-20 )<1: data_X[1, get_pos(l_y_grid, y), get_pos(l_z_grid, z)] = x
            elif abs(y-0  )<1: data_Y[get_pos(l_x_grid, x), 0, get_pos(l_z_grid, z)] = y
            elif abs(y-300)<1: data_Y[get_pos(l_x_grid, x), 1, get_pos(l_z_grid, z)] = y
            elif abs(z-0  )<1: data_Z[get_pos(l_x_grid, x), get_pos(l_y_grid, y), 0] = z
            elif abs(z-300)<1: data_Z[get_pos(l_x_grid, x), get_pos(l_y_grid, y), 1] = z
            else:
                print("did not find",x,y,z)
                print(nro_pt)
                exit()
            nro_pt += 1
    print("X positions")
    print(data_X)
    print()
    print("Y positions")
    print(data_Y)
    print()
    print("Z positions")
    print(data_Z)
    print()
    print()
    
    #def interpole(m):
    #    for i in range(m.shape[0]):
    #        for j in range(m.shape[1]):
    #            if m[i,j]
    #    exit()
    def iaff(v):
        return aff(int(v*1000)/1000)
    
    
    dec = 0.
    for i in [0,1]:
        v1 = data_X[i,0,1]*2-data_X[i,0,0]
        v2 = data_X[i,0,3]*2-data_X[i,0,4]
        v3 = data_X[i,1,2]*2-data_X[i,2,2]
        data_X[i,0,2] = (v1+v2+v3)/3 + dec
    
    
    """
    v1 = data_X[1,9,6]*2-data_X[1,9,5]
    v2 = data_X[1,9,8]*2-data_X[1,9,9]
    v3 = data_X[1,8,7]*2-data_X[1,7,7]
    data_X[1,9,7] = (v1+v2+v3)/3 + dec
    """
    for i in [0,1]:
        v1 = data_Y[i,0,1]*2 - data_Y[i,0,0]
        v2 = data_Y[i,0,3]*2 - data_Y[i,0,4]
        data_Y[i,0,2] = (v1+v2)/2 + dec
    
    for i in [0,1]:
        data_Z[i,0,0] = data_Z[i,1,0]*2-data_Z[i,2,0] + dec
        data_Z[i,9,0] = data_Z[i,8,0]*2-data_Z[i,7,0] + dec
    
    
    '''
        dec = 0.
        v1 = data_X[0,0,1]*2-data_X[0,0,0]
        v2 = data_X[0,0,3]*2-data_X[0,0,2]
        v3 = data_X[0,1,2]*2-data_X[0,2,2]
        data_X[0,1,2] = (v1+v2+v3)/3 + dec
    '''
    '''
    for i in range(2):
        for j in range(10):
            #print(iaff(data_X[1,i,j]), end="")
            #print(iaff(data_Y[i,1,j]), end="")
            print(iaff(data_Z[i,j,1]), end="")
        print()
    exit()'''
    
    # print("X positions")
    # print(data_X)
    # print()
    # print("Y positions")
    # print(data_Y)
    # print()
    # print("Z positions")
    # print(data_Z)
    # print()
    # print()
    
    def ave(m):
        return m.sum()/m.size
    
    l_x_grid      -= ave(data_X[0,:,:])
    data_X[:,:,:] -= ave(data_X[0,:,:])
    thickness_x    = ave(data_X[1,:,:])
    
    
    l_y_grid      -= ave(data_Y[:,0,:])
    data_Y[:,:,:] -= ave(data_Y[:,0,:])
    thickness_y    = ave(data_Y[:,1,:])
    
    
    l_z_grid      -= ave(data_Z[:,:,0])
    data_Z[:,:,:] -= ave(data_Z[:,:,0])
    thickness_z    = ave(data_Z[:,:,1])
    
    
    
    #data_X[0,0,0] = 1
    '''
    print("#"*100)
    
    print(aff(""),end="")
    for j in range(10):
        print(iaff(l_z_grid[j]), end="")
    print()
    for i in range(10):
        print(iaff(l_y_grid[i]), end="")
        for j in range(10):
            print(iaff(data_X[1,i,j]-data_X[0,i,j]), end="")
        print()
    print("#"*100)'''
    
    
    def aff_mat(ax, lx,ly,mat,xlab,ylab,ori,bar_title,minimaxi=None, nb_leg=4, xlim=None, ylim=None, pad=None, logz=False, contour=None, offset=0):
        cmap = make_cmap([( 0, 0,255), (0,150,255), (40,255,255), (255,255,255),(255,255,40), (255,150,0), (255,0, 0 )])
        
        if minimaxi is not None: mini, maxi = minimaxi
        else:                    mini, maxi = np.min(mat), np.max(mat)+1e-10
        pos = interval_joli(mini, maxi, nb=nb_leg)
        #print(lx)
        min_x_extra = lx[ 0]*1.5 - lx[ 1]*0.5
        max_x_extra = lx[-1]*1.5 - lx[-2]*0.5
        min_y_extra = ly[ 0]*1.5 - ly[ 1]*0.5
        max_y_extra = ly[-1]*1.5 - ly[-2]*0.5
        mode_smooth = False
        if mat.shape == (10,10) or True:
            x,y = np.mgrid[lx[0]:lx[-1]:complex(0,len(lx)), ly[0]:ly[-1]:complex(0,len(ly))]
            #xnew, ynew = np.mgrid[min_x_extra:max_x_extra:100j, min_y_extra:max_y_extra:100j]
            xnew, ynew = np.mgrid[0:300:200j, 0:300:200j]
            #print(mat.shape, x.shape, y.shape)
            tck  = interpolate.bisplrep(x, y, mat, s=1e-3) # , s=0
            matnew = interpolate.bisplev(xnew[:,0], ynew[0,:], tck)
            if mode_smooth:
                im = ax.imshow(matnew,cmap=cmap, vmin=mini, vmax=maxi, interpolation='nearest', extent=[min_x_extra, max_x_extra,min_y_extra,max_y_extra]) # nearest gaussian
            else:
                im = ax.imshow(mat,cmap=cmap, vmin=mini, vmax=maxi, interpolation='nearest', extent=[min_x_extra, max_x_extra,min_y_extra,max_y_extra]) # nearest gaussian
        
        ax.set_xlabel(tex(xlab), size=get_aff_size("s_xylabel")*1.5)
        ax.set_ylabel(tex(ylab), size=get_aff_size("s_xylabel")*1.5)
        ax.tick_params(labelsize=get_aff_size("s_tick")*1.5)
        #ax.axis('tight')
        if ori:
            if pad is None: pad = 0.05 if ori == "vertical" else (0.15 if len(xlab)>0 else 0.01)
            cbar = plt.colorbar(im, ax=ax, format='%.1e',  orientation=ori, aspect=30, pad=pad) #, pad=0.01) fraction=0.046
            cbar.set_ticks(pos)
            cbar.set_ticklabels(list(map(lambda p: nice_nb(p, mode_exp=False, log=logz),pos)))
            cbar.ax.tick_params(labelsize=get_aff_size("s_tick")*1.3)
            if bar_title is not None and len(bar_title)>0:
                cbar.set_label(tex(bar_title), rotation= 90 if ori == "vertical" else 0 , size=get_aff_size("s_leg")*1.2)
        if xlim: ax.set_xlim(xlim)
        if ylim: ax.set_ylim(ylim)
        
        if contour is not None or mat.shape == (10,10):
            lvl = np.arange(-0.2,0.20001, 0.025)
            #cs = ax.contour(lx,list(reversed(ly)), mat, lvl, linewidths=1.5, colors='k') # extent=(0,len(lx),0,len(ly)), smoothing=2.,
            cs = ax.contour(xnew[:,0],list(reversed(ynew[0,:])), matnew, lvl, linewidths=1, colors='k', linestyles='solid') # extent=(0,len(lx),0,len(ly)), smoothing=2.,
            fmt = {}
            if contour is None : contour=0
            for v in lvl:
                nb = format(contour+v+1e-15, ".3f")
                while "0" == nb[-1]: nb = nb[:-1]
                if "." == nb[-1]: nb = nb[:-1]
                fmt[v] = "$"+nb+"$"
            try:
                ax.clabel(cs,colors='black', inline=True,  fontsize=16, fmt=fmt) #inline_spacing=0,
            except:
                print("tp plat")
            
    print()
    
    def face_mean(Meas,axis=0):
        if axis==1:Meas=np.swapaxes(Meas,axis,0)
        elif axis==2:Meas=np.moveaxis(Meas,axis,0)
        Mean=np.zeros((len(Meas),len(Meas[0,:,:])+1,len(Meas[0,0,:])+1))
        for i in range(len(Meas)):
            Mean[i,0,0]=Meas[i,0,0]
            Mean[i,-1,0]=Meas[i,-1,0]
            Mean[i,0,-1]=Meas[i,0,-1]
            Mean[i,-1,-1]=Meas[i,-1,-1]
            for j in range(len(Meas[i])-1):
                Mean[i,j+1,0]=(Meas[i,j,0]+Meas[i,j+1,0])/2
                Mean[i,j+1,-1]=(Meas[i,j,-1]+Meas[i,j+1,-1])/2
                for l in range(len(Meas[i,j])-1):
                    if j==0:
                        Mean[i,j,l+1]=(Meas[i,j,l]+Meas[i,j,l+1])/2
                        Mean[i,-1,l+1]=(Meas[i,-1,l]+Meas[i,-1,l+1])/2
                    Mean[i,j+1,l+1]=(Meas[i,j,l]+Meas[i,j,l+1]+Meas[i,j+1,l]+Meas[i,j+1,l+1])/4
        return Mean
        
    X_faces_voxel=face_mean(data_X)
    Y_faces_voxel=face_mean(data_Y,1)
    Z_faces_voxel=face_mean(data_Z,2)
    
    # print(data_X)
    # print()
    # print(X_faces_voxel) # Warning : order is matrix order not cartesian 
    # print()
    # print(data_Y)
    # print()
    # print(Y_faces_voxel) # Warning : order is matrix order not cartesian 
    # print()
    # print(Z_faces_voxel) # Warning : order is matrix order not cartesian 
    
    print()
    print(data_Y[0,1,1],np.swapaxes(data_Y,1,0)[1,0,1])
    print()
    print(data_Y,np.swapaxes(data_Y,1,0))
    
    # print(data_Z[0,1,1],np.moveaxis(data_Z,2,0)[1,0,1])
    # print()
    # print(data_Z)
    # print()
    # print(np.moveaxis(data_Z,2,0))
    l_cuboid=[]#cuboid order: x0, x1, y0, y1, z0 and z1 
    l_name=[]
    
    Y_Pos=np.zeros((len(l_y_grid)+2,len(l_x_grid)+1,len(l_z_grid)+1)) #dimensions:(main,x-axis,z-axis)
    Z_Pos=np.zeros((len(l_z_grid)+2,len(l_x_grid)+1,len(l_y_grid)+1))
    X_Pos=[X_faces_voxel[0,:,:].tolist()]
    Y_Pos[0,:,:]=Y_faces_voxel[0,:,:].tolist()
    Z_Pos[0,:,:]=Z_faces_voxel[0,:,:].tolist()
    for val in l_x_grid:
        X_Pos+=[[[val]*(len(l_y_grid)+1)]*(len(l_z_grid)+1)]
    for i in range(len(l_y_grid)):
        Y_Pos[i+1,:,:]=[[l_y_grid[i]]*(len(l_z_grid)+1)]*(len(l_x_grid)+1)
        # print([[[val]*(len(l_x_grid)+1)]*(len(l_z_grid)+1)])
    for i in range(len(l_z_grid)):
        Z_Pos[i+1,:,:]=[[l_z_grid[i]]*(len(l_y_grid)+1)]*(len(l_x_grid)+1)
    X_Pos+=[X_faces_voxel[1,:,:].tolist()]
    Y_Pos[-1,:,:]=Y_faces_voxel[1,:,:].tolist()
    Z_Pos[-1,:,:]=Z_faces_voxel[1,:,:].tolist()
    X_Pos=np.array(X_Pos)
    Y_Pos=np.array(Y_Pos)
    Z_Pos=np.array(Z_Pos)
    print()
    # print(Y_faces_voxel) # Warning : order is matrix order not cartesian 
    print()
    print(X_Pos.shape)
    print(X_Pos)
    print(Y_Pos.shape)
    print(Y_Pos)
    print(Z_Pos.shape)
    print(Z_Pos)
    
    #pour les bord prendre tout les ligne, pour les autre juste les extrême
    if "FE" in path:
        name_tmp=path[8:12]
    elif "CR" in path:
        name_tmp=path[-9:-5]
    elif "NI" in path:
        name_tmp=path[-10:-8]+path[-7:-5]
    elif "SS" in path:
        name_tmp=path[-8:-6]+"0"+path[-6]
    else:
        print("Error material unknown")
        exit()
    for i in range(len(X_Pos[0])): #Y-axis
        for j in range(len(X_Pos[0,0])): #Z-axis
            if (i in [0,len(X_Pos[0])-1]) or (j in [0,len(X_Pos[0,0])-1]):
                for k in range(len(X_Pos)-1): # X-axis
                    l_cuboid+=[[X_Pos[k,i,j],X_Pos[k+1,i,j],Y_Pos[i,k,j],Y_Pos[i+1,k,j],Z_Pos[j,k,i],Z_Pos[j+1,k,i]]]
                    l_name+=["P"+name_tmp+"X"+str(k)+"Y"+str(i)+"Z"+str(j)]
            else:
                l_cuboid+=[[X_Pos[0,i,j],X_Pos[-1,i,j],Y_Pos[i,0,j],Y_Pos[i+1,0,j],Z_Pos[j,0,i],Z_Pos[j+1,0,i]]]
                l_name+=["P"+name_tmp+"X0"+"Y"+str(i)+"Z"+str(j)]
       
    # For angle points for checking
    print(l_cuboid[0])
    print(data_X[0,0,0])
    print(data_Y[0,0,0])
    print(data_Z[0,0,0])
    print(l_cuboid[32])
    print(data_X[1,-1,0])
    print(data_Y[1,-1,0])
    print(data_Z[1,-1,0])
    print(l_cuboid[-31])
    print(l_cuboid[-33])
    print(data_X[0,0,-1])
    print(data_Y[0,0,-1])
    print(data_Z[0,0,-1])
    print(l_cuboid[-1])
    print(data_X[-1,-1,-1])
    print(data_Y[-1,-1,-1])
    print(data_Z[-1,-1,-1])
    s_path=path.split("/")
    n_path=s_path[0]+"/"+s_path[1]+"/"
    f = open(n_path+name_tmp+"sss_geom","w")
    Volumes.append(str(sum(lmap(lambda i: (i[1]-i[0])*(i[3]-i[2])*(i[5]-i[4])/1000,l_cuboid))))
    l_cuboid_str=lmap(lambda i : lmap(lambda j : " "+str(j/10),i),l_cuboid)
    for name, geom in zip(l_name,l_cuboid_str):
        f.write("surf s_"+name+" cuboid"+"".join(geom)+" \n")
        f.write("cell c_"+name+" 4 mat_petale -s_"+name+" \n")
    f.close()



        
    aff_mat(l_ax[0], l_y_grid, l_z_grid, repeat(rotate,3,data_X[0,:,:])             , "y pos", "z pos", "", "", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,300], ylim=[0,300])
    aff_mat(l_ax[1], l_y_grid, l_z_grid, repeat(rotate,3,data_X[1,:,:])-thickness_x , "y pos", "z pos", "", "", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,300], ylim=[0,300], offset=thickness_x) #possibly plotting inversing Y and Z
    # aff_mat(l_ax[0], l_y_grid, l_z_grid, data_X[0,:,:].T             , "y pos", "z pos", "", "", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,300], ylim=[0,300])
    # aff_mat(l_ax[1], l_y_grid, l_z_grid, data_X[1,:,:].T-thickness_x , "y pos", "z pos", "", "", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,300], ylim=[0,300], offset=thickness_x)
    
    aff_mat(l_ax[2], l_x_grid, l_z_grid, data_Y[:,0,:].T             , "x pos", "z pos", "", "", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,20], ylim=[0,300])
    aff_mat(l_ax[3], l_x_grid, l_z_grid, data_Y[:,1,:].T-thickness_y , "x pos", "z pos", "", "", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,20], ylim=[0,300])
    
    aff_mat(l_ax[4], l_x_grid, l_y_grid, data_Z[:,:,0].T             , "x pos", "y pos", "", "",                    minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,20], ylim=[0,300])
    aff_mat(l_ax[5], l_x_grid, l_y_grid, data_Z[:,:,1].T-thickness_z , "x pos", "y pos", "vertical", "\Delta [mm]", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,20], ylim=[0,300],pad=0.2)
    
    thickness = data_X[1,:,:]-data_X[0,:,:]
    aff_mat(l_ax[6], l_y_grid, l_z_grid, thickness-20 , "y pos", "z pos", "", "", minimaxi=(-0.15,0.15), nb_leg=2, xlim=[0,300], ylim=[0,300], contour=20)
    
    # l_ax[6].text(310,280,tex("Average thickness"),va="top",ha="left", size=16)
    # l_ax[6].text(310,265,tex(str(round(thickness_x,3))),va="top",ha="left", size=16)
    
    # m = data_X[1,:,:]-data_X[0,:,:]
    # l_ax[6].text(310,230,tex("Max thickness"),va="top",ha="left", size=16)
    # l_ax[6].text(310,215,tex(str(round(m.max(),3))),va="top",ha="left", size=16)
    
    # m = data_X[1,:,:]-data_X[0,:,:]
    # l_ax[6].text(310,180,tex("Face to face thickness"),va="top",ha="left", size=16)
    # l_ax[6].text(310,165,tex(str(round(data_X.max()-data_X.min(),3))),va="top",ha="left", size=16)
    
    
    print("average(face_A) - average(face_B)    "+aff_t([thickness_x, thickness_y, thickness_z], 20))
    print("max(face_A - face_B)                 "+aff_t(map(lambda m: m.max(), [data_X[1,:,:]-data_X[0,:,:], data_Y[:,1,:]-data_Y[:,0,:], data_Z[:,:,1]-data_Z[:,:,0]]), 20))
    print("(max face_A) - (min face_B)          "+aff_t(map(lambda m: m.max()-m.min(), [data_X, data_Y, data_Z]), 20))
    
    
    l_mini.append(str((data_X[1,:,:]-data_X[0,:,:]).min()))
    l_maxi.append(str((data_X[1,:,:]-data_X[0,:,:]).max()))
    l_ave.append(str(thickness_x))
    '''
    aff_mat4(l_x_grid, l_z_grid, data_Y[:,0,:].T,             tab_ax[2,0], "", "", "x pos", "z pos", centered=False, midblanc=True, minimaxi=(-0.15,0.15), pcol=False, nb_leg=2)
    aff_mat4(l_x_grid, l_z_grid, data_Y[:,1,:].T-thickness_y, tab_ax[3,0], "", "", "x pos", "z pos", centered=False, midblanc=True, minimaxi=(-0.15,0.15), pcol=False, nb_leg=2)
    
    aff_mat4(l_x_grid, l_y_grid, data_Z[:,:,0],             tab_ax[4,0], "", "", "x pos", "y pos", centered=False, midblanc=True, minimaxi=(-0.15,0.15), pcol=False, nb_leg=2)
    aff_mat4(l_x_grid, l_y_grid, data_Z[:,:,1]-thickness_z, tab_ax[5,0], "vertical", "", "x pos", "y pos", centered=False, midblanc=True, minimaxi=(-0.15,0.15), pcol=False, nb_leg=2)
    '''

offset = 0

# l_todo = lmap(lambda i : "data/ss/mesure_points_SS"+str(i+1+offset)+".xlsx", range(8))
# l_todo = lmap(lambda i : "data/ni/mesure_points_NI_"+("0" if (i+1+offset)<10 else "")+str(i+1+offset)+".xlsx", range(10))
l_todo = lmap(lambda i : "data/cr/mesure_points_CR"+("0" if (i+1+offset)<10 else "")+str(i+1+offset)+".xlsx", range(10))
# l_todo = lmap(lambda i : "data/fe/FE"+("0" if (i+1+offset)<10 else "")+str(i+1+offset)+".xlsx", range(12))

nb = len(l_todo)

fig = plt.figure(figsize=(27,7*nb))
fig.patch.set_facecolor('white')

tab_ax = my_sub6(fig,1,1,0,list_ry=[1]*nb, list_sy=[0.2]*(nb-1), list_rx=[1,1,0.2,0.2,0.2,0.2,1], list_sx=[0.0]*5+[0.2], auto_y=False,auto_x=False, mb=0.1, mh=0.1, mg=0.15, md=0.25)

for i, path in enumerate(l_todo):
    do_you_job(path, tab_ax[:,len(l_todo)-1-i])

if True:
    print("coucou")
    print("\n".join(l_mini))
    print("coucou")
    print("\n".join(l_maxi))
    print("coucou")
    print("\n".join(l_ave))
    print("coucou Volumes")
    print("\n".join(Volumes))
    print()
matrix = [[4, 5, 8, 7],
          [6, 2, 1, 5],
          [6, 4, 5, 3], 
          [2, 1, 8, 9]]
print(rotate(matrix))

# plt.rcParams.update({'font.size':24})
fig.savefig("img.png", bbox_inches=('tight'), dpi=200)

# plt.show()

#aff_mat4(lx, ly, mat, ax, orientation, titre, xlab, ylab, xlim=None, ylim=None,
#    logz=None, logx=False, logy=False, minimaxi=None, midblanc=False, midgreen=False, minblanc=False, simple_scale=False,nb_leg=4,
#    maxblanc=False, centered=False, smooth=None, pad=None, pcol=False,head_top=True, maskout=False):

                 #l_x += [x]
                 #l_y += [y]
                 #l_z += [z]
         #ll_xyz = []

#print(len(data))
#print(len(l_x))
#exit()
'''
for s,axe in l_bloc:
    print("#"*30)
    print(l_x[:s])
    print()
    print(l_y[:s])
    print()
    print(l_z[:s])
    print()
    
    if axe == "X":
        iy = get_pos()
    
    ll_xyz += [[l_x[:s], l_y[:s], l_z[:s]]]
    l_x = l_x[s:]
    l_y = l_y[s:]
    l_z = l_z[s:]



print(ll_xyz[0][1])
'''
