import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math


%matplotlib inline

x = []
y = []
for i in range (-8, 0):
    x.append(i)
    if abs(i)%4 == 1: 
        y.append(0)
    else:
        y.append(1)
        
for i in range (0, 8):
    x.append(i)
    if i%4 == 2: 
        y.append(0)
    else:
        y.append(1)
        


plt.step(x, y)
plt.grid()
plt.xlim(-6.5, 6.5)
plt.ylim(-3, 3)
plt.show()