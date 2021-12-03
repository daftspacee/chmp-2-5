import numpy as np
import math
 
x = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
y = [10.517, 10.193, 9.807, 9.387, 8.977, 8.637]
h = x[1] - x[0]

def f(arr_y, j):
  mas = []
  for i in range(len(arr_y)):
    mas.append(arr_y[i] - arr_y[i-1])
  mas.pop(0)
  if j == 1:
    return mas
  else:
    j -= 1
    return f(mas, j)
  
  
pox1 = 1 /h * ((f(y, 1)[1]) - (f(y, 2)[1])/2 + (f(y, 3)[1])/3 - (f(y, 4)[1])/4)
pox2 = 1 /h**2 *((f(y, 2)[1]) - (f(y, 3)[1])+ 11/12*(f(y,4)[1]))
  
print('Derivative y1=', round(pox1, 2))
print('Derivative y2=', round(pox2, 2))