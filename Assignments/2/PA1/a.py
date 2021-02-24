import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

%matplotlib inline

t = np.arange(-10, 11, 0.01) 
x1 = np.sin(t/2)
x2 = np.cos(t/2)
y = signal.convolve(x1, x2)

plt.plot(y)
plt.ylabel('sin(x/2) * cos(x/2)')
plt.title('Plot of sin(x/2) * cos(x/2)')
plt.grid()
plt.show()