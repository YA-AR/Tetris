from genetic_algorithem import GeneticAlgorithem
import graphic_interface as gi


if __name__ == '__main__':
    a = GeneticAlgorithem(generation_num = 5, population_size = 10, parameter_num = 10,
                 fitness_function  = gi.graphic , best_num = 5, crossover_ratio = 0.5, frequency = 0.1)
