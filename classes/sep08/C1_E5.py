"Appel de la fonction bissection dans un autre fichier"
from fonctions_c1 import bissection
"Assume que le fichier de fonction est au même répertoire que ce fichier"
import numpy as np
import matplotlib.pyplot as plt

"Déclaration d'une fonction mathématique à étudier"
def F(x):
    import numpy as np
    y=np.power(x,3)-x
    #y=np.exp(-x)*(3.2*np.sin(x)-0.5*np.cos(x))
    return y

"Tracage d'une fonction"
x=np.linspace(-2,2,35)
y=F(x)

t=bissection(F, -1.5, -0.5)

plt.figure(1)
plt.plot(x,y,'-g')
plt.plot(t,F(t),'or')
plt.xlabel('axes des x')
plt.ylabel('axes des y')
plt.grid('on')

    