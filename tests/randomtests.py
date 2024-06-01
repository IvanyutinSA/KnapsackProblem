from ortools.algorithms.python import knapsack_solver
from algorithm.genetic import Genetic
from numpy.random import randint
import datetime
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

        def files_filling(path):
                    with open(path, 'a') as f:
                                f.write(f"{len(values)} {capacity}\n")
                                for i in range(len(values)):
                                    f.write(f"{values[i]} {weights[i]}\n")

        if os.path.isfile(f"rand_tests/Input{self.test_number}.txt"):
            self.test_number += 1
        files_filling(f"rand_tests/Input{self.test_number}.txt")
        gentime_b = datetime.datetime.now().microsecond
        genetic_result = genetic.solve(knapsack, capacity)[0]
        gentime_e = datetime.datetime.now().microsecond
        gen_time = gentime_e - gentime_b
        
        lib.init(values, [weights], [capacity])
        libtime_b = datetime.datetime.now().microsecond
        lib_value = lib.solve()
        libtime_e = datetime.datetime.now().microsecond
        lib_time = libtime_e - libtime_b

        # packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
        lib_result = lib_value

        return genetic_result, lib_result, gen_time, lib_time
    
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
    def RandomMultipleAttempts(self, items: int = 3, attempts: int = 1) -> tuple[list[int], list[int], list[int], list[int]]:
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
        libtime_b = datetime.datetime.now().microsecond
        lib_value = lib.solve()
        libtime_e = datetime.datetime.now().microsecond
        lib_time = libtime_e - libtime_b
        gen_times = []
        for _ in range(attempts):
            gentime_b = datetime.datetime.now().microsecond
            genetic_value = genetic.solve(knapsack, capacity)[0]
            gentime_e = datetime.datetime.now().microsecond
            gen_time = gentime_e - gentime_b
            gen_times.append(gen_time)
            genetic_values.append(genetic_value)
            lib_values.append(lib_value)
    
        return genetic_values, lib_values, gen_times, [lib_time for _ in range(len(gen_times))]

    # Fixed
    def RandomMultipleCases(self, items: int = 3, cases: int = 1) -> tuple[list[int], list[int], list[int], list[int],]:
        genetic_results = []
        lib_results = []
        gen_times = []
        lib_times = []
        for _ in range(cases):
            genetic_value, lib_value, gen_time, lib_time = self.Random(items)
            genetic_results.append(genetic_value)
            lib_results.append(lib_value)
            gen_times.append(gen_time)
            lib_times.append(lib_time)
        return genetic_results, lib_results, gen_times, lib_times

    def RandomMultiple(self, items: int = 3, cases: int = 1, attempts: int = 1):
        genetic_results = []
        lib_results = []
        gen_times = []
        lib_times = []
        for _ in range(cases):
            genetic_attempt_results, lib_attempt_results, g_times, l_times  = self.RandomMultipleAttempts(items=items, attempts=attempts)
            genetic_results.extend(genetic_attempt_results)
            lib_results.extend(lib_attempt_results)
            gen_times.extend(g_times)
            lib_times.extend(l_times)
        return genetic_results, lib_results, gen_times, lib_times


