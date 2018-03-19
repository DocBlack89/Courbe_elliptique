#!/usr/bin/python3

import ecc
import config

def menu():
    print("############################")
    print("#                          #")
    print("#  Ceci n'est pas un menu  #")
    print("#                          #")
    print("############################")
    print("1- Création de la courbe")
    print("2- Multiplication de deux points")
    print("3- Doublement d'un point")
    print("4- Vérification de la présence du point sur la courbe")
    print("5- Addition de deux points")
    print("6- Calcul de l'inverse")
    print("7- Tout")
    choix = int(input("Votre choix : "))
    if (choix == 1):
        print(creation_courbe())
    if (choix == 2):
        multiplication_point()
    if (choix == 3):
        doublement_point()
    if (choix == 4):
        verif_presence()
    if (choix == 5):
        addition_points
    if (choix == 6):
        inverse_points()
    if (choix == 7):
        tout()

def creation_courbe():
    curve = ecc.Curve(config.A, config.B, config.N)
    return curve

def multiplication_point():
    curve = creation_courbe()
    mul = ecc.Curve.mul(curve, config.n, config.P)
    print(mul)

def doublement_point():
    curve = creation_courbe()
    dbl = ecc.Curve.mul(curve, 2, config.P)
    print(dbl)

def verif_presence():
    curve = creation_courbe()
    isOn = ecc.Curve.isOn(curve, config.P)
    print(isOn)

def addition_points():
    curve = creation_courbe()
    add = ecc.Curve.add(curve, config.P, config.Q)
    print(add)

def inverse_points():
    inv = ecc.inv(config.N, config.P)
    print(inv)

def tout():
    curve = ecc.Curve(config.A, config.B, config.N)
    isOnP = ecc.Curve.isOn(curve, config.P)
    isOnQ = ecc.Curve.isOn(curve, config.P)
    add = ecc.Curve.add(curve, config.P, config.Q)
    mul = ecc.Curve.mul(curve, config.n, config.Q)
    dbl = ecc.Curve.mul(curve, 2, config.Q)
    #inv = ecc.inv(config.N, config.P)

    print(curve)
    print(add)
    print(mul)
    print(isOnP)
    print(isOnQ)
    print(dbl)
    #print(inv)


<<<<<<< HEAD
while 1:
    menu()
=======
menu()
>>>>>>> 3ad70e6b0953c18c43b57ed2e0af03ecb761a610
