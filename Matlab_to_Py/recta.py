'''
Programa que traza una recta con respecto a los puntos
P(-3,2) , Q(3,3) 
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.1 )
y1 = ((x/6)+ 5/2) #Correco
y2 = ((x/6)+7/3) #Incorrecto

plt.plot(x,y1,'r',x,y2,'b')
plt.grid(True)
plt.show()