from algorithm.genetic import Genetic
from ortools.algorithms.python import knapsack_solver
import datetime

# TEST FILES FORMAT:
# 
# dim capacity 
# value weight

# Adjusted
def  lib_tests(alg: Genetic = Genetic()):
    n = 9
    genetic_results = []
    lib_results = []
    gen_times = []
    lib_times = []
    answers = []
    for i in range(1, n+1):
        with open(f"test_cases/Input{i}.txt") as f:
            dim, capacity = map(int, f.readline().split())
            values = []
            weights = []
            for _ in range(dim):
                v, w = map(int, f.readline().split())
                values.append(v)
                weights.append(w)
            genetic_result, lib_result, gen_time, lib_time = help_function(capacity, values, weights, alg=alg)
            genetic_results.append(genetic_result)
            lib_results.append(lib_result)
            gen_times.append(gen_time)
            lib_times.append(lib_time)
        with open(f"test_cases/Output{i}.txt") as f:
            answers.append(int(f.readline().strip()))

    return genetic_results, lib_results, answers, gen_times, lib_times

            
    
# I don't know for what this's for
def help_function(capacity: int, values: list, weights: list, alg: Genetic = Genetic()) -> tuple[int, int]:
    genetic = alg
    lib = knapsack_solver.KnapsackSolver(
    knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
    "KnapsackExample",
    )

    knapsack = list(zip(values, weights))
    gentime_begin = datetime.datetime.now().microsecond
    
    genetic_result = genetic.solve(knapsack, capacity)[0]
    gentime_end = datetime.datetime.now().microsecond
    gen_time = gentime_end - gentime_begin
    lib.init(values, [weights], [capacity])
    libtime_begin = datetime.datetime.now().microsecond
    lib_value = lib.solve()
    libtime_end = datetime.datetime.now().microsecond
    lib_time = libtime_end - libtime_begin
    # packed_items = [knapsack[i] for i in range(len(values)) if lib.best_solution_contains(i)]
    lib_result = lib_value

    return genetic_result, lib_result, gen_time, lib_time

