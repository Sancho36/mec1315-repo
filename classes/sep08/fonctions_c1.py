import numpy as np            

# Methode de dérivation numérique, centré, 
#avant(forward), arrière(backward selon le cas)
def MaDerivee(y, h=1): # derivee premiere
    n = len(y)
    dy = np.zeros(n)
    for i in range(n):
        if i==0: # derivee premiere avant, forward
            dy[i] = (y[i+1] - y[i])/h
        elif i==n-1: # derivee premiere arriere, backward
            dy[i] = (y[i] - y[i-1])/h
        else: # derivee premiere centree
            dy[i] = (y[i+1] - y[i-1])/(2*h)
    return dy


# Methode de la bissection
def bissection(f, a, b, tol=1e-6, maxiter=100):
    if f(a)*f(b)>=0:
        raise ValueError("La fonction est le meme signe aux bornes a et b!")
    i = 0
    while (b-a)/2 > tol and i < maxiter:
        m = (b + a) / 2     # Calcule le point milieu
        if f(m) == 0:
            return m
        elif f(a)*f(m) > 0: # Si vrai, il n'y a pas de changement de signe
            a = m           # Alors on déplace la borne de gauche
        else:               # Si faux, il y a un changement de signe
            b = m           # Alors on déplace la borne de droit
        i += 1         
            
    return m                # Retourne la racine m

def f(x):                   # Fonction f(x) = x¨^^2 - 2
    return x**2-2
    
r = bissection(f,0,3)       # Cherche la racine entre 0 et 3
print('Racine de f(x): r = %f,  f(r) = %f' % (r, f(r)))



"Ancienne algorithme désuet à titre de référence seulement"
def my_fzeros(f,xg,xd):
    fxg=f(xg)
    fxd=f(xd)
    "Évaluer l'algorithme si un 0 existe"
    if fxg*fxd>=0:
        print('Erreur, la fonction ne contient pas de zéros dans cet interval')
        r=[]
    else:
        r=(xg+xd)/2
        "En fonction de quel bord le zéro, les bornes s'ajuste"
        while abs(xg-xd)/2>1e-5:
            r=(xg+xd)/2
            fr=f(r)
            if fxg*fr<0:
                xd=r
            else:
                xg=r
    return r

