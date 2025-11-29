import random as rd

def lancer_de():
    return rd.randint(1, 6)

def lancer_main():
    main = []
    for i in range(3):
        main.append(lancer_de())
    return main

def combinaison_main(main_triée):
    if est_421(main_triée):
        return 421
    elif est_fiche(main_triée):
        return "Fiche"
    elif est_suite(main_triée):
        return "Suite"
    elif est_nenette(main_triée):
        return "Nénette"
    else:
        return "Banal"

def valeur_main(main):
    combinaison = combinaison_main(main)
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
    N = [4, 2, 1]
    V = []     
    for i in range(3):
        if main[i] == N[i]:
            V.append(True)
    if V == [True, True, True]:
        return True
    else:
        return False


def est_brelan(main):
    if main[0] == main[2]:
        return True


def est_fiche(main):
    if main[1] == 1 and main[2] == 1:
        return True


def est_suite(main):
    V = []   
    testeur = main[0] - 1
    for i in range(1, len(main)):
        if main[i] == testeur:
            V.append(True)
            testeur = testeur - 1
    if V == [True, True]:
        return True
    else:
        return False


def est_nenette(main):
    if main == [2, 2, 1]:
        return True
    else:
        return False
    

def meilleur_main(main1, main2):
    if valeur_main(main1) > valeur_main(main2):
        return 1    
    elif valeur_main(main1) < valeur_main(main2):
        return 2    
    else:
        return 0                      
                   

def choisir_des_a_relancer():
    des_à_relancer = []
    n = int(input("Combien de dés voulez-vous relancer ?"))
    while n <= 3:
        if n == 3:
            des_à_relancer = ["1", "2", "3"]
        elif n == 2:
            des_à_relancer.append(int(input("Quel est le premier dé que vous voulez relancer (indiquez la position du dé à relancer) ?")))
            des_à_relancer.append(int(input("Quel est le second dé que vous voulez relancer (indiquez la position du dé à relancer) ?")))   
        else:
              des_à_relancer.append(int(input("Quel dé souhaitez vous relancer (indiquez la position du dé à relancer) ?")))
    return des_à_relancer


def relancer_main(main, des_à_relancer):
    if len(des_à_relancer) == 3:
        main = lancer_main()

    elif len(des_à_relancer) == 2:
        main[des_à_relancer[0]] = main(lancer_de)
        main[des_à_relancer[1]] = main(lancer_de)

    else:
        main(des_à_relancer[0]) = main(lancer_de)
