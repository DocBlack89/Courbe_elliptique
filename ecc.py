# coding: utf-8

import random()
import config
"""
Ce qui est fait:
    - Initialisation variable globale (fichier config.py)
    - vérifier l'appartenance du point à la courbe
    - Calcul de la somme de deux points
    - Calcul de n.P
    - Doublement d'un point (fait dans la fonction add)
    - Calcul de l'opposé d'un point (fais dans la fonction inverse)
Ce qu'il reste entièrement à faire :
    - méthode simulant l'échange Diffie-Hellman
    - méthode simulant l'envoie de message
    - correction du code pour être en accord avec PEP8
"""


def inv(x, n):
    """
    Calcul de l'inverse
    """
    assert n > 0

    n_tmp = n
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, x, n = x // n, n, x % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0 % n_tmp


class Point:
    """
    Class point, represente un point sur la courbe
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isInf(self):
        return False

    def __str__(self):
        if self.isInf():
            return "O"
        else:
            return "(%d,%d)" % (self.x, self.y)

    def copy(self):
        if self.isInf():
            return PointInf()
        else:
            return Point(self.x, self.y)

    def isEqual(self, p):
        return self.x == p.x and self.y == p.y


class PointInf(Point):
    """
    Le point a l'infini
    """
    def __init__(self):
        Point.__init__(self, None, None)

    def isInf(self):
        return True


class Curve:
    def __init__(self, a, b, p):
        """
        Le constructeur de la courbe
        """
        assert a > 0
        assert b > 0
        assert p > 0

        self.a = a
        self.b = b
        self.p = p

    def isOn(self, p):
        """
        Vérifier si le point est bien sur la courbe
        """
        if p.isInf():
            return True

        y_square = (p.x**3 + self.a*p.x + self.b) % self.p
        return y_square == p.y**2 % self.p

    def add(self, p, q):
        """
        Somme des deux points
        """
        assert self.isOn(p)
        assert self.isOn(q)

        if p.isInf():
            return q.copy()
        if q.isInf():
            return p.copy()

        if p.x == q.x and p.y == -q.y % self.p:
            return PointInf()

        l = 0

        if p.x != q.x or p.y != q.y:
            a = (q.y - p.y) % self.p
            b = (q.x - p.x) % self.p
            l = (a*inv(b, self.p)) % self.p
        else:
            a = (3*(p.x**2) + self.a) % self.p
            b = (2*p.y) % self.p
            l = (a*inv(b, self.p)) % self.p

        x3 = (l**2 - p.x - q.x) % self.p
        y3 = (l*(p.x - x3) - p.y) % self.p

        return Point(x3, y3)

    def mul(self, n, p):
        """
        Calcul de n.P (exponentiation rapide)
        """
        assert n >= 0
        assert self.isOn(p)

        Q = p.copy()
        R = PointInf()

        while n > 0:
            if n % 2 == 1:
                R = self.add(R, Q)
            Q = self.add(Q, Q)

            n //= 2
        return R

    def __str__(self):
        return "Y^2 = X^3 + (%d)X + (%d) (mod %d)" % (self.a, self.b, self.p)

<<<<<<< HEAD
    def generation_A(self):
        a = random.randint(0, config.l-1,)
        A = self.mul(a, config.P)
        return a, A

    def generation_B(self):
        b = random.randint(0, config.l-1,)
        B = self.mul(b, config.P)
        return b, B
    
    def Alice(self):
        print("récupération de B")
        a, A = self.generation_A()
        b, B = self.generation_B()
        aB =  self.mul(a, B)
        return aB

    def Bob(self):
        print("récupération de A")
        a, A = self.generation_A()
        b, B = self.generation_B()
        bA = self.mul(b, A)
        return bA
=======

class Diffie_Hellman:
    def Alice():
        a = random.randint(0, config.l-1,)
        A = mul(a, config.P)
    def Bob():
        b = random.randint(0, config.l-1,)
        print(b)
>>>>>>> parent of ef466a2... fin séance
