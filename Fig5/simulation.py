import numpy as np
from parameters import *
import sys
import nest
import pylab as pl

i = int(sys.argv[1])
rank = nest.Rank() 
np.save(T+str(i)+"/data/started.npy",np.arange(i))

seed        = i*6748+7928
grng_seed   = seed
rng_seeds   = range(seed+1,seed+total_num_virtual_procs+1)

nest.ResetKernel()
nest.EnableStructuralPlasticity()
nest.SetKernelStatus({"resolution": dt, "print_time": False})
nest.SetKernelStatus({
    'structural_plasticity_update_interval' : int(MSP_update_interval/dt),
    'grng_seed'                             : grng_seed,
    'rng_seeds'                             : rng_seeds,
    'total_num_virtual_procs'               : total_num_virtual_procs})

nest.SetDefaults(neuron_model, neuron_params)

# Create generic neuron with Axon and Dendrite
nest.CopyModel(neuron_model, 'excitatory')
nest.CopyModel(neuron_model, 'inhibitory')

# growth curves
gc_den = {'growth_curve': growth_curve_d, 'z': z0_mean, 'growth_rate': slope*target_rate, 'eps': target_rate, 'continuous': False}
gc_axon = {'growth_curve': growth_curve_a, 'z': z0_mean, 'growth_rate': slope*target_rate, 'eps': target_rate, 'continuous': False}

nest.SetDefaults('excitatory', 'synaptic_elements', {'Axon_exc': gc_axon, 'Den_exc': gc_den})

# Create synapse models
nest.CopyModel(synapse_model, 'msp_excitatory', {"weight":weight, "delay":max_delay})

# Use SetKernelStatus to activate the synapse model
nest.SetKernelStatus({
    'structural_plasticity_synapses': {
        'syn1': {
            'model': 'msp_excitatory',
            'post_synaptic_element': 'Den_exc',
            'pre_synaptic_element': 'Axon_exc',
        }
    },
    'autapses': False,
})


# build network
pop_exc = nest.Create('excitatory', NE)
pop_inh = nest.Create('inhibitory', NI)

aux = 0
for neuron in pop_exc:
    gc_den = {'growth_curve': growth_curve_d,
              'z': z0_mean,
              'growth_rate':  slope*target_rate,
              'eps': target_rate,
              'continuous': False}
    gc_axon = {'growth_curve': growth_curve_a,
              'z': z0_mean,
              'growth_rate':  slope*target_rate,
              'eps': target_rate,
              'continuous': False}
              
    nest.SetStatus([neuron], 'synaptic_elements', {'Axon_exc': gc_axon, 'Den_exc': gc_den})
    aux += 1

nest.CopyModel("static_synapse","device",{"weight":weight, "delay":max_delay})

poisson_generator_inh = nest.Create('poisson_generator')
nest.SetStatus(poisson_generator_inh, {"rate": rate})
nest.Connect(poisson_generator_inh, pop_inh,'all_to_all',model="device")

poisson_generator_ex = nest.Create('poisson_generator')
nest.SetStatus(poisson_generator_ex, {"rate": rate})

nest.Connect(poisson_generator_ex, pop_exc,'all_to_all', model="device")

spike_detector = nest.Create("spike_detector")
nest.SetStatus(spike_detector,{
                                "withtime"  : True,
                                "withgid"   : True,
                                })


nest.Connect(pop_exc+pop_inh, spike_detector,'all_to_all',model="device")

nest.CopyModel("static_synapse","inhibitory_synapse",{"weight":-g*weight, "delay":max_delay})
nest.Connect(pop_inh,pop_exc+pop_inh,{'rule': 'fixed_indegree','indegree': CI},'inhibitory_synapse')

nest.CopyModel("static_synapse","EI_synapse",{"weight":weight, "delay":max_delay})
nest.Connect(pop_exc,pop_inh,{'rule': 'fixed_indegree','indegree': CE},'EI_synapse')


def simulate_cicle(growth_steps):
    for simulation_time in growth_steps:

        nest.SetStatus(spike_detector,{"start": simulation_time+growth_step-5000.,"stop": simulation_time+growth_step})
        nest.Simulate(growth_step)

        local_connections = nest.GetConnections(pop_exc, pop_exc)
        sources = nest.GetStatus(local_connections,'source')
        targets = nest.GetStatus(local_connections,'target')
        weights = nest.GetStatus(local_connections,'weight')

        events = nest.GetStatus(spike_detector,'events')[0]
        times = events['times']
        senders = events['senders']

        extension = str(simulation_time+growth_step)+'_seed_'+str(i)+'_'+str(rank)+".npy"
        np.save(T+str(i)+"/data/times_"+extension,times)
        np.save(T+str(i)+"/data/senders_"+extension,senders)
        nest.SetStatus(spike_detector,'n_events',0)

        del local_connections

        np.save(T+str(i)+"/data/sources_"+extension,sources)
        np.save(T+str(i)+"/data/targets_"+extension,targets)




# Grow network
growth_steps = np.arange(0, growth_time,growth_step)
simulate_cicle(growth_steps)

for rounde in np.arange(1,81,1): #repetitive stimulation
    growth_steps_DC_on = np.arange(growth_time+(rounde-1)*2*growth_step,growth_time+(rounde-1)*2*growth_step+1.*growth_step, growth_step)
    projections = [{"I_e":elec_field_stren} for x in pop_exc[0:N]]
    nest.SetStatus(pop_exc[0:N],projections)
    simulate_cicle(growth_steps_DC_on)


    growth_steps_DC_off = np.arange(growth_time+(rounde-1)*2*growth_step+1.*growth_step,growth_time+(rounde-1)*2*growth_step+2.*growth_step, growth_step)
    projections = [{"I_e":0.} for x in pop_exc]
    nest.SetStatus(pop_exc,projections)
    simulate_cicle(growth_steps_DC_off)
