# -*- coding: utf-8 -*-

import random
import math


def esperanza(n):
    """
    Esperanza con la Ley de los Grandes Numeros.
    """
    exito = 0 # Veces que la carta-i == i

    for _ in xrange(n):
        mazo = range(1, 101) # Lista de 100 cartas
        random.shuffle(mazo) # Desordena el mazo
        # Chequeo todo el mazo para ver si hay algun 'exito', de ser asi lo
        # lo sumamos.
        exito += sum([mazo[i-1]==i for i in xrange(1, 101)])

    return float(exito)/n


def varianza(n):
    """
    Varianza en base a la esperanza.
    """
    suma1 = 0
    suma2 = 0

    for _ in xrange(n):
        mazo = range(1, 101) # Lista de 100 cartas
        random.shuffle(mazo) # Desordena el mazo
        # Chequeo todo el mazo para ver si hay algun 'exito', de ser asi lo
        # lo sumamos.
        exito = sum([mazo[i-1]==i for i in xrange(1, 101)])

        suma1 += exito # x
        suma2 += exito**2 # x^2

    varianza = suma2/float(n) - (suma1/float(n))**2 # V(x) = E(x^2) - E(x)^2

    return varianza


for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> E(X) =", esperanza(n))

print("--------------------------------")

for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> V(X) =", varianza(n))
