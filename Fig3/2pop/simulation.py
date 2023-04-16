import numpy as np
import parameters
from parameters import *
import sys
import nest

i = int(sys.argv[1]) #combined with arrayjob to run multiple sandom simulations at the same time
print str(sys.argv[1])
seed        = i*6748+7928
grng_seed   = seed
numpy_seed  = seed+1000
np.random.seed(numpy_seed)
nest.ResetKernel()
nest.EnableStructuralPlasticity()
nest.SetKernelStatus({"resolution": dt, "print_time": True})
nest.SetKernelStatus({
    'structural_plasticity_update_interval' : int(MSP_update_interval/dt),
    'grng_seed'                             : grng_seed,
    'total_num_virtual_procs':1})
nest.SetDefaults(neuron_model, neuron_params)

# Create generic neuron with Axon and Dendrite
nest.CopyModel(neuron_model, 'excitatory')
nest.CopyModel(neuron_model, 'inhibitory')

# growth curves
gc_den = {'growth_curve': growth_curve_d, 'z': z0_mean, 'growth_rate': slope*target_rate, 'eps': target_rate, 'continuous': False}
gc_axon = {'growth_curve': growth_curve_a, 'z': z0_mean, 'growth_rate': slope*target_rate, 'eps': target_rate, 'continuous': False}

nest.SetDefaults('excitatory', 'synaptic_elements', {'Axon_exc': gc_axon, 'Den_exc': gc_den})

# Create synapse models
nest.SetDefaults(synapse_model, synapse_params)
nest.CopyModel(synapse_model, 'msp_excitatory')

# Use SetKernelStatus to activate the synapse model
nest.SetKernelStatus({
    'structural_plasticity_synapses': {
        'syn1': {
            'model': 'msp_excitatory',
            'delay': max_delay,
            'weight': weight,
            'post_synaptic_element': 'Den_exc',
            'pre_synaptic_element': 'Axon_exc',
        }
    },
    'autapses': False,
})

# build network
pop_exc = nest.Create('excitatory', NE)
pop_inh = nest.Create('inhibitory', NI)


for neuron in pop_exc:
    gc_den = {'growth_curve': growth_curve_d,
              'z': np.random.normal(z0_mean,z0_std),
              'growth_rate':  slope*target_rate,
              'eps': target_rate,
              'continuous': False}
    gc_axon = {'growth_curve': growth_curve_a,
              'z': np.random.normal(z0_mean,z0_std),
              'growth_rate':  slope*target_rate,
              'eps': target_rate,
              'continuous': False}
              
    nest.SetStatus([neuron], 'synaptic_elements', {'Axon_exc': gc_axon, 'Den_exc': gc_den})

nest.CopyModel("static_synapse","device",{"weight":weight, "delay":max_delay})
poisson_generator_inh = nest.Create('poisson_generator')
nest.SetStatus(poisson_generator_inh, {"rate": rate})
nest.DivergentConnect(poisson_generator_inh, pop_inh,model="device")

poisson_generator_ex = nest.Create('poisson_generator')
nest.SetStatus(poisson_generator_ex, {"rate": rate})

nest.DivergentConnect(poisson_generator_ex, pop_exc, model="device")
spike_detector = nest.Create("spike_detector")
nest.SetStatus(spike_detector,{
                                "withtime"  : True,
                                "withgid"   : True,
                                })

nest.ConvergentConnect(pop_exc+pop_inh, spike_detector,model="device")

nest.CopyModel("static_synapse","inhibitory_synapse",{"weight":-g*weight, "delay":max_delay})
source = np.random.random_integers(NE+1,N_neurons,(N_neurons,CI))
for n in np.arange(N_neurons):
    nest.ConvergentConnect(list(source[n,:]),[n+1],model='inhibitory_synapse')

