from noyau import *
from affichage import *

def distribution_des_jetons(nb_jetons_total=11, afficher=True):
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

jetons_joueur1 = distribution_des_jetons(afficher = False)
print(jetons_joueur1)

def bataille(jetons_joueur1, jetons_joueur2):
        jetons_joueur2 = 11 - jetons_joueur1
        while jetons_joueur1 != 11 and jetons_joueur2 != 11:
            pass