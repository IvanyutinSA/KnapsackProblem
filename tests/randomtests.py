from ortools.algorithms.python import knapsack_solver
from algorithm.genetic import Genetic
from numpy.random import randint

import os.path 
# import sys
# if os.path.dirname(os.path.dirname(os.path.realpath(__file__))) not in sys.path:
#       sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class Tests:
    def __init__(self, test_number: int = -1, alg: Genetic = Genetic()):
              self.test_number = test_number
              self.alg = alg

    # Fixed
    def Random(self, items: int = 3) -> tuple[int, int]:
        genetic = self.alg
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

        if os.path.isfile(f"rand_tests/Input{self.test_number}.txt"):
            self.test_number += 1
        file_filling(f"rand_tests/Input{self.test_number}.txt")

        genetic_result = genetic.solve(knapsack, capacity)[0]

        lib.init(values, [weights], [capacity])
        lib_value = lib.solve()
        # packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
        lib_result = lib_value

        return genetic_result, lib_result
    
    # I don't know for what this's for
    # def Library(self, capacity: int, values: list, weights: list) -> tuple[int, int]:
    #     genetic = self.alg
    #     lib = knapsack_solver.KnapsackSolver(
    #     knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
    #     "KnapsackExample",
    #     )
    #
    #     knapsack = list(zip(values, weights))
    #     
    #     genetic_result = genetic.solve(knapsack, capacity)[0]
    #     
    #     lib.init(values, [weights], [capacity])
    #     lib_value = lib.solve()
    #     # packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
    #     lib_result = lib_value
    #
    #     return genetic_result, lib_result

    # Fixed
    def RandomMultipleAttempts(self, items: int = 3, attempts: int = 1) -> tuple[list[int], list[int]]:
        values, weights = randint(low=1, high=100, size=(2, items))
        capacity = randint(low=min(weights), high=sum(weights))
        knapsack = list(zip(values, weights))
        genetic_value = 0
        lib_value = 0
        genetic_values = []
        lib_values = []
    
        genetic = self.alg
        lib = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
        )
        lib.init(values, [weights], [capacity])
        lib_value = lib.solve()
        for _ in range(attempts):
            genetic_value = genetic.solve(knapsack, capacity)[0]
            genetic_values.append(genetic_value)
            lib_values.append(lib_value)
    
        return genetic_values, lib_values

    # Fixed
    def RandomMultipleCases(self, items: int = 3, cases: int = 1) -> tuple[list[int], list[int]]:
        genetic_results = []
        lib_results = []
        for _ in range(cases):
            genetic_value, lib_value = self.Random(items)
            genetic_results.append(genetic_value)
            lib_results.append(lib_value)
            
        return genetic_results, lib_results

    def RandomMultiple(self, items: int = 3, cases: int = 1, attempts: int = 1):
        genetic_results = []
        lib_results = []
        for _ in range(cases):
            genetic_attempt_results, lib_attempt_results = self.RandomMultipleAttempts(items=items, attempts=attempts)
            genetic_results.extend(genetic_attempt_results)
            lib_results.extend(lib_attempt_results)
        return genetic_results, lib_results


