import random

from Board import Board
from Path import Path
from Point import Point
from Segment import Segment
from Solution import Solution


def generate_random_path_list(board: Board):
    result_solution = Solution()

    for start_point, end_point in board.point_pairs:
        cur_point = start_point
        cur_path = Path()

        horizontal = random.random() < 0.5

        while cur_point != end_point:
            cur_segment = get_random_segment(cur_point, end_point, board, horizontal)
            cur_path.append_segment(cur_segment)
            cur_point = cur_segment.get_end_point(cur_point)
            horizontal = not horizontal

        result_solution.append_path(cur_path)

    return result_solution


def get_random_segment(start_point: Point, end_point: Point, board: Board, horizontal: bool):
    result_segment = Segment()

    if horizontal:
        result_segment.length = start_point.x - end_point.x
        if result_segment.length > 0:
            result_segment.direction = 'W'
        elif result_segment.length < 0:
            result_segment.direction = 'E'
            result_segment.length = abs(result_segment.length)
        else:
            result_segment.direction = 'E' if random.random() < 0.5 else 'W'
            result_segment.length = 1
    else:
        result_segment.length = start_point.y - end_point.y
        if result_segment.length > 0:
            result_segment.direction = 'N'
        elif result_segment.length < 0:
            result_segment.direction = 'S'
            result_segment.length = abs(result_segment.length)
        else:
            result_segment.direction = 'N' if random.random() < 0.5 else 'S'
            result_segment.length = 1

    result_segment.direction = set_direction_within_bounds(start_point,
                                                           horizontal,
                                                           board,
                                                           result_segment.direction)
    result_segment.length = random.randint(1, result_segment.length)
    return result_segment


def set_direction_within_bounds(point: Point, horizontal: bool, board: Board, direction):
    if horizontal:
        if point.x == 0:
            direction = 'E'
        elif point.x == board.width - 1:
            direction = 'W'
    else:
        if point.y == 0:
            direction = 'S'
        elif point.y == board.width - 1:
            direction = 'N'
    return direction
