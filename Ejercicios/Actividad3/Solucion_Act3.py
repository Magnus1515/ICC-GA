from random import randrange, uniform,randint
import numpy as np
#prueba_pesos = [8.61, 8.2, 1.51]  
#poblacion = [[1,0,1],[1,1,1],[1,0,0],[0,0,0],[1,1,0]]

#print(prueba_poblacion)
file_path = "Actividad3/Dataset-knapsack_100-Obj.txt"

def read_and_convert_data():
    data = []
    with open(file_path, 'r') as file:
        for line in file:
                main_array = np.array(line.split())
                main_array  
            #Split the line into words based on spaces
            #print(main_array)
        for i in main_array:
            x = float(i)
            data.append(x)
    return data 


def random_poblation(cromosomas, genes):
    resultado = []
    for _ in range(0,cromosomas):
        lista = []
        for _ in range(0,genes):
            temp = randint(0,1)
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


def RP(poblacion,w,V):
    resultados = []
    values_init_list = []
    values_repair_list = []
    index = 1
    for fila in poblacion:
        # fila = poblacion
        xj = fila
        print(f"Cromosoma Numero {index} -------------------")
        print(f"Cromosoma Inicial-> {xj}")
        
        #print(f"Pesos -> {w}")
        
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
        print(f"Cromosoma Final -> {xj}")        
        index += 1
    print(f"Capacidad De Mochila ->           {V}") 
    print("POBLACION INICIAL -> ",values_init_list)
    print("POBLACION REPARADA ->" , values_repair_list)
    print(f"Maximo valor pesos Pob Inicial -> {maximum_value_weigths(values_init_list)}")
    print(f"Maximo valor pesos Pob Reparada-> {maximum_value_weigths(values_repair_list)}")
    print(f"Minimo valor pesos Pob Inicial -> {minium_value_weigths(values_init_list)}")
    print(f"Minimo valor pesos Pob Reparada-> {minium_value_weigths(values_repair_list)}")
    print(f"Promedio pesos Pob Inicial ->     {average_value_weigths(values_init_list)}")
    print(f"Promedio pesos Pob Reparada->     {average_value_weigths(values_repair_list)}")
    print(f"Desviacion Estandar Pob Inicial-> {standar_deaviation_weigths(values_init_list)}")
    print(f"Desviacion Estandar Pob Reparad-> {standar_deaviation_weigths(values_repair_list)}")

    #return resultados

    # return print("valor maximo de los cromosomas", maximum_value_weigths(maximum_value_list), "La lista completa" , maximum_value_list)
    #return print(maximum_value_list)

data = read_and_convert_data()
resultado_random_poblacion = random_poblation(100,100)
sum_knapsack_capacity =  knapsack_capacity(data)
valor_maximo = maximum_value_weigths(data)  
#print(valor_maximo)

#print(RP(resultado_random_poblacion,data,sum_knapsack_capacity))
RP(resultado_random_poblacion,data,sum_knapsack_capacity)




