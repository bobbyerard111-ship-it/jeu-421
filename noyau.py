import random as rd
from affichage import *

def lancer_de():
    """ 
    Entrée: aucune
    Sortie: un entier entre 1 et 6
    But:  générer et retourner un entier aléatoire compris entre 1 et 6
    """

    return rd.randint(1, 6)

def lancer_main():
    """ 
    Entrée: aucune
    Sortie: une liste de 3 entiers qu'on nomme "main" entre 1 et 6
    But: créer et retourner une main composÃ©e de 3 résultats de lancer_de()
    """

    return [lancer_de() for _ in range(3)]

def combinaison_main(main):
    """
    Entrée: la main générée par la fonction lancer_main() 
    Sortie:  Une chaine de caractère qui indique la nature de la combinaison :
    "421"; "brelan"; "fiche"; "suite"; "nénette"; "banal"
    But: Déterminer et retourner la nature de la combinaison de la main
    """

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
    """
    Entrée: la main générée par la fonction lancer_main() 
    Sortie: la valeur de la main (un entier), c'est a dire le nombre de jontons qui correspond en suivant les règles du 421 
    But: retourner la valeur numérique qui permet de comparer les mains entre elles ou de gérer la redistribution des jetons.
    """

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
    Entrée: une liste de 3 valeurs représentant la main
    Sortie: la même main triée dans l'ordre décroissant
    But: organiser les dés pour faciliter les vérifications
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
    """
    Entrée: une main triée
    Sortie: True ou False
    But: vérifier si la main correspond à 4-2-1
    """
    return main == [4,2,1]


def est_brelan(main):
    """
    Entrée: une main triée
    Sortie: True ou False
    But: vérifier si les trois dés sont identiques
    """
    return main[0] == main[1] == main[2]


def est_fiche(main):
    """
    Entrée: une main triée
    Sortie: True ou False
    But: vérifier si la main contient deux 1
    """
    return main[1] == 1 and main[2] == 1


def est_suite(main):
    """
    Entrée: une main triée
    Sortie: True ou False
    But: vérifier si la main forme une suite 
    """
    return main[0] - 1 == main[1] and main[1] - 1 == main[2]


def est_nenette(main):
    """
    Entrée: une main triée
    Sortie: True ou False
    But: vérifier si la main est 2-2-1
    """
    return main == [2,2,1]
    

def meilleure_main(main1, main2):
    """
    Entrée: deux mains triées
    Sortie: 1 si main1 gagne, 2 si main2 gagne, 0 si égalité
    But: comparer les deux mains et déterminer le vainqueur
    """

    if valeur_main(main1) > valeur_main(main2):
        return 1    
    elif valeur_main(main1) < valeur_main(main2):
        return 2    
    else:
        return 0                      
                   

def distribution_des_jetons(nb_jetons_total=11):
    """
    Entrée: nombre total de jetons à distribuer (11)
    Sortie: nombre de jetons gagnés par le joueur 1
    But: jouer des manches, comparer les mains et distribuer les jetons jusqu’à épuisement
    """
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

def jouer_tour():
    """
    Entrée: aucune
    Sortie: la main finale du joueur après le tour
    But: effectuer le tour complet d’un joueur (lancer la main initiale, permettre au joueur de relancer certains dés jusqu’à 2 fois, afficher les mains avant et après relance, retourner la main finale)
    """
    main = trier_main(lancer_main())
    afficher_main(main)

    relances_restantes = 2  
    relancer = True        

    while relances_restantes > 0 and relancer:
        des_a_relancer = choisir_des_a_relancer()  # demander quels dés relancer
        if des_a_relancer == []:                   # si le joueur ne relance rien
            relancer = False
        else:
            main = relancer_main(main, des_a_relancer)  
            main = trier_main(main)
            afficher_main(main)
            relances_restantes -= 1

    return main

