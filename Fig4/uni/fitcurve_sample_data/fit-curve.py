import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# recorded time points 
x1 = np.arange(1,11,1)*75.
x2 = np.arange(1,61,1)*7.5+750
x3 = np.arange(1,75,1)*75.+750+60*7.5

x_all = np.hstack((x1,x2,x3))


#only stat to fit the curve after the stimulation is terminated
x = x_all[30::]
x = x-x[0]
x_fit =np.linspace(0,x[-1],1000)


#define the fitting function

def func(x,a,b,c,d,e,f):
    return a*np.exp(-b*x)+c*np.exp(-d*x)+e*np.exp(-f*x)




i = 0 # I used one trial as an example here
g1g1_mean = np.load("1000g1g1_seed_"+str(i)+".npy") #load connectivity of the cell assembly


g = g1g1_mean[30::] #get the connectivity after the stimulation is turned off

length = len(g-g1g1_mean[9])

        
popt_stimulation,pcov = curve_fit(func,x[0:length],g-g1g1_mean[9],p0=(.1,1e-2,0.1,1e-3,0.0001,1e-1)) #p0 are the initial guess, you can input different values here for different fitting; and when we fit, we put the starting point to [0,0] to avoid fitting the constant.

amp1 = popt_stimulation[0]
tau1 = 1./popt_stimulation[1]
amp2 = popt_stimulation[2]
tau2 = 1./popt_stimulation[3]
amp3 = popt_stimulation[4]
tau3 = 1./popt_stimulation[5]

y_fit=func(x_fit,popt_stimulation[0],popt_stimulation[1],popt_stimulation[2],popt_stimulation[3],popt_stimulation[4],popt_stimulation[5])

plt.plot(x_all[0:length+30],g1g1_mean,'o',label='raw data')
plt.text(4000,0.15,r'$\tau_{1} = %0.f s$' %tau1)
plt.text(4000,0.145,r'$\mathrm{A}_1 = %0.7f$' %amp1)
plt.text(4000,0.14,r'$\tau_{2} = %0.f s$' %tau2)
plt.text(4000,0.135,r'$\mathrm{A}_2 = %0.7f$' %amp2)
plt.text(4000,0.13,r'$\tau_{3} = %0.f s$' %tau3)
plt.text(4000,0.125,r'$\mathrm{A}_3 = %0.7f$' %amp3)
    
plt.plot(x_fit+900,y_fit+g1g1_mean[9],label='fitted')
plt.legend()
    
plt.ylabel("G1 connectivity")
plt.axvspan(750,900,color='grey',alpha=0.3)
plt.ylim(0.08,0.16)


plt.show()

