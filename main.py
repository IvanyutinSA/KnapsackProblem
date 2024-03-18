from algorithm.genetic import Genetic


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

