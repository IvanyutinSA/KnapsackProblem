knapsack, capacity, genetic_result, lib_result = Tests.Random(items=5)
print("Knapsack:", knapsack)
print("Capacity:", capacity)
print("Genetic Result:", genetic_result)
print("Library Result:", lib_result)

knapsack, capacity, genetic_value, lib_value = Tests.RandomMultipleAttempts(items=30, attempts=10)
print("Genetic Value:", genetic_value)
print("Library Value:", lib_value)

genetic_results, lib_results = Tests.RandomMultipleCases(items=100, cases=10)
print("Genetic Results:", genetic_results)
print("Library Results:", lib_results)
