import pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.image as img
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.optimize import leastsq
import matplotlib.text as Text
import string
import scipy.stats
from scipy.stats import sem
import seaborn as sns

font={'family': 'serif'}
plt.rc('font', **font)

plt.rcParams["axes.titlesize"]=18
plt.rcParams["axes.labelsize"]=18
plt.rcParams["lines.linewidth"]=2
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'custom'

color1 = '#5599FF'
color2 = '#4D4D4D'
color3 = '#999999'
color4 = '#FFE680'

fig = plt.figure(figsize=(15,13))
gs1 = gridspec.GridSpec(3, 1)
gs1.update(left=0.1, right=0.58,top=0.95,bottom=0.05,hspace=0.1)
ax1 = plt.subplot(gs1[0,0])
ax3 = plt.subplot(gs1[1,0])
ax4 = plt.subplot(gs1[2,0])

gs2 = gridspec.GridSpec(9, 1)
gs2.update(left=0.67, right=0.98, top=0.98,bottom=0.05,hspace=0.3)
ax2 = plt.subplot(gs2[0:5,0])
ax5 = plt.subplot(gs2[6:9,0])

###ax1
ax1.axis("off") #leave space for illustration

###ax2
###set colors####
c1 = '#50504E'
c2 = '#F35F5D'
c3 = '#FEE066'
c4 = '#237B9F'
c5 = '#70C0B3'
c6 = '#8C7B11'

T = "./interval_exp/"
data1 = np.load(T+"7575_mean_conns.npy")
var1 = np.load(T+"7575_std_conns.npy")
conn1 = np.load(T+"7575_conns.npy")

data2 = np.load(T+"75150_mean_conns.npy")
var2 = np.load(T+"75150_std_conns.npy")
conn2 = np.load(T+"75150_conns.npy")

data3 = np.load(T+"15075_mean_conns.npy")
var3 = np.load(T+"15075_std_conns.npy")
conn3 = np.load(T+"15075_conns.npy")

data4 = np.load(T+"150150_mean_conns.npy")
var4 = np.load(T+"150150_std_conns.npy")
conn4 = np.load(T+"150150_conns.npy")

data5 = np.load(T+"150300_mean_conns.npy")
var5 = np.load(T+"150300_std_conns.npy")
conn5 = np.load(T+"150300_conns.npy")

data6 = np.load(T+"300150_mean_conns.npy")
var6 = np.load(T+"300150_std_conns.npy")
conn6 = np.load(T+"300150_conns.npy")


labels=['6000s','300s','150s','150s','150s','75s','75s']
bplots = ax2.boxplot([conn5[:,1],conn6[:,20],conn5[:,40],conn4[:,40],conn3[:,40],conn2[:,80],conn1[:,80]],patch_artist=True,labels=labels)


c7 = 'w'
colors = [c7,c6,c5,c4,c3,c2,c1]

for box in bplots:
    for patch, color in zip(bplots['boxes'],colors):
        patch.set_facecolor(color)

ax2.legend([bplots["boxes"][6], bplots["boxes"][5],bplots["boxes"][4],bplots["boxes"][3],bplots["boxes"][2],bplots["boxes"][1],bplots["boxes"][0]], ['t1=75s, t2=75s', 't1=75s, t2=150s', 't1=150s, t2=75s', 't1=150s, t2=150s', 't1=150s, t2=300s', 't1=300s, t2=150s', 'DC stimulation'], loc='lower right')

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.axvline(x=1.5,linestyle='--',color='grey',alpha=0.4)
ax2.axvline(x=2.5,linestyle='--',color='grey',alpha=0.4)
ax2.axvline(x=5.5,linestyle='--',color='grey',alpha=0.4)
ax2.set_ylabel(r'$\Gamma$')
ax2.set_ylim(0.0895,0.0942)
ax2.set_xlabel("t1 (s)")


