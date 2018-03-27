import config
import ecc
import random
import hashlib

def gen_cle(curve):
    cle_pri = random.randint(1, config.l-1)
    cle_pub = ecc.Curve.mul(curve, cle_pri, config.P)
    return cle_pri, cle_pub


def Signature_Alice(curve):
    u = 0
    v = 0
    cle_pri, cle_pub = gen_cle(curve)

    m="Salut!"
    hashe = hashlib.sha256(m.encode()).hexdigest()
    hash_int = int(hashe, 16)
    while u == 0 or v == 0:
        k = random.randint(1, config.l-1)
        kP = ecc.Curve.mul(curve, k, config.P)
        print("kP: ", kP)
        u = (kP.x) % config.l
        v_sans_inv = ((hash_int + (cle_pri * u)))
        v = ecc.inv(v_sans_inv, config.l)
        print(v)
    return m,u,v,cle_pub


def Verif_signature(curve):
    m,u,v,Q = Signature_Alice(curve)
    if (u > 1) and (u < config.l-1) and (v > 1) and (v < config.l-1):
        hashe = hashlib.sha256(m.encode()).hexdigest()
        hash_int = int(hashe, 16)
        v_inv = ecc.inv(v, config.l)
        part1 = ((hash_int*(v_inv)))%config.l
        part2 = (u*(v_inv))%config.l
        print("Part1 et Part2 calculé")
        part1_add = ecc.Curve.mul(curve, part1, config.P)
        part2_add = ecc.Curve.mul(curve, part2, Q)
        print("Part1_add et Part2_add calculé")
        point = ecc.Curve.add(curve, part1_add, part2_add)
        print("point calculé")
        print(point)
        x = point.x%config.l
        print(u==x)
        if (u == point.x % config.l):
            print("u = x[n]")
            if (Q!=0):
                print("q != 0")
                if (ecc.Curve.isOn(curve, Q)):
                    print("Q isON")
                    if (ecc.Curve.mul(curve, config.l, Q)==0):
                        print("Le message vient bien de Alice!")

curve = ecc.Curve(config.A, config.B, config.N)
print(Verif_signature(curve))