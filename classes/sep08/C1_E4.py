import numpy as np
import matplotlib.pyplot as plt
from scipy import special #usage pour appeler la fonction erreur
from fonctions_c1 import MaDerivee

xi,xf,npts=-3,3,30
x=np.linspace(xi,xf,npts)
y=special.erf(x)

dy_dx=np.empty(npts)
"**********************************************************"
"Méthode boucle for: Forward Dérivation "
for i in range(0,npts-1):
    dy_dx[i]=  ( y[i+1]-y[i] ) / ( x[i+1] - x[i]  )  
"Pour le dernier points on applique la pente du point précédent"    
dy_dx[npts-1]=dy_dx[i]
"Que faire si on applique un backward dérivation? "
"*********************************************************"
"Méthode MaDerivee"
dy_dx2=MaDerivee(y,h=x[1]-x[0]) 
"pas h constant"

erreur=abs(dy_dx2-dy_dx)

plt.plot(x,y,'-b',label=r"$Fct. Erreur$")
plt.plot(x,dy_dx,'-1m',label=r" Dérivé forward")
plt.plot(x,dy_dx2,'-vb',label=r" MaDerivee")
plt.legend()