import pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import string
import matplotlib.image as img

plt.rcParams["axes.titlesize"]=18
plt.rcParams["axes.labelsize"]=18
plt.rcParams["lines.linewidth"]=2
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'custom'

c1 = '#958979' #on-off 2.5
c1_2 = '#77A09B'#on-off -2.5
c2 = '#E8CFA1' # half
c3 = '#252115' # alternative

fig = plt.figure(figsize=(15,10))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(left=0.05, right=0.35,top=0.95,bottom=0.1)
ax1 = plt.subplot(gs1[0,0])

gs2 = gridspec.GridSpec(2, 1)
gs2.update(left=0.46, right=0.98, hspace=0.05,top=0.95,bottom=0.1)
ax2 = plt.subplot(gs2[0,0])
ax3 = plt.subplot(gs2[1,0])


####ax1
ax1.axis("off") #leave space for illustration

####ax2
x1 = np.arange(1,11,1)*75.
x2 = np.arange(1,161,1)*7.5+750
x = np.hstack((x1,x2))

N = 3000
T = "./alternating_DC_exp/"
pone_g1g1_mean = np.load(T+"pone_"+str(N)+'g1g1_mean.npy')
pone_g1g1_std = np.load(T+"pone_"+str(N)+'g1g1_std.npy')
pone_gamma = np.load(T+"pone_/"+str(N)+'gamma.npy')

pozero_g1g1_mean = np.load(T+"pozero_"+str(N)+'g1g1_mean.npy')
pozero_g1g1_std = np.load(T+"pozero_"+str(N)+'g1g1_std.npy')
pozero_gamma = np.load(T+"pozero_"+str(N)+'gamma.npy')

nepo_g1g1_mean = np.load(T+"nepo_"+str(N)+'g1g1_mean.npy')
nepo_g1g1_std = np.load(T+"nepo_"+str(N)+'g1g1_std.npy')
nepo_gamma = np.load(T+"nepo_"+str(N)+'gamma.npy')

nezero_g1g1_mean = np.load(T+"ne_zero_"+str(N)+'g1g1_mean.npy')
nezero_g1g1_std = np.load(T+"ne_zero_"+str(N)+'g1g1_std.npy')
nezero_gamma = np.load(T+"ne_zero_"+str(N)+'gamma.npy')

halfPN_g1g1_mean = np.load(T+"half_PN_"+str(N)+'g1g1_mean.npy')
halfPN_g1g1_std = np.load(T+"half_PN_"+str(N)+'g1g1_std.npy')
halfPN_gamma = np.load(T+"half_PN_"+str(N)+'gamma.npy')

halfNP_g1g1_mean = np.load(T+"half_NP_"+str(N)+'g1g1_mean.npy')
halfNP_g1g1_std = np.load(T+"half_NP_"+str(N)+'g1g1_std.npy')
halfNP_gamma = np.load(T+"half_NP_"+str(N)+'gamma.npy')


ax2.plot(x,pone_g1g1_mean,'o-',color=c3,markerfacecolor=c3,markeredgecolor='none',label=r'$\mathrm{alternative 1}$')
ax2.fill_between(x,pone_g1g1_mean-pone_g1g1_std,pone_g1g1_mean+pone_g1g1_std,color=c3,alpha=0.2)
ax2.plot(x,halfPN_g1g1_mean,'o-',color=c2,markerfacecolor=c2,markeredgecolor='none',label=r'$\mathrm{alternative 2}$')
ax2.fill_between(x,halfPN_g1g1_mean-halfPN_g1g1_std,halfPN_g1g1_mean+halfPN_g1g1_std,color=c2,alpha=0.2)
ax2.plot(x,pozero_g1g1_mean,'o-',color=c1_2,markerfacecolor=c1_2,markeredgecolor='none',label=r'$\mathrm{2.5pA}$')
ax2.fill_between(x,pozero_g1g1_mean-pozero_g1g1_std,pozero_g1g1_mean+pozero_g1g1_std,color=c1_2,alpha=0.2)

ax2.axhline(pone_g1g1_mean[9], linestyle='--',color='k')
ax2.set_xlim(600,2000)
ax2.set_ylim(0.0875,0.0935)
ax2.set_yticks((0.088,0.090,0.092))
ax2.set_xticks(([]))
ax2.axvspan(750,900,alpha=0.1,color='grey')
ax2.axvspan(1050,1200,alpha=0.1,color='grey')
ax2.axvspan(1350,1500,alpha=0.1,color='grey')
ax2.set_ylabel(r'$\Gamma$')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')



####ax3
ax3.hist(nepo_gamma,histtype='step',linewidth=3.,color=c3)
ax3.hist(nezero_gamma,histtype='step',linewidth=3.,color=c1_2)
ax3.hist(halfNP_gamma,histtype='step',linewidth=3.,color=c2)
ax3.set_xticks((0.09,0.0904,0.0908,0.0912))
ax3.set_ylim(0,10)
ax3.set_xlabel(r'$\Gamma$')
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')

###ax4
ax4 = fig.add_axes([0.68,0.25,0.15,0.2])
ax4.bar(x=[3],height=[np.mean(nepo_gamma)],yerr=np.std(pone_gamma),color=c3,width=0.5,edgecolor='none',ecolor='k',capsize=3.)
ax4.bar(x=[2],height=[np.mean(halfNP_gamma)],yerr=np.std(halfPN_gamma),color=c2,width=0.5,edgecolor='none',ecolor='k',capsize=3.)
ax4.bar(x=[1],height=[np.mean(nezero_gamma)],yerr=np.std(pozero_gamma),color=c1_2,width=0.5,edgecolor='none',ecolor='k',capsize=3.)
ax4.set_xticks((3,2,1))
labels=["","",""]
ax4.set_xticklabels(labels,rotation=30.)
ax4.set_yticks((0.09,0.091,0.092))
ax4.set_ylim(0.09,0.092)
ax4.set_ylabel(r'$\Gamma$')
ax4.spines['right'].set_color('none')
ax4.spines['top'].set_color('none')


plt.savefig("Fig6_canvas.svg")

plt.show()
