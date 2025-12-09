from noyau import *
from affichage import *
from saisie import *
from mode_un_joueur import *

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
            if valeur_main(main_joueur1) == valeur_main(main_joueur2):
                if afficher:
                    print("Egalité ! Aucun jeton distribué.\n")
                    input()
            else:
                jetons_a_distribuer = valeur_main(main_joueur1)
                jetons_recus = min(jetons_a_distribuer, jetons_restants)
                jetons_joueur2 += jetons_recus
                jetons_restants -= jetons_recus
                if afficher:
                    print(f"Joueur 1 gagne ! Joueur 2 reçoit {jetons_recus} jeton(s).") 
                    print(f"Jetons restants : {jetons_restants}.\n")
                    input()
        else:
            if valeur_main(main_joueur1) == valeur_main(main_joueur2):
                if afficher:
                    print("Egalité ! Aucun jeton distribué.\n")
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
    """
    Entrée: nombre de jetons du joueur 1 et du joueur 2 après la phase de distribution
    Sortie: numéro du joueur vainqueur (1 ou 2)
    But: dérouler la phase de bataille jusqu'à ce qu'un joueur n'ait plus de jetons
    """
    joueur_commence = 1
    
    while jetons_joueur1 > 0 and jetons_joueur2 > 0:
        print(f"\n--- Manche: Joueur 1 ({jetons_joueur1} jetons) vs Joueur 2 ({jetons_joueur2} jetons) ---\n")
        
        print("Au tour du Joueur 1:")
        main_joueur1 = jouer_tour()
        
        print("Au tour du Joueur 2:")
        main_joueur2 = jouer_tour()
        
        gagnant = meilleure_main(main_joueur1, main_joueur2)
        
        if gagnant == 1:
            jetons_a_perdre = valeur_main(main_joueur1)
            jetons_recus = min(jetons_a_perdre, jetons_joueur2)
            jetons_joueur2 += jetons_recus
            jetons_joueur1 -= jetons_recus
            print(f"\nJoueur 1 gagne ! Joueur 2 perd {jetons_recus} jeton(s).")
            joueur_commence = 2
        elif gagnant == 2:
            jetons_a_perdre = valeur_main(main_joueur2)
            jetons_recus = min(jetons_a_perdre, jetons_joueur1)
            jetons_joueur1 += jetons_recus
            jetons_joueur2 -= jetons_recus
            print(f"\nJoueur 2 gagne ! Joueur 1 perd {jetons_recus} jeton(s).")
            joueur_commence = 1
        else:
            print("\nÉgalité ! Aucun jeton distribué.")
    
    if jetons_joueur1 == 0:
        return 1
    else:
        return 2


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

def jouer():
    """
    Entrée: aucune 
    Sortie: aucune mais affiche le gagnant
    But: distribuer les jetons aux joueurs, lancer la bataille et afficher le vainqueur
    """
    jetons_joueur1 = distribution_des_jetons(afficher=True)
    jetons_joueur2 = 11 - jetons_joueur1

    vainqueur = bataille(jetons_joueur1, jetons_joueur2)
    print(f"\nLe joueur {vainqueur} a gagné !")

def bataille_ia(jetons_joueur1, jetons_ia):
    joueur_commence = 1
    
    while jetons_joueur1 > 0 and jetons_ia > 0:
        print(f"\n--- Manche: Joueur 1 ({jetons_joueur1} jetons) vs Ordinateur ({jetons_ia} jetons) ---\n")
        
        print("Au tour du Joueur 1:")
        main_joueur1 = jouer_tour()
        
        print(f"--- Manche: Ordinateur ({jetons_ia} jetons) vs Joueur 1 ({jetons_joueur1} jetons) ---\n")
        main_ia = trier_main(lancer_main())
        print("Main de l'Ordinateur:")
        afficher_main_ia(main_ia)
        input()
        relancer_main(main_ia, choix_ia(main_ia))
        afficher_main_ia(main_ia)
        input()
        relancer_main(main_ia, choix_ia(main_ia))
        afficher_main_ia(main_ia)

        gagnant = meilleure_main(main_joueur1, main_ia)
        
        if gagnant == 1:
            jetons_a_perdre = valeur_main(main_joueur1)
            jetons_recus = min(jetons_a_perdre, jetons_ia)
            jetons_ia += jetons_recus
            jetons_joueur1 -= jetons_recus
            print(f"\nJoueur 1 gagne ! Joueur 1 perd {jetons_recus} jeton(s).")
            joueur_commence = 2
        elif gagnant == 2:
            jetons_a_perdre = valeur_main(main_ia)
            jetons_recus = min(jetons_a_perdre, jetons_joueur1)
            jetons_joueur1 += jetons_recus
            jetons_ia -= jetons_recus
            print(f"\nOrdinateur gagne ! Ordinateur perd {jetons_recus} jeton(s).")
            joueur_commence = 1
        else:
            print("\nÉgalité ! Aucun jeton distribué.")
    
    if jetons_joueur1 == 0:
        return 1
    else:
        return 2
    

def jouer_ia():
    """Fonction principale du mode "Un joueur" contre l'ordinateur."""
    print("Bienvenue dans le jeu du 421 ! Vous jouez contre l'ordinateur.")
    jetons_joueur1 = distribution_des_jetons(afficher=True)
    jetons_ia = 11 - jetons_joueur1
    vainqueur = bataille_ia(jetons_joueur1, jetons_ia)
    if vainqueur == 1:
        print("Vous avez gagné !")
    else:
        print("L'ordinateur a gagné. Retentez votre chance !")


if __name__ == "__main__":
    valide = False
    while not valide:
        print("Voulez-vous jouer en mode 1 joueur ou en mode 2 joueur ?")
        n = lire_entier()
        if n == 1 or n == 2:
            valide = True
        else:
            print("Erreur. Veuillez entrer 1 ou 2.\n")
    
    if n == 2:
        jouer()
    else:
        jouer_ia()

