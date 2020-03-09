# Name: Miranda Towne
# Description: Plotting several lines w/diff format styles in 1 command using arrays

import numpy as np
import matplotlib.pyplot as plt

# Evenly sampled time at 200ms intervals.
t = np.arange(0., 5., 0.2)

# Red dashes, blue squares and green triangles.
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()



