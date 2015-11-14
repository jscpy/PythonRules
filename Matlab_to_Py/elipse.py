'''
Programa que grafica una interseccion entre 
elipses en el II y IV cuadrante
'''
import numpy as np
import matplotlib.pyplot as plt

#Elipse con centro en P1 (-5,2) , a = 4 y b = 2.
x = np.arange(-10,0,0.01)
a = 4
b = -16
c = ((x**2)+(10*x)+25)

aux_1 = ((b**2)-4*a*c)

y1 = (-b + np.sqrt(aux_1))/2*a
y2 = (-b - np.sqrt(aux_1))/2*a

plt.plot(x,y1,'r',x,y2,'b')
plt.grid(True)
plt.show()