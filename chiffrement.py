import ecc
import random
import config


def chiffrement_Alice(curve):
    da = random.randint(1, config.l-1)
    A = ecc.Curve.mul(curve, da, config.P)
    f = open("cle.txt", "w")
    f.write(str(da))
    return A


def chiffrement_Bob(curve):
    A = chiffrement_Alice(curve)
    k = random.randint(1, config.l)
    C1 = ecc.Curve.mul(curve, k, config.P)
    kA = ecc.Curve.mul(curve, k, A)
    C2 = ecc.Curve.add(curve, config.M, kA)
    return C1, C2


def dechiffrement_Alice(curve):
    C1, C2 = chiffrement_Bob(curve)
    f = open("cle.txt", "r")
    cle = int(f.read())
    daC1 = ecc.Curve.mul(curve, cle, C1)
    daC1_inv = ecc.Point(daC1.x, -daC1.y)
    M = ecc.Curve.add(curve, C2, daC1_inv)
    return M
