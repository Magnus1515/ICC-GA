# def mutate_population(population, mutation_rate):
#     selected_cromos = math.floor(len(population) * mutation_rate)
#     # selected_cromos_values = random.choices(population, k=selected_cromos)
#     selected_cromos_index = [randint(0, len(population) - 1) for _ in range(selected_cromos)]

#     for chrom_idx in selected_cromos_index:
#         print(f"CHROMOSOME TO MUT:{population[chrom_idx]}")
#         aleatorio = randint(0, 5)
#         print(f"INDEX TO MUT:{aleatorio}")
#         if population[chrom_idx][aleatorio] == 0:
#             population[chrom_idx][aleatorio] = 1
#         else:
#             population[chrom_idx][aleatorio] = 0
#         print(f"CHROMOSOME AFTER MUT:{population[chrom_idx]}")
#         # selected_temp = population.index(chromosome)
#         # selected_cromos_index.append(selected_temp)
#     return population
