from random import randrange, uniform,randint, choice
import numpy as np
import math

def random_poblation(cromosomas, genes):
    resultado = []
    for _ in range(0, cromosomas):
        lista = []
        for _ in range(0, genes):
            temp = randint(0, 1)
            lista.append(temp)
        resultado.append(lista)
    return resultado


def random_weigths(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(1, 10)
        lista.append(aleatorio)

    return lista


def random_values(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(1, 100)
        lista.append(aleatorio)

    return lista


def print_poblation_line(poblacion):
    for cromosoma in poblacion:
        print(cromosoma)


def random_probabilidades(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(0.0, 1.0) 
        lista.append(aleatorio)

    return lista


def operation_profits(pesos):
    lista = []
    for wi in pesos:
        tempo = wi + 5
        lista.append(tempo)

    return lista


def knapsack_capacity(pesos):
    suma = np.sum(pesos)/2
    return suma


    up = 0
    down = 0
    lista_pn = []
    #down = sum(range(1, n_keep + 1))
    cumulative_sum_cm = sum(cn)

    for x in cn:
        up = x
        down = cumulative_sum_cm
        Pn = abs(up/down)
        lista_pn.append(Pn)
    
    cumulative_sum = np.cumsum(lista_pn).tolist()

    #rounded_sum = [round(x, 2) for x in lista_pn]

    return cumulative_sum,lista_pn


def operation_dot_product(pesos, poblacion):
    array_1 = np.array(pesos)
    array_2 = np.array(poblacion)

    resultado = np.dot(array_1, array_2)

    return resultado


def RP(poblacion, w, V):
    resultados = []
    values_init_list = []
    values_repair_list = []
    index = 1
    for fila in poblacion:
        # fila = poblacion
        xj = fila

        values_init_list.append(operation_dot_product(xj,w))
        
        #print(f"Sumatoria -> {suma_rela}")
        knapsak_full  = False
        if(operation_dot_product(xj,w) > V):
            knapsak_full = True
            
        while knapsak_full == True:
            for i in range(len(xj)):
                if xj[i] == 1:
                    xj[i] = 0
                    #print("suma relacion 1 antes", operation_dot_product(xj,w))
                    if operation_dot_product(xj,w) < V:
                        #print("suma relacion 1 despues", operation_dot_product(xj,w))
                        knapsak_full = False
                        break
        
        while knapsak_full == False:
            for i in range(len(xj)):
                if xj[i] == 0:
                    xj[i] = 1
                    #print("suma relacion 2 antes", operation_dot_product(xj,w))
                    if operation_dot_product(xj,w) > V:
                        xj[i] = 0
                        #print("suma relacion 2 despues", operation_dot_product(xj,w))
                        knapsak_full = True
                        break
        
        values_repair_list.append(operation_dot_product(xj,w))
        
        resultados.append(xj)
        #print(f"Cromosoma Final -> {xj}")
        index += 1
    return resultados


def operation_aptitud(poblacion, costos):

    array_1 = np.array(poblacion)
    array_2 = np.array(costos)

    resultado = np.dot(array_1, array_2)

    return resultado.tolist()


def equal_lists(padre, madre):
    n_p = len(padre)
    n_m = len(madre)
    while n_p < n_m:
        valor_temp2 = choice(padre)
        padre.append(valor_temp2)
        n_p += 1
    
    while n_m < n_p:
        valor_temp = choice(madre)
        madre.append(valor_temp)
        n_m += 1
    return padre, madre

def just_even_lists(padre, madre):
    n_p = len(padre)
    n_m = len(madre)
    if n_p % 2 != 0:
        valor_temp2 = choice(padre)
        padre.append(valor_temp2)
        n_p += 1
    
    if n_m % 2 != 0:
        valor_temp = choice(madre)
        madre.append(valor_temp)
        n_m += 1
    return padre, madre

def cutting_selection(lista):
    n = len(lista)
    subarray_length = n // 3
    remainder = n % 3

    new_lista = []
    start = 0
     
    for _ in range(3):
        end = start + subarray_length
        if remainder > 0:
            end += 1
            remainder -= 1
        subarray = lista[start:end]
        new_lista.append(subarray)
        start = end
    
    return new_lista

def recombination_method(padre, madre, tasa_recomb):

    padre1,madre1 = equal_lists(padre,madre)
    padre, madre = just_even_lists(padre1,madre1)
    
    hijo1 = []
    hijo2 = []
    
    for cromosoma_p,cromosoma_m in zip(padre,madre):
        lista_p = []
        lista_m = []
        x1,x2,x3 = cutting_selection(cromosoma_p)
        y1,y2,y3 = cutting_selection(cromosoma_m)
        x = random_probabilidades(1)

        if(x[0] <= tasa_recomb):
            
            lista_p.extend(x1)
            lista_p.extend(y2)
            lista_p.extend(x3)
            hijo1.append(lista_p)
            lista_m.extend(y1)
            lista_m.extend(x2)
            lista_m.extend(y3)
            hijo2.append(lista_m)
        else:
            lista_p.extend(cromosoma_p)
            hijo1.append(lista_p)
            lista_m.extend(cromosoma_m)
            hijo2.append(lista_m)

        print("valor de x: ", x)
        print("Padre: ",cromosoma_p)
        print("Madre: ",cromosoma_m)
        print("Hijo1: ",lista_p)
        print("Hijo2: ",lista_m) 



def REP(poblacion, x_rate):
    pob_size = len(poblacion)

    n_keep = math.ceil(pob_size * x_rate)

    padres = []
    madres = []
    lista_aleatorios = []
    #Funcion de 0 hasta el valor de n_keep
    for _ in range(0,n_keep):
        temp = randint(1, n_keep)
        lista_aleatorios.append(temp)

    for index, value in enumerate(lista_aleatorios):
        if index % 2 == 0:
            padres.append(poblacion[value-1])
        else:
            madres.append(poblacion[value-1])
            
    print("Lista seleccionados")
    print(lista_aleatorios)
    print("poblacion: ")
    print(poblacion)
    print("madres: ")
    print(madres)
    print("padres: ")
    print(padres)
    return padres, madres



#VALORES PARA LAS PRUEBAS GUARDADOS EN VARIABLES PARA QUE FUNCIONE EL METODO
resultado_random_poblacion = random_poblation(10, 3)
pesos = random_weigths(3)
valores = operation_profits(pesos)
sum_knapsack_capacity = knapsack_capacity(pesos)
poblacion_reparada = RP(resultado_random_poblacion,pesos,sum_knapsack_capacity)

px = operation_aptitud(poblacion_reparada,valores)


#IMPRIMER VALORES PARA LA POBLACION
print("Poblacion Reparada :")
print_poblation_line(poblacion_reparada)
print("\nPesos: \n", pesos)
print("\nValores de cada objeto: \n",valores)
print("\nCosto(fitness) de cada cromosoma: \n" , px)
print("Sumatoria de px: \n", sum(px))

#LLAMADA A LA FUNCION DE SELECCION ALEATORIA
padres,madres = REP(resultado_random_poblacion,0.5)


#Llamado a la funcion del método de recombinacion
recombination_method(padres,madres,0.5)


# px_padre = operation_aptitud(padres,valores)
# px_madre = operation_aptitud(madres,valores)
# sum_padre =  sum(px_padre)
# sum_madre = sum(px_madre)
# print("Madres: \n", madres)
# print("Fitness de la poblacion pre seleccion: ", sum(px))
# print("Fitness de la poblacion pos seleccion: ", sum_padre + sum_madre)





