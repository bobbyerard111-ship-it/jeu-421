from noyau import *
from affichage import *
from saisie import *

def distribution_des_jetons(nb_jetons_total=11, afficher=True):
    """
    Entrée: nombre total de jetons à distribuer (11) et un booléen pour savoir s'il faut afficher les résultats
    Sortie: nombre de jetons gagnés par le joueur 1
    But: distribuer aléatoirement les jetons entre deux joueurs
    """
    jetons_joueur1 = 0
    jetons_joueur2 = 0
    jetons_restants = nb_jetons_total

    while jetons_restants > 0:
        main_joueur1 = trier_main(lancer_main())
        main_joueur2 = trier_main(lancer_main())

        if afficher:
            print("Joueur 1:\n")
            afficher_main(main_joueur1)
            print("Joueur 2:\n")
            afficher_main(main_joueur2)

        gagnant = meilleure_main(main_joueur1, main_joueur2)
        if gagnant == 0:
            if afficher:
                print("Egalité ! Aucun jeton distribué.\n")
                input()
        elif gagnant == 1:
            jetons_a_distribuer = valeur_main(main_joueur1)
            jetons_recus = min(jetons_a_distribuer, jetons_restants)
            jetons_joueur2 += jetons_recus
            jetons_restants -= jetons_recus
            if afficher:
                print(f"Joueur 1 gagne ! Joueur 2 reçoit {jetons_recus} jeton(s).") 
                print(f"Jetons restants : {jetons_restants}.\n")
                input()
        else:
            jetons_a_distribuer = valeur_main(main_joueur2)
            jetons_recus = min(jetons_a_distribuer, jetons_restants)
            jetons_joueur1 += jetons_recus
            jetons_restants -= jetons_recus
            if afficher:
                print(f"Joueur 2 gagne ! Joueur 1 reçoit {jetons_recus} jeton(s).")
                print(f"Jetons restants : {jetons_restants}\n")
                input()

    return jetons_joueur1

def bataille(jetons_joueur1, jetons_joueur2):
    if distribution_des_jetons(nb_jetons_total=11, afficher=False) == 11:
        return 2
    if distribution_des_jetons(nb_jetons_total=11, afficher=False) == 0:
        return 1
    while jetons_joueur1 != 11 and jetons_joueur2 != 11:
            jetons_joueur2 = 11 - distribution_des_jetons(nb_jetons_total=11)
            jetons_joueur1 = distribution_des_jetons(afficher = False)
            print(jetons_joueur1)
            if jetons_joueur1 == 11:
               grand_vainqueur = 1
            elif jetons_joueur2 == 11:
               grand_vainqueur = 2
        
    return grand_vainqueur                     #pt il vaut mieux que ce soit un return 1 ou 2 dans la boucle plutot que de mettre dans une variable que l'on return dans ce cas la pas besoin de boucle while ou a modifier et aussi faudrait voir si ca correspond au return demandé

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