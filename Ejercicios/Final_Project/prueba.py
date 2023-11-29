import random

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




def inicializar_hormigas(num_hormigas, num_objetos):
    # Crea hormigas aleatorias con una lista de objetos seleccionados
    hormigas = []
    for _ in range(num_hormigas):
        objetos_seleccionados = [random.choice([0, 1]) for _ in range(num_objetos)]
        capacidad_restante = calcular_capacidad_restante(objetos_seleccionados)
        feromona = 1.0  # Puedes ajustar esto según sea necesario
        hormigas.append({'objetos': objetos_seleccionados, 'capacidad': capacidad_restante, 'feromona': feromona})
    return hormigas



def actualizar_feromonas(hormigas, evaporacion_rate):
    # Actualiza las feromonas en función del rendimiento de las hormigas
    for hormiga in hormigas:
        if hormiga['capacidad'] >= 0:
            # Puedes ajustar cómo se actualizan las feromonas según el rendimiento de la hormiga
            hormiga['feromona'] *= (1 - evaporacion_rate)
            hormiga['feromona'] += calcular_valor_rendimiento(hormiga)  # Ajusta esto según tu lógica específica



def seleccionar_objetos(hormiga, feromona_factor):
    # Selecciona objetos para la próxima iteración basándote en las feromonas
    # Puedes ajustar la lógica de selección de objetos según las feromonas
    objetos_seleccionados = [1 if random.random() < feromona_factor * hormiga['feromona'] else 0 for _ in range(len(hormiga['objetos']))]
    capacidad_restante = calcular_capacidad_restante(objetos_seleccionados)
    return {'objetos': objetos_seleccionados, 'capacidad': capacidad_restante, 'feromona': hormiga['feromona']}



def ant_colony_optimization(num_iteraciones, num_hormigas, num_objetos, capacidad_maxima, evaporacion_rate, feromona_factor):
    # Función principal que ejecuta el algoritmo ACO
    hormigas = inicializar_hormigas(num_hormigas, num_objetos)
    
    for _ in range(num_iteraciones):
        for i in range(num_hormigas):
            if hormigas[i]['capacidad'] >= 0:
                hormigas[i] = seleccionar_objetos(hormigas[i], feromona_factor)
        
        actualizar_feromonas(hormigas, evaporacion_rate)
    
    # Devuelve la mejor solución encontrada
    mejor_solucion = max(hormigas, key=lambda x: calcular_valor_rendimiento(x))
    return mejor_solucion

# Agrega las funciones adicionales que necesites, como calcular_capacidad_restante, calcular_valor_rendimiento, etc.
