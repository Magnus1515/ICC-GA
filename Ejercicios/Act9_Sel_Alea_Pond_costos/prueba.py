from random import randrange, uniform, randint, choice
import numpy as np
import math

def random_population(cromosomes, genes):
    resultado = []
    for _ in range(0, cromosomes):
        lista = []
        for _ in range(0, genes):
            temp = randint(0, 1)
            lista.append(temp)
        resultado.append(lista)
    return resultado

def random_weights(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(1, 10)
        aleatorio_rounded = round(aleatorio, 1)
        lista.append(aleatorio_rounded)
    return lista

def random_values(cantidad):
    lista = []
    for x in range(cantidad):
        aleatorio = uniform(1, 100)
        lista.append(aleatorio)
    return lista

def random_probabilities(cantidad):
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
    suma = np.sum(pesos) / 2
    return suma

def PN(cn):
    up = 0
    down = 0
    lista_pn = []
    cumulative_sum_cm = sum(cn)
    for x in cn:
        up = x
        down = cumulative_sum_cm
        Pn = abs(up / down)
        lista_pn.append(Pn)
    cumulative_sum = np.cumsum(lista_pn).tolist()
    return cumulative_sum, lista_pn

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
        xj = fila
        values_init_list.append(operation_dot_product(xj, w))
        knapsack_full = False
        if operation_dot_product(xj, w) > V:
            knapsack_full = True
        while knapsack_full:
            for i in range(len(xj)):
                if xj[i] == 1:
                    xj[i] = 0
                if operation_dot_product(xj, w) < V:
                    knapsack_full = False
                    break
        while not knapsack_full:
            for i in range(len(xj)):
                if xj[i] == 0:
                    xj[i] = 1
                if operation_dot_product(xj, w) > V:
                    xj[i] = 0
                    knapsack_full = True
                    break
        values_repair_list.append(operation_dot_product(xj, w))
        resultados.append(xj)
        index += 1
    return resultados

def operation_aptitud(poblacion, costos):
    array_1 = np.array(poblacion)
    array_2 = np.array(costos)
    resultado = np.dot(array_1, array_2)
    return resultado.tolist()



# Rest of your code...

# Example usage of SCW function
resultado_random_poblacion = random_population(10, 5)
tasa_de_seleccion = 0.5
pesos = random_weights(5)
valores = operation_profits(pesos)
px = operation_aptitud(resultado_random_poblacion, valores)
sum_knapsack_capacity = knapsack_capacity(pesos)
poblacion_reparada = RP(resultado_random_poblacion, pesos, sum_knapsack_capacity)
numeros_aleatorios_var = random_probabilities(5)

def N_keep(pob_size, x_rate):
    n_keep = math.ceil(pob_size * x_rate)
    return n_keep

def n_population(poblacion):
    pob_size = len(poblacion)
    return pob_size

def cromos_to_values(chromosomes, values):
    value_to_cromos = {}
    for i in range(len(chromosomes)):
        cromos_str = str(chromosomes[i])
        value = values[i]
        if value not in value_to_cromos:
            value_to_cromos[value] = []
        value_to_cromos[value].append(cromos_str)
    return value_to_cromos

def SCW(cromosomas, costos, x_rate):
    costos = sorted(costos)
    selected_cromos = math.ceil(len(cromosomas) * x_rate)
    selected_costs = math.ceil(len(costos) * x_rate)
    selected_elements = cromosomas[:selected_cromos]
    selected_elem_costs = costos[:selected_costs]
    not_selected_elem_costs = costos[selected_costs:]
    min_not_select_elem_costs = min(not_selected_elem_costs)

    #cromosomas_dict = cromos_to_values(cromosomas, costos)
    #cromosoma_descartado = cromosomas_dict[min_not_select_elem_costs]
    cn_list = []

    for ci in selected_elem_costs:
        temp_cn = ci - min_not_select_elem_costs
        cn_list.append(temp_cn)
    sumatory_cn_list = sum(cn_list)
    sum_valores_pn, valores_pn = PN(cn_list)
    numeros_aleatorios = random_probabilities(len(valores_pn))
    padres = []
    madres = []
    append_to_madres = True
    for numero_aleatorio in numeros_aleatorios:
        for i, acumulado in enumerate(sum_valores_pn):
            if numero_aleatorio <= acumulado:
                if append_to_madres:
                    padres.append(selected_elements[i])
                else:
                    madres.append(selected_elements[i])
                append_to_madres = not append_to_madres
                break
            else:
                lista_seleccionada = choice([padres, madres])
                lista_seleccionada.append(selected_elements[-1])
    
    print("Cromosomas descartados:\n",not_selected_elem_costs)
    print("Cromosoma descartado: " + str(min_not_select_elem_costs))
    
    #print("Fitness del cromosoma descartado: " + str(cromosoma_descartado))
    
    print("Valores de Cn:\n", cn_list)
    print("Valores de sumatoria de costos: " + str(sumatory_cn_list))
    print("Valores de Pn:\n", valores_pn, "\nSumatoria de las probabilidades:\n", sum_valores_pn)
    print("Numeros aleatorios:", numeros_aleatorios)
    print("madres:\n", madres)
    print("padres:\n", padres)

#Example usage of the SCW function
SCW(poblacion_reparada, px, tasa_de_seleccion)

