import pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.image as img
from mpl_toolkits.axes_grid1 import make_axes_locatable
import string

color1 =  '#5599FF' #blue
color2 = '#4D4D4D' #dark grey
color3 = '#999999' #light grey
color4 =  '#FFE680' #yellow

plt.rcParams["axes.titlesize"]=18
plt.rcParams["axes.labelsize"]=18
plt.rcParams["lines.linewidth"]=2
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'custom'

fig = plt.figure(figsize=(15,13))

gs1 = gridspec.GridSpec(3, 1)
gs1.update(top=0.95,bottom=0.05,left=0.08, right=0.48)
ax1 = fig.add_subplot(gs1[0,0])
ax2 = fig.add_subplot(gs1[1,0])
ax3 = fig.add_subplot(gs1[2,0])

gs2 = gridspec.GridSpec(3, 1)
gs2.update(top=0.95,bottom=0.05,left=0.53, right=0.93)
ax4 = plt.subplot(gs2[0,0])
ax5 = plt.subplot(gs2[1,0])
ax6 = plt.subplot(gs2[2,0])

###ax1
ax1.axis("off") #leave some space for illustration

###ax2 and ax3
x1 = np.arange(1,11,1)*75.
x2 = np.arange(1,21,1)*7.5+750
x3 = np.arange(1,41,1)*7.5+750+75.*2.
x = np.hstack((x1,x2,x3))

N=3000
T = "./2pop/data/"
g1g1_mean = np.load(T+str(N)+'g1g1_mean.npy')
g1g2_mean = np.load(T+str(N)+'g1g2_mean.npy')
g2g1_mean = np.load(T+str(N)+'g2g1_mean.npy')
g2g2_mean = np.load(T+str(N)+'g2g2_mean.npy')

g1g1_std = np.load(T+str(N)+'g1g1_std.npy')
g1g2_std = np.load(T+str(N)+'g1g2_std.npy')
g2g2_std = np.load(T+str(N)+'g2g2_std.npy')

rates1_mean = np.load(T+str(N)+'rates1_mean.npy')
rates2_mean = np.load(T+str(N)+'rates2_mean.npy')


rates1_std = np.load(T+str(N)+'rates1_std.npy')
rates2_std = np.load(T+str(N)+'rates2_std.npy')


ax2.plot(x,rates1_mean,'o-',color = color1,markerfacecolor=color1,markeredgecolor='none',label=r'$\mathrm{G1}$')
ax2.plot(x,rates2_mean,'o-',color=color4,markerfacecolor=color4,markeredgecolor='none',label=r'$\mathrm{G2}$')

ax2.fill_between(x,rates1_mean-rates1_std,rates1_mean+rates1_std,color=color1,alpha=0.2)
ax2.fill_between(x,rates2_mean-rates2_std,rates2_mean+rates2_std,color=color4,alpha=0.2)

ax2.axvspan(750,900,alpha=0.1,color='grey')

ax2.set_xlim(590,1300)
ax2.set_ylim(7.5,8.7)
ax2.axes.get_xaxis().set_visible(False)
ax2.set_yticks((7.6,8.0,8.4))

ax2.set_ylabel('Firing rate (Hz)')
ax2.legend(loc='best')

ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')

ax3.plot(x,g1g1_mean,'o-',color=color1,markerfacecolor=color1,markeredgecolor='none',label=r'$\mathrm{G1} \rightarrow  \mathrm{G1}$')
ax3.plot(x,g2g2_mean,'o-',color=color4,markerfacecolor=color4,markeredgecolor='none',label=r'$\mathrm{G2} \rightarrow  \mathrm{G2}$')

ax3.fill_between(x,g1g1_mean-g1g1_std,g1g1_mean+g1g1_std,color=color1,alpha=0.2)
ax3.fill_between(x,g2g2_mean-g2g2_std,g2g2_mean+g2g2_std,color=color4,alpha=0.2)


ax3.axvspan(750,900,alpha=0.1,color='grey')
ax3.set_xlim(590,1300)
ax3.set_xticks((600,750,900,1050,1200))
ax3.set_yticks((0.086,0.088,0.090,0.092))
ax3.set_xlabel("Time(s)")
ax3.set_ylim(0.086,0.092)

