import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

%matplotlib inline

t = np.arange(-100, 101, 0.01) 
x1 = np.sin(t)
x2 = np.sin(t)
y = signal.correlate(x1, x2)

plt.plot(y)
plt.grid()
plt.show()