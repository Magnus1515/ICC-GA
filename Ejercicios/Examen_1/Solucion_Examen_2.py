padre_1 = [1, 0, 1, 1, 1, 0, 0, 0]
padre_2 = [0, 0, 1, 0, 1, 0, 1, 0]

print("Selecciona el punto de recombinación -> ")
punto_recomb = int(input())
parte_1 = []
parte_2 = []
parte_3 = []
parte_4 = []

if (punto_recomb >= 1 and punto_recomb <= 8):

    parte_1 = padre_1[:punto_recomb]
    parte_2 = padre_2[:punto_recomb]
    parte_3 = padre_1[punto_recomb:]
    parte_4 = padre_2[punto_recomb:]
    
    hijo_1 = parte_1 + parte_4
    hijo_2 = parte_2 + parte_3
    
    print("Hijo 1:")
    print(hijo_1)
    print("Hijo 2:")
    print(hijo_2)
else:
    print("El punto de recombinación debe estar entre 1 y 7.")
