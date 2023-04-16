import numpy as np
import parameters
from parameters import *
import sys
import nest


# the simulation code is the same as the 2pop experiments, except for the protocol for DC injection
projections = [{"I_e":-1.*elec_field_stren} for x in pop_exc[0:N]] #one pop with N neurons were stimulated
nest.SetStatus(pop_exc[0:N],projections)

projections = [{"I_e":1.*elec_field_stren} for x in pop_exc[N:2*N]] #a second pop with N neurons were stimulated with opposite current
nest.SetStatus(pop_exc[N:2*N],projections)

