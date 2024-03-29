# -*- coding: utf-8 -*-

import random
import math
import matplotlib.pyplot as plt


INFINITO = float("inf") # Constante Infinito


def exponencial(lamda):
    """
    Genera una v.a. X con distribucion Exponencial de parametro lamda.
    Usando el Metodo de Transformada Inversa.
    X ~ Exponencial(lamda).
    """
    u = random.random()
    x = -(1/float(lamda))*math.log(u)

    return x


def devolverLambda(esperanza):
    """
    Devuelve el lambda correspondiente segun la esperanza ingresada.
    """
    lamda = 1/float(esperanza)

    return lamda


def lavadero01(N, S, Tf, Tr):
    """
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """
    lamda_falla = devolverLambda(Tf) # Lambda de los tiempos de falla
    lamda_reparacion = devolverLambda(Tr) # Lambda de los tiempos de reparacion

    T = 0 # Tiempo en que falla el sistema
    t = 0 # Variable de tiempo
    r = 0 # Numero de Lavadoras rotas en el instante t

    t_estrella = INFINITO # Tiempo en el que la Lavadora en reparacion vuelve a funcionar

    lavadoras = [] # Lista de tiempos de falla de las Lavadoras

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        lavadoras.append(F)

    lavadoras.sort() # Ordenamos los tiempos de falla de las Lavadoras

    while True:
        # Lavadora falla antes de que se repare alguna
        if lavadoras[0] < t_estrella:
            t = lavadoras[0]
            r += 1 # Se rompio una Lavadora
            # Si hay mas de S Lavadoras descompuestas (no hay repuestos)
            if r == S+1:
                T = t
                break
            # Hay Lavadoras de repuesto para reponer. Se agrega la Lavadora de repuesto, ya que fallo alguna
            if r < S+1:
                X = exponencial(lamda_falla) # Tiempo hasta fallar de la lavadora de repuesto
                lavadoras.pop(0) # Quitamos la Lavadora que fallo
                lavadoras.append(t+X) # Agregamos la nueva Lavadora al sistema (tiempo actual + tiempo de falla)
                lavadoras.sort() # Ordenamos los tiempos en que fallan las Lavadoras
            # La Lavadora rota es la unica descompuesta, entonces se comienza a reparar
            if r == 1:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Lavadora rota
                t_estrella = t + Y # Tiempo en que concluira la reparacion de la Lavadora rota

        # Lavadora que estaba en reparacion, esta disponible
        elif lavadoras[0] >= t_estrella:
            t = t_estrella
            r -= 1 # Se reparo la Lavadora que estaba rota
            # Hay una o mas Lavadoras para Reparar
            if r > 0:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Lavadora rota
                t_estrella = t + Y # Tiempo en que concluira la reparacion de la Lavadora rota
            # No hay Lavadoras que Reparar
            if r == 0:
                t_estrella = INFINITO # Tecnico no tiene nada que reparar

    return T


