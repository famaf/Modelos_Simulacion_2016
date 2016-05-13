# -*- coding: utf-8 -*-

import random
import math


def calculoPromedio(lista):
    sumatoria = sum(lista)

    return sumatoria/float(len(lista))


def bootstrap(B, n, muestra):
    """
    Ejericicio 6 b.
    B = numero de sorteos.
    n = tamaño de la muestra.
    muestra = lista con los datos de la muestra.
    """
    a, b = -5, 5 # Limites
    
    exitos = 0 # Cantidad de veces que: a < v < b

    suma = 0
    for x in muestra:
        suma += x

    media_muestral = suma/float(n) # Media muestral de la muetra dada (X barra)

    # Hacemos el sorteo para B muestras aleatorias
    for _ in xrange(B):
        temporal = [] # Lista que contiene elementos de la muestra aplicando Bootstrap

        # Seleccionamos de forma aleatoria 10 elementos de la muestra
        # (se puede repetir) para el calculo de la expresion correspondiente
        for _ in xrange(n):
            elemento = muestra[random.randint(0, 9)]
            temporal.append(elemento)

        v = calculoPromedio(temporal) - media_muestral # Calculamos la expresion

        # Si a < v < b ==> tenemos un exito
        if v > a and v < b:
            exitos += 1

    # La probabilidad esta dada las veces que se cumple la condicion sobre
    # las veces que se realizo
    p = exitos/float(B)

    return p



muestra = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69] # Valores de la muetra obtenida

for B in [100, 1000, 10000, 100000, 1000000]:
    # Si B = 1000000 ---> p = 0.761043
    print "B =", B, "---> p =", bootstrap(B, 10, muestra)
