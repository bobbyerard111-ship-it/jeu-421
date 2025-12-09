# <p align="center">Projet 421 – README</p>

## <u>Auteurs: </u>
- Gabriel Astrued
- Elsa Lelouch
- Joseph Colonna d'Istria 

## <u>Contexte du projet: </u>
Cadre d’un travail portant sur la programmation d’un jeu de dés complet : le 421, incluant lancés de dés, reconnaissance des combinaisons, redistribution des jetons, bataille, gestion des entrées utilisateur et affichage.

## <u>Date:</u>
09/12/2025

## <u>Version du programme:</u> 
v1.0
## <u>Langage utilisé:</u>
Python
## <u>Version: </u>
Python 3.6 

## <u>Fichier principal à exécuter: </u>
421.py 


## <u>Listes des modules implantés: </u>

**1. noyau.py**

- <u>lancer_de():</u> génère un entier aléatoire entre 1 et 6
- <u>lancer_main():</u> crée une main de 3 dés
- <u>trier_main():</u> trie les dés dans l'ordre décroissant
- <u>Fonctions de test de combinaisons:</u>
est_421(), est_brelan(), est_fiche(), est_suite(), est_nenette()
- <u>combinaison_main():</u> renvoie le nom de la combinaison
- <u>valeur_main():</u> calcule la valeur numérique d'une main
- <u>meilleure_main():</u> compare deux mains

**2. saisie.py**

- <u>lire_entier():</u> validation d’entrée entière
- <u>choisir_des_a_relancer():</u> choix des dés à relancer
- <u>relancer_main():</u> relance effective des dés choisis

**3. affichage.py**

- <u>afficher_main():</u> affiche trois dés + type de combinaison + valeur

**4. mode_un_joueur.py**

- <u>choix_ia(main_ia):</u> sélectionne intelligemment quels dés relancer

**5. 421.py**

- <u>distribution_des_jetons():</u> phase de distribution
- <u>bataille():</u> phase finale jusqu’à épuisement des jetons
- <u>jouer_tour():</u> tour complet d'un joueur
- <u>jouer():</u> lance le jeu complet

## <u>Liste des autres modules Pyton utilisés: </u>
- random()
- input()
- print()

## <u>Cas échéant: </u>
distribution_des_jetons(nb_jetons_total=11, afficher=True)
- <u>nb_jetons_total:</u> nombre total de jetons distribués au début
- <u>afficher:</u> s’il faut afficher (True) ou non (False) tous les lancers pendant la distribution





