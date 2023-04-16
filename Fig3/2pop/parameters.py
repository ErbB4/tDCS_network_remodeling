import numpy as np


#
N = 5000 #stimulated population size


# Parameter of the simulation
dt                      = 0.1
MSP_update_interval     = 100                                   # update interval for MSP in ms
growth_time             = 750000.                                # simulation time in ms
cicles                  = 10
growth_step             = growth_time/cicles
stimulate_step          = growth_step/cicles
min_delay               = 1.0
max_delay               = 1.5

# Parameters for asynchronous irregular firing
g       = 8.0
eta     = 1.5
epsilon = 0.1                                                   # connection probability

order     = 2500
NE        = 4*order
NI        = 1*order
N_neurons = NE+NI

CE    = epsilon*NE                                              # number of excitatory synapses per neuron
CI    = epsilon*NI                                              # number of inhibitory synapses per neuron  
C_tot = int(CI+CE)                                              # total number of synapses per neuron


# Initialize the parameters of the integrate and fire neuron
neuron_model    = "iaf_psc_delta"
CMem            = 250.0
tauMem          = 10.0
theta           = 20.0
tau_Ca          = 10000.
beta_Ca         = 1./tau_Ca
J               = 0.1                                           # postsynaptic amplitude in mV

neuron_params   = {
                    "C_m"       : CMem,
                    "tau_m"     : tauMem,
                    "t_ref"     : 2.0,
                    "E_L"       : 0.0,
                    "V_reset"   : 10.0,
                    "V_m"       : 0.0,
                    "beta_Ca"   : beta_Ca,
                    "tau_Ca"    : tau_Ca,
                    "V_th"      : theta
                   }

weight          = J


# threshold rate, equivalent rate of events needed to
# have mean input current equal to threshold
nu_th  = theta/(J*CE*tauMem)
nu_ex  = eta*nu_th
rate = 1000.0*nu_ex*CE  

 
# Parameter for synpatic elements' growth curve
growth_curve_d    = "linear"
z0_mean           = 1.
growth_curve_a    = "linear"
z0_std            = .1
slope             = 0.5
target_rate       = 0.008


# Parameter for structural plasticity synapse model
synapse_model   = "static_synapse"

synapse_params  = {
                    "min_delay": min_delay, 
                    "max_delay": max_delay
                   }
                   

R = tauMem/neuron_params["C_m"]*10**9
delta_U = 0.1 #mV
elec_field_stren = delta_U*10**(-3)/R*10**12 #pA

