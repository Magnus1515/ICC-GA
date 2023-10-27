from random import randrange, uniform,randint
import numpy as np
#prueba_pesos = [8.61, 8.2, 1.51]  
#poblacion = [[1,0,1],[1,1,1],[1,0,0],[0,0,0],[1,1,0]]

#print(prueba_poblacion)

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


def random_weigths(cantidad):
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
    

def knapsack_capacity(pesos):
    suma = np.sum(pesos)/2
    return suma

def maximum_value_weigths(pesos):
    return max(pesos)

def minium_value_weigths(pesos):
    return min(pesos)

def average_value_weigths(pesos):
    return sum(pesos)/len(pesos)

def standar_deaviation_weigths(pesos):
    return np.std(pesos)


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
        #print(f"Cromosoma Numero {index} -------------------")
        #print(f"Cromosoma Inicial-> {xj}")
        
        
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


def AR(poblacion, costos):

    array_1 = np.array(poblacion)
    array_2 = np.array(costos)

    resultado = np.dot(array_1, array_2)

    return resultado.tolist()


def PUD(poblacion, X_rate):
    poblacion_after = round(len(poblacion) * X_rate)
    padres = []
    madres = []
    for cromosoma in range(0, poblacion_after):
        if (cromosoma+1) % 2 == 0:
            padres.append(poblacion[cromosoma])
        else:
            madres.append(poblacion[cromosoma])

    print(poblacion)
    print("madres")
    print(madres)
    print("padres")
    print(padres)


resultado_poblacion = random_poblation(10, 10)
resultado_random_poblacion = random_poblation(5, 5)
valores = random_values(5)
pesos = random_weigths(5)
print("valores: ")
print(valores)


#PUD(resultado_poblacion, 0.5)

sum_knapsack_capacity = knapsack_capacity(pesos)
#print(sum_knapsack_capacity)

# valor_maximo = maximum_value_weigths(data)

#print(valor_maximo)

poblacion_reparada = RP(resultado_random_poblacion, pesos, sum_knapsack_capacity)
print("Pobacion reparada: ")
print(poblacion_reparada)

# RP(resultado_random_poblacion, valores, sum_knapsack_capacity)

aptitud_reparada = AR(poblacion_reparada, valores)
print("Valor de aptitud reparada: ")
print(aptitud_reparada)






