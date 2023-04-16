import pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.image as img
from mpl_toolkits.axes_grid1 import make_axes_locatable
import string

plt.rcParams["axes.titlesize"]=18
plt.rcParams["axes.labelsize"]=18
plt.rcParams["lines.linewidth"]=2
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'custom'

color1 =  '#5599FF' #blue
color2 = '#4D4D4D' #dark grey
color3 = '#999999' #light grey#

fig = plt.figure(figsize=(15,13))

gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.95, bottom=0.7, left=0.08,right=0.98,wspace=0.1)
ax1 = fig.add_subplot(gs1[0,0])
ax2 = fig.add_subplot(gs1[0,1:3])

gs2 = gridspec.GridSpec(1, 2)
gs2.update(top=0.65, bottom=0.05, left=0.08,right=0.98,wspace=0.1)
gs20 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs2[0,0])
gs21 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs2[0,1])

ax3 = plt.subplot(gs20[0,0])
ax4 = plt.subplot(gs20[1,0])
ax5 = plt.subplot(gs21[0,0])
ax6 = plt.subplot(gs21[1,0])

###ax1
ax1.axis("off") #leave space for illustration
ax2.axis("off") #leave space for illustration

###ax3 and ax4
x1 = np.arange(1,11,1)*75.
x2 = np.arange(1,21,1)*7.5+750
x3 = np.arange(1,41,1)*7.5+750+75.*2.
x = np.hstack((x1,x2,x3))

N = 1000

T = "./positive/data/"
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

ax3.plot(x,rates1_mean,'o-',markerfacecolor=color1,markeredgecolor='none',color=color1,label=r'$\mathrm{sti}$')
ax3.plot(x,rates2_mean,'o-',markerfacecolor=color2,markeredgecolor='none',color=color2,label=r'$\mathrm{background}$')

ax3.axvspan(750,900,alpha=0.1,color='grey')
ax3.fill_between(x,rates1_mean-rates1_std,rates1_mean+rates1_std,color=color1,alpha=0.2)
ax3.fill_between(x,rates2_mean-rates2_std,rates2_mean+rates2_std,color=color2,alpha=0.2)
ax3.set_xlim(590,1280)
ax3.set_ylim(7.5,8.5)
ax3.axes.get_xaxis().set_visible(False)
ax3.set_yticks((7.6,8.,8.4))

ax3.set_ylabel('Firing rate (Hz)',fontsize=20.)
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')

ax4.plot(x,g1g1_mean,'o-',markerfacecolor=color1,color=color1,markeredgecolor='none',label=r'$\mathrm{sti} \rightarrow  \mathrm{sti}$')
ax4.plot(x,g2g1_mean,'s-',markerfacecolor=color3,color=color3,markeredgecolor='none',label=r'$\mathrm{bg} \leftrightarrow  \mathrm{sti}$')
ax4.plot(x,g2g2_mean,'o-',markerfacecolor=color2,color=color2,markeredgecolor='none',label=r'$\mathrm{bg} \rightarrow  \mathrm{bg}$')

ax4.fill_between(x,g1g1_mean-g1g1_std,g1g1_mean+g1g1_std,color=color1,alpha=0.2)
ax4.fill_between(x,g2g2_mean-g2g2_std,g2g2_mean+g2g2_std,color=color2,alpha=0.2)
ax4.fill_between(x,g2g1_mean-g2g1_std,g2g1_mean+g2g1_std,color=color3,alpha=0.2)
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')

ax4.axvspan(750,900,alpha=0.1,color='grey')
ax4.set_xlim(590,1280)
ax4.set_xticks((600,750,900,1050,1200))
ax4.set_yticks((0.088,0.090,0.092))
ax4.set_ylim(0.087,0.0926)
ax4.set_xlabel('Time (s)',fontsize=15.)
ax4.set_ylabel('Connectivity '+r'$\Gamma$',fontsize=20.)


###ax5 and ax6
N = 1000
T = "./negative/data/"
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

ax5.plot(x,rates1_mean,'o-',markerfacecolor=color1,color=color1,markeredgecolor='none',markersize=5.,label=r'$\mathrm{sti}$')
ax5.plot(x,rates2_mean,'o-',markerfacecolor=color2,color=color2,markeredgecolor='none',markersize=5.,label=r'$\mathrm{background}$')

ax5.axvspan(750,900,alpha=0.1,color='grey')
ax5.fill_between(x,rates1_mean-rates1_std,rates1_mean+rates1_std,color=color1,alpha=0.2)
ax5.fill_between(x,rates2_mean-rates2_std,rates2_mean+rates2_std,color=color2,alpha=0.2)
ax5.set_xlim(590,1280)
ax5.set_ylim(7.5,8.5)
ax5.axes.get_xaxis().set_visible(False)
ax5.set_yticks((7.6,8.,8.4))
ax5.legend(fancybox=True, loc='best')
ax5.spines['right'].set_color('none')
ax5.spines['top'].set_color('none')

ax6.plot(x,g1g1_mean,'o-',markeredgecolor='none',markerfacecolor=color1,color=color1,markersize=5.,label=r'$\mathrm{sti} \rightarrow  \mathrm{sti}$')
ax6.plot(x,g2g1_mean,'s-',markeredgecolor='none',markerfacecolor=color3,color=color3,markersize=5.,label=r'$\mathrm{bg} \leftrightarrow  \mathrm{sti}$')
ax6.plot(x,g2g2_mean,'o-',markerfacecolor=color2,color=color2,markeredgecolor='none',markersize=5.,label=r'$\mathrm{bg} \rightarrow  \mathrm{bg}$')

ax6.fill_between(x,g1g1_mean-g1g1_std,g1g1_mean+g1g1_std,color=color1,alpha=0.2)
ax6.fill_between(x,g2g2_mean-g2g2_std,g2g2_mean+g2g2_std,color=color2,alpha=0.2)
ax6.fill_between(x,g2g1_mean-g2g1_std,g2g1_mean+g2g1_std,color=color3,alpha=0.2)
ax6.spines['right'].set_color('none')
ax6.spines['top'].set_color('none')

ax6.axvspan(750,900,alpha=0.1,color='grey')
ax6.set_xlim(590,1280)
ax6.set_xticks((600,750,900,1050,1200))
ax6.set_yticks((0.088,0.090,0.092))
ax6.set_ylim(0.087,0.0926)
ax6.set_xlabel('Time (s)',fontsize=15.)

ax6.legend(fancybox=True, loc='lower right')
plt.savefig("Fig2_canvas.svg")

plt.show()
