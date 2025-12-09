from noyau import *

# Représentations graphiques des dés.
DE_1 = [
"┌─────────┐",
"│         │",
"│    ●    │",
"│         │",
"└─────────┘"
]

DE_2 = [
"┌─────────┐",
"│  ●      │",
"│         │",
"│      ●  │",
"└─────────┘"
]

DE_3 = [
"┌─────────┐",
"│  ●      │",
"│    ●    │",
"│      ●  │",
"└─────────┘"
]

DE_4 = [
"┌─────────┐",
"│  ●   ●  │",
"│         │",
"│  ●   ●  │",
"└─────────┘"
]

DE_5 = [
"┌─────────┐",
"│  ●   ●  │",
"│    ●    │",
"│  ●   ●  │",
"└─────────┘"
]

DE_6 = [
"┌─────────┐",
"│  ●   ●  │",
"│  ●   ●  │",
"│  ●   ●  │",
"└─────────┘"
]

# Liste contenant les dessins des dés
dessin_dés = [DE_1, DE_2, DE_3, DE_4, DE_5, DE_6]

def afficher_main(main):
    """
    Entrée: une main de 3 dés sous forme de liste 
    Sortie: aucun, affichage des dés et infos textuelles sur la combinaison et la valeur
    But: afficher graphiquement les 3 dés, leur combinaison et leur valeur, lignes par lignes.
    """
    de_1 = dessin_dés[main[0]-1]
    de_2 = dessin_dés[main[1]-1]
    de_3 = dessin_dés[main[2]-1]

    print(de_1[0], de_2[0], de_3[0])
    print(de_1[1], de_2[1], de_3[1])
    print(de_1[2], de_2[2], de_3[2])
    print(de_1[3], de_2[3], de_3[3])
    print(de_1[4], de_2[4], de_3[4])
    print() 

    print(f'Combinaison : {combinaison_main(main)}')
    print(f'Valeur : {valeur_main(main)}')
    if combinaison_main(main) == 421:
        print("Wow ! Quelle chance ! C'est la combinaison la plus forte du jeu !")
    if combinaison_main(main) == "Nénette":
        print("Dommage ! C'est la combinaison la plus faible !")

def r(texte): 
    return "\033[32m" + str(texte) + "\033[0m"

def afficher_main_ia(main_ia):
    """
    Entrée: une main de 3 dés sous forme de liste 
    Sortie: aucun, affichage des dés et infos textuelles sur la combinaison et la valeur
    But: afficher graphiquement les 3 dés de l'IA, leur combinaison et leur valeur
    """
    de_1 = dessin_dés[main_ia[0]-1]
    de_2 = dessin_dés[main_ia[1]-1]
    de_3 = dessin_dés[main_ia[2]-1]

    print(r(f'{de_1[0]} {de_2[0]} {de_3[0]}'))
    print(r(f'{de_1[1]} {de_2[1]} {de_3[1]}'))
    print(r(f'{de_1[2]} {de_2[2]} {de_3[2]}'))
    print(r(f'{de_1[3]} {de_2[3]} {de_3[3]}'))
    print(r(f'{de_1[4]} {de_2[4]} {de_3[4]}'))
    print() 

    print(r(f'Combinaison : {combinaison_main(main_ia)}'))
    print(r(f'Valeur : {valeur_main(main_ia)}'))
    if combinaison_main(main_ia) == 421:
        print(r("Wow ! Quelle chance ! C'est la combinaison la plus forte du jeu !"))
    if combinaison_main(main_ia) == "Nénette":
        print(r("C'est la combinaison la plus faible !"))
