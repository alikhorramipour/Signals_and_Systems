import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

x = np.arange(-2 * np.pi, 2*np.pi, 0.1)   # start, stop, step
y = np.sin(2 * x)

plt.plot(x, y)
plt.xlabel('x values from -2π to 2π')
plt.ylabel('sin(2x)')
plt.title('Plot of sin(2x) from -2π to 2π')
plt.legend(['sin(2x)'], loc = 'upper right') 
plt.grid()
plt.show()