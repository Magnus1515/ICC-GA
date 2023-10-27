# import numpy as np

# lista =[135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]

# #print(sum(lista))
# Best_Cromosome =[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1] 

# def operation_aptitud(poblacion, costos):
#     array_1 = np.array(poblacion)
#     array_2 = np.array(costos)

#     resultado = np.dot(array_1, array_2)

#     return resultado.tolist()

# print(operation_aptitud(Best_Cromosome,lista))


from tabulate import tabulate

# Sample data in two separate lists
names = ["Alice", "Bob", "Charlie"]
ages = [28, 24, 22]

# Combine the lists into a list of lists
data = list(zip(names, ages))

# Create a table with the "fancy_grid" style
table = tabulate(data, headers=["Name", "Age"], tablefmt="fancy_grid")

# Print the fancy grid table
print(table)

