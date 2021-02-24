import matplotlib.pyplot as plt
import numpy as np
import math


%matplotlib inline


def system_function(n):
    if n == 0 or n%4 == 0 or n%4 == 1:
        return 1
    return 0

x = np.arange(-4, 21, 1)   # start, stop, step
y = []
for i in range(len(x)):
    y.append(system_function(x[i]))

plt.plot(x, y)
plt.grid()
plt.show()