def lavadero02(N, S, Tf, Tr):
    """
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """

    lamda_falla = devolverLambda(Tf) # Lambda de los tiempos de falla
    lamda_reparacion = devolverLambda(Tr) # Lambda de los tiempos de reparacion

    T = 0 # Tiempo en que falla el sistema
    t = 0 # Variable de tiempo
    r = 0 # Numero de Lavadoras rotas en el instante t

    t_estrella = [INFINITO, INFINITO] # Tiempo en el que las Lavadoras en reparacion vuelve a funcionar

    lavadoras = [] # Lista de tiempos de falla de las Lavadoras

    # Generamos N tiempos de falla (uno para cada maquina)
    for _ in xrange(N):
        F = exponencial(lamda_falla) # Tiempo hasta Fallar
        lavadoras.append(F)

    lavadoras.sort() # Ordenamos los tiempos

    while True:
        # Lavadora falla antes de que se repare alguna
        if lavadoras[0] < t_estrella[0]:
            t = lavadoras[0]
            r += 1 # Se rompio una Lavadora
            # Si hay mas de S Lavadoras descompuestas (no hay repuestos)
            if r == S+1:
                T = t
                break
            # Hay Lavadoras de repuesto para reponer. Se agrega la Lavadora de repuesto, ya que fallo alguna
            if r < S+1:
                X = exponencial(lamda_falla) # Tiempo hasta fallar de la lavadora de repuesto
                lavadoras.pop(0) # Quitamos la Lavadora que fallo
                lavadoras.append(t+X) # Agregamos la nueva Lavadora al sistema (tiempo actual + tiempo de falla)
                lavadoras.sort() # Ordenamos los tiempos en que fallan las Lavadoras
            # Primera Lavadora rota, entonces se comienza a reparar
            if r == 1:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Primera Lavadora rota
                t_estrella[0] = t + Y # Tiempo en que concluira la reparacion de la Primera Lavadora rota
            # Segunda Lavadora rota, entonces se comienza a reparar
            if r == 2:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Segunda Lavadora rota
                t_estrella[1] = t + Y # Tiempo en que concluira la reparacion de la Segunda Lavadora rota

            t_estrella.sort() # Ordenamos los tiempos de reparacion en orden decreciente (para ver quien tarda menos)

        # Lavadora que estaba en reparacion, esta disponible
        elif lavadoras[0] >= t_estrella[0]:
            t = t_estrella[0]
            r -= 1 # Se reparo una maquina
            # Hay 2 o + Lavadoras para Reparar
            if r > 1:
                Y = exponencial(lamda_reparacion) # Tiempo de reparacion de la Lavadora para reparar
                t_estrella[0] = t + Y # Tiempo en que concluira la reparacion de la Lavadora rota
                                      # Se la damos al Tecnico que termino primero de reparar
            # Hay 1 o 0 Lavadoras para reparar
            elif r <= 1:
                t_estrella[0] = INFINITO # Tecnico queda no tiene nada que reparar
                                         # El otro Tecnico esta reparando la lavadora

            t_estrella.sort() # Ordenamos los tiempos de reparacion en orden decreciente (para ver quien tarda menos)

    return T


def esperanzaYVarianza(lavadero, N, S, Tf, Tr, n):
    """
    Esperanza y Varianza del Tiempo de Fallo del Sistema del Lavadero.
    N = Lavadoras en servicio
    S = Lavadoras de repuesto

    Tf = Tiempo medio hasta fallar
    Tr = Tiempo medio de reparacion
    """
    suma1 = 0
    suma2 = 0

    for _ in xrange(n):
        exito = lavadero(N, S, Tf, Tr)

        suma1 += exito # x
        suma2 += exito**2 # x^2

    esperanza = suma1/float(n)
    varianza = suma2/float(n) - esperanza**2 # V(x) = E(x^2) - E(x)^2

    des_est = math.sqrt(varianza) # Desviacion estandar = V(X)**(1/2.0)

    return esperanza, varianza, des_est


def printEV():
    print("\n### Lavadero con 2 Repuestos y 1 Tecnico ###")
    for n in [100, 1000, 10000, 100000]:
        esperanza, varianza, des_est = esperanzaYVarianza(lavadero01, 5, 2, 1, 1/8.0, n)
        print("E[T] =", esperanza, ", V[T] =", varianza, ", V[T]**(1/2.0) =", des_est)

    print("----------------------------------------------------------------------")

    print("### Lavadero con 2 Repuestos y 2 Tecnicos ###")
    # (2.61, 2.76)
    for n in [100, 1000, 10000, 100000]:
        esperanza, varianza, des_est = esperanzaYVarianza(lavadero02, 5, 2, 1, 1/8.0, n)
        print("E[T] =", esperanza, ", V[T] =", varianza, ", V[T]**(1/2.0) =", des_est)

    print("----------------------------------------------------------------------")

    print("### Lavadero con 3 Repuestos y 1 Tecnico ###")
    for n in [100, 1000, 10000, 100000]:
        esperanza, varianza, des_est = esperanzaYVarianza(lavadero01, 5, 3, 1, 1/8.0, n)
        print("E[T] =", esperanza, ", V[T] =", varianza, ", V[T]**(1/2.0) =", des_est)
    print("")


