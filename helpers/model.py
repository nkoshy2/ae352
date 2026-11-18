import numpy as np
from helpers.parameters import *

# <x, y, z, vx, vy, vz, phi, theta, psi, omega1, omega2, omega3, Omega1, Omega2, Omega3, Omega4, E>

def state_dot(r, t, u):

    phi = r[6]
    theta = r[7]
    psi = r[8]

    omega_i = r[9:12]
    Omega_i = r[12:16]

    T_i = np.array([k_T * Omega**2 for Omega in Omega_i])
    Q_i = np.array([k_Q * Omega**2 for Omega in Omega_i])
    h_r = J_r * np.array([s[i] * Omega_i[i] for i in range(4)]).sum()

    T = T_i.sum()

    M1 = l*(T_i[1] - T_i[3])
    M2 = l*(T_i[2] - T_i[0])

    r_dot = np.zeros(17)

    r_dot[0] = r[3] # vx
    r_dot[1] = r[4] # vy
    r_dot[2] = r[5] # vz
    r_dot[3] = T/m * (np.cos(psi)*np.sin(theta)*np.cos(phi) + np.sin(psi)*np.sin(phi)) # ddot x
    r_dot[4] = T/m * (np.sin(psi)*np.sin(theta)*np.cos(phi) - np.cos(psi)*np.sin(phi)) # ddot y
    r_dot[5] = T/m * np.cos(theta)*np.cos(phi) - g # ddot z
    r_dot[6] = omega_i[0] + np.sin(phi)*np.tan(theta)*omega_i[1] + np.cos(phi)*np.tan(theta)*omega_i[2] # dot phi
    r_dot[7] = np.cos(phi)*omega_i[1] - np.sin(phi)*omega_i[2] # dot theta
    r_dot[8] = np.sin(phi)/np.cos(theta) * omega_i[1] + np.cos(phi)/np.cos(theta) * omega_i[2] # dot psi
    r_dot[9] = (M1 - (I3 - I2)*omega_i[1]*omega_i[2] - h_r*omega_i[1])/I1
    r_dot[10] = (M2 - (I1 - I3)*omega_i[2]*omega_i[0] + h_r*omega_i[0])/I2
    r_dot[11] = (-np.array([s[i] * u[i] for i in range(4)]).sum() - (I2 - I1)*omega_i[0]*omega_i[1])/(I3 - 4*J_r)

    Omega_dot = np.array([(u[i] - Q_i[i])/J_r - s[i]*r_dot[11] for i in range(4)]) # Omega dot 1-4
    r_dot[12:16] = Omega_dot

    r_dot[16] = P_aux + 1/eta * np.array([u[i] * Omega_i[i] for i in range(4)]).sum() # E dot

    return r_dot

def forward_euler(f, w_start, t_end, dt):
    """
    Note: Taken from Prof. Goza's AE 370 Lecture 10
    March w' = f(w, t) from t = 0 to t_end with the forward Euler method.

    Parameters
    ----------
    f : callable
        The dynamics, f(w, t) -> ndarray
    w_start : ndarray
        The state at t = 0
    t_end : float
        Final time
    dt : float
        Time step

    Returns
    -------
    w : ndarray
        Shape (n + 1, len(w_start)); row k is the state at t_k
    times : ndarray
        The n + 1 times t_k
    """
    n = int(round(t_end / dt))
    w = np.empty((n + 1, np.size(w_start)))
    w[0] = w_start
    for k in range(n):
        w[k + 1] = w[k] + dt * f(w[k], k * dt)
    return w, np.arange(n + 1) * dt
