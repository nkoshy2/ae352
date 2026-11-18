import numpy as np
import matplotlib.pyplot as plt

def plotDegreesOfFreedom(times, r, title):
    fig = plt.figure(figsize=(18, 10))

    dimension = [0, 1, 2, 6, 7, 8]
    titles = ['x [m] vs time [s]', 'y [m] vs time [s]', 'z [m] vs time [s]', r'$\phi$ [rad] vs time [s]', r'$\theta$ [rad] vs time [s]', r'$\psi$ [rad] vs time [s]']
    y_labels = ['x [m]', 'y [m]', 'z [m]', r'$\phi$ [rad]', r'$\theta$ [rad]', r'$\psi$ [rad]']

    for i in range(6):
        ax = fig.add_subplot(231 + i)
        ax.set_title(titles[i])
        ax.set_ylabel(y_labels[i])
        ax.set_xlabel(r'$t$ [s]')
        ax.plot(times, r[:, dimension[i]], label=title)
        ax.legend()

    return fig

def plotMoreDegreesOfFreedom(fig, times, r, title):
    dimension = [0, 1, 2, 6, 7, 8]
    titles = ['x [m] vs time [s]', 'y [m] vs time [s]', 'z [m] vs time [s]', r'$\phi$ [rad] vs time [s]', r'$\theta$ [rad] vs time [s]', r'$\psi$ [rad] vs time [s]']
    y_labels = ['x [m]', 'y [m]', 'z [m]', r'$\phi$ [rad]', r'$\theta$ [rad]', r'$\psi$ [rad]']

    for i in range(6):
        ax = fig.axes[i]
        ax.set_title(titles[i])
        ax.set_ylabel(y_labels[i])
        ax.set_xlabel(r'$t$ [s]')
        ax.plot(times, r[:, dimension[i]], label=title)
        ax.legend()

    return
