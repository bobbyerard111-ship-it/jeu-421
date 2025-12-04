from noyau import *
from saisie import *
from affichage import *

def recommend_keep_simple(main_ia):

    kept_indices = []
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
                kept_indices = [0,1,2]
                triple_trouve = True
                tout_garder = True
            de_i = de_i + 1

    pair_found = False
    pair_i = -1
    pair_j = -1
    if not tout_garder:
        i = 0
        while i < 3:
            j = i + 1
            while j < 3:
                if not pair_found:
                    if main_ia[i] == main_ia[j]:
                        pair_found = True
                        pair_i = i
                        pair_j = j
                j = j + 1
            i = i + 1
        if pair_found:
            kept_indices = [pair_i, pair_j]

    if not all_kept and not pair_found:
        best = -1
        best_i = -1
        i = 0
        while i < 3:
            if main_ia[i] > best:
                best = main_ia[i]
                best_i = i
            i = i + 1
        if best >= 5:
            kept_indices = [best_i]
        else:
            kept_indices = []
    kept_values = []
    i = 0
    while i < len(kept_indices):
        kept_values = kept_values + [main_ia[kept_indices[i]]]
        i = i + 1