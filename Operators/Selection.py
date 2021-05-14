import random
import Constants
from Problem import Problem


def get_random_indexes(max_number):
    return random.sample(range(max_number), Constants.TOURNEY_SIZE)


def tourney_selection(problem: Problem):
    tourney = [problem.get_solution_with_cost(i) for i in get_random_indexes(Constants.POPULATION_SIZE)]
    return min(tourney, key=lambda x: x[1])[0]


def roulette_selection(problem: Problem, tourney_weights):
    # sum_cost = 0
    # for i in range(Constants.POPULATION_SIZE):
    #     sum_cost += problem.get_solution_with_cost(i)[1]
    #
    # tourney_weights = []
    # for i in range(Constants.POPULATION_SIZE):
    #     weight = problem.get_solution_with_cost(i)[1] / sum_cost
    #     weight = 1 - weight
    #     weight = weight / (Constants.POPULATION_SIZE - 1)
    #     tourney_weights.append(weight)

    roulette_result = random.random()
    helper = 0
    result_index = 0
    while helper < roulette_result and result_index < Constants.POPULATION_SIZE:
        helper += tourney_weights[result_index]
        result_index += 1
    return problem.get_solution_with_cost(result_index - 1)[0]


def calculate_roulette_probabilities(problem: Problem):
    # sum_cost = 0
    # for i in range(Constants.POPULATION_SIZE):
    #     sum_cost += problem.get_cost(i)
    #
    # tourney_weights = []
    # for i in range(Constants.POPULATION_SIZE):
    #     weight = problem.get_cost(i) / sum_cost
    #     weight = 1 - weight
    #     weight = weight / (Constants.POPULATION_SIZE - 1)
    #     tourney_weights.append(weight)

    sum_cost = 0
    for i in range(Constants.POPULATION_SIZE):
        sum_cost += 1/problem.get_cost(i)

    tourney_weights = []
    for i in range(Constants.POPULATION_SIZE):
        weight = sum_cost/problem.get_cost(i)
        tourney_weights.append(weight)

    return tourney_weights
