
from scipy.optimize import curve_fit
from ZPyDosi.Common.utils_general import lmap, get_aff_size, tex
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.Plots.SubPlots import my_sub6
from ZPyDosi.Prints.PrintnSave import aff_list
import numpy as np
import matplotlib.pyplot as plt

path_tka = get_param_vari("tka" , str, None).split("//")
peak_x = get_param_vari("peak_x" , bool, "False")

fig = plt.figure(0, figsize=(15.,10.))
fig.patch.set_facecolor('white')
ax2,ax1 = my_sub6(fig, 1, 1, 0, list_ry=[1,1], list_rx=[1], auto_x=True, auto_y=False)[0,:]


def get_ab_from_Eu_TKA(path_tka_):
    for path_tka in path_tka_ :
        l_val = lmap(lambda l:float(l), open(path_tka).readlines()[2:])
    
        pos_121 = l_val.index(max(l_val))
        if peak_x:
            print("Peak X",pos_121)
            pos_121 = l_val.index(max(l_val[pos_121+20:]))
        print(pos_121), l_val[pos_121]
        pos_344 = l_val.index(max(l_val[pos_121+20:]))
        print(pos_344), l_val[pos_344]
    
        x1, y1 = pos_121, 121.782
        x2, y2 = pos_344, 344.275
        a = (y2-y1)/(x2-x1)
        b = (y1-a*x1)
        print (a,b)
    
        l_nrj = [    121.782 ,
                244.697 ,
                344.275 ,
                411.1165,
                443.965,
                488.6792,
                586.265, 
                778.904 ,
                964.042 ,
                1005.272,
                1085.837,
                1112., 
                1212.948, 
                1408.01, 
                1528.103, 
                #1605.61
            ]
        l_pos = []
        print ()
        for nrj in l_nrj:
            pos_approx = int((nrj-b)/a)
            sub_l_val = l_val[pos_approx-50:pos_approx+50]
            pos = pos_approx-50 + sub_l_val.index(max(sub_l_val))
            larg = 4
            var = sum(l_val[pos-larg:pos+larg+1] * np.arange(-larg,larg+1))/sum(l_val[pos-larg:pos+larg+1])
            #print(l_val[pos-larg:pos+larg+1] , np.arange(-larg,larg+1),l_val[pos-larg:pos+larg+1])
            pos += var
            print(aff_list("",[nrj,pos_approx,pos,var]))
            l_pos += [pos]
            #print pos, l_val[pos]
        print()
        l_nrj = np.array(l_nrj)
        l_pos = np.array(l_pos)
        
        ax1.plot(l_nrj,     l_pos,"o", c=(0,0,0))
        
        
        '''
        x1, y1 = l_pos[0], l_nrj[0]                    # lin fit with 2 first point
        x2, y2 = l_pos[2], l_nrj[2]
        a = (y2-y1)/(x2-x1)
        b = (y1-a*x1)
        ax1.plot(a*l_pos[[0,-1]]+b, l_pos[[0,-1]], c=(1,0,0))
        ax2.plot(l_nrj, (l_nrj-b)/a - l_pos,"o", c=(1,0,0))
        '''
        def fct_nrj2pos(x,a,b):                        # lin fit with all points
            return a*x+b
        best_p, covar = curve_fit(fct_nrj2pos, l_nrj, l_pos)
        ax1.plot(l_nrj[[0,-1]], fct_nrj2pos(l_nrj[[0,-1]], *best_p))
        ax2.plot(l_nrj,         l_pos - fct_nrj2pos(l_nrj, *best_p),"o", label=str("ax+b, a="+str(round(best_p[0],4)) +" $\pm$ " +str('{:0.0e}'.format(covar[0][0]**0.5))+" b="+str(round(best_p[1],1))+"$\pm$ " + str('{:0.0e}'.format(covar[1][1]**0.5))))
        print("a*x+b", "\t".join(map(lambda v: format(v, "0.20e"),best_p)))
        print("sig : a*x+b", "\t".join(map(lambda v: format(v, "0.20e"),np.sqrt(np.diag(covar)))))
        
        def fct_nrj2pos(x,a,b,c):                    # lin fit with all points
            return a*x**2+b*x+c
        best_p, covar = curve_fit(fct_nrj2pos, l_nrj, l_pos)
        #ax1.plot(l_nrj[[0,-1]], fct_nrj2pos(l_nrj[[0,-1]], *best_p), c=(0,0,1))
        #ax2.plot(l_nrj,         l_pos - fct_nrj2pos(l_nrj, *best_p),"o", c=(0,0,1), label=str("ax**2+b*x+c, a="+str('{:0.3e}'.format(best_p[0]))+" b="+str('{:0.3e}'.format(best_p[1]))+" c="+str('{:0.3e}'.format(best_p[2]))))
        print("a*x**2+b*x+c", "\t".join(map(lambda v: format(v, "0.20e"),best_p)))
        print("sig : a*x**2+b*x+c", "\t".join(map(lambda v: format(v, "0.20e"),np.sqrt(np.diag(covar)))))
        

get_ab_from_Eu_TKA(path_tka)

ax2.legend(loc='best', fontsize=get_aff_size("s_leg"), ncol=1)



ax2.set_xlabel(tex(r"Energy [keV]"), size=get_aff_size("s_xylabel"))
ax1.set_ylabel(tex(r"Channel [bin]"), size=get_aff_size("s_xylabel"))
ax2.set_ylabel(tex(r"Error [bin]"), size=get_aff_size("s_xylabel"))
#ax1.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
#ax1.tick_params(labelbottom='off')
#ax1.tick_params(axis='x',labelbottom='off')

ax1.set_xticklabels([])
plt.tight_layout()
plt.show()




