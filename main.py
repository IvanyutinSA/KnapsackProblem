from algorithm.genetic import Genetic
import numpy as np
from itertools  import product
import random
import test_algorithms

def error_rate(true, actual):
    return true - actual

def test_evaluation(N, R, iterations=10):
    for i in range(iterations):
        knapsack1 = random.sample(list(product(range(1, R + 1), repeat = 2)), N)
        capacity1 = random.randint(1, R) 
        
        print(f"knapsack1: {knapsack1}, capacity1: {capacity1}")
        print("-----------------------------------")
        actual = genetic.solve(knapsack1, capacity1)[0]

        greedy = test_algorithms.knapsack_greedy(N, capacity1, knapsack1)
        dynamic = test_algorithms.knapsack_dynamic(N, capacity1, knapsack1)
        true = max(greedy, dynamic)
        print(f"actual: {actual}, true: {true}")
        print(f"error rate: {error_rate(true, actual)}")

genetic = Genetic()
knapsack = [(10, 3), (5, 2), (6, 2)]
capacity = 4

print(genetic.solve(knapsack, capacity))

knapsack = [
    (60, 10),
    (100, 20),
    (120, 30),
]
capacity = 50
print(genetic.solve(knapsack, capacity))
# value - weight
N = 10
R = 1000

test_evaluation(N, R)

