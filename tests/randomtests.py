from ortools.algorithms.python import knapsack_solver
from numpy.random import randint

class Tests:
    def Random(items: int = 3):
        genetic = Genetic()
        lib = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
        )

        values, weights = randint(low=1, high=100, size=(2, items))
        capacity = randint(low=min(weights), high=sum(weights))
        knapsack = list(zip(values, weights))
        
        genetic_result = genetic.solve(knapsack, capacity)

        lib.init(values, [weights], [capacity])
        lib_value = lib.solve()
        packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
        lib_result = lib_value, packed_items

        return knapsack, capacity, genetic_result, lib_result
