#!/usr/bin/python3

import config
import ecc

curve = ecc.Curve(config.A, config.B, config.N)
isOn = ecc.Curve.isOn(config.P)
add = ecc.Curve.add(config.P, config.Q)
mul = ecc.Curve.mul(config.N, config.P)
print(curve)