ax3.set_ylabel('Connectivity '+r'$\Gamma$')
ax3.legend(loc='lower left')

ax3.axhline(g1g1_mean[9], linestyle='--',color='k')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')

####ax4
ax4.axis("off") #leave some space for illustration

####ax5 and ax6
x1 = np.arange(1,11,1)*75.
x2 = np.arange(1,21,1)*7.5+750
x3 = np.arange(1,41,1)*7.5+750+75.*2.
x = np.hstack((x1,x2,x3))

N=3000

T = "./3pop/data/"

g1g1_mean = np.load(T+str(N)+'g1g1_mean.npy')
g2g2_mean = np.load(T+str(N)+'g2g2_mean.npy')
g3g3_mean = np.load(T+str(N)+'g3g3_mean.npy')

g1g1_std = np.load(T+str(N)+'g1g1_std.npy')
g2g2_std = np.load(T+str(N)+'g2g2_std.npy')
g3g3_std = np.load(T+str(N)+'g3g3_std.npy')



rates1_mean = np.load(T+str(N)+'rates1_mean.npy')
rates2_mean = np.load(T+str(N)+'rates2_mean.npy')
rates3_mean = np.load(T+str(N)+'rates3_mean.npy')



rates1_std = np.load(T+str(N)+'rates1_std.npy')
rates2_std = np.load(T+str(N)+'rates2_std.npy')
rates3_std = np.load(T+str(N)+'rates3_std.npy')


ax5.plot(x,rates1_mean,'o-',color=color1,markerfacecolor=color1,markeredgecolor='none',label=r'$\mathrm{G1}$')
ax5.plot(x,rates2_mean,'o-',color=color4,markerfacecolor=color4,markeredgecolor='none',label=r'$\mathrm{G2}$')
ax5.plot(x,rates3_mean,'o-',color=color2,markerfacecolor=color2,markeredgecolor='none',label=r'$\mathrm{bg}$')

ax5.fill_between(x,rates1_mean-rates1_std,rates1_mean+rates1_std,color=color1,alpha=0.2)
ax5.fill_between(x,rates2_mean-rates2_std,rates2_mean+rates2_std,color=color4,alpha=0.2)
ax5.fill_between(x,rates3_mean-rates3_std,rates3_mean+rates3_std,color=color2,alpha=0.2)

ax5.axvspan(750,900,alpha=0.1,color='grey')

ax5.set_xlim(590,1300)
ax5.set_ylim(7.5,8.7)
ax5.axes.get_xaxis().set_visible(False)
ax5.set_yticks((7.6,8.0,8.4))
ax5.spines['right'].set_color('none')
ax5.spines['top'].set_color('none')

ax5.legend(loc='best')

ax6.plot(x,g1g1_mean,'o-',color=color1,markerfacecolor=color1,markeredgecolor='none',label=r'$\mathrm{G1} \rightarrow  \mathrm{G1}$')
ax6.plot(x,g2g2_mean,'o-',color=color4,markerfacecolor=color4,markeredgecolor='none',label=r'$\mathrm{G2} \rightarrow  \mathrm{G2}$')
ax6.plot(x,g3g3_mean,'o-',color=color2,markerfacecolor=color2,markeredgecolor='none',label=r'$\mathrm{bg} \rightarrow  \mathrm{bg}$')

ax6.fill_between(x,g1g1_mean-g1g1_std,g1g1_mean+g1g1_std,color=color1,alpha=0.2)
ax6.fill_between(x,g2g2_mean-g2g2_std,g2g2_mean+g2g2_std,color=color4,alpha=0.2)
ax6.fill_between(x,g3g3_mean-g3g3_std,g3g3_mean+g3g3_std,color=color2,alpha=0.2)

ax6.axvspan(750,900,alpha=0.1,color='grey')
ax6.set_xlim(590,1300)
ax6.set_xticks((600,750,900,1050,1200))
ax6.set_yticks((0.087,0.089,0.091,0.093))
ax6.set_xlabel("Time(s)")
ax6.set_ylim(0.087,0.093)
ax6.spines['right'].set_color('none')
ax6.spines['top'].set_color('none')

ax6.legend(loc='lower right')

plt.savefig("Fig3_canvas.svg")
plt.show()
