from random import randrange, uniform,randint, choice
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


resultado_poblacion2 = random_poblation(10, 3)
#print(resultado_poblacion2)

def print_poblation_line(poblacion):
    for cromosoma in poblacion:
        print(cromosoma)



#PUD(resultado_poblacion, 0.5)

def random_cromosomes(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(0.0, 1.0) 
        lista.append(aleatorio)

    return lista


#print(numeros_aleatorios)

def n_poblation(poblacion):
    pob_size = len(poblacion)
    return pob_size



def N_keep(pob_size, x_rate):
    n_keep = math.ceil(pob_size * x_rate)
    return n_keep



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

# [0.4, 0.3, 0.2, 0.1 ]


def RP(poblacion, x_rate):
    pob_size = len(poblacion)

    n_keep = math.ceil(pob_size * x_rate)

    padres = []
    madres = []
    lista_aleatorios = []
    for _ in range(0,n_keep):
        temp = randint(1, n_keep)
        lista_aleatorios.append(temp)

    
    # lista_aleatorios = [1, 2, 4, 4, 2]  
    # print(lista_aleatorios)
    
    for index, value in enumerate(lista_aleatorios):
        if index % 2 == 0:
            padres.append(poblacion[value-1])
        else:
            madres.append(poblacion[value-1])
            
    print("Lista seleccionados")
    print(lista_aleatorios)
    print("poblacion: ")
    print(print_poblation_line(poblacion))
    print("madres: ")
    print(madres)
    print("padres: ")
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

xRate = 0.5

numeros_aleatorios = random_cromosomes(5)
pob_size = n_poblation(resultado_poblacion2)
n_keep = N_keep(pob_size, xRate)
sum_pi = PN(n_keep)

print(sum_pi)
RW(resultado_poblacion2,sum_pi,numeros_aleatorios)

#resultado_poblacion2 = random_poblation(8, 3)
#RP(resultado_poblacion2,0.5)





