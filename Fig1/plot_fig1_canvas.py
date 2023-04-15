import pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.image as img
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.optimize import leastsq
from params import *
import string
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.ticker as tck
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage

# define plotting parameters
plt.rcParams["axes.titlesize"]=18
plt.rcParams["axes.labelsize"]=18
plt.rcParams["lines.linewidth"]=2
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

c1 = '#162947'
c2 = '#c79000'
c3 = [153./255.,153./255.,153./255.]

fig = plt.figure(figsize=(15,13))

gs1 = gridspec.GridSpec(1, 8)
gs1.update(top=.95,bottom=0.7,left=0.05,right=0.95,wspace=0.07)
ax1 = fig.add_subplot(gs1[0,0:3])
ax3 = fig.add_subplot(gs1[0,3:5])
ax2 = fig.add_subplot(gs1[0,6:8])

gs2 = gridspec.GridSpec(2, 3)
gs2.update(top=0.65,bottom=0.05,left=0.05,right=0.95,hspace=0.07,wspace=0.07)
ax3_hold = plt.subplot(gs2[0,0])
ax4 = plt.subplot(gs2[0,1:3])
ax5 = plt.subplot(gs2[1,0:2])
ax6 = plt.subplot(gs2[1,2])


###ax1

ax1.axis("off") # leave the space for illustration

###ax2 and ax7

angles = np.arange(0.,2.*np.pi+1/96.*np.pi,1/96.*np.pi)
currents = np.arange(0.,30.,0.625)
mem_V = np.arange(0.,30.,0.625)*R*10**(-9)
rates_matrix = np.load("./single_neuron/rates_matrix.npy")

Z = rates_matrix[:,:-1]
Z2 = ndimage.gaussian_filter(Z, sigma=2.0, order=0)

image2 = ax2.pcolor(angles[0:-1],mem_V,rates_matrix[:,:-1],vmin=0.,vmax=25.,cmap=cm.summer)
image3 = ax2.contour(angles[0:-1],mem_V,Z2,vmin=7.,vmax=9.,levels=np.array([7,8,9]),cmap=cm.Oranges)
labels = [r'$0$',r'$\frac{1}{2}\pi$',r'$\pi$',r'$\frac{3}{2}\pi$',r'$2\pi$']
ax2.set_xticks(np.arange(0, 2.*np.pi+1/8.*np.pi,1/2.*np.pi))
ax2.set_xticklabels(labels)
ax2.set_xlabel(r'$\theta$')
ax2.set_ylabel(r'$\mathrm{max. }\Delta V_m \ \mathrm{(mV)}$')
cax2 = fig.add_axes([0.953,0.7,0.003,0.25])
cbar2 = plt.colorbar(image2,cax=cax2,orientation='vertical')
cbar2.set_ticks((0,5,10,15,20,25))
cbar2.set_label('Firing rate (Hz)', rotation=90)
ax2.axhline(y=0.1,linestyle='--',color='k',alpha=0.2)
ax2.axhline(y=0.5,linestyle='--',color='k',alpha=0.5)
ax2.axhline(y=1.0,linestyle='--',color='k',alpha=1.)

###ax3
ax3.plot(angles[:-1],rates_matrix[4,:-1],'k-',alpha=0.2,label='0.1mV') # pick 0.1mV value
ax3.plot(angles[:-1],rates_matrix[20,:-1],'k-',alpha=0.5,label='0.5mV') # pick 0.5mV value
ax3.plot(angles[:-1],rates_matrix[40,:-1],'k-',alpha=1.,label='1.mV') # pick 1.0mV value

ax3.spines['left'].set_position('center')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data',7.85))
ax3.spines['left'].set_smart_bounds(True)
ax3.spines['bottom'].set_smart_bounds(True)

labels = [r'$0$',' ',' ',' ',r'$2\pi$']
ax3.set_xticks(np.arange(0, 2.*np.pi+1/8.*np.pi,1/2.*np.pi))
ax3.set_xticklabels(labels)
ax3.text(6.6,9,'0.1mV',color='k',alpha=0.2)
ax3.text(6.6,14,'0.5mV',color='k',alpha=0.5)
ax3.text(6.6,20,'1.0mV',color='k',alpha=1.)
ax3.plot(1.57,7.9,'o',color='r',alpha=0.9)
ax3.plot(4.7,7.9,'o',color='r',alpha=0.9)
ax3.text(4.5,3,r'$8\mathrm{Hz, }\Delta V_m = 0 \mathrm{mV}$',color='r',alpha=0.9)
ax3.set_yticks((5,10,15,20))
ax3.set_title("Firing rate (Hz)")

#ax4
ax3_hold.axis("off")
ax4.axis("off") # leave the space for illustration

### ax5 
ax5.axis("off") # leave the space for illustration

### ax6 and ax7
g = np.load("./grow_network/"+"connectivity_seed_0.npy")*10.
rate = np.load("./grow_network/"+"rates_seed_0.npy")
x = np.arange(0,11,1)*75.

ax6.plot(x,np.hstack((0,rate)),'o--',color=c1,markerfacecolor=c1,markeredgecolor='none')
ax6.set_xlabel("Time (s)")
ax6.set_ylabel("Firing rate (Hz)",color=c1)
ax6.set_ylim(0.,10.)
ax6.set_xlim(0.,770.)
ax6.set_yticks((0.,2.,4.,6.,8.,10.))
ax7 = ax6.twinx()
ax7.plot(x,np.hstack((0,g)),'s-',color=c2,markerfacecolor=c2,markeredgecolor='none')
ax7.set_ylabel("Connectivity "+r'$\Gamma$',color=c2)
ax7.set_ylim(0.,0.1)
ax7.set_xlim(0.,770.)

plt.savefig("fig1_canvas.svg")
plt.show()