### ax3 
x1 = np.arange(1,11,1)*75.
x2 = np.arange(1,201,1)*7.5+750
x = np.hstack((x1,x2))

N=1000

T = "./rep_example/"
g1g1_mean = np.load(T+str(N)+'g1g1_mean.npy')
g1g2_mean = np.load(T+str(N)+'g1g2_mean.npy')
g2g1_mean = np.load(T+str(N)+'g2g1_mean.npy')
g2g2_mean = np.load(T+str(N)+'g2g2_mean.npy')

rates1_mean = np.load(T+str(N)+'rates1_mean.npy')
rates2_mean = np.load(T+str(N)+'rates2_mean.npy')


g1g1_std = np.load(T+str(N)+'g1g1_std.npy')
g1g2_std = np.load(T+str(N)+'g1g2_std.npy')
g2g1_std = np.load(T+str(N)+'g2g1_std.npy')
g2g2_std = np.load(T+str(N)+'g2g2_std.npy')

rates1_std = np.load(T+str(N)+'rates1_std.npy')
rates2_std = np.load(T+str(N)+'rates2_std.npy')


ax3.plot(x,rates1_mean,'o-',color=color1,markerfacecolor=color1,markeredgecolor='none',label=r'$\mathrm{sti}$')
ax3.plot(x,rates2_mean,'o-',color=color2,markerfacecolor=color2,markeredgecolor='none',label=r'$\mathrm{bg}$')

ax3.fill_between(x,rates1_mean-rates1_std,rates1_mean+rates1_std,color=color1,alpha=0.2)
ax3.fill_between(x,rates2_mean-rates2_std,rates2_mean+rates2_std,color=color2,alpha=0.2)
ax3.axvspan(750,900,alpha=0.1,color='grey')
ax3.axvspan(1050,1200,alpha=0.1,color='grey')
ax3.axvspan(1350,1500,alpha=0.1,color='grey')
ax3.axvspan(1650,1800,alpha=0.1,color='grey')
ax3.axvspan(1950,2100,alpha=0.1,color='grey')
ax3.text(900.,8.55,r'$t_1 = 150\mathrm{s}, t_2=150\mathrm{s}, \Delta V_m=0.1\mathrm{mV}$',fontsize=18.,fontname='serif')


ax3.set_xlim(590,2300)
ax3.set_ylim(7.5,8.7)
ax3.set_yticks((7.6,8.0,8.4))
ax3.set_xticks(([]))
ax3.set_ylabel('Firing rate (Hz)')
ax3.legend(loc='best')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')


ax4.plot(x,g1g1_mean,'o-',color=color1,markerfacecolor=color1,markeredgecolor='none',label=r'$\mathrm{sti} \rightarrow  \mathrm{sti}$')
ax4.plot(x,g2g1_mean,'s-',color=color3,markerfacecolor=color3,markeredgecolor='none',label=r'$\mathrm{bg} \leftrightarrow  \mathrm{sti}$')
ax4.plot(x,g2g2_mean,'o-',color=color2,markerfacecolor=color2,markeredgecolor='none',label=r'$\mathrm{bg} \rightarrow  \mathrm{bg}$')

ax4.fill_between(x,g1g1_mean-g1g1_std,g1g1_mean+g1g1_std,color=color1,alpha=0.2)
ax4.fill_between(x,g2g1_mean-g2g1_std,g2g1_mean+g2g1_std,color=color3,alpha=0.2)
ax4.fill_between(x,g2g2_mean-g2g2_std,g2g2_mean+g2g2_std,color=color2,alpha=0.2)
ax4.axvspan(750,900,alpha=0.1,color='grey')
ax4.axvspan(1050,1200,alpha=0.1,color='grey')
ax4.axvspan(1350,1500,alpha=0.1,color='grey')
ax4.axvspan(1650,1800,alpha=0.1,color='grey')
ax4.axvspan(1950,2100,alpha=0.1,color='grey')

