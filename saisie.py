from noyau import *

def choisir_des_a_relancer():
    des_à_relancer = []
    n = int(input("Combien de dés voulez-vous relancer ?"))
    while n > 3:
        n = int(input("Veuillez saisir le nombre de dés à relancer (3 au maximum) !"))
    if n == 3:
        des_à_relancer = [1, 2, 3]
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
        m = lancer_de()
        main[des_à_relancer[0] - 1] = m
        n = lancer_de()
        main[des_à_relancer[1] - 1] = n

    else:
        y = lancer_de()
        main[des_à_relancer[0] - 1] = y

    return main

main = relancer_main([3,2,1], [2])
print(main)