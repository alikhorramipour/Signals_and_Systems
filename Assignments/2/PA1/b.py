import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

%matplotlib inline

def unit_step(n):
    if n >= 0:
        return 1
    else:
        return 0
    
x1 = []
x2 = []
for index in range(-5, 16):
    x1.append((0.73)**index * unit_step(index))
    x2.append(unit_step(index) - unit_step(index-3))
    
y1 = signal.convolve(x1, x2)

plt.plot(y1)
plt.grid()
plt.show()