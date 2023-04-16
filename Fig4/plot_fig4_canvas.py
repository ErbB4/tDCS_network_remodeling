import pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.image as img
from mpl_toolkits.axes_grid1 import make_axes_locatable
import string

color1 = [85./255.,153./255.,255./255.]
color2 = [77./255.,77./255.,77./255.]
color3 = [153./255.,153./255.,153./255.]
color4 = [255./255.,230./255.,128./255.]
plt.rcParams["axes.titlesize"]=18
plt.rcParams["axes.labelsize"]=18
plt.rcParams["lines.linewidth"]=2
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'custom'

mem_V = np.array([-1.2, -0.8, -0.4,  0. ,  0.4,  0.8,  1.2])
fig = plt.figure(figsize=(15,13))

gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.95, bottom=0.7, left=0.06,right=0.93,wspace=0.15)

gs2 = gridspec.GridSpec(1, 3)
gs2.update(top=0.7, bottom=0.35, left=0.06,right=0.93,wspace=0.15)

gs3 = gridspec.GridSpec(1, 3)
gs3.update(top=0.33, bottom=0.05, left=0.06,right=0.93,wspace=0.15)


ax1 = fig.add_subplot(gs1[0,0])
ax2 = fig.add_subplot(gs1[0,1])
ax3 = fig.add_subplot(gs1[0,2]) 

ax4 = fig.add_subplot(gs2[0,0])
ax5 = fig.add_subplot(gs2[0,1])
ax6 = fig.add_subplot(gs2[0,2])

ax7 = fig.add_subplot(gs3[0,0])
ax8 = fig.add_subplot(gs3[0,1])
ax9 = fig.add_subplot(gs3[0,2])


###ax1
ax1.axis("off") #leave space for illustration

###ax2
ax2.axis("off") #leave space for illustration

###ax3
ax3.axis("off") #leave space for illustration

### ax4, dual-group
gains = np.load("./bi/si.npy")
gain1 = gains[3,:]
gain3 = gains[2,:]
gain5 = gains[1,:]
gain7 = gains[0,:]

img4 = ax4.imshow(gains, aspect='equal',interpolation='nearest',vmin=0.0,vmax=150.)
ax4.set_xticks((0,1,2,3,4,5))
ax4.set_xticklabels(("-1.2","-0.8","-0.4","0.4","0.8","1.2"))
ax4.set_yticks((3,2,1,0))
ax4.set_yticklabels(("10%","30%","50%","70%"))
ax4.set_ylabel("G1 ratio")

divider = make_axes_locatable(ax4)

###ax5, uni-group
GAINS = np.load("./uni/si.npy")
GAIN1 = GAINS[3,:]
GAIN3 = GAINS[2,:]
GAIN5 = GAINS[1,:]
GAIN7 = GAINS[0,:]

img5 = ax5.imshow(GAINS, aspect='equal',interpolation='nearest',vmin=0.0,vmax=150.)
ax5.set_xticks((0,1,2,3,4,5))
ax5.set_xticklabels(("-1.2","-0.8","-0.4","0.4","0.8","1.2"))
ax5.set_yticks((3.5,3.0,2.5,2.0,1.5,1.0,0.5,0.0,-0.5))
ax5.set_yticklabels((" ","10%"," ","30%"," ","50%"," ","70%"," "))
ax5.set_xlabel(r'$\Delta V_m$ (mV)')

divider = make_axes_locatable(ax5)

###ax6, tri-group
Gains = np.load("./tri/si.npy")
Gain1 = Gains[3,:]
Gain2 = Gains[2,:]
Gain3 = Gains[1,:]
Gain4 = Gains[0,:]

img = ax6.imshow(Gains, aspect='equal',interpolation='nearest',vmin=0.0,vmax=150.)
ax6.set_xticks((0,1,2,3,4,5))
ax6.set_xticklabels(("-1.2","-0.8","-0.4","0.4","0.8","1.2"))
ax6.set_yticks((3,2,1,0))
ax6.set_yticklabels(("10%","20%","30%","40%"))

cax6 = fig.add_axes([0.94,0.437,0.005,0.176])
cbar = plt.colorbar(img,cax=cax6)
cbar.set_label(r'$\mathrm{I}_{G_1}$', rotation=0)
cbar.set_ticks((0.0,50,100.,150.))


###compare 1 and 2

