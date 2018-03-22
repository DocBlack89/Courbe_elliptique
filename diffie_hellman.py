import config
import random
import ecc


def Alice(curve):
    '''
    La fonction random n'est pas conseillée en cryptographie
    la fonction retourne la clé secrête générée par Diffie-Hellman entre Alice et Bob
    '''
    a = random.randint(0, config.l-1,)
    A = ecc.Curve.mul(curve, a, config.P)
    B = Bob(curve, A)
    aB = ecc.Curve.mul(curve, a, B)
    return aB


def Bob(curve, A):
    '''
    La fonction random n'est pas conseillée en cryptographie
    La fonction envoie B à Alice pour le calcul de la clé secrête
    Elle calcul également le clé secrête
    '''
    b = random.randint(0, config.l-1,)
    B = ecc.Curve.mul(curve, b, config.P)
    bA = ecc.Curve.mul(curve, b, A)
    return B
