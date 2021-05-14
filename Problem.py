from typing import List

from Board import Board
from Constants import POPULATION_SIZE, WEIGHT
from PopulationGenerator import generate_random_path_list
from Solution import Solution
from statistics import stdev, mean


class Problem:
    def __init__(self, board: Board = Board()):

        self.__solution_list: List[Solution] = []
        self.__cost_list: List[int] = []
        self.__board: Board = board

    def calculate_points(self, solution_index: int):
        path_points = {}
        # Iterate through all paths for given solution index
        for j in range(len(self.__solution_list[solution_index].path_list)):
            current_position = self.__board.point_pairs[j][0]
            if current_position in path_points:
                path_points[current_position] += 1
            else:
                path_points[current_position] = 0
            # Iterating through all segments of path
            for segment in self.__solution_list[solution_index].path_list[j].segment_list:
                # Adding all points between the segment starting and ending position to hash table
                for point in segment.get_points_between(current_position):
                    if point in path_points:
                        path_points[point] += 1
                    else:
                        path_points[point] = 0
                current_position = segment.get_end_point(current_position)
                if current_position in path_points:
                    path_points[current_position] += 1
                else:
                    path_points[current_position] = 0
        return path_points

    def calculate_points_out_of_bounds(self, path_points):
        points_out_of_bounds = 0
        for point in path_points:
            if point.x < 0 or point.y < 0 or point.x >= self.__board.width or point.y > self.__board.height:
                points_out_of_bounds += 1
        return points_out_of_bounds

    def calculate_paths_len_segment_num(self, solution_index):
        paths_length = 0
        segment_number = 0
        for path in self.__solution_list[solution_index].path_list:
            for segment in path.segment_list:
                paths_length += segment.length
                segment_number += 1
        return paths_length, segment_number,

    def calculate_cost(self):
        self.__cost_list = []
        for i in range(len(self.__solution_list)):
            solution_points = self.calculate_points(i)
            common_points_num = sum(solution_points.values())
            points_out_of_bounds_num = self.calculate_points_out_of_bounds(solution_points)
            paths_len, num_segments = self.calculate_paths_len_segment_num(i)

            cost = common_points_num * WEIGHT['COMMON_POINTS'] + \
                   points_out_of_bounds_num * WEIGHT['OUT_OF_BOUNDS_POINTS'] + \
                   paths_len * WEIGHT['PATHS_LENGTH'] + \
                   num_segments * WEIGHT['NUMBER_OF_SEGMENTS']

            self.__cost_list.append(cost)

    # def calculate_new(self):
    #     self.calculate_points(self.__new_solution)
    #     self.calculate_common_points()
    #     self.calculate_points_outside()
    #     self.calculate_details()
    #
    # def optimize_random(self):
    #     self.reset()
    #     self.__new_solution = generate_random_path_list(self.__board)
    #     self.calculate_new()
    #     temp = self.get_cost()
    #     if self.__current_cost > temp:
    #         self.__solution = self.__new_solution
    #         self.__current_cost = temp

    def get_solution_with_cost(self, index):
        return self.__solution_list[index], self.__cost_list[index],

    def start_population(self):
        for _ in range(POPULATION_SIZE):
            self.__solution_list.append(generate_random_path_list(self.__board))

    def append_solution(self, sol: Solution):
        self.__solution_list.append(sol)

    def get_best_solution_with_cost(self):
        result = self.get_solution_with_cost(0)
        for i in range(1, POPULATION_SIZE):
            if result[1] > self.get_solution_with_cost(i)[1]:
                result = self.get_solution_with_cost(i)
        return result

    def get_statistics(self):
        helper = [self.get_cost(i) for i in range(0, POPULATION_SIZE)]
        result = {
            'max': max(helper),
            'avg': mean(helper),
            'min': min(helper),
            'std': stdev(helper)
        }
        return result

    def get_cost(self, index):
        return self.__cost_list[index]

    @property
    def solution_list(self):
        return self.__solution_list

    @solution_list.setter
    def solution_list(self, new_solution):
        self.__solution_list = new_solution

    @property
    def population_size(self):
        return len(self.__solution_list)

    @property
    def board(self):
        return self.__board
