from tests.randomtests import Tests
# TEST FILES FORMAT:
# 
# dim capacity 
# value weight
def lib_tests():
    n = 4
    for i in range(1, n+1):
        with open(f"test_cases/Input{i}.txt") as f:
            dim, capacity = map(int, f.readline().split())
            values = []
            weights = []
            for i in range(dim):
                v, w = map(int, f.readline().split())
                values.append(v)
                weights.append(w)

            knapsack, capacity, genetic_result, lib_result = Tests.Library(capacity, values, weights)
            print("Knapsack:", knapsack)
            print("Capacity:", capacity)
            print("Genetic Result:", genetic_result)
            print("Library Result:", lib_result)
