#!/usr/bin/python3

import config
import ecc


choix = config.menu()

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
    isOnP = ecc.Curve.isOn(curve, config.P)
    isOnQ = ecc.Curve.isOn(curve, config.P)
    add = ecc.Curve.add(curve, config.P, config.Q)
    mul = ecc.Curve.mul(curve, config.n, config.Q)
    dbl = ecc.Curve.mul(curve, 2, config.Q)
    inv = ecc.inv(config.N, config.P)

    print(curve)
    print(add)
    print(mul)
    print(isOnP)
    print(isOnQ)
    print(dbl)
    print(inv)