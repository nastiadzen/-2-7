import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy import integrate,interpolate
a=0.5
b=0.3
N=1000000
S0=990000
I0=7000
R0=3000
t0=0
tf=25
t=np.linspace(t0, tf, 25)
S=[]
S.append(S0)
I=[]
I.append(I0)
R=[]
R.append(R0)
for i in range(1, 25):
    S.append(S[-1]-a*S[-1])
    I.append(I[-1]+a*S[-1]-b*I[-1])
    R.append(R[-1]+b*I[-1])
plt.plot(t, S, 'g', 'o')
plt.xlabel("Time")
plt.ylabel("A healthy favorable population")
plt.grid()
plt.show()
plt.plot(t, I, 'b', 'o')
plt.xlabel("Time")
plt.ylabel("Infected population")
plt.grid()
plt.show()
plt.plot(t, R, 'r', 'o')
plt.xlabel("Time")
plt.ylabel("A healthy disadvantaged population")
plt.grid()
plt.show()
f_S=interpolate.interp1d(t, S, kind='cubic')
f_I=interpolate.interp1d(t, I, kind='cubic')
f_R=interpolate.interp1d(t, R, kind='cubic')
tnew=np.linspace(t0, tf, 100000)
Snew=f_S(tnew)
Inew=f_I(tnew)
Rnew=f_R(tnew)
plt.plot(tnew, Snew, 'g', label="A healthy favorable population")
plt.plot(tnew, Inew, 'b', label="Infected population")
plt.plot(tnew, Rnew, 'r', label="A healthy disadvantaged population")
plt.xlabel("Time")
plt.ylabel("Population")
plt.yticks(np.arange(0, 1100000, 100000))
plt.grid()
plt.legend()
plt.show()