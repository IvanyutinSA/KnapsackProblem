from algorithm.genetic import Genetic
from tests.randomtests import Tests

def test(knapsack, capacity):
    genetic = Genetic()
    return genetic.solve(knapsack, capacity)

def display_action(f):
    print(f())

def main():
    knapsack = [
    ]

    knapsacks = [
        [
            (60, 10),
            (100, 20),
            (120, 30),
        ],
        [
            (300,75),
            (500,80),
            (400,100),
            (200,50),
            (200,40),
            (200,70),
            (300,80),
            (200,30),
            (100,30),
            (200,60),
            (150,20),
            (150,30),
            (250,45),
            (250,70),
            (150,30),
            (100,20),
            (300,70),
            (25,10),
            (30,20),
            (45,25),
            (175,30),
            (25,40),
            (250,40),
            (20,30),
            (30,35),
            (200,40),
            (100,80),
            (150,25),
            (100,25)
        ],
    ]

    capacities = [50, 20]


    for index, knapsack, capacity in zip(range(1, len(knapsacks)+1),knapsacks, capacities):
        print(f'{index} | {capacity} | {knapsack}')
        for i in range(1, 4):
            print(f'{i} try: ', end='')
            display_action(lambda: test(knapsack, capacity))
        print()


def rand_tests():
    t = Tests();
    knapsack, capacity, genetic_result, lib_result = t.Random(items=500)
    print("Knapsack:", knapsack)
    print("Capacity:", capacity)
    print("Genetic Result:", genetic_result)
    print("Library Result:", lib_result)


if __name__ == '__main__':
    main();
    rand_tests();

