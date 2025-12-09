from noyau import *
from saisie import *
from affichage import *

def choix_ia(main_ia):
    """
    Entrée : main_ia, une liste de trois entiers représentant les dés de l'IA.
    Sortie : indices_a_relancer, une liste d'entiers représentant les indices des dés à relancer.
    """
    main_triee = trier_main(main_ia)

    if est_421(main_triee):
        return []  # Ne rien relancer - 421 est la meilleure main!
    
    if est_brelan(main_triee):
        return []  # Ne rien relancer - Brelan est déjà très bon
    
    if est_suite(main_triee):
        return []  # Ne rien relancer - Suite (1-2-3, 2-3-4, etc), dans le cas d'une suite avec comme dés 1-2-3 on ne prends pas le risque de tenter le 421
    
    if est_fiche(main_triee):
        return []  # Fiche (deux dés 1 identiques) = assez bon, on garde
    
    # ÉTAPE 2: Logique pour améliorer la main
    
    # Une paire est une bonne base pour tenter le brelan
    i = 0
    while i < 3:
        j = i + 1
        while j < 3:
            if main_ia[i] == main_ia[j]:
                # On a trouvé une paire! On relance le dé qui n'est pas dans la paire !
                indices_a_relancer = []
                for k in range(3):
                    if k != i and k != j:
                        indices_a_relancer.append(k+1)
                return indices_a_relancer
            j = j + 1
        i = i + 1
    
    #  ÉTAPE 3: Si pas de paire, stratégie d'amélioration intelligente
    
    # Trouver le plus grand dé pour évaluer la main
    meilleur = -1
    meilleur_i = -1
    deuxieme = -1
    deuxieme_i = -1
    
    i = 0
    while i < 3:
        if main_ia[i] > meilleur:
            deuxieme = meilleur
            deuxieme_i = meilleur_i
            meilleur = main_ia[i]
            meilleur_i = i
        elif main_ia[i] > deuxieme:
            deuxieme = main_ia[i]
            deuxieme_i = i
        i = i + 1
    
    # Stratégie 2: Si on a au moins un dé >= 4, le garder + un autre dé et relancer le 3e
    if meilleur >= 4:
        indices_a_relancer = []
        for k in range(3):
            if k != meilleur_i and k != deuxieme_i:
                indices_a_relancer.append(k+1)
        return indices_a_relancer
    
    # Stratégie 3: Si tous les dés sont petits (< 4), on relance tout pour avoir une chance

    return [1, 2, 3]