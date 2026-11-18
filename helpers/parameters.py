import numpy as np

# Parameters and Constants
g = 9.81 # m/s^2
l = 0.250 # m -> rod length
m = 1.250 # kg -> total mass
J_r = 7e-5 # kg m^2 -> relative rotor spin inertia

# centered components dimensions as a box of a x a x c
a = 0.16 # m
c = 0.08 # m

# Inertia Tensor Componenets
I1 = 0.0135821 # kg m^2
I2 = I1 # kg m^2
I3 = 0.0263748 # kg m^2

k_T = 1.19692e-5 # UNIT ??
k_Q = 1.63772e-7 # UNIT ??

P_aux = 5 # W
eta = 0.60 # motor controller efficiency

s = np.array([1, -1, 1, -1]) # rotor spin directions

E_available = 170496 # J