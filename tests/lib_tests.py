from algorithm.genetic import Genetic
from ortools.algorithms.python import knapsack_solver

# TEST FILES FORMAT:
# 
# dim capacity 
# value weight

# Adjusted
def lib_tests(alg: Genetic = Genetic()):
    n = 4
    genetic_results = []
    lib_results = []
    for i in range(1, n+1):
        with open(f"test_cases/Input{i}.txt") as f:
            dim, capacity = map(int, f.readline().split())
            values = []
            weights = []
            for i in range(dim):
                v, w = map(int, f.readline().split())
                values.append(v)
                weights.append(w)

            genetic_result, lib_result = help_function(capacity, values, weights, alg=alg)
            genetic_results.append(genetic_result)
            lib_results.append(lib_result)
    return genetic_results, lib_results


            
    
# I don't know for what this's for
def help_function(capacity: int, values: list, weights: list, alg: Genetic = Genetic()) -> tuple[int, int]:
    genetic = alg
    lib = knapsack_solver.KnapsackSolver(
    knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
    "KnapsackExample",
    )

    knapsack = list(zip(values, weights))
    
    genetic_result = genetic.solve(knapsack, capacity)[0]
    
    lib.init(values, [weights], [capacity])
    lib_value = lib.solve()
    # packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
    lib_result = lib_value

    return genetic_result, lib_result

