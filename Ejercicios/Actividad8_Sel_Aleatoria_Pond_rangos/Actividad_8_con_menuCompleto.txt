from random import randrange, uniform,randint,choice
import numpy as np
import math

def random_poblation(cromosomas, genes):
    resultado = []
    for _ in range(0, cromosomas):
        lista = []
        for _ in range(0, genes):
            temp = randint(0, 1)
            #temp_rounded = round(temp, 0)
            lista.append(temp)
        resultado.append(lista)
    return resultado

def random_cromosomes(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(0.0, 1.0) 
        lista.append(aleatorio)

    return lista

def print_poblation_line(poblacion):
    for cromosoma in poblacion:
        print(cromosoma)

def n_poblation(poblacion):
    pob_size = len(poblacion)
    return pob_size

def PN(n_keep):
    up = 0
    down = 0
    lista_pn = []
   
    
    for i in range(1,n_keep + 1):
        down += i
    
    for i in range(1,n_keep+1):  
        up = n_keep - i + 1
        Pn = up/down
        lista_pn.append(Pn)
    
    cumulative_sum = np.cumsum(lista_pn).tolist()

    rounded_sum = [round(x, 2) for x in cumulative_sum]

    return rounded_sum

def N_keep(pob_size, x_rate):
    n_keep = math.ceil(pob_size * x_rate)
    return n_keep


def PUD(poblacion, X_rate):
    poblacion_after = round(len(poblacion) * X_rate)
    padres = []
    madres = []
    for cromosoma in range(0, poblacion_after):
        if (cromosoma+1) % 2 == 0:
            padres.append(poblacion[cromosoma])
        else:
            madres.append(poblacion[cromosoma])

    print("poblacion")
    print(print_poblation_line(poblacion))
    print("madres")
    print(madres)
    print("padres")
    print(padres)

def RP(poblacion, x_rate):
    pob_size = len(poblacion)

    n_keep = math.ceil(pob_size * x_rate)

    padres = []
    madres = []
    lista_aleatorios = []
    for _ in range(0,n_keep):
        temp = randint(1, n_keep)
        lista_aleatorios.append(temp)

    print(lista_aleatorios)
    # lista_aleatorios = [1, 2, 4, 4, 2]  
    # print(lista_aleatorios)
    
    for index, value in enumerate(lista_aleatorios):
        if index % 2 == 0:
            padres.append(poblacion[value-1])
        else:
            madres.append(poblacion[value-1])

    print("Lista seleccionados")
    print(lista_aleatorios)
    print("poblacion")
    print(print_poblation_line(poblacion))
    print("madres")
    print(madres)
    print("padres")
    print(padres)

def RW(cromosomas, sum_pi, numeros_aleatorios):
    padres = []
    madres = []
    append_to_madres = True
    for numero_aleatorio in numeros_aleatorios:
        for i, acumulado in enumerate(sum_pi):
            if numero_aleatorio <= acumulado:
                if append_to_madres:
                    padres.append(cromosomas[i])
                else:
                     madres.append(cromosomas[i])
                append_to_madres = not append_to_madres
                break
                
        else:
            lista_seleccionada = choice([padres, madres])
            lista_seleccionada.append(cromosomas[-1])
             
    
    print("Cromosomas: ")
    print(print_poblation_line(cromosomas))
    print("Sumatoria de pi ")
    print(sum_pi)
    print("Numeros aleatorios ")
    print(numeros_aleatorios)
    print("madres: ")
    print(madres)
    print("padres: ")
    print(padres)

while True:
    print("Que menu desea utilizar?")
    # response_tdp =  input("Ingrese TDP -> Metodo de seleccion arriba - abajo\n")
    # response_rp = input("Ingrese RP -> Metodo de seleccion aleatorio\n")
    print("Ingrese TDP -> Metodo de seleccion arriba - abajo")
    print("Ingrese RP -> Metodo de seleccion aleatorio")
    print("Ingrese RW -> Método de selección aleatoria ponderada por rangos")
    response = input()



    if(response == "TDP"):
        cromosoma_input = input("Tamaño de la poblacion -> ")
        longitud_cromosomas_input = input("Longitud de los cromosomas -> ")
        tasa_selec_input = input("Tamaño de seleccion (0 a 1) -> ")
        try:
            cromosomas = int(cromosoma_input)
            longitud_cromosomas = int(longitud_cromosomas_input)
            tasa_selec = float(tasa_selec_input)  
            resultado_poblacion_tdp = random_poblation(cromosomas, longitud_cromosomas)
            PUD(resultado_poblacion_tdp, tasa_selec)
        except ValueError:
            print("Alguno de los valores ingresados no es válido.")


    elif(response == "RP"):

        cromosoma_input = input("Tamaño de la poblacion -> ")
        longitud_cromosomas_input = input("Longitud de los cromosomas -> ")
        tasa_selec_input = input("Tamaño de seleccion (0 a 1) -> ")
        try:
            cromosomas = int(cromosoma_input)
            longitud_cromosomas = int(longitud_cromosomas_input)
            tasa_selec = float(tasa_selec_input)  
            resultado_poblacion_tdp = random_poblation(cromosomas, longitud_cromosomas)
            RP(resultado_poblacion_tdp, tasa_selec)
        except ValueError:
            print("Alguno de los valores ingresados no es válido.")

    elif(response == "RW"):
        cromosoma_input = input("Tamaño de la poblacion -> ")
        longitud_cromosomas_input = input("Longitud de los cromosomas -> ")
        tasa_selec_input = input("Tamaño de seleccion (0 a 1) -> ")
        try:
            cromosomas = int(cromosoma_input)
            longitud_cromosomas = int(longitud_cromosomas_input)
            tasa_selec = float(tasa_selec_input)  
            resultado_poblacion_rw = random_poblation(cromosomas, longitud_cromosomas)
            pob_size = n_poblation(resultado_poblacion_rw)
            n_keep = N_keep(pob_size,tasa_selec)
            sum_pi = PN(n_keep)
            numeros_aleatorios = random_cromosomes(n_keep)
            RW(resultado_poblacion_rw,sum_pi,numeros_aleatorios)

        except ValueError:
            print("Alguno de los valores ingresados no es válido.")


    else: 
        print("Opcion no valida intente nuevamente ...")






