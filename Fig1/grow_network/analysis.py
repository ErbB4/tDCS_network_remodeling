import numpy as np
import pylab as pl

from parameters import *


def analysis(senders,times,starttime,simtime=5000.):
    binsize = 10.
    bins = int(simtime/binsize)
    firing_matrix = np.zeros([NE,bins])
    rates = []

    for i in np.arange(0,NE,1):
        idx = np.where(senders==i+1)
        time = times[idx]
        firing_matrix[i,:] = np.histogram(time,bins,(starttime,starttime+simtime))[0]

        rate = len(time)/(simtime/1000.)
        rates.append(rate)

    ccs = np.corrcoef(firing_matrix)
    np.fill_diagonal(ccs,0)

    return rates,ccs

T = 'grow' #your path

#analysis of growth stage
seed = int(sys.argv[1])
step_size = growth_step

for k in np.arange(1,11,1):
    connection_matrix = np.zeros((NE,NE))
    step = k*step_size
    starttime = step-5000.
            
    senders = np.load(T+"/senders_"+str(step)+'_seed_'+str(seed)+".npy")
    times   = np.load(T+"/times_"  +str(step)+'_seed_'+str(seed)+".npy")
    sources = np.load(T+"/sources_"+str(step)+'_seed_'+str(seed)+".npy")
    targets = np.load(T+"/targets_"+str(step)+'_seed_'+str(seed)+".npy")
    weights = np.load(T+"/weights_"+str(step)+'_seed_'+str(seed)+".npy")

    sourceIDs = np.unique(sources)
    for sourceID in sourceIDs:
        share_source = targets[np.where(sources==sourceID)]
        targetIDs = np.unique(share_source)
        for targetID in targetIDs:
            same_target = share_source[np.where(share_source==targetID)]
            connection_matrix[sourceID-1,targetID-1] = 0.1*len(same_target)
    rates,ccs = analysis(senders,times,starttime)  
    np.save(T+"/raw_all_rates_"+str(step)+'_seed_'+str(seed),rates)
    np.save(T+"/weight_matrix"+str(step)+'_seed_'+str(seed),connection_matrix)


