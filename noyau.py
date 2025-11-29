import random as rd

def lancer_de():
    return rd.randint(1, 6)

def lancer_main():
    main = []
    for i in range(3):
        main.append(lancer_de())
    return main

def combinaison_main(main_triée):
    if est_421():
        return 421
    elif est_fiche():
        return "Fiche"
    elif est_suite():
        return "Suite"
    elif est_nenette():
        return "Nénette"
    else:
        return "Banal"

def valeur_main(combinaison, main):
    if combinaison == 421:
        return 8
    elif combinaison == "Fiche":
        return main[0]
    elif combinaison == "Suite":
        return 2
    elif combinaison == "Nénette":
        return 0
    elif combinaison == "Brelan":
        return main[0]
    elif main == [1, 1, 1]:
        return 7
    else: 
        return 1

def trier_main(main):
    """
   Entrée :
        - main : une liste de 3 valeurs représentant un tirage 
   Role : 
        - déterminer la plus petite valeur et la placer en main[2]
   Sortié: 
    """
    mini = main[0]
    maxi = main[0]
    for i in range(len(main)):
        if main[i] < mini:
            mini = main[i]
    main[0] = maxi
    for j in range(len(main)):
        if main[j] > maxi:
            maxi = main[j]
    main[2] = mini
