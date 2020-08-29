import numpy as np
import math
import matplotlib.pyplot as plt

# D = 5,68 x 10^-10 m^2 s^-1 = 568 um^2 s^-1
DIFFUSION_COEFFICIENT = 568

# F = 1.5 uL/min
FLOW_RATE = 1.5

# Following parameters in micrometers (um)
CHANNEL_WIDTH = 120
CHANNEL_LENGTH = 240000
CHANNEL_HEIGHT = 50

def mixer(l, w, h, flow, d):
    
    u = flow/60 * (math.pow(10, 9)) / (w * h)
    c = np.zeros(w + 1)
    s = 0

    for i in range(w + 1):
        c[i] = conc(l, w/2 - i, u, d)
        s += abs(2 * (0.5 - c[i]))

    print("Mixing index: " + str((1 - s/w) * 100))
    print("Residence time: " + str(l/u))
    plt.plot(c)
    plt.ylabel("C/C0")
    plt.xlabel("Channel cross-section")
    plt.show()

    # Calculate mixing index with t_mix formula from reference article
    for i in range(w + 1):
        c[i] = conc((w**2 / d) * u, w/2 - i, u, d)
        s += abs(2 * (0.5 - c[i]))

    print("IGNORE! Mixing index with t_mix = l * l / D: " + str((1 - s/w) * 100))
    return "Finished!" 

# Calculate concentration on location (x,y)
def conc(x, y, u, d):
    return 0.5 * (1 - math.erf( (y * math.sqrt(u)) / (2 * math.sqrt(d * x))))


mixer(CHANNEL_LENGTH, CHANNEL_WIDTH, CHANNEL_HEIGHT, FLOW_RATE, DIFFUSION_COEFFICIENT)
