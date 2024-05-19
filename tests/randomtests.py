from ortools.algorithms.python import knapsack_solver
from algorithm.genetic import Genetic
from numpy.random import randint

import os.path 
# import sys
# if os.path.dirname(os.path.dirname(os.path.realpath(__file__))) not in sys.path:
#       sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class Tests:
    test_number = 1
    def Random(self, items: int = 3):
        genetic = Genetic()
        lib = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
        )

        values, weights = randint(low=1, high=100, size=(2, items))
        capacity = randint(low=min(weights), high=sum(weights))
        knapsack = list(zip(values, weights))
        def file_filling(path):
                        with open(path, 'a') as f:
                                f.write(f"{len(values)} {capacity}\n")
                                for i in range(len(values)):
                                    f.write(f"{values[i]} {weights[i]}\n")

        if os.path.isfile(f"rand_tests/Input{Tests.test_number}.txt"):
            Tests.test_number += 1
        file_filling(f"rand_tests/Input{Tests.test_number}.txt")

        genetic_result = genetic.solve(knapsack, capacity)

        lib.init(values, [weights], [capacity])
        lib_value = lib.solve()
        packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
        lib_result = lib_value, packed_items
        
        

        return knapsack, capacity, genetic_result, lib_result
    
    def Library(capacity: int, values: list, weights: list):
        genetic = Genetic()
        lib = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
        )

        knapsack = list(zip(values, weights))
        
        genetic_result = genetic.solve(knapsack, capacity)
        
        lib.init(values, [weights], [capacity])
        lib_value = lib.solve()
        packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
        lib_result = lib_value, packed_items

        return knapsack, capacity, genetic_result, lib_result

