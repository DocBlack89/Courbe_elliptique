#!/usr/bin/python3

import config
import ecc

curve = ecc.Curve(config.A, config.B, config.N)
isOn = ecc.Curve.isOn(curve, config.P)
add = ecc.Curve.add(curve, config.P, config.Q)
mul = ecc.Curve.mul(curve, config.N, config.P)
print(curve)
print(isOn)
print(add)
print(mul)