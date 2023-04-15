import numpy as np
import parameters
from parameters import *

for seed in np.arange(0,10,1):
    g = []
    rate = []
    for k in np.arange(1*growth_step,11*growth_step,growth_step):
        wm = np.load("weight_matrix"+str(k)+"_seed_"+str(seed)+".npy")
        g.append(np.mean(wm))

        rates = np.load("raw_all_rates_"+str(k)+'_seed_'+str(seed)+".npy")
        rate.append(np.mean(rates))

    np.save(str(N)+"connectivity_seed_"+str(seed),g)
    np.save(str(N)+'rates'+'_seed_'+str(seed),rate)

    print seed



