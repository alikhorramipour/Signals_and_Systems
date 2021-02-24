import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

%matplotlib inline

t = np.arange(-10, 11, 0.01) 
x1 = np.sinc(t)
x2 = np.sin(t-2)
y = signal.correlate(x1, x2)

plt.plot(y)
plt.grid()
plt.show()