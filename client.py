#!/usr/bin/python3

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
    print("Valeur de A")
    A = int(input())
    print("Valeur de B")
    B = int(input())
    print("Ordre de la courbe")
    N = int(input())
    curve = ecc.Curve(A, B, N)
    return curve

def multiplication_point():
    curve = creation_courbe()
    print("Valeur du point")
    P = int(input())
    print("Nombre de multiplication")
    n = int(input())
    mul = ecc.Curve.mul(curve, n, P)
    print(mul)

def doublement_point():
    curve = creation_courbe()
    print("Valeur du point")
    P = int(input())
    dbl = ecc.Curve.mul(curve, 2, P)
    print(dbl)

def verif_presence():
    curve = creation_courbe()
    print("Valeur du point")
    P = int(input())
    isOn = ecc.Curve.isOn(curve, P)
    print(isOn)

def addition_points():
    curve = creation_courbe()
    print("Valeur du point P")
    P = int(input())
    print("Valeur du point Q")
    Q = int(input())
    add = ecc.Curve.add(curve, P, Q)
    print(add)

def inverse_points():
    print("Valeur de l'ordre de la courbe")
    N = int(input())
    print("Valeur du point P")
    P = int(input())
    inv = ecc.inv(N, P)
    print(inv)

def tout():
    print("Valeur du point A")
    A = int(input())
    print("Valeur du point B")
    B = int(input())
    print("Valeur du point P")
    P = int(input())
    print("Valeur du point Q")
    Q = int(input())
    print("Nombre de multiplication")
    n = int(input())
    print("Valeur de l'ordre de la courbe")
    N = int(input())
    curve = ecc.Curve(A, B, N)
    isOnP = ecc.Curve.isOn(curve, P)
    isOnQ = ecc.Curve.isOn(curve, P)
    add = ecc.Curve.add(curve, P, Q)
    mul = ecc.Curve.mul(curve, n, Q)
    dbl = ecc.Curve.mul(curve, 2, Q)
    inv = ecc.inv(N, P)

    print(curve)
    print(add)
    print(mul)
    print(isOnP)
    print(isOnQ)
    print(dbl)
    print(inv)

menu()