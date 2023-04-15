import nest
import numpy as np
import params
reload (params)
from params import *
import sys

seed        = 0
grng_seed   = seed
numpy_seed  = seed+1000
np.random.seed(numpy_seed)
currents = np.arange(0.,30.,0.625)

for i in np.arange(0,48,1):
    nest.ResetKernel()
    nest.SetKernelStatus({"resolution":dt,"print_time":True,"overwrite_files":True})

    nest.SetDefaults("iaf_psc_delta",neuron_params)
    nest.SetDefaults("poisson_generator",{"rate": p_rate})

    neuron = nest.Create("iaf_psc_delta",1)
    noise = nest.Create("poisson_generator",1)
    spikes = nest.Create("spike_detector",1)

    nest.SetStatus(spikes,{"label":"spikes",
                            "withtime":True,
                            "withgid":True,
                            "to_file":False })

    nest.CopyModel("static_synapse","excitatory",{"weight":J,"delay":delay})
                            
    nest.Connect(noise,neuron,syn_spec="excitatory")
    nest.Connect(neuron,spikes,syn_spec="excitatory")

    for ang in np.arange(0,2.*np.pi+1/96.*np.pi,1/96.*np.pi):
        projection = np.cos(ang)*currents[i]
        nest.SetStatus(neuron,{"I_e":projection})
        nest.Simulate(simtime)
        events = nest.GetStatus(spikes,'events')[0]
        times = events['times']
        senders = events['senders']
        extension = 'angle_'+str(ang)+'_current_'+str(i)+".npy"

        np.save("times_"+extension,times)
        np.save("senders_"+extension,senders)
        
        nest.SetStatus(spikes,'n_events',0)