nest.CopyModel("static_synapse","EI_synapse",{"weight":weight, "delay":max_delay})
source = np.random.random_integers(1,NE,(NI,CE))
for n in np.arange(NI):
    nest.ConvergentConnect(list(source[n,:]),[NE+n+1],model='EI_synapse')


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

        extension = str(simulation_time+growth_step)+'_seed_'+str(i)+".npy"
        T = "./" #add your own path here
        np.save(T+str(N)+"/times_"+extension,times)
        np.save(T+str(N)+"/senders_"+extension,senders)
        nest.SetStatus(spike_detector,'n_events',0)

        del local_connections

        np.save(T+str(N)+"/sources_"+extension,sources)
        np.save(T+str(N)+"/targets_"+extension,targets)
        np.save(T+str(N)+"/weights_"+extension,weights)

# Grow network
growth_steps = np.arange(0, growth_time,growth_step)
simulate_cicle(growth_steps)

#turn on tDCS
growth_steps_DC_on = np.arange(growth_time, growth_time+2*growth_step, stimulate_step)
def simulate_cicle2(growth_steps):
    for simulation_time in growth_steps:
        nest.SetStatus(spike_detector,{"start": simulation_time+stimulate_step-5000.,"stop": simulation_time+stimulate_step})
        nest.Simulate(stimulate_step)
        local_connections = nest.GetConnections(pop_exc, pop_exc)
        sources = nest.GetStatus(local_connections,'source')
        targets = nest.GetStatus(local_connections,'target')
        weights = nest.GetStatus(local_connections,'weight')

        events = nest.GetStatus(spike_detector,'events')[0]
        times = events['times']
        senders = events['senders']

        extension = str(simulation_time+stimulate_step)+'_seed_'+str(i)+".npy"
        np.save(T+str(N)+"/DC_times_"+extension,times)
        np.save(T+str(N)+"/DC_senders_"+extension,senders)
        nest.SetStatus(spike_detector,'n_events',0)

        del local_connections

        np.save(T+str(N)+"/DC_sources_"+extension,sources)
        np.save(T+str(N)+"/DC_targets_"+extension,targets)
        np.save(T+str(N)+"/DC_weights_"+extension,weights)

projections = [{"I_e":1.*elec_field_stren} for x in pop_exc[0:N]] #stimulate one pop
nest.SetStatus(pop_exc[0:N],projections)

projections = [{"I_e":-1.*elec_field_stren} for x in pop_exc[N::]] #stimulate the ress pop
nest.SetStatus(pop_exc[N::],projections)

simulate_cicle2(growth_steps_DC_on)
growth_steps_DC_off = np.arange(growth_time+2*growth_step, growth_time+6*growth_step,stimulate_step)

def simulate_cicle3(growth_steps):
    for simulation_time in growth_steps:

        nest.SetStatus(spike_detector,{"start": simulation_time+stimulate_step-5000.,"stop": simulation_time+stimulate_step})
        nest.Simulate(stimulate_step)

        local_connections = nest.GetConnections(pop_exc, pop_exc)
        sources = nest.GetStatus(local_connections,'source')
        targets = nest.GetStatus(local_connections,'target')
        weights = nest.GetStatus(local_connections,'weight')

        events = nest.GetStatus(spike_detector,'events')[0]
        times = events['times']

        senders = events['senders']
        extension = str(simulation_time+stimulate_step)+'_seed_'+str(i)+".npy"
        np.save(T+str(N)+"/DC_off_times_"+extension,times)
        np.save(T+str(N)+"/DC_off_senders_"+extension,senders)
        nest.SetStatus(spike_detector,'n_events',0)

        del local_connections
        np.save(T+str(N)+"/DC_off_sources_"+extension,sources)
        np.save(T+str(N)+"/DC_off_targets_"+extension,targets)
        np.save(T+str(N)+"/DC_off_weights_"+extension,weights)

projections = [{"I_e":0.} for x in pop_exc]
nest.SetStatus(pop_exc,projections)
simulate_cicle3(growth_steps_DC_off)



