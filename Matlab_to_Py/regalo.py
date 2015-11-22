import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,num=10000)

x = 12*np.sin(t) - 4*np.sin(3*t)
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

plt.plot(x,y,color='red')
plt.grid(True)
plt.show()