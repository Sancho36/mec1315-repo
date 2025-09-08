import numpy as np
import matplotlib.pyplot as plt

xi=0
xf=4
npts=15
x=np.linspace(xi,xf,npts) #0 à 4 avec 100 pts

#Méthode 1
y=np.power(x,3)
#Méthode 2
y=x**3

dx_c=x[1]-x[0]    #pas dx constant

"Méthode d'intégration avec forward integration"
A1=0
for j in range(0,npts-1):
    A1= A1 +  ( y[j]+y[j+1] )/2*dx_c
"Méthode d'intégration avec backward integration"    
A2=0
for i in range(1,npts):
    A2=A2 + ( y[i]+ y[i-1] )/2*dx_c   

print("L'intégration avec la méthode forward et backward sont :%g et %g" % (A1,A2))
plt.plot(x,y,'-.r',label=r"$y=x^3$")
plt.legend()

"Méthode de Numpy "  
A3=np.trapz(y,dx=dx_c)
"Méthode de trapèze(backward) après simplification algébrique 4.3 page 17"  
A4 = (dx_c/2)*(y[0]+ 2*sum(y[1:npts-1]) + y[npts-1]) # Methode trapeze