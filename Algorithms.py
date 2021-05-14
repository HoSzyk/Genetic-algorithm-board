import copy
import random
import Constants
from Operators import Selection, Crossover, Mutation
from Problem import *


def genetic(problem, selection):
    start_stat_file()
    best_solution_with_cost = problem.get_best_solution_with_cost()
    for i in range(Constants.NUMBER_OF_GENERATIONS):
        if selection == 'r':
            helper = Selection.calculate_roulette_probabilities(problem)
        get_stats_to_file(problem)
        new_generation = Problem(problem.board)
        while new_generation.population_size != problem.population_size:

            if selection == 'r':
                p1 = Selection.roulette_selection(problem, helper)
                p2 = Selection.roulette_selection(problem, helper)
            else:
                p1 = Selection.tourney_selection(problem)
                p2 = Selection.tourney_selection(problem)

            if random.random() < Constants.CROSSOVER_PROBABILITY:
                des1, des2 = Crossover.crossover_path(p1, p2)
            else:
                des1, des2 = p1, p2

            des1 = Mutation.mutate(des1, problem.board)
            des2 = Mutation.mutate(des2, problem.board)

            new_generation.append_solution(des1)
            new_generation.append_solution(des2)

        new_generation.calculate_cost()
        best_generation_solution_with_cost = new_generation.get_best_solution_with_cost()
        if best_solution_with_cost[1] > best_generation_solution_with_cost[1]:
            best_solution_with_cost = copy.deepcopy(best_generation_solution_with_cost)

        if i % 10 == 0:
            best_generation_solution_with_cost[0].show(problem.board)

        problem = new_generation

        print(f'\n------------------------------------\nGeneration {i}\nBest Solution:\n {best_solution_with_cost}')
        print(f'\nBest in generation: \n{best_generation_solution_with_cost}')

    return best_solution_with_cost


def random_method(problem):
    start_stat_file()
    best_solution_with_cost = copy.deepcopy(problem.get_best_solution_with_cost())
    for i in range(Constants.NUMBER_OF_GENERATIONS):
        problem.solution_list = []
        problem.start_population()
        problem.calculate_cost()

        best_generation_solution_with_cost = problem.get_best_solution_with_cost()
        if best_solution_with_cost[1] > best_generation_solution_with_cost[1]:
            best_solution_with_cost = copy.deepcopy(best_generation_solution_with_cost)

        get_stats_to_file(problem)

        print(f'\n------------------------------------\nGeneration {i}\nBest Solution:\n {best_solution_with_cost}')
        print(f'\nBest in generation: \n{best_generation_solution_with_cost}')

    return best_solution_with_cost


def start_stat_file():
    with open('stats.txt', 'w') as writer:
        writer.write('worst,avg,best,std\n')


def get_stats_to_file(problem: Problem):
    stats = problem.get_statistics()
    with open('stats.txt', 'a') as writer:
        for value in stats.values():
            writer.write(f'{value},')
        writer.write('\n')
