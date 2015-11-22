'''
Programa que traza un circulo con las siguiente coordenadas
Centro (-4,4) con radio = 2
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8,8,0.01)
a = 1
b = -8
c = ((x**2)+(8*x)+28)

aux_1 = ((b**2)-4*a*c)

y1 = (-b + np.sqrt(aux_1))/2*a
y2 = (-b - np.sqrt(aux_1))/2*a

plt.plot(x,y1,'r',x,y2,'b')
plt.grid(True)
plt.show()