from noyau import *

def lire_entier():
    """
    Entrée: aucune
    Sortie: l’entier s , une fois validé par le code
    But: Vérifier l'entier entrée pour forcer la saisie d’un nombre entier
    """
    valide = False
    while valide == False:
        s = input()
        valide = True
        
        if len(s) == 0:
            valide = False
        else:
            i = 0
            if s[0] == "-":
                if len(s) == 1:
                    valide = False
                else:
                    i = 1
            
            while i < len(s) and valide == True:
                if s[i] < "0" or s[i] > "9":
                    valide = False
                i += 1
        
        if valide == False:
            print("Veuillez entrer un nombre entier : ")

    return int(s)


def choisir_des_a_relancer():
    """
    Entrée: aucune
    Sortie: une liste avec les numéros des dés à relancer choisi par le joueur
    But: demander à l’utilisateur quels dés (1 à 3) il veut relancer.
    """
    print("Combien de dés voulez-vous relancer (0 à 3) ?")
    n = lire_entier()

    valide = False
    while valide == False:
        if n >= 0 and n <= 3:
            valide = True
        else:
            print("Veuillez entrer un nombre entre 0 et 3 : ")
            n = lire_entier()

    if n == 0:
            return []

    if n == 3:
        des_a_relancer = [1, 2, 3]

    if n == 2:
        print("Premier dé à relancer (1, 2 ou 3) :")
        m = lire_entier()
        print("Deuxième dé à relancer (1, 2 ou 3) :")
        y = lire_entier()

        valide = False
        while valide == False:
            if (m in [1, 2, 3]) and (y in [1, 2, 3]) and (m != y):
                valide = True
            else:
                print("Positions invalides !")
                print("Premier dé :")
                m = lire_entier()
                print("Deuxième dé :")
                y = lire_entier()

        des_a_relancer = [m, y]

    if n == 1:
        print("Quel dé souhaitez vous relancer (1, 2 ou 3) ?")
        x = lire_entier()

        valide = False
        while valide == False:
            if x in [1, 2, 3]:
                valide = True
            else:
                print("Position invalide ! Entrez 1, 2 ou 3 : ")
                x = lire_entier()

        des_a_relancer = [x]

    return des_a_relancer


def relancer_main(main, des_a_relancer):
    """
    Entrée: la main et la liste des positions des dés à relancer (des_à_relancer)
    Sortie: la main mise à jour après que le joueur est choisi ou pas de relance
    But: relancer les dés choisis par le joueur et mettre à jour sa main 
    """
    if len(des_a_relancer) == 3:
        main = lancer_main()

    elif len(des_a_relancer) == 2:
        
        main[des_a_relancer[0] - 1] = lancer_de()
        main[des_a_relancer[1] - 1] = lancer_de()

    elif len(des_a_relancer) == 1:
        main[des_a_relancer[0] - 1] = lancer_de()
    
    else:              # cas de des_a_relancer est vide(sans aucune valeur)
        return main
    return main
