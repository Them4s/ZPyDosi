from ZPyDosi.Common.utils_general import lmap, tex, get_c
from ZPyDosi.Common.GetParam import get_param_vari
from ZPyDosi.DataIrrad.DataIrrad import DataIrrad
from ZPyDosi.Prints.PrintnSave import aff_s_v
import numpy as np
import datetime
import matplotlib.pyplot as plt

path_csv_data  = get_param_vari("csv_data", str)
path_csv_dosi  = get_param_vari("csv_dosi", str)
lcase_csv  = get_param_vari("lcase", str).split("/")
DT_corr  = get_param_vari("dt_corr", bool, "True")
rr_shape  = get_param_vari("rr_shape", bool, "False")

puiss_max_plot = get_param_vari("puiss_max_plot", float, "110")

l_time_dash_todo = []

data_irrad = DataIrrad  (   path_csv_data,
                            path_csv_dosi,
                            lcase_csv,
                            use_sqrt_for_meas_sig=False,
                            load_hpge_eff=True,
                            load_sss_results=True,
                            #load_sss_spectrum=True,
                            load_ndup=False,
                            load_ndup_nuis=False,
                            load_ndup_nuis_tosuppress=False,
                            load_up_pos=False,
                            load_up_pos_tosuppress=False,
                            remove_data=True )

