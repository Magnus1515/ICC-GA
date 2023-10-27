from random import randrange, uniform, randint, choice
import random
import numpy as np
import math
import copy
from tabulate import tabulate
from num2words import num2words


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
        aleatorio = uniform(1.0, 10.0)
        lista.append(aleatorio)

    return lista


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
    suma = np.sum(pesos) / 2
    return suma


def print_poblation_line(poblacion):
    for cromosoma in poblacion:
        print(cromosoma)
    return poblacion


def PN(cn):
    up = 0
    down = 0
    lista_pn = []
    # down = sum(range(1, n_keep + 1))
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


def operation_aptitud(poblacion, costos):
    array_1 = np.array(poblacion)
    array_2 = np.array(costos)

    resultado = np.dot(array_1, array_2)

    return resultado.tolist()


def RP(poblacion, w, V):
    resultados = []
    values_init_list = []
    values_repair_list = []
    index = 1
    for fila in poblacion:
        # fila = poblacion
        xj = fila

        values_init_list.append(operation_dot_product(xj, w))

        # print(f"Sumatoria -> {suma_rela}")
        knapsak_full = False
        if operation_dot_product(xj, w) > V:
            knapsak_full = True

        while knapsak_full == True:
            for i in range(len(xj)):
                if xj[i] == 1:
                    xj[i] = 0
                    # print("suma relacion 1 antes", operation_dot_product(xj,w))
                    if operation_dot_product(xj, w) < V:
                        # print("suma relacion 1 despues", operation_dot_product(xj,w))
                        knapsak_full = False
                        break

        while knapsak_full == False:
            for i in range(len(xj)):
                if xj[i] == 0:
                    xj[i] = 1
                    # print("suma relacion 2 antes", operation_dot_product(xj,w))
                    if operation_dot_product(xj, w) > V:
                        xj[i] = 0
                        # print("suma relacion 2 despues", operation_dot_product(xj,w))
                        knapsak_full = True
                        break

        values_repair_list.append(operation_dot_product(xj, w))

        resultados.append(xj)
        # print(f"Cromosoma Final -> {xj}")
        index += 1
    return resultados


def N_keep(pob_size, x_rate):
    # pob_size = len(poblacion)
    n_keep = math.ceil(pob_size * x_rate)
    return n_keep


def n_poblation(poblacion):
    pob_size = len(poblacion)
    return pob_size



# Sorted the populated related with their fitness
def population_sorted(population, population_fitness):

    repaired_population_indexes = np.arange(len(population)).tolist()

    fitness_sorted, indexes_sorted = map(list,zip(*sorted(zip(operation_aptitud(population, population_fitness),repaired_population_indexes,),reverse=True,)),)

    # Sorted the population using the indexes to changed it
    new_population = [population[i] for i in indexes_sorted]

    return new_population, fitness_sorted


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


