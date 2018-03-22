#!/usr/bin/python3

import ecc
import config
import diffie_hellman
import chiffrement
import sys


def menu():
    '''
    Menu permettant de choisir ce que l'on souhaite faire
    '''
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
    print("6- Création courbe, multiplication de deux points, doublement de P, addition de deux points")
    print("7- Diffie-Hellman")
    print("8- Chiffrement")
    print("9- Quitter")
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
        addition_points()
    if (choix == 6):
        tout()
    if (choix == 7):
        DH()
    if (choix == 8):
        envoie_message()
    if (choix == 9):
        sys.exit()


def creation_courbe():
    '''
    Crée une courbe elliptique
    '''
    curve = ecc.Curve(config.A, config.B, config.N)
    return curve


def multiplication_point():
    '''
    Multiplie deux point sur une courbe
    '''
    curve = creation_courbe()
    mul = ecc.Curve.mul(curve, config.n, config.P)
    print(mul)


def doublement_point():
    '''
    Double un point sur une courbe
    '''
    curve = creation_courbe()
    dbl = ecc.Curve.mul(curve, 2, config.P)
    print(dbl)


def verif_presence():
    '''
    Vérifie la présence d'un point sur la courbe
    '''
    curve = creation_courbe()
    isOn = ecc.Curve.isOn(curve, config.M)
    print(isOn)


def addition_points():
    '''
    Additionne deux points sur la courbe
    '''
    curve = creation_courbe()
    add = ecc.Curve.add(curve, config.P, config.Q)
    print(add)


def tout():
    '''
    Crée une courbe elliptique
    Multiplie deux point sur une courbe
    Double un point sur une courbe
    Vérifie la présence d'un point sur la courbe
    Additionne deux points sur la courbe
    '''
    curve = ecc.Curve(config.A, config.B, config.N)
    isOnP = ecc.Curve.isOn(curve, config.P)
    add = ecc.Curve.add(curve, config.P, config.Q)
    mul = ecc.Curve.mul(curve, config.n, config.Q)
    dbl = ecc.Curve.mul(curve, 2, config.P)

    print(curve)
    print(add)
    print(mul)
    print(isOnP)
    print(dbl)


def DH():
    '''
    Effectue un échange Diffie-Hellman entre Bob et Alice
    '''
    curve = ecc.Curve(config.A, config.B, config.N)
    Alice = diffie_hellman.Alice(curve)
    print(Alice)


def envoie_message():
    '''
    Simule l'envoie d'un message chiffré par la courbe elliptique
    '''
    curve = ecc.Curve(config.A, config.B, config.N)
    M = chiffrement.dechiffrement_Alice(curve)
    print(M)


while 1:
    menu()
