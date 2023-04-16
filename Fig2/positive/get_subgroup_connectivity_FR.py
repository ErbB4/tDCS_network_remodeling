import numpy as np
import parameters
reload (parameters)
from parameters import *

for seed in np.arange(0,30,1):
    g1g1 = []
    g1g2 = []
    g2g1 = []
    g2g2 = []

    rate1 = []
    rate2 = []

    for k in np.arange(1*growth_step,11*growth_step,growth_step):
        wm = np.load("weight_matrix"+str(k)+"_seed_"+str(seed)+".npy")
        g1g1.append(np.mean(wm[0:N,0:N]))
        g1g2.append(np.mean(wm[0:N,N::]))
        g2g1.append(np.mean(wm[N::,0:N]))
        g2g2.append(np.mean(wm[N::,N::]))

        rates = np.load("raw_all_rates_"+str(k)+'_seed_'+str(seed)+".npy")
        rate1.append(np.mean(rates[0:N]))
        rate2.append(np.mean(rates[N::]))

    for k in np.arange(1*stimulate_step+growth_time,61*stimulate_step+growth_time,stimulate_step):
        wm = np.load("weight_matrix"+str(k)+"_seed_"+str(seed)+".npy")
        g1g1.append(np.mean(wm[0:N,0:N]))
        g1g2.append(np.mean(wm[0:N,N::]))
        g2g1.append(np.mean(wm[N::,0:N]))
        g2g2.append(np.mean(wm[N::,N::]))
        rates = np.load("raw_all_rates_"+str(k)+'_seed_'+str(seed)+".npy")
        rate1.append(np.mean(rates[0:N]))
        rate2.append(np.mean(rates[N::]))

    np.save(str(N)+"g1g1_seed_"+str(seed),g1g1)
    np.save(str(N)+"g1g2_seed_"+str(seed),g1g2)
    np.save(str(N)+"g2g1_seed_"+str(seed),g2g1)
    np.save(str(N)+"g2g2_seed_"+str(seed),g2g2)

    np.save(str(N)+'rates1'+'_seed_'+str(seed),rate1)
    np.save(str(N)+'rates2'+'_seed_'+str(seed),rate2)




