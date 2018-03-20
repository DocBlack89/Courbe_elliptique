#!/usr/bin/python3
# -*- encoding:utf-8

import random

def euclide(a, b):
    """ 
    Algorithme d'Euclide étendu 

    @type  a: number
    @param a: Dividende
    @type  b: number
    @param b: Diviseur

    
    @rtype: tuple
    @return: ...
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = euclide(b % a, a)
        return (g, x - (b // a) * y, y)

def invMod(a,n):
    """ 
    Renvoie l'inverse modulaire d'un nombre par rapport à un autre.

    @type  a: number
    @param a: Nombre dont on cherche l'inverse
    @type  n: number
    @param n: Modulo appliqué

    @raise Exception: Lève une exception si l'inverse modulaire n'existe pas.

    @rtype: number
    @return: Inverse modulaire de a par n
    """
    g, x, y = euclide(a, n)
    if g != 1:
        raise Exception("L'inverse modulaire demandé n'existe pas")
    else:
        return x % n


class Courbe:
    """ Courbe Elliptique """
    
    def __init__(self,a,b,P,p):
        """ 
        Constructeur de la classe Courbe Elliptique.

        @type  a: number
        @param a: Coefficient a de la courbe
        @type  b: number
        @param b: Coefficient b de la courbe
        @type  P: tuple
        @param P: Point P de la courbe
        @type  p: number 
        @param p: Paramètre du corps Fp
        """
        self.a = a
        self.b = b
        self.P = P
        self.p = p

    def isPtInf(self,Pt):
        """ 
        Renvoie True si le point passé en paramètre est le point à l'infini

        @type  Pt: tuple
        @param Pt: Point à tester
        
        @rtype: boolean
        @return: Renvoie True si le point passé en paramètre est le point à l'infini
        """
        return Pt[0] == None and Pt[1] == None

    def appartient(self,Pt):
        """
        Détermine si un point Pt appartient ou non à la courbe.

        @type  Pt: tuple
        @param Pt: Point à vérifier
        
        @rtype:   boolean
        @return:  Etat du point par rapport à la courbe
        """
        if Pt[0] is None and Pt[1] is None: # Point à l'infini
            return True
        return (Pt[1]**2)%self.p == (Pt[0]**3+self.a*Pt[0]+self.b)%self.p
        
    def sommePoints(self,Pt1,Pt2):
        """
        Renvoie l'addition de deux point sur la courbe.
        Lève une exception si les points ne sont pas sur la courbe.
        
        @type  Pt1: tuple
        @param Pt1: Point 1 à additionner
        @type  Pt2: tuple
        @param Pt2: Point 2 à additionner

        @raise Exception: Lève une exception si un point n'est pas sur la courbe.
        @raise Exception: Lève une exception si l'inverse modulaire n'existe pas.

        @rtype:  tuple
        @return: Point sur la courbe, résultat de l'addition
        """

        x1 = Pt1[0]
        x2 = Pt2[0]
        y1 = Pt1[1]
        y2 = Pt2[1]

        if not self.appartient(Pt1):
            raise Exception("Le point Pt1 n'est pas sur la courbe")
        if not self.appartient(Pt2):
            raise Exception("Le point Pt2 n'est pas sur la courbe")
  
        # Gestion des points à l'infini
        if self.isPtInf(Pt1):
            x3 = x2
            y3 = y2
        elif self.isPtInf(Pt2):
            x3 = x1
            y3 = y1
        else:
            if x1 == x2 and y1 == y2: # 2P
                if y1 == 0: # 2P = 0 (point à l'infini)
                    x3,y3 = None,None
                else:
                    l = (3*(x1**2)+self.a)*invMod((2*y1)%self.p,self.p) # Lambda
                    x3 = l**2-2*x1
                    y3 = l*(x1-x3)-y1
            else: # P + Q
                if x1 == x2: # x1 = x2 , P + Q = 0 (point à l'infini)
                    x3,y3 = None,None
                else:
                    l = (y2-y1) * invMod((x2-x1)%self.p,self.p)
                    x3 = l**2-x1-x2
                    y3 = l*(x1-x3)-y1
        if(x3 is not None):
            x3 = x3%self.p
        if(y3 is not None):
            y3 = y3%self.p
        return (x3,y3)
    
    def doublementPoints(self,Pt):
        """
        Renvoie l'addition d'un point avec lui-même sur la courbe.
        Lève une exception si le point n'est pas sur la courbe.
        
        @type  Pt: tuple
        @param Pt: Point additionner avec lui-même

        @raise Exception: Lève une exception si un point n'est pas sur la courbe.
        @raise Exception: Lève une exception si l'inverse modulaire n'existe pas.

        @rtype:  tuple
        @return: Point sur la courbe, résultat de l'addition
        """
        return self.sommePoints(Pt,Pt)
        
    def opposePoint(self,Pt):
        """
        Renvoie l'opposé d'un point.
        
        @type  Pt: tuple
        @param Pt: Point dont on cherche l'inverse

        @rtype:  tuple
        @return: Opposé du point Pt.
        """
        if self.isPtInf(Pt):
            return Pt
        return (Pt[0],-Pt[1])

            
    def exponentiationRapide(self,n,P):
        """
        Renvoie n * P à l'aide de l'exponentiation rapide.
        
        @type  n: number
        @param n: n
        @type  P: tuple
        @param P: P

        @rtype:  number
        @return: Renvoie n * P en utilisant l'opération de la courbe.
        """
        b, m = P, n
        r = (None,None)
        while m > 0: # Tant qu'il faut ajouter
            if m % 2 == 1: # M impaire
                r = self.sommePoints(r,b) 
            b = self.doublementPoints(b)
            m = m //2
        return r 

class chiffrement:
    """ Classe de chiffrement pour les courbes elliptiques """
    
    def __init__(self,c):
        """ 
        Constructeur de la classe de test.

        @type  c: Courbe
        @param c: Courbe à utiliser pour le chiffrement et déchiffrement
        """
        self.courbe = c

    def chiffrer(self,m,P):
        """
        Chiffre un message m avec le point secret P et la courbe élliptique définie.

        @type  m: tuple
        @param m: Point à chiffrer

        @type  P: tuple
        @param P: Point "secret" utilisé lors du chiffrement.

        @rtype:  tuple
        @return: Renvoie la somme des points m et P.
        """
        return self.courbe.sommePoints(m,P)

    def dechiffrer(self,m,P):
        """
        Dechiffre un message m avec le point secret P et la courbe élliptique définie.

        @type  m: tuple
        @param m: Point à chiffrer

        @type  P: tuple
        @param P: Point "secret" utilisé lors du chiffrement.

        @rtype:  tuple
        @return: Renvoie la somme des points m et l'opposé de P.
        """
        return self.courbe.sommePoints(m,self.courbe.opposePoint(P))


class diffieHellmanEC:
    """ Classe pour Diffie Hellman sur Courbe ELliptique """
    
    def __init__(self,a,b,P,p):
        """ 
        Constructeur de la classe diffieHellmanEC.

        @type  a: number
        @param a: Coefficient a de la courbe

        @type  b: number
        @param b: Coefficient b de la courbe

        @type  P: number
        @param P: Point "générateur" de la courbe.

        @type  p: number
        @param p: Taille du corp de la courbe.
        """
        self.a = a
        self.b = b
        self.P = P
        self.p = p
        self.courbe = Courbe(a,b,P,p)
        self.chiffrement = chiffrement(self.courbe)
    
    def generateRandP(self):
        """ 
        Génère un point aléatoire à partir du point de départ et stock le 
        coefficient multiplicateur dans r.

        Utilise SystemRandom pour utilisation cryptographique, en accord avec
        la documentation :
        
        https://docs.python.org/2/library/random.html#random.SystemRandom

        @rtype:  tuple
        @return: Renvoie un point aléatoire sur la courbe.
        """
        self.r = random.SystemRandom().randint(1,self.p-1) #  is secure
        f = self.P
        for i in range(1,self.r):
            f = self.courbe.sommePoints(f,self.P)
        return f
    
    def generateRandInt(self):
        """ 
        Génère un nombre aléatoir.

        Utilise SystemRandom pour utilisation cryptographique, en accord avec
        la documentation :
        
        https://docs.python.org/2/library/random.html#random.SystemRandom

        @rtype:  number
        @return: Renvoie un nombre aléatoire < à l'ordre.
        """
        return random.SystemRandom().randint(1,self.p-1)
        


###################################
# Diffie-Hellman
###################################

G = (3,4) # Point 'générateur'
DH = diffieHellmanEC(1,3,G,17) # Courbe Eliptique
a = DH.generateRandInt() # Alice génère un nombre aléatoire
b = DH.generateRandInt() # Bob génère un nombre aléatoire
print("Alice génère un aléa: "+str(a))
print("Bob génère un aléa: "+str(b))
P = DH.courbe.exponentiationRapide(a,G) # Alice génère P
Pprime =  DH.courbe.exponentiationRapide(b,G) # Bob génère P'
print("Alice calcule P: "+str(P))
print("Bob calcule P': "+str(Pprime))
Ta = DH.courbe.exponentiationRapide(a,Pprime) # Alice calcul Ta = a*Pprime
Tb = DH.courbe.exponentiationRapide(a,Pprime) # Bob calcul Tb = b*P
print("Alice et Bob calculent de leurs cotés et partagent maintenant un secret partagé:")
print("Ta = "+str(Ta))
print("Tb = "+str(Tb))



print("\n-----------------------\n")



# Chiffrement El-gamal
G = (3,4) # Point 'générateur'
DH = diffieHellmanEC(1,3,G,17) # Courbe Eliptique
dA = DH.generateRandInt() # Alice génère un nombre aléatoire
A = DH.courbe.exponentiationRapide(dA,G) # Clé publique d'Alice
print("Clé privée d'Alice: "+str(dA))
print("Clé publique d'Alice: "+str(A))

M = (6,2) # Message secret M
print("Bob veut passer le message secret M: "+str(M))
k = DH.generateRandInt() # Bob génère un nombre aléatoire
C1 = DH.courbe.exponentiationRapide(k,G)
C2 = DH.courbe.sommePoints(M,DH.courbe.exponentiationRapide(k,A))
Mprime = (C1,C2)
print("Bob calcule C1: "+str(C1)+" , C2: "+str(C2))
dAC1 = DH.courbe.exponentiationRapide(dA,Mprime[0]) # Alice calcule dAC1 = kdAP = kA
Mseconde = DH.courbe.sommePoints(Mprime[1],DH.courbe.opposePoint(dAC1))
print("Alice calcule dAC1 = kdAP = kA: "+str(dAC1))
print("Alice retrouve M: "+str(M))


