import copy
from random import randrange, random

from Solution import Solution


def crossover_path(sol_one: Solution, sol_two: Solution):
    path_list_len = len(sol_one.path_list)

    descendant_one = copy.deepcopy(sol_one)
    descendant_two = copy.deepcopy(sol_two)

    path_index = randrange(path_list_len)
    temp = descendant_one.path_list[path_index]
    descendant_one.path_list[path_index] = descendant_two.path_list[path_index]
    descendant_two.path_list[path_index] = temp

    return descendant_one, descendant_two,
