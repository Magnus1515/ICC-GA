from random import randrange, uniform,randint
import numpy as np

file_path = "Actividad3/Dataset-knapsack_100-Obj.txt"

with open(file_path, 'r') as file:
    for line in file:
            main_array = line.split()  # Split the line into words based on spaces
            #print(main_array)
    

    
        # Code to read the file goes here

print(main_array[0])
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
    
prueba_pesos2 = random_weigths(3)
prueba_poblacion = random_poblation(10,3)
#print(prueba_poblacion)

def knapsack_capacity(pesos):
    suma = np.sum(pesos)/2

    return suma

def relacion_suma_individual(pesos, poblacion):
    array_1 = np.array(pesos)
    array_2 = np.array(poblacion)

    resultado = np.dot(array_1, array_2)

    return resultado

def RP(poblacion,w,V):
    resultados = []
    index = 1
    for fila in poblacion:
        # fila = poblacion
        xj = fila
        print(f"Cromosoma Numero {index} -------------------")
        print(f"Cromosoma Inicial-> {xj}")
        # pesos = [5.8, 5.5, 7.7]
        #cromosomas ->  [1,1,0]
        print(f"Pesos -> {w}")
        print(f"Capacidad De Mochila -> {V}") 

        #print(f"Sumatoria -> {suma_rela}")
        knapsak_full  = False
        if(relacion_suma_individual(xj,w) > V):
            knapsak_full = True
        
        while knapsak_full == True:
            for i in range(len(xj)):
                if xj[i] == 1:
                    xj[i] = 0
                    #print(suma_rela_2)
                    if relacion_suma_individual(xj,w) < V:
                        knapsak_full = False
                        break
        
        while knapsak_full == False:
            for i in range(len(xj)):
                if xj[i] == 0:
                    xj[i] = 1
                    if relacion_suma_individual(xj,w) > V:
                        xj[i] = 0
                        knapsak_full = True
                        break
        
            
        resultados.append(xj)
        print(f"Cromosoma Final -> {xj}")
        index += 1
     
    return resultados

print(RP(random_poblation(5,3),random_weigths(3),knapsack_capacity(prueba_pesos2)))





