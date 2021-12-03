import matplotlib.pyplot as plt

from numpy import *

from scipy.interpolate import UnivariateSpline

  

x = [0,0.2,0.5,0.9,1.5]

y = [1.75,2.68,1.24,0.72,1.35]

  

spl = UnivariateSpline(x,y)

xs = linspace(-2, 2, 100)

  

plt.plot(x,y, 'ro',xs,spl(xs), 'g')

plt.show()