def weight_random_pairing(cromosomas, costos, x_rate):
    # We order from Greater to Minor in order descending
    # costos = sorted(costos, reverse=True)
    cromosomas, costos = population_sorted(cromosomas, costos)
    # selected_cromos = math.ceil(len(cromosomas) * x_rate)

    # selected_costs = math.ceil(len(costos) * x_rate)

    # selected_cromos = cromosomas[:selected_cromos]
    # selected_costs = costos[:selected_costs]

    # not_selected_cromos = cromosomas[selected_cromos:]
    # not_selected_costs = costos[selected_costs:]

    # min_not_selected_cost = min(not_selected_costs)

    selected_cromos = math.ceil(len(cromosomas) * x_rate)
    selected_costs = math.ceil(len(costos) * x_rate)

    selected_elements_cromos = cromosomas[:selected_cromos]
    selected_elem_costs = costos[:selected_costs]
    # selected_elem_costs = [23.86569316, 19.58156339, 17.52276708, 16.06364778]
    not_selected_costs = costos[selected_costs:]
    min_not_selected_costs = min(not_selected_costs)

    # cromosoma_descartado = cromosomas_dict[min_not_selected_costs]
    cn_list = []

    for ci in selected_elem_costs:
        temp_cn = ci - (min_not_selected_costs)
        cn_list.append(temp_cn)

    sumatory_cn_list = sum(cn_list)
    sum_valores_pn, valores_pn = PN(cn_list)
    numeros_aleatorios = random_probabilidades(len(valores_pn))

    padres = []
    madres = []
    append_to_madres = True
    for numero_aleatorio in numeros_aleatorios:
        for i, acumulado in enumerate(sum_valores_pn):
            if numero_aleatorio <= acumulado:
                if append_to_madres:
                    padres.append(selected_elements_cromos[i])
                else:
                    madres.append(selected_elements_cromos[i])
                append_to_madres = not append_to_madres
                break
            # else:
            #     lista_seleccionada = choice([padres, madres])
            #     lista_seleccionada.append(selected_elements[-1])

    # print("Pesos de los objetos: \n", pesos)
    # print("Valores de cada objeto")

    # print("\nCromosomas descartados: \n", not_selected_costs)
    # # print("Cromosoma descartado: " , min_not_selected_costs)
    # print("Cromsomas seleccionados: \n", selected_elem_costs)
    # print("Fitness del cromosoma descartado: ",min_not_selected_costs)
    # print("\nValores de Cn: \n", cn_list)
    # print("Valores de sumatoria de costos ", sumatory_cn_list)
    # print("\nValores de Pn :\n",valores_pn,"\nSumatoria de las probabilidades:\n",sum_valores_pn)
    # print("\nNumeros aleaotorios: \n", numeros_aleatorios)
    # print("madres: \n", madres)
    # print("padres: \n", padres)
    return padres, madres


def two_points_crossover(parent1, parent2):
    length = len(parent1)
    one_third = length // 3
    two_thirds = 2 * one_third
    points_cut = [one_third, two_thirds]
    # Perform two-thirds crossover
    child1 = parent1[:one_third] + parent2[one_third:two_thirds] + parent1[two_thirds:]
    child2 = parent2[:one_third] + parent1[one_third:two_thirds] + parent2[two_thirds:]

    return child1, child2, points_cut


def recombination_method2(padre, madre, tasa_recomb):
    # WE NEED TO CONSIDER THESE FUNCTIONS FURTHER
    padre, madre = equal_lists(padre, madre)
    # padre, madre = just_even_lists(padre1,madre1)
    hijo1 = []
    hijo2 = []
    for cromosoma_p, cromosoma_m in zip(padre, madre):
        # lista_p = []
        # lista_m = []
        after_cut_padre, after_cut_madre, cut_points = two_points_crossover(
            cromosoma_p, cromosoma_m
        )

        x = random_probabilidades(1)

        if x[0] < tasa_recomb:
            hijo1.append(after_cut_padre)
            hijo2.append(after_cut_madre)
        else:
            hijo1.append(cromosoma_p)
            hijo2.append(cromosoma_m)

        # print("valor de x: ", x)
        # print("Padre: ", cromosoma_p)
        # print("Madre: ", cromosoma_m)
        # print("Puntos de corte: ",cut_points)
        # print("Hijo1: ", after_cut_padre)
        # print("Hijo2: ", after_cut_madre)
    return hijo1 + hijo2


def mutate_population(population, mutation_rate):
    selected_cromos = math.floor(len(population) * mutation_rate)
    #Generate random indexes in range of selected_cromos to be mutated
    selected_cromos_index = [
        randint(0, len(population) - 1) for _ in range(selected_cromos)
    ]

    # Create a deep copy of the population to avoid modifying the original and using in the for
    new_population = copy.deepcopy(population)

    for chrom_idx in selected_cromos_index:
        # print(f"CHROMOSOME TO MUT:{new_population[chrom_idx]}")
        aleatorio = randint(0, len(population[chrom_idx]) - 1)
        # print(f"INDEX TO MUT:{aleatorio}")
        if new_population[chrom_idx][aleatorio] == 0:
            new_population[chrom_idx][aleatorio] = 1
        else:
            new_population[chrom_idx][aleatorio] = 0
        # print(f"CHROMOSOME AFTER MUT:{new_population[chrom_idx]}")

    return new_population


def add_offspring_to_repairpopulation(
    repair_population, mutated_offsprings, x_rate, costos
):
    # function to sorted population with their costs
    mutated_offsprings_list, _ = population_sorted(mutated_offsprings, costos)

    selected_n_cromos = math.ceil(len(repair_population) * x_rate)
    mutated_offsprings_end = mutated_offsprings_list[:-1]
    # Replace the selected part of repair_population with mutated_offsprings
    repair_population[:selected_n_cromos] = mutated_offsprings_end

    # print("Mutated List: \n",mutated_offsprings_end)
    return repair_population


best_cromos_after_runs = []
worst_cromos_after_runs = []
best_fitnes_after_runs = []
worst_fitness_after_runs = []

n_runs = 30

number_list = list(range(1, n_runs + 1))

for _ in range(n_runs):
    population_size = 500
    objects = 15
    selection_rate = 0.5
    mutation_rate = 0.2
    recombination_rate = 0.5
    sum_knapsack_capacity = 750
    pesos = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    valores = [135,139,149,150,156,163,173,184,192,201,210,214,221,229,240]
    best_values_after_recomb = []
    best_values_after_mutated = []
    lista = []

    temp_best_cromos = []
    temp_best_fitness = []
    resultado_random_poblacion = random_poblation(population_size, objects)
    poblacion_reparada = RP(resultado_random_poblacion, pesos, sum_knapsack_capacity)
    lista.append(poblacion_reparada)

    for _ in range(1000):
    
        # Llamado a la funcion del método de selección aleatoria ponderada por costo.
        select_padres, select_madres = weight_random_pairing(
            lista[0], valores, selection_rate
        )

        lista_antes_de_aptitud = operation_aptitud(
            select_padres + select_madres, valores
        )

        # Llamado a la funcion del método de recombinacion

        recombinated_list = recombination_method2(
            select_padres, select_madres, recombination_rate
        )

        # Llamado a la funcion del método de mutacion

        mutated_list = mutate_population(recombinated_list, mutation_rate)

        population_w_mutation_list = add_offspring_to_repairpopulation(
            poblacion_reparada, mutated_list, selection_rate, valores
        )

        mutate_repair_list = RP(
            population_w_mutation_list, pesos, sum_knapsack_capacity
        )
        # print_poblation_line(mutate_repair_list)
        lista.pop(0)
        lista.append(mutate_repair_list)
        best_cromos_afterLoop, fitness_sorted = population_sorted(
            mutate_repair_list, valores
        )
        temp_best_cromos.append(best_cromos_afterLoop[0])

        # print(
        #     "-------------------------------\nBest cromosome pos Selection :\n",
        #     max(operation_aptitud(select_padres + select_madres, valores)),
        # )

        # temp_best_fitness.append(fitness_sorted[0])

    # print("Best Cromosome after loop after Recom: ", max(best_values_after_mutated))
    # print(
    #     "Best Cromosome after loop after Mutate: ",
    #     x_cromos[0],
    #     "\nBest Fitness : ",
    #     y_fitness[0],
    #     "\nWorst Cromosome after after Mutate",
    #     x_cromos[-1],
    #     "\nWorst Fitness: ",
    #     y_fitness[-1],
    # )
    x_cromos, y_fitness = population_sorted(temp_best_cromos, valores)
    best_cromos_after_runs.append(x_cromos[0])
    worst_cromos_after_runs.append(x_cromos[-1])
    best_fitnes_after_runs.append(y_fitness[0])
    worst_fitness_after_runs.append(y_fitness[-1])


#Creating the tables using tabulate with fancy_grid
data = list(
    zip(
        number_list,
        best_cromos_after_runs,
        best_fitnes_after_runs,
    )
)

table = tabulate(
    data, headers=["Runs", "Best Chromosome", "Best Fitness"], tablefmt="fancy_grid"
)

print(table)

data2 = list(zip(number_list, worst_cromos_after_runs, worst_fitness_after_runs))

table2 = tabulate(
    data2, headers=["Runs", "Worst Chromosome", "Worst Fitness"], tablefmt="fancy_grid"
)

print(table2)
