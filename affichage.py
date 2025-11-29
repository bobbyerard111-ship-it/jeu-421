from noyau import *


def afficher_main(main_triée):
  print(f'''
  Dé n°1  Dé n°2  Dé n°3
    {main_triée[0]}       {main_triée[1]}       {main_triée[2]}

  Combinaison : {combinaison_main(main_triée)}
  Valeur : {valeur_main(main_triée)}
  ''')

main = lancer_main()
print(main)
main_triée = trier_main(main)
print(main_triée)
afficher_main(main_triée)