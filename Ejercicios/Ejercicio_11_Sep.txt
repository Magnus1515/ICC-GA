from random import randrange, uniform,randint

def random_poblation(cromosomas, genes):
    resultado = []
    for _ in range(0,cromosomas):
        lista = []
        for _ in range(0,genes):
            temp = randint(0,1)
            lista.append(temp)
        resultado.append(lista)
    return resultado

padres = random_poblation(2,8)



def recombinacion():
    padre_1 = padres[0]
    padre_2 = padres[1]
    while True :
        print("Seleccion el punto de recombinacion -> ")
        punto_recomb = int(input())
        if (punto_recomb >=1 and punto_recomb <=8):
            x = punto_recomb
            parte_1 = []
            parte_2 = []
            parte_3 = []
            parte_4 = []
            for i in range(0,punto_recomb):
                parte_1.append(padre_1[i])
            
            
            for i in range(0,punto_recomb):
                parte_2.append(padre_2[i])
         

            for i in range(punto_recomb, len(padre_1)):
                parte_3.append(padre_1[i])
          

            for i in range(punto_recomb, len(padre_2)):
                parte_4.append(padre_2[i])
            print("Padres")
            print(padre_1)
            print(padre_2)
            hijo_1 = parte_1 + parte_4
            hijo_2 = parte_2 + parte_3
            print("Hijos antes de mutar")
            print(hijo_1)
            print(hijo_2)
            print("Ingresa Gen a mutar -> ")
            punto_mutar = int(input()) 
            if(punto_mutar >=1 and punto_mutar <=8):
                punto_temp = punto_mutar-1
                if hijo_1[punto_temp] == 0:
                   hijo_1[punto_temp] = 1
                else:
                    hijo_1[punto_temp] = 0

                if hijo_2[punto_temp] == 0:
                    hijo_2[punto_temp] = 1
                else:
                    hijo_2[punto_temp] = 0
                

                print("Hijos Mutados")
                print(hijo_1)
                print(hijo_2)
                print("")
            else:
                print("Gen de mutacion invalido")
        else: 
            print("Punto de corte no valido")

    
print(recombinacion())
