#!/usr/bin/python3

import config
import ecc

curve = ecc.Curve(config.A, config.B, config.N)
isOnP = ecc.Curve.isOn(curve, config.P)
isOnQ = ecc.Curve.isOn(curve, config.P)
add = ecc.Curve.add(curve, config.P, config.Q)
mul = ecc.Curve.mul(curve, config.n, config.Q)

print(curve)
print(add)
print(mul)
print(isOnP)
print(isOnQ)