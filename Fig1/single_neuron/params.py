tauMem = 10.0   # time constant of membrane potential in ms
theta  = 20.0   # membrane threshold potential in mV
neuron_params= {"C_m":        250.0,
                "tau_m":      tauMem,
                "t_ref":      2.0,
                "E_L":        0.0,
                "V_reset":    10.0,
                "V_m":        0.0,
                "V_th":       theta}
                
p_rate = 18100.0

R = tauMem/neuron_params["C_m"]*10**9

J = 0.1 #mV
delay = 0.1

simtime = 100000. #ms
dt = 0.1

delta_U = 0.1 #mV

elec_field_stren = delta_U*10**(-3)/R*10**12 #pA
