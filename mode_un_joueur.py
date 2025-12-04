from noyau import *
from saisie import *
from affichage import *

def choix_ia(main_ia):
    indices = []
    priorite = [4, 2, 1]

    for valeur in priorite:
        for i in range(len(main_ia)):
            if des[i] == valeur:
                indices.append(i)

    return indices
