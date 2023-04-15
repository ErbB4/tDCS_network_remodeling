import numpy as np
from scipy.optimize import leastsq

import params
from params import *

angles = np.arange(0.,2.*np.pi+1/96.*np.pi,1/96.*np.pi)
for i in np.arange(0,48,1):
    rates = []
    for ang in angles:
        extension = 'angle_'+str(ang)+'_current_'+str(i)+".npy"
        times = np.load("times_"+extension)
        
        rate = len(times)/(simtime/1000.)
        rates.append(rate)
        os.remove("times_"+extension)
        os.remove("senders_"+extension)

    rates = np.array(rates)
    np.save("rates_current_"+str(i)+".npy",rates)
  


