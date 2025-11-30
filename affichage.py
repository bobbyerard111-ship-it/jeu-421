from noyau import *
from saisie import *

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

dessin_dés = [DE_1, DE_2, DE_3, DE_4, DE_5, DE_6]

def afficher_main(main):
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


