import matplotlib.pyplot as plt
import numpy as np
import math


%matplotlib inline


def unit_impulse_discrete(n):
    if int(n) == 0:
        return 1
    return 0


def system_function(n):

    return ((0.73) ** n) * unit_impulse_discrete(n) + ((0.94) ** n) * unit_impulse_discrete(n-5)

x = np.arange(-4, 21, 1)   # start, stop, step
y = []
for i in range(len(x)):
    y.append(system_function(x[i]))

plt.plot(x, y)
plt.grid()
plt.show()