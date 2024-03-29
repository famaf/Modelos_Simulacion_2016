# -*- coding: utf-8 -*-

import random
import math


def aproximacion(n):
    """
    Ejercicio 4a.
    """
    a = 0 # Acumulador de la suma de N's tq' min{ N : Sn > 1 }
    for i in xrange(n):
        N = 0 # min { N : Sn > 1}
        s = 0 # Sn

        # Si Sn <= 1 entonces sumamos otro numero aleatorio
        # y aumentamos el N
        while s <= 1.0:
            s += random.random()
            N += 1

        a += N

    return float(a)/n


# def aproximacion(n):
#     """
#     Ejercicio 4a.
#     Version optimizada.
#     """
#     a = 0 # Acumulador de la suma de n tq' min{ n : Sn > 1 }
#     for i in xrange(n):
#         N = 2 # Es el n tq' min{ n : Sn > 1 } el min n que lo cumple es 2
#         s = random.random() + random.random()

#         # Si s es menor a 1 => sumamos un nuevo numero aleatorio y
#         # actualizamos el n tq' min{ n : Sn > 1 }
#         while s <= 1.0:
#             s += random.random()
#             N += 1

#         a += N

#     return float(a)/n

for n in [100, 1000, 10000, 100000, 1000000]:
    print("n =", n,  "--> e =", aproximacion(n))
