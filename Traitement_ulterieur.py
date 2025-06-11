import numpy as np
import matplotlib.pyplot as plt

t0,u0=np.loadtxt("Premier_test_06-12-2024.txt",unpack=True) #importation du fichier source

##Lissage par moyenne glissante d'ordre n :
#Chaque point est ramplacé par la moyenne des n points autour le lui.
def lissage(n,sign_b):
    sign_l = np.copy(sign_b)
    for i in range (1,len(sign_b)-1):
        ord_g = min(i,n)
        ord_d = min(len(sign_b)-i-1,n)
        ord_i=min(ord_g,ord_d)
        sign_l[i]=np.sum(sign_b[i-ord_i:i+ord_i+1])/(2*ord_i+1)
    return(sign_l)

##Lissage par l'implémentation d'un filtre passe-bas:
#Ce filtre a une fréquence de coupure fc et un pas de temps h
def Filtrage(fc,S,h):
    Yexp=np.copy(S)
    for k in range(1,len(S)-1):
        Yexp[k+1]=Yexp[k]*(1-h*2*np.pi*fc)+h*2*np.pi*fc*S[k] #équation de récurrence
    return Yexp

te = t0[1]-t0[0]

sf=Filtrage(1,u0,te) #Création d'une liste correspondant au premier filtrage
sf2=lissage(131,sf)  #Création dd'une liste correspondant au deuxième filtrage

#Affichage d'une des deux courbes obtenues aux lignes précédentes :
plt.figure()
plt.plot(t0,sf,ls='None',marker='+',markersize=3)
plt.tick_params(axis = 'both', labelsize = 15)
plt.xlabel("Temps (en s)",fontsize=15)
plt.ylabel("Tension (en V)",fontsize=15)
plt.title("Tension aux bornes de la résistance en fonction du temps",fontsize=25)
plt.grid()
plt.show()



