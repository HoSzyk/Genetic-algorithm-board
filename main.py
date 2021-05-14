import random

import Algorithms
import Constants
from Board import Board
from Point import Point
from Problem import Problem
from Operators.Mutation import mutate
from Segment import Segment

if __name__ == '__main__':
    if Constants.SEED:
        random.seed(Constants.SEED)

    random_problem = Problem(Board.load_from_file('test_files/zad1.txt'))
    random_problem.start_population()
    for i in range(len(random_problem.solution_list)):
        for _ in range(25):
            random_problem.solution_list[i] = mutate(random_problem.solution_list[i], random_problem.board)
    random_problem.calculate_cost()

    # for sol in random_problem.solution_list:
    #     sol.show(random_problem.board)

    result = Algorithms.genetic(random_problem, 'r')

    # result = Algorithms.random_method(random_problem)

    result[0].show(random_problem.board)

    # sol_one = sel.roulette_selection(random_problem)
    # sol_two = sel.roulette_selection(random_problem)
    # print(cros.crossover_path(sol_one, sol_two))
    # print('--------------------')
    # print(mut.mutate_whole_segment(sol_one))


    # seg1 = Segment('S', 7)
    # seg2 = Segment('E', 3)
    # seg3 = Segment('N', 1)
    # seg4 = Segment('E', 1)
    # yep = [seg1, seg2, seg3, seg4]
    #
    #
    # path = Path([seg1, seg2, seg3, seg4])
    # print(path)
    # mut.mutate_path(path)
    # print(path)
    print()

