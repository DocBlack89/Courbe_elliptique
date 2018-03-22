import config
import random
import ecc


def Alice(curve):
    a = random.randint(0, config.l-1,)
    A = ecc.Curve.mul(curve, a, config.P)
    B = Bob(curve, A)
    aB = ecc.Curve.mul(curve, a, B)
    return aB


def Bob(curve, A):
    b = random.randint(0, config.l-1,)
    B = ecc.Curve.mul(curve, b, config.P)
    bA = ecc.Curve.mul(curve, b, A)
    return B
