from ortools.algorithms.python import knapsack_solver
from algorithm.genetic import Genetic
from numpy.random import randint
import os.path 


class Tests:

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

        
        max_test_number = max([index for index in range(1, 100) if os.path.isfile(f"rand_tests/Input{index}.txt")], default=0)
        test_number = max_test_number + 1

        file_filling(f"rand_tests/Input{test_number}.txt")

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

    def RandomMultipleAttempts(items: int = 3, attempts: int = 1) -> int:
        values, weights = randint(low=1, high=100, size=(2, items))
        capacity = randint(low=min(weights), high=sum(weights))
        knapsack = list(zip(values, weights))
        genetic_value = 0
        lib_value = 0
    
        for k in range(attempts):
            genetic = Genetic()
            lib = knapsack_solver.KnapsackSolver(
            knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
            "KnapsackExample",
            )
            genetic_value += genetic.solve(knapsack, capacity)[0]
            lib.init(values, [weights], [capacity])
            lib_value += lib.solve()
    
        return knapsack, capacity, genetic_value, lib_value


    def RandomMultipleCases(items: int = 3, cases: int = 1):
        genetic_results = []
        lib_results = []
        for _ in range(cases):
            result = Tests.Random(items)
            genetic_results.append(result[2][0])
            lib_results.append(result[3][0])
            
        return genetic_results, lib_results
