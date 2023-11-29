from random import randrange, uniform, randint, choice, choices
import random
import numpy as np
import math
import copy
from tabulate import tabulate
from num2words import num2words





n_runs = 30 
n_generations = 1000
number_list = list(range(1, n_runs + 1))


population_size = 500
objects = 15
selection_rate = 0.5
mutation_rate = 0.2
knapsack_capacity = 750

pesos = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]

valores = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]

tao = 1.0
ant_k = 0
zj = 0

# Variable feromonas 

hormigas = []

def random_poblation(cromosomas, genes):
    resultado = []
    for _ in range(0, cromosomas):
        lista = []
        for _ in range(0, genes):
            temp = randint(0, 1)
            lista.append(temp)
        resultado.append(lista)
    return resultado


def Pj(valores,tao):
    lista_pj = []
    #Regresa los 15 valores
    cumulative_sum_pj = sum(tao for _ in range(len(valores)))

    
    for _ in range(len(valores)):
        up = tao
        down = cumulative_sum_pj
        temp_pj = up/down
        lista_pj.append(temp_pj)

    cumulative_sum_list = np.cumsum(lista_pj).tolist()

    return cumulative_sum_list



def random_probabilidades(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(0.0, 1.0)
        lista.append(aleatorio)

    return lista


#la cantidad de objetos va a depender del peso de la mochila 
#la cantidad de soluciones que tengan no puede ser mayor que el peso de la mochila

def ants_neighborhood(num_ants, num_obj):

    hormigas = []
    for _ in range(num_ants):
        objetos_seleccionados = [random.choice([0, 1]) for _ in range(num_obj)]
        capacidad_restante = calcular_capacidad_restante(objetos_seleccionados)
        feromona = 1.0  # Puedes ajustar esto según sea necesario
        hormigas.append(objetos_seleccionados)
    return hormigas






    #Si no ha trabajo todavia, existe
    #while ant_k == 0:

def update_pheromone(ants, evaporation_rate):

    while knapsack_capacity >= 0:
        #seleccionamos un Objeto
        random_prob_list = random_probabilidades(15)
        cumulative_list_valores = Pj(valores,tao)

        for numero_aleatorio in random_prob_list:
            for i,acumulado in enumerate(cumulative_list_valores):
                if numero_aleatorio <= acumulado:
                    selected_elem.append(pesos[i])
                    print(pesos[i])
                    knapsack_capacity -= pesos[i]
                    zj += valores[i]


# Una que crea las hormigas los obejtos, la capacidad, la feromona -> y reparar
# Una que me actualiza las feromonas
# Una que te selecciona los objetos 
# Funcion principal
   
                    



 
