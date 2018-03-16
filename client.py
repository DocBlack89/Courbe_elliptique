#!/usr/bin/python3

from common import *
import config
import ecc


def get_flag(sock, key):
    data = recvmsg(sock)
    while data != None:
        plain = decrypt(key, data).decode('utf-8')
        print(plain)

        data = recvmsg(sock)

sock = connect_to_serv(config.HOST, config.PORT)
curve = ecc.Curve(config.A, config.B, config.N)
key = key_exchange(sock, curve, config.P)
aes_key = gen_aes_key(key.x)

get_flag(sock, aes_key)
