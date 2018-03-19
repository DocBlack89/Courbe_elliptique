import ecc




def menu():
    print("######################")
    print("#  Ceci est un menu  #")
    print("######################")
    print("1- Création de la courbe")
    print("2- Multiplication de deux points")
    print("3- Doublement d'un point")
    print("4- Vérification de la présence du point sur la courbe")
    print("5- Addition de deux points")
    print("6- Calcul de l'inverse")
    print("7- Tout")
    choix = int(input("Votre choix"))
    return choix


###### Création de la courbe elliptiques #####
#A = 367894248157291519724356994675367555090991868479757
#B = 650136343866907590034711240239825334223238899223249
A = 1
B = 7

##### Ordre de la courbe elliptique ####
N = 17


##### n pour la multiplication ####
n = 2

##### Point de la courbe elliptique #####
#P = ecc.Point(11370152050562514760725829841636301722527983698782725, 7252135185890240681446231840366738239134349061512895)
#Q = ecc.Point(11370152050562514760725829841636301722527983698782725, 7252135185890240681446231840366738239134349061512895)
P = ecc.Point(6, 5)
Q = ecc.Point(2, 0)


menu()