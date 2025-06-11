# Ce script effectue une acquisition sur une voie
# et une analyse spectrale du signal

import pycanum.main as pycan
import matplotlib.pyplot as plt
import numpy as np
import os as os

# ouverture de l'interface pour SysamSP5
can = pycan.Sysam("SP5")
# configuration de l'entrée 1 avec un calibre 1.0 V
can.config_entrees([1],[1.0])

# Période d'échantillonnage (minimum 1e-7 secondes)
te = 1e-3
# durée de l'acquisition
T = 3
# nombre d'échantillons (Max 260000 environ)
N = int(T/te)
print(N)

# configuration de l'échantillonnage. La période d'échantillonnage est donnée en
microsecondes
can.config_echantillon(te*10**6,N)
# acquisition
can.acquerir()
# Lecture des instants et des tensions pour la voie 0
t0=can.temps()[0]
u0=can.entrees()[0]
# fermeture de l'interface
can.fermer()
# enregistrement dans un fichier texte pour un traitement ultérieur
np.savetxt('valeurs.txt',[t0,u0])

# On relie la période d'échantillonnage et la durée à partir des données
# car il peut y avoir une différence avec les valeurs spécifiées au départ
te = t0[1]-t0[0]
fe = 1.0/te
N = t0.size
T = t0[N-1]-t0[0]

# Tracé temporel du signal et enregistrement de la figure dans un fichier pdf
plt.figure()
plt.plot(t0, u0, color="blue", lw=1, ls='-', marker='o', markersize=2.5)
plt.title("Representation temporelle "+" Te="+str(te*1e6)+"$\mu$s")
plt.xlabel("EA0 (s)")
plt.ylabel("u (V)")
#plt.axis([0,0.01,-5.5,6.5])
plt.grid()
plt.savefig("signal.pdf")