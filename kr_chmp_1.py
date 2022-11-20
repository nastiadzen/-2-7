import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy import integrate,interpolate
speed=[25,35,45,30,60,120,100,100,70,75,80,65]
time=(np.linspace(0,11,12))
print(time)
plt.plot(time,speed,'d', time, speed, 'cyan')
plt.xticks(np.arange(0, 12, 1))
plt.yticks(np.arange(0, 140, 10))
f=interpolate.interp1d(time, speed,kind='cubic')
r=interpolate.interp1d(time, speed,kind='quadratic')
new=np.linspace(0, 11,10000)
g,err=integrate.quad(f,11,0)
print("Kind='cubic': ",round(g, 5))
g,err=integrate.quad(r,11,0)
print("Kind='quadratic': ",round(g, 5))
y1=f(new)
y2=r(new)
plt.xlabel("Time")
plt.ylabel("Speed")
plt.legend(["Dots","Graph"])
plt.grid()
plt.show()