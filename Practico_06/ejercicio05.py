# -*- coding: utf-8 -*-

import random
import math


def generarPI():
    PI = 0
    U = random.random() # U ~ U(0, 1)
    V = random.random() # V ~ U(0, 1)
    X = 2*U - 1 # X ~ U(-1, 1)
    Y = 2*V - 1 # Y ~ U(-1, 1)

    # Punto cae adentro del circulo de radio 1
    if X**2 + Y**2 <= 1:
        PI += 1

    PI = 4 * PI # Puede ser 0 o 4

    return PI


def estimacion01():
    """
    Ejercicio 5.
    """
    n = 30 # Minimo numero de simulaciones
    N = n # Observaciones Realizadas
    X = generarPI()
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = generarPI()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    j = n
    # Iteramos hasta que el ancho de IC sea < 0.1
    while True:
        N += 1
        j += 1
        X = generarPI()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

        S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral

        IC = (M - 1.96*(S/math.sqrt(j)) , M + 1.96*(S/math.sqrt(j)))

        # Si el ancho del IC < 0.1 cortamos el bucle
        if IC[1] - IC[0] < 0.1:
            break

    ancho_IC = IC[1] - IC[0] # Ancho del intervalo

    return IC, ancho_IC, N


def estimacion02():
    """
    Ejercicio 5.
    """
    n = 30 # Minimo numero de simulaciones
    N = n # Observaciones Realizadas
    X = generarPI()
    M = X # Media Muestral (valor inicial: M(1) = X1)
    S_cuadrado = 0 # Varianza Muestral (valor inicial: S_cuadrado(1) = 0)
    # Calculamos M(n) y  S_cuadrado(n)
    for j in xrange(2, n+1):
        X = generarPI()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    j = n
    # Iteramos hasta que el ancho de IC sea < 0.1
    # Parar cuando: 2 * z(alfa/2) * S(k)/raiz(n) <= d --> calcular S(k) en cada paso
    while 2 * 1.96 * math.sqrt(S_cuadrado/float(j)) >= 0.1:
        N += 1
        j += 1
        X = generarPI()
        A = M
        M += (X - M)/float(j)
        S_cuadrado = (1 - 1.0/(j-1))*S_cuadrado + j*((M-A)**2)

    S = math.sqrt(S_cuadrado) # Desviacion Estandar Muestral

    IC = (M - 1.96*(S/math.sqrt(j)) , M + 1.96*(S/math.sqrt(j)))

    ancho_IC = IC[1] - IC[0] # Ancho del intervalo

    return IC, ancho_IC, N

# IC = (Xbarra - Z_alfa/2 * (S/sqrt(n)), Xbarra + Z_alfa/2 * (S/sqrt(n)))

# Longitud
# 2 * Z_alfa/2 * S/sqrt(n)

# Longitud de a lo sumo d
# 2 * Z_alfa/2 * S/sqrt(n) <= d


def printEstimacion01():
    IC, ancho_IC, N = estimacion01()
    print("\nIntervalo de Confianza =", IC)
    print("Ancho de IC =", ancho_IC)
    print("Ejecuciones necesarias =", N)
    print("")


def printEstimacion02():
    IC, ancho_IC, N = estimacion02()
    print("\nIntervalo de Confianza =", IC)
    print("Ancho de IC =", ancho_IC)
    print("Ejecuciones necesarias =", N)
    print("")


printEstimacion01()
printEstimacion02()