def plot():
    """
    Ploteo de Histogramas
    """
    n = 100000
    v1 = [lavadero01(5, 2, 1, 1/8.0) for _ in xrange(n)] # S = 2 y Tecnicos = 1
    v2 = [lavadero02(5, 2, 1, 1/8.0) for _ in xrange(n)] # S = 2 y Tecnicos = 2
    v3 = [lavadero01(5, 3, 1, 1/8.0) for _ in xrange(n)] # S = 3 y Tecnicos = 1

    plt.figure(1)
    plt.title("Sistema de Lavadero Actual")
    plt.ylabel("Frecuencia de Fallo (%)")
    plt.xlabel("Tiempo hasta Fallar [Meses]")
    plt.grid(True)
    plt.xticks(xrange(0, 20, 1))
    plt.xlim(0, 20)
    plt.text(10, 0.35, "E[T] = " + str(round(1.75451847743, 2)))
    plt.text(10, 0.3, "V[T] = " + str(round(2.56715632376, 2)))
    plt.text(10, 0.25, "Desviacion estandar[T] = " + str(round(1.60223479046, 2)))
    plt.hist(v1, bins=50, normed=True, color="g", label="2 Repuestos y 1 Tecnico")
    plt.legend()

    plt.figure(2)
    plt.title("Sistema de Lavadero con Opcion 1")
    plt.ylabel("Frecuencia de Fallo (%)")
    plt.xlabel("Tiempo hasta Fallar [Meses]")
    plt.grid(True)
    plt.xticks(xrange(0, 20, 1))
    plt.xlim(0, 20)
    plt.text(10, 0.25, "E[T] = " + str(round(2.58903738453, 2)))
    plt.text(10, 0.2, "V[T] = " + str(round(6.07975267469, 2)))
    plt.text(10, 0.15, "Desviacion estandar[T] = " + str(round(2.46571544885, 2)))
    plt.hist(v2, bins=50, normed=True, color="b", label="2 Repuestos y 2 Tecnicos")
    plt.legend()

    plt.figure(3)
    plt.title("Sistema de Lavadero con Opcion 2")
    plt.ylabel("Frecuencia de Fallo (%)")
    plt.xlabel("Tiempo hasta Fallar [Meses]")
    plt.grid(True)
    plt.xticks(xrange(0, 20, 1))
    plt.xlim(0, 20)
    plt.text(10, 0.2, "E[T] = " + str(round(3.60410154483, 2)))
    plt.text(10, 0.15, "V[T] = " + str(round(11.0641450939, 2)))
    plt.text(10, 0.1, "Desviacion estandar[T] = " + str(round(3.32628097037, 2)))
    plt.hist(v3, bins=50, normed=True, color="r", label="3 Repuestos y 1 Tecnico")
    plt.legend()

    plt.figure(4)
    plt.title("Sistema de Lavadero comparacion de Opcion 1 y Opcion 2")
    plt.ylabel("Frecuencia de Fallo (%)")
    plt.xlabel("Tiempo hasta Fallar [Meses]")
    plt.grid(True)
    plt.xticks(xrange(0, 20, 1))
    plt.xlim(0, 20)
    plt.hist([v2, v3], bins=50, normed=True, color=["b", "r"], label=["2 Repuestos y 2 Tecnicos", "3 Repuestos y 1 Tecnico"])
    # plt.hist(v3, bins=50, normed=True, color="r", label="3 Repuestos y 1 Tecnico")
    plt.legend()

    plt.show()


# printEV()
plot()