###ax7
## comapare dual-group and uni-group
diff12 = gains - GAINS
img7 = ax7.imshow(diff12, aspect='equal',cmap='coolwarm',interpolation='nearest',vmin=-50,vmax=50)
ax7.set_title(r'$\mathrm{I}_\mathrm{bi}-\mathrm{I}_\mathrm{uni}$')
ax7.set_xticks((0,1,2,3,4,5))
ax7.set_xticklabels(("-1.2","-0.8","-0.4","0.4","0.8","1.2"))

ax7.set_yticks((3,2,1,0))
ax7.set_yticklabels(("10%","30%","50%","70%"))
ax7.set_ylabel("G1 ratio")
ax7.set_xlabel(r'$\Delta V_m$ (mV)')

##comapare tri-group and uni-group
GAINS_2 = np.vstack((GAIN3,GAIN1))
Gains_2 = np.vstack((Gain3,Gain1))
diff13 = Gains_2 - GAINS_2

ax8.set_title(r'$\mathrm{I}_\mathrm{tri}-\mathrm{I}_\mathrm{uni}$')
img8 = ax8.imshow(diff13, aspect='equal',cmap='coolwarm',interpolation='nearest',vmin=-50,vmax=50)
ax8.set_xticks((0,1,2,3,4,5))
ax8.set_xticklabels(("-1.2","-0.8","-0.4","0.4","0.8","1.2"))

ax8.set_yticks((1,0))
ax8.set_yticklabels(("10%","30%"))
ax8.set_xlabel(r'$\Delta V_m$ (mV)')

cax8 = fig.add_axes([0.364,0.085,0.262,0.005])
cbar = plt.colorbar(img8,cax=cax8,orientation='horizontal')
cbar.set_ticks((-50,-25.,0.0,25.,50.))


##ax9 background
data = np.load("./3expo/"+"si.npy")
img9 = ax9.imshow(data, aspect='equal',cmap='hot',interpolation='nearest',vmin=0.0,vmax=30)
ax9.set_xticks((0,1,2,3,4,5,6))
ax9.set_xticklabels(("-1.2","-0.8","-0.4","0.","0.4","0.8","1.2"))

ax9.set_yticks((6,5,4,3,2,1,0))
ax9.set_yticklabels(("-1.2","-0.8","-0.4","0.","0.4","0.8","1.2"))


ax9.plot([1.5,1.5],[6.5,5.5],'-',linewidth=3.,color='white')
ax9.plot([2.5,2.5],[6.5,5.5],'-',linewidth=3.,color='white')
ax9.plot([1.5,2.5],[5.5,5.5],'-',linewidth=3.,color='white')
ax9.plot([1.5,2.5],[6.5,6.5],'-',linewidth=3.,color='white')

ax9.plot([2.5,2.5],[4.5,5.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,3.5],[4.5,5.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,2.5],[5.5,5.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,2.5],[4.5,4.5],'-',linewidth=3.,color='white')

ax9.plot([4.5,4.5],[4.5,3.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,3.5],[4.5,3.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,4.5],[4.5,4.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,4.5],[3.5,3.5],'-',linewidth=3.,color='white')

ax9.plot([4.5,3.5],[0.5,0.5],'-',linewidth=3.,color='white')
ax9.plot([4.5,3.5],[-0.5,-0.5],'-',linewidth=3.,color='white')
ax9.plot([4.5,4.5],[-0.5,0.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,3.5],[-0.5,0.5],'-',linewidth=3.,color='white')

ax9.plot([2.5,2.5],[0.5,1.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,3.5],[0.5,1.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,2.5],[0.5,0.5],'-',linewidth=3.,color='white')
ax9.plot([3.5,2.5],[1.5,1.5],'-',linewidth=3.,color='white')

ax9.plot([1.5,1.5],[2.5,1.5],'-',linewidth=3.,color='white')
ax9.plot([2.5,2.5],[2.5,1.5],'-',linewidth=3.,color='white')
ax9.plot([1.5,2.5],[2.5,2.5],'-',linewidth=3.,color='white')
ax9.plot([1.5,2.5],[1.5,1.5],'-',linewidth=3.,color='white')

ax9.set_xlabel(r'G2 $\Delta V_m$ (mV)')
ax9.set_ylabel(r'G1 $\Delta V_m$ (mV)')

cax9 = fig.add_axes([0.94,0.05,0.005,0.2805])
cbar = plt.colorbar(img9,cax=cax9)
cbar.set_ticks((0.,10,20,30.))
cbar.set_label(r'$\mathrm{I}_{G_1}$', rotation=0)

plt.savefig("Fig4_canvas.svg")
plt.show()