ax4.set_xlim(590,2300)
ax4.set_xticks((750,900,1050,1200,1350,1500,1650,1800,1950,2100,2250))
ax4.set_yticks((0.087,0.088,0.089,0.090,0.091,0.092))
ax4.set_ylim(0.087,0.0925)
ax4.set_ylabel('Connectivity '+r'$\Gamma$')
ax4.set_xlabel('Time (s)')
ax4.legend(loc='best')
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')




### intensity-dependent manner
T = "./saturation_exp/"

data01 = np.load(T+"small_1000g1g1_seed_1.npy")*10.
data02 = np.load(T+"small_1000g1g1_seed_2.npy")*10.
data03 = np.load(T+"small_1000g1g1_seed_3.npy")*10.
data04 = np.load(T+"small_1000g1g1_seed_4.npy")*10.
data1 = np.load(T+"1000g1g1_seed_1.npy")*10.
data2 = np.load(T+"1000g1g1_seed_2.npy")*10.
data3 = np.load(T+"1000g1g1_seed_3.npy")*10.
data4 = np.load(T+"1000g1g1_seed_4.npy")*10.
data5 = np.load(T+"1000g1g1_seed_5.npy")*10.
data6 = np.load(T+"1000g1g1_seed_6.npy")*10.
data7 = np.load(T+"1000g1g1_seed_7.npy")*10.
data8 = np.load(T+"1000g1g1_seed_8.npy")*10.
data9 = np.load(T+"1000g1g1_seed_9.npy")*10.
data10 = np.load(T+"1000g1g1_seed_10.npy")*10.
data11 = np.load(T+"1000g1g1_seed_11.npy")*10.
data12 = np.load(T+"1000g1g1_seed_12.npy")*10.
data50 = np.load(T+"1000g1g1_seed_50.npy")*10.
data100 = np.load(T+"1000g1g1_seed_100.npy")*10.

Is = [0.5,1.0,1.5,2.0,2.5,5,7.5,10,12.5,15.]
R = 40000000.0
V = np.array(Is)*R*10**(-12)*10**3

ax5.plot(V[0:9],[data01[-1],data02[-1],data03[-1],data04[-1],data1[-1],data2[-1],data3[-1],data4[-1],data5[-1]],'k.-')
ax5.plot(V[4],data1[-1],'o',color='r',label=r'$0.1\mathrm{mV}$',markersize=7.)

ax5.set_xlabel(r'$\Delta V_m \ (\mathrm{mV})$')
ax5.set_ylabel('Peak connectivity')
ax5.set_xlim(0,1.0)
ax5.set_ylim(0.086,0.15)
ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
ax5.axhline(y=0.09,linestyle='--',linewidth=0.5,color='grey')

ax5_inset = fig.add_axes([0.86,0.135,0.12,0.15])

x1 = np.arange(0,81,1)*225
ax5_inset.plot(x1,data01[9::3],color='k',alpha=0.1)
ax5_inset.plot(x1,data02[9::3],color='k',alpha=0.2)
ax5_inset.plot(x1,data03[9::3],color='k',alpha=0.3)
ax5_inset.plot(x1,data04[9::3],color='k',alpha=0.4)
ax5_inset.plot(x1,data1[9::3],color='r',label=r'$0.1\mathrm{mV}$')
ax5_inset.plot(x1,data2[9::3],color='k',alpha=0.5)
ax5_inset.plot(x1,data3[9::3],color='k',alpha=0.6)
ax5_inset.plot(x1,data4[9::3],color='k',alpha=0.7)
ax5_inset.plot(x1,data5[9::3],color='k',alpha=0.8)

ax5_inset.set_ylabel(r'$\Gamma$')
ax5_inset.set_xlabel("Time (s)",fontsize=12.)
ax5_inset.spines["right"].set_visible(False)
ax5_inset.spines["top"].set_visible(False)


plt.savefig("Fig5_canvas.svg")
plt.show()
