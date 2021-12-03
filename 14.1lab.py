import math 

import numpy as np 

from numpy import * 

import matplotlib.pyplot as plt 

  

  

def f(x,y): 

    bibi=x+math.cos(y/math.sqrt(0.7)) 

    return bibi 

   

   

x0=0.9 

b=1.9 

h=0.1 

x=np.arange(x0,b+h,h) 

n=len(x)-1 

y=np.empty(n+1) 

y[0]=1.7 

  

  

for i in range(n): 

    y[i+1]=y[i]+f(x[i],y[i])*h 

     

     

y_rounded=np.round_(y,4) 

  

  

print('x=',x) 

print('y=',y_rounded) 

  

  

plt.plot(x, y,'o',x,y,'red') 

plt.xlabel('x')  

plt.ylabel('y') 

plt.title('Метод Ейлера')  

plt.legend(['точки','x+cos(y/sqrt(0.7))']) 

plt.grid() 

plt.show()