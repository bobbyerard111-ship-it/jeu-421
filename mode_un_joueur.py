from noyau import *
from saisie import *
from affichage import *

def choix_ia(main_ia):

    garder_indices = []
    c1 = 0
    c2 = 0
    c4 = 0
    i = 0

    while i < 3:
        if main_ia[i] == 1:
            c1 = c1 + 1
        if main_ia[i] == 2:
            c2 = c2 + 1
        if main_ia[i] == 4:
            c4 = c4 + 1
        i = i + 1
    if c1 > 0 and c2 > 0 and c4 > 0:
        garder_indices = [0,1,2]

    tout_garder = False
    if len(garder_indices) == 3:
        tout_garder = True

    if not tout_garder:
        liste_de = [1,2,3,4,5,6]
        de_i = 0
        triple_trouve = False
        while de_i < 6:
            de = liste_de[de_i]
            cpt = 0
            j = 0
            while j < 3:
                if main_ia[j] == de:
                    cpt = cpt + 1
                j = j + 1
            if cpt == 3:
                garder_indices = [0,1,2]
                triple_trouve = True
                tout_garder = True
            de_i = de_i + 1

    paire_trouvee = False
    paire_i = -1
    paire_j = -1
    if not tout_garder:
        i = 0
        while i < 3:
            j = i + 1
            while j < 3:
                if not paire_trouvee:
                    if main_ia[i] == main_ia[j]:
                        paire_trouvee = True
                        paire_i = i
                        paire_j = j
                j = j + 1
            i = i + 1
        if paire_trouvee:
            garder_indices = [paire_i, paire_j]

    if not tout_garder and not paire_trouvee:
        meilleur = -1
        meilleur_i = -1
        i = 0
        while i < 3:
            if main_ia[i] > meilleur:
                meilleur = main_ia[i]
                meilleur_i = i
            i = i + 1
        if meilleur >= 5:
            garder_indices = [meilleur_i]
        else:
            garder_indices = []
    garder_indices = []
    i = 0
    while i < len(garder_indices):
        garder_indices = garder_indices + [main_ia[garder_indices[i]]]
        i = i + 1

    return garder_indices