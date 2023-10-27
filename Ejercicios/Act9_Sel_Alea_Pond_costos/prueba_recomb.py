# import random

# def two_point_crossover(parent1, parent2):
#     if len(parent1) != len(parent2):
#         raise ValueError("Parents must have the same length")

#     # Choose two distinct random crossover points
#     crossover_points = sorted(random.sample(range(1, len(parent1)), 2))
#     print(crossover_points)
#     # Perform two-point crossover
#     child1 = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]
#     child2 = parent2[:crossover_points[0]] + parent1[crossover_points[0]:crossover_points[1]] + parent2[crossover_points[1]:]

#     return child1, child2

# # Example usage:
# parent1 = [1, 2, 3, 4, 5, 6]
# parent2 = [7, 8, 9, 10, 11, 12]
# child1, child2 = two_point_crossover(parent1, parent2)
# print("Child 1:", child1)
# print("Child 2:", child2)

import random

def two_thirds_crossover(parent1, parent2):
    if len(parent1) != len(parent2):
        raise ValueError("Parents must have the same length")

    length = len(parent1)
    one_third = length // 3
    two_thirds = 2 * one_third
    print(one_third,two_thirds)
    # Perform two-thirds crossover
    child1 = parent1[:one_third] + parent2[one_third:two_thirds] + parent1[two_thirds:]
    child2 = parent2[:one_third] + parent1[one_third:two_thirds] + parent2[two_thirds:]

    return child1, child2

# Example usage:
parent1 = [1, 2, 3, 4, 5, 6]
parent2 = [7, 8, 9, 10, 11,12]
child1, child2 = two_thirds_crossover(parent1, parent2)
print("Child 1:", child1)
print("Child 2:", child2)
