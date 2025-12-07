from noyau import *

def choisir_des_a_relancer():
    """
    Entrée: aucune
    Sortie: liste des positions des dés à relancer 
    But: demander au joueur quels dés il souhaite relancer
    """
    des_a_relancer = []
    n = int(input("Combien de dés voulez-vous relancer (0 si vous ne souhaitez ne rien relancer)?"))
    while n > 3:
        n = int(input("Veuillez saisir le nombre de dés à relancer (3 au maximum) !"))
    if n == 3:
        des_a_relancer = [1, 2, 3]
    elif n == 2:
        while des_a_relancer[0] not in [1, 2, 3] or des_a_relancer[1] not in [1, 2, 3] or len(des_a_relancer) != 2:
            des_a_relancer.append(int(input("Quel est le premier dé que vous voulez relancer (indiquez la position du dé à relancer (première position : 1)) ?")))
            des_a_relancer.append(int(input("Quel est le second dé que vous voulez relancer (indiquez la position du dé à relancer (première position : 1)) ?")))   
    elif n == 1:
        while des_a_relancer[0] not in [1, 2, 3] or len(des_a_relancer) != 1:
            des_a_relancer.append(int(input("Quel dé souhaitez vous relancer (indiquez la position du dé à relancer (première position : 1)) ?")))
    else:
        des_a_relancer = []
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
