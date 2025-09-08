import matplotlib.pyplot as plt
import numpy as np

ti=0
tf=2*np.pi
npts=125    #nbr de points
n=4         #paramètre de la rosace
t=np.linspace(ti,tf,npts)

"Méthode 1"
x=2*np.sin(n*t)*np.cos(t)
y=2*np.sin(n*t)*np.sin(t)
"Méthode 2"
x1, y1=np.zeros([len(t)]), np.zeros([len(t)])
for j in range(npts):
    x1[j]=2*np.sin(n*t[j])*np.cos(t[j])
    y1[j]=2*np.sin(n*t[j])*np.sin(t[j])


plt.plot(x,y,'-.b')
plt.plot(x1,y1,'--r')