from random import getrandbits, randint, random

class Greed:
    def __init__(self):
        pass

    def evaluate(self, knapsack: list[tuple[int, int]], capacity: int) -> list[tuple[int, int]]:
        result_items = []
        result_weight = 0
        for value, weight in sorted(knapsack, reverse=True):
            if weight + result_weight <= capacity:
                result_weight += weight
                result_items.append((value, weight))

        return result_items


class Genetic:
    def __init__(self):
        self.initial_population_size = 10
        self.stop = False
        self.k_chromosomes_after_selection = 2 
        self.k_pairs_of_offsprings = 1
        self.mutate_chance = .4

    def solve(self, knapsack: list[tuple[int, int]], capacity: int) -> tuple[int, list[tuple[int, int]]]:
        population = self.initialize_population(len(knapsack))
        chromosome_values = [self.evaluate_chromosome_value(knapsack, capacity, chromosome) for chromosome in population]

        iteration = 0
        while not self.stop:
            # Selection
            population = self.select(population, chromosome_values)
            # Crossover
            population += self.crossover(population)
            # Mutation
            population = [self.mutate(chromosome) for chromosome in population]
            # Evaluation
            chromosome_values = [self.evaluate_chromosome_value(knapsack, capacity, chromosome) for chromosome in population]
            # Stop???
            if 50 < iteration:
                self.stop = True
            iteration += 1

        return self.extract_best(knapsack, population, chromosome_values)

    def initialize_population(self, size: int) -> list[str]:
        return [bin(getrandbits(size))[2:] for _ in range(self.initial_population_size)]

    def evaluate_chromosome_value(self, knapsack: list[tuple[int, int]], capacity: int, chromosome: str) -> int:
        total_value = 0
        for gen, item in zip(chromosome, knapsack):
            value, weight = item
            if gen:
                total_value += value
                capacity -= weight
            if capacity < 0:
                return 0
        return total_value

    def select(self, population: list[str], chromosome_values: list[int]) -> list[str]:
        pairs = [(x, y) for x, y in zip(chromosome_values, population)]
        pairs.sort(reverse=True)
        return [chromosome for _, chromosome in pairs[:self.k_chromosomes_after_selection]]

    def get_pivot(self, size: int) -> int:
        return randint(1, size)

    def get_parents(self, population: list[str]) -> list[tuple[str, str]]:
        parents = []
        for i in range(0, len(population), 2):
            parents.append((population[i], population[i+1]))

        if len(population) % 2:
            parents.append((population[0], population[-1]))

        return parents

    def crossover(self, population: list[str]) -> list[str]:
        offsprings = []
        parents = self.get_parents(population)

        for x, y in parents:
            for _ in range(self.k_pairs_of_offsprings):
                pivot = self.get_pivot(len(x))
                offsprings.append(x[:pivot] + y[pivot:])
                offsprings.append(y[:pivot] + x[pivot:])

        return offsprings

    # if it was in binary then
    # simply ~(chromosome^genes_to_mutate)
    def mutate(self, chromosome: str) -> str:
        total = []
        # I'm done
        for gen in chromosome:
            gen = False if gen == '0' else True
            mut = random() < self.mutate_chance
            if not mut and not gen:
                total_gen = '0'
            elif not mut and gen:
                total_gen = '1'
            elif mut and not gen:
                total_gen = '1'
            else:
                total_gen = '0'

            total.append(total_gen)
        
        return ''.join(total)

    def extract_best(self, knapsack: list[tuple[int, int]], population: list[str], values: list[int]) -> tuple[int, list[tuple[int, int]]]:
        ans_knapsack = []

        index = values.index(max(values))
        for index, gen in enumerate(population[index]):
            if gen:
                ans_knapsack.append(knapsack[index])

        return values[index], ans_knapsack