class Measure:
    def __init__(self, dwell, t0, l_path, J_per_I, irrad_time_stop, dwell_obj=None, corrected_tka=True): #key : Measure, added the parameter corrected tka to allow the usage of DataIrrad specific function of DT correction.
        if dwell_obj is None: dwell_obj = dwell
        #dwell_obj = 1
        self.t0 = t0
        #dwell = 1
        if corrected_tka and not data_irrad:
            print("Error : \"data_irrad\" variable of \"DataIrrad\" class must be defined in script in order to apply dead time correction. \n Script aborted") 
            exit()
        l_v = []
        t_prev, l_v_prev = None, None
        for path in l_path.split("//"):
        
            if path.endswith(".CNF"):
                print("ERROR - CNF file instead of TKA input file :",path)
                exit()
                
            ye,mo,da,ho,mi,se,voie,dw = path.split("/")[-1].split("_")[:8]
            t =  datetime.datetime(*map(lambda s: int(s), [ye,mo,da,ho,mi,se]))
            if t_prev is not None:
                manque = int((t-t_prev).total_seconds() - len(l_v_prev))
                nb_s = 10
                ave_v, ave_s = sum(l_v_prev[-nb_s:]) / nb_s, (sum(l_v_prev[-nb_s:]))**0.5 / nb_s
                print("# il manque",manque,"secondes, utilisation de la valeur moyenne des 10 dernieres secondes :",ave_v, "+-", ave_s/ave_v*100,"[\%]")
                l_v += [ave_v] * manque
            t_prev = t
            l_v_prev = lmap(lambda v:float(v), open(path).readlines()[2:])
            l_v += l_v_prev
        #print("len(l_v)", len(l_v))
        #exit()
        if corrected_tka : #Key : corrected monitor, correction for dead time, dwell time and voie are expected to be the same for all tka.
            l_v = np.array(data_irrad.linearity_loss_corrected_tka(l_v,id_voie=voie,dwell_time=dw))
            l_v=l_v.tolist()
        while l_v[-1] == 0:
            l_v.pop(len(l_v)-1)
        fact = int(dwell_obj/dwell)
        if fact > 1:
            print("reduce time serie (dwell)")
            new_l_v = []
            while len(l_v)>fact:
                new_l_v += [sum(l_v[:fact])]
                l_v = l_v[fact:]
            dwell = dwell * fact
            l_v = new_l_v
        self.l_v = np.array(l_v)
        self.l_t = np.arange(len(self.l_v))*dwell
        self.l_s = self.l_v**0.5
        if dwell_obj<dwell:
            fact = int(dwell/dwell_obj)
            print ("expand time serie (dwell)", dwell/dwell_obj, fact)
            new_l_v, new_l_s = np.zeros(len(self.l_v)*fact), np.zeros(len(self.l_v)*fact)
            for i in range(len(l_v)):
                for j in range(fact):
                    new_l_v[i*fact+j] = self.l_v[i]/fact
                    new_l_s[i*fact+j] = self.l_s[i]/fact
            dwell = dwell / fact
            self.l_v = new_l_v
            self.l_s = new_l_s
            self.l_t = np.arange(len(self.l_v))*dwell
        pos_maxi = l_v.index(max(self.l_v))
        if self.l_v[pos_maxi+10] == 0: # alors le G2K comptait quand les moni on ete arretes
            self.l_v[pos_maxi-10:pos_maxi+10] = [0] * 20

        self.l_v *= J_per_I
        self.l_s *= J_per_I
        self.l_v /= dwell
        self.l_s /= dwell
        self.dwell = dwell
        self.tot_power=sum(self.l_v*dwell)
        print("total_power: {} Wh".format(self.tot_power/3600))
        maxi = max(self.l_v)
        i_fall = len(self.l_v)-1
        while self.l_v[i_fall] < maxi*0.5: i_fall -= 1
        while self.l_v[i_fall-1] > self.l_v[i_fall]*1.05: i_fall -= 1
        if i_fall == len(self.l_v)-1: i_fall -= 1
        avancement = 1.*self.l_v[i_fall+1]/self.l_v[i_fall]
        self.t_fall = self.l_t[i_fall] + avancement*(self.l_t[i_fall+1]-self.l_t[i_fall]) + self.dwell
        t_stop = (irrad_time_stop-t0).total_seconds()
        
        #print(l_path)
        print("# t0 =", self.t0)
        print("# t_stop - "+str(irrad_time_stop)+" ("+str(t_stop)+" s after begin)")
        print ("# Warning - compensation of the stop-time in the csv and interpreted with the monitor:", t_stop - self.t_fall,"s")
        self.t0 += datetime.timedelta(seconds=(t_stop-self.t_fall))
        print("# after correction t0 =", self.t0)

        cut = 0.9
        s_v, s_d = 0, 0
        maxi = max(self.l_v)
        for v in self.l_v:
            if v>cut*maxi:
                s_v += v*self.dwell
                s_d += self.dwell
        print("# info (not used for analysis): with a cut at "+str(cut*100)+" %, the irradiation time is "+str(s_d)+" s and the average power "+str(s_v/s_d)+" W")
        print()
    # def plot(self, ax, c, label=None):
    #     dec = (self.t0-time_ref).total_seconds()
    #     dec = 0
    #     aff_curve(ax, dupx(self.l_t + dec)/3600.,dup(self.l_v),dup(self.l_s),c,1.,0.3, label=label)
        
        
        #ax.plot([(self.t_fall+dec)/3600., (self.t_fall+dec)/3600.],ax.get_ylim(),c=(0.3,0.3,0.3),dashes=[2,5])
        
    def calc_diff_shape(self, fact, halftime, date_start, hpge_time, time_in_hpge, name, ax=None,minutes_mid=7.5,minu_max=7.1,minu_min=9.9):
        l_prod = 1.*self.l_v
        l_t = np.array((self.l_t))
        l_v2=np.zeros(len(l_t))
        l_v3=np.zeros(len(l_t))
        l_v4=np.zeros(len(l_t))
        for i in range(len(l_t)):
            if l_t[i] >= self.t_fall-minutes_mid*60 and l_t[i]<self.t_fall:
                l_v2[i]=self.tot_power/minutes_mid/60
            if l_t[i] >= self.t_fall-minu_max*60 and l_t[i]<self.t_fall:
                l_v3[i]=self.tot_power/minu_max/60
            if l_t[i] >= self.t_fall-minu_min*60 and l_t[i]<self.t_fall:
                l_v4[i]=self.tot_power/minu_min/60
        l_at = []
        l_at2 = []
        l_at3 = []
        l_at4 = []
        lambd = np.log(2)/halftime
        at = 0
        at2 = 0
        at3 = 0
        at4 = 0
        sum_cp_irrad = 0
        t_irrad = (date_start-self.t0).total_seconds()
        for i in range(len(l_t)):
            if l_t[i]>t_irrad:
                sum_cp_irrad += fact*self.l_v[i]*self.dwell
                at += (fact*self.l_v[i] -lambd*at)*self.dwell
                at2 += (fact*l_v2[i] -lambd*at2)*self.dwell
                at3 += (fact*l_v3[i] -lambd*at3)*self.dwell
                at4 += (fact*l_v4[i] -lambd*at4)*self.dwell
                if l_t[i]>(self.t_fall):
                    idt=i
                    print("Relative difference flat over plofile : {}%".format(at2/at*100-100))
                    print("Relative difference flat over plofile : {}%".format(at3/at*100-100))
                    print("Relative difference flat over plofile : {}%".format(at4/at*100-100))
                    break
            else:
                l_prod[i] = 0
            l_at += [at]
            l_at2 += [at2]
            l_at3 += [at3]
            l_at4 += [at4]
        plt.figure()
        plt.plot(l_t/60,self.l_v/self.l_v[idt-2]  ,label="True shape"                                    )
        plt.plot(l_t/60,l_v2/self.l_v[idt-2]      ,label="Averaged, start at middle of power increase"   )
        plt.plot(l_t/60,l_v3/self.l_v[idt-2]      ,label="Averaged, start at the end of power increase"  )
        plt.plot(l_t/60,l_v4/self.l_v[idt-2]      ,label="Averaged, start at beginning of power increase")
        plt.xlabel("Time [min]")
        plt.ylabel("Reactor Power [a.u]")
        plt.xlim(14,26.5)
        plt.legend()
        fig, ax=plt.subplots()
        plt.plot(np.arange(len(l_at))/60,l_at /l_at[-1],label="True shape"                                    )
        plt.plot(np.arange(len(l_at))/60,l_at2/l_at[-1],label="Averaged, start at middle of power increase"   )
        plt.plot(np.arange(len(l_at))/60,l_at3/l_at[-1],label="Averaged, start at the end of power increase"  )
        plt.plot(np.arange(len(l_at))/60,l_at4/l_at[-1],label="Averaged, start at beginning of power increase")
        plt.xlabel("Time [min]")
        plt.ylabel("Activity [Bq]")
        plt.xlim(14,26.5)
        axins=ax.inset_axes([0.1,0.65,0.40,0.30],xlim=(24.5,25.5),ylim=(0.93,1.02))
        axins.plot(np.arange(len(l_at))/60,l_at /l_at[-1],label="True shape"                                    )
        axins.plot(np.arange(len(l_at))/60,l_at2/l_at[-1],label="Averaged, start at middle of power increase"   )
        axins.plot(np.arange(len(l_at))/60,l_at3/l_at[-1],label="Averaged, start at the end of power increase"  )
        axins.plot(np.arange(len(l_at))/60,l_at4/l_at[-1],label="Averaged, start at beginning of power increase")
        axins.indicate_inset_zoom(axins,edgecolor="black")

        # plt.legend()
        plt.show()
        return at2/at*100-100
        
    def propagate_rr(self, fact, halftime, date_start, hpge_time, time_in_hpge, name, ax=None):
        global label_already_done
        lambd = np.log(2)/halftime
        cp_histo = []
        cp_histo_met_2 = []
        
        l_t = list(self.l_t)
        l_at = []
        
        t_irrad = (date_start-self.t0).total_seconds()
        t_final = (hpge_time-self.t0).total_seconds()+time_in_hpge+60
        
        #l_time_dash_todo.append((date_start-time_ref).total_seconds()/3600.)
        #l_time_dash_todo.append((self.t_fall+(self.t0-time_ref).total_seconds())/3600.)
        l_time_dash_todo.append((date_start-self.t0).total_seconds()/3600.)
        l_time_dash_todo.append((self.t_fall)/3600.)
        
        
        
        l_prod = 1.*self.l_v
        at = 0
        sum_cp_irrad = 0
        for i in range(len(l_t)):
            if l_t[i]>t_irrad:
                sum_cp_irrad += fact*self.l_v[i]*self.dwell
                at += (fact*self.l_v[i] -lambd*at)*self.dwell
            else:
                l_prod[i] = 0
            l_at += [at]
        
        dt = 10
        if True:
            print (aff_s_v("cp_histo at irrad end",at))
        while l_t[-1]<t_final:
            at += -lambd*at* (self.dwell*dt)
            l_at += [at]
            l_t  += [l_t[-1]+(self.dwell*dt)]
        
        t_begin = (hpge_time-self.t0).total_seconds()
        decay, i = 0, 0
        while l_t[i]<t_begin : i += 1
        i0 = i
        while l_t[i]-t_begin < time_in_hpge:
            decay += lambd*l_at[i]*self.dwell*(l_t[i+1]-l_t[i])
            i += 1
        cp_histo = decay
        
        elt = name.split('-')[0]
        # c = get_c_elt(elt)
        
        lab = tex(name[:2])
        if lab in label_already_done: lab = None
        else:     label_already_done += [lab]
        
        
        # ax.plot((np.array(l_t)+(self.t0-time_ref).total_seconds())/3600.,np.array(l_at)/3600., c=c, linewidth=2, label=lab, zorder = -int(halftime))
        #print("Max_Wh",np.max(np.array(l_at)/3600.))
        # ax.fill_between((np.array(l_t[i0:i])+(self.t0-time_ref).total_seconds())/3600., np.array(l_at[i0:i])*0, np.array(l_at[i0:i])/3600., facecolor=c, alpha=0.5,linewidth=0.0, zorder = 0)
        #ax.plot((np.array(l_t))/3600.,np.array(l_at)/3600., c=c, linewidth=2, label=lab, zorder = -int(halftime))
        #ax.fill_between((np.array(l_t[i0:i]))/3600., np.array(l_at[i0:i])*0, np.array(l_at[i0:i])/3600., facecolor=c, alpha=0.5,linewidth=0.0, zorder = 0)
        
        l_t_prod = np.arange(len(l_prod))*self.dwell
        
        cp_histo_met_2 = self.dwell*sum(fact * l_prod * np.exp(-lambd*(t_begin-l_t_prod)) * (1-np.exp(-lambd*time_in_hpge)))
        if True:
            print (aff_s_v("cp_histo",cp_histo))
            print (aff_s_v("cp_histo_met_2",cp_histo_met_2))
            print (aff_s_v("diff [%]",(cp_histo_met_2/cp_histo-1)*100))
            
        #ax.set_xlim([-1, ax.set_xlim()[-1]])
        return cp_histo_met_2




