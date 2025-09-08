

"Pour effacer une figuire, cliquer sur la figure et faire CTRL+W"
import numpy as np
import matplotlib.pyplot as plt

"Déclaration des paramètres de départs"
xi=0
xf=2*np.pi
npts=45
#ou
xi,xf,npts= 0,2*np.pi, 45

"Méthode 1"
x=np.linspace(xi,xf,npts)
"Méthode 2"
dx=(xf-xi)/(npts-1)
x2=np.arange(xi,xf+dx,dx)

"Est-ce que les 2 méthodes donnes le même résultat?"
erreur=abs(x-x2)


y1=np.cos(x)
y2=np.power(x,3)*0.01

plt.figure(1)
plt.plot(x,y1,'-r',label=r"$y=\cos(x)$")
plt.plot(x,y2,'+b',label=r"$y=0.01 \cdot x^3$")

"Ligne 34 à 39 facultatif et modifie l\'apparence de la figure"
plt.xlabel('Axe des x')
plt.ylabel('Axe des y')
plt.title('Graphique d\'une fonction')
plt.legend()
plt.grid(axis='x')
plt.grid(axis='y')

