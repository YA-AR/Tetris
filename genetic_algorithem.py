import numpy as np
import random

class GeneticAlgorithem:
    def __init__(self, generation_num, population_size, parameter_num,
                 fitness_function, best_num, crossover_ratio, frequency, draw = False):
        population = np.random.uniform(-1, 1, (population_size, parameter_num))
        for i in range(generation_num):
            fitness = calc_population_fitness(population, fitness_function, draw)
            best = np.argmax(fitness)
            s = fitness_function(population[best], True)
            print(s)
            parents = choose_best(population, fitness, best_num)
            offspring = crossover(parents, population_size, crossover_ratio)
            population = mutation(offspring, frequency)

        print(population, max(fitness))


def calc_population_fitness(population, fitness_function, draw):
    # Calculating the fitness values of each solution in the current population.
    p = []
    for weights in population:
        fitness = fitness_function(weights, draw)
        p.append(fitness)
    return p


def choose_best(population, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = []
    for i in range(num_parents):
        index = np.argmax(fitness)
        parents.append(population[index])
        fitness[index] = -1
    return parents


def crossover(parents, offspring_size, crossover_ratio):
    offspring = []
    crossover_point = int(crossover_ratio*len(parents[0]))
    for k in range(0, offspring_size, 2):
        p_1 = k % len(parents)
        p_2 = (k+1) % len(parents)
        offspring.append(list(parents[p_1][0:crossover_point]) + list(parents[p_2][crossover_point:]))
        offspring.append(list(parents[p_2][0:crossover_point]) + list(parents[p_1][ crossover_point:]))

    return offspring

    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    crossover_point = numpy.uint8(offspring_size[1] / 2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k % parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k + 1) % parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring, frequency):

    for idx in range(len(offspring)):
        is_mutation = np.random.uniform(0, 1)
        if is_mutation < frequency:
            mutation_place = np.random.randint(len(offspring[0]))
            mutation_value = np.random.uniform(-1, 1)
            offspring = list(offspring)
            offspring[idx][mutation_place] = mutation_value


    return offspring