d_path2moni={}
l_diff = []
for idosi in range(data_irrad.nb_dosi):
    #print(data_irrad.l_monitor_path[idosi])
    ye,mo,da,ho,mi,se,voie,dw = data_irrad.l_monitor_path[idosi].split("//")[0].split("/")[-1].split("_")[:8]
    dwell = float(dw[1:])
    if data_irrad.l_monitor_path[idosi] in d_path2moni:
        moni = d_path2moni[data_irrad.l_monitor_path[idosi]]
    else:
        print ("# load monitor",data_irrad.l_monitor_path[idosi])
        J_per_I = 1./data_irrad.l_monitor_calib[idosi]
        moni = Measure(    dwell,
                datetime.datetime(*map(lambda s: int(s), [ye,mo,da,ho,mi,se])),
                data_irrad.l_monitor_path[idosi],
                J_per_I,
                data_irrad.l_irrad_time_stop[idosi], 
                corrected_tka=DT_corr)
        c = get_c(list(set(data_irrad.l_case_csv)).index(data_irrad.l_case_csv[idosi]),len(list(set(data_irrad.l_case_csv))))
        # moni.plot(l_ax[0], c, label=tex(data_irrad.l_case_csv[idosi]))  # , label=r"$\mathrm{monitor~}"+str(i_path_moni+1)+"$"
        d_path2moni[data_irrad.l_monitor_path[idosi]] = moni
        for t in [
                (data_irrad.l_irrad_time_start[idosi]-moni.t0).total_seconds()/3600.,
                moni.t_fall/3600,
                 ]:
            # l_ax[0].plot([t,t],[0,puiss_max_plot],c=c, alpha=0.25, zorder=-10) # dashes=[2,5],
            a=1
    #print("propagate_rr",data_irrad.l_name[idosi])
    l_diff += [moni.calc_diff_shape(    1.,
                        data_irrad.l_half_time[idosi],
                        data_irrad.l_irrad_time_start[idosi],
                        data_irrad.l_hpge_time[idosi],
                        data_irrad.l_time_in_hpge[idosi],
                        data_irrad.l_name[idosi],
                        ax=None)]
print(l_diff)