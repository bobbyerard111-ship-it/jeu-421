import random as rd
from affichage import *

def lancer_de():
    return rd.randint(1, 6)

def lancer_main():
    return [lancer_de() for _ in range(3)]

def combinaison_main(main):
    m = trier_main(main)
    if est_421(m):
        return 421
    elif est_brelan(m):
        return "Brelan"
    elif est_fiche(m):
        return "Fiche"
    elif est_suite(m):
        return "Suite"
    elif est_nenette(m):
        return "Nénette"
    else:
        return "Banal"

def valeur_main(main):
    m = trier_main(main)
    combinaison = combinaison_main(m)
    
    if combinaison == 421:
        return 8
    elif m == [1, 1, 1]:
        return 7
    elif est_brelan(m):
        return m[0]
    elif combinaison == "Fiche":
        return m[0]
    elif combinaison == "Suite":
        return 2
    elif combinaison == "Nénette":
        return 0
    else:
        return 1
  
def trier_main(main):
    """
   Entrée :
        - main : une liste de 3 valeurs représentant un tirage 
   Role : 
        - déterminer la plus petite valeur et la placer en main[2]
   Sortie: 
    """
    if main[0] < main[1]:
        temp_memory = main[0]
        main[0] = main[1]
        main[1] = temp_memory
    if main[1] < main[2]:
        temp_memory = main[1]
        main[1] = main[2]
        main[2] = temp_memory
    if main[0] < main[1]:
        temp_memory = main[0]
        main[0] = main[1]
        main[1] = temp_memory
    return main

def est_421(main):
    return main == [4,2,1]


def est_brelan(main):
    return main[0] == main[1] == main[2]


def est_fiche(main):
    return main[1] == 1 and main[2] == 1


def est_suite(main):
    return main[0] - 1 == main[1] and main[1] - 1 == main[2]


def est_nenette(main):
    return main == [2,2,1]
    

def meilleure_main(main1, main2):
    if valeur_main(main1) > valeur_main(main2):
        return 1    
    elif valeur_main(main1) < valeur_main(main2):
        return 2    
    else:
        return 0                      
                   

def distribution_des_jetons(nb_jetons_total=11):
    jetons_joueur1 = 0
    jetons_joueur2 = 0
    jetons_restants = nb_jetons_total

    while jetons_restants > 0:
        main_joueur1 = trier_main(lancer_main())
        print("Joueur 1:\n")
        print(main_joueur1)
        main_joueur2 = trier_main(lancer_main())
        print("Joueur 2:\n")
        print(main_joueur2)

        gagnant = meilleure_main(main_joueur1, main_joueur2)
        if gagnant == 0:
            print("Egalité ! Aucun jeton distribué.\n")
        elif gagnant == 1:
            jetons_a_distribuer = valeur_main(main_joueur1)
            jetons_recus = min(jetons_a_distribuer, jetons_restants)
            jetons_joueur2 += jetons_recus
            jetons_restants -= jetons_recus
            print(f"Joueur 1 gagne ! Joueur 1 reçoit {jetons_recus} jeton(s).") 
            print(f"Jetons restants : {jetons_restants}.\n")
        else:
            jetons_a_distribuer = valeur_main(main_joueur2)
            jetons_recus = min(jetons_a_distribuer, jetons_restants)
            jetons_joueur1 += jetons_recus
            jetons_restants -= jetons_recus
            print(f"Joueur 2 gagne ! Joueur 1 reçoit {jetons_recus} jeton(s).")
            print(f"Jetons restants : {jetons_restants}\n")

    return jetons_joueur1