import copy
import random

import Constants
from Path import Path
from Segment import Segment
from Solution import Solution
from Board import Board


def mutate(sol: Solution, board: Board):
    result = copy.deepcopy(sol)

    for i in range(len(result.path_list)):
        if random.random() < Constants.MUTATION_PROBABILITY:
            mutate_path(result.path_list[i], board.point_pairs[i][0], board.width, board.height)
    return result


def repair_path(path: Path):
    new_segments = [path.segment_list[0]]

    # Check all segment_list in given path
    for i in range(1, len(path.segment_list)):
        # Get new segment if new_segments is empty(pop empty)
        if len(new_segments) == 0:
            new_segments.append(path.segment_list[i])
        # Delete empty segment_list
        elif len(new_segments) == 1 and new_segments[0].length == 0:
            new_segments.pop()
            new_segments.append(path.segment_list[i])
        elif path.segment_list[i].length > 0:
            # Merging same segments
            if path.segment_list[i].direction == new_segments[-1].direction:
                new_segments[-1].length += path.segment_list[i].length
            # Check opposite direction
            elif path.segment_list[i].direction == get_inverted_direction(new_segments[-1].direction):
                # Get difference between opposite directions
                if path.segment_list[i].length > new_segments[-1].length:
                    new_segments[-1].length = path.segment_list[i].length - new_segments[-1].length
                    new_segments[-1].direction = path.segment_list[i].direction
                elif path.segment_list[i].length == new_segments[-1].length:
                    new_segments.pop()
                else:
                    new_segments[-1].length -= path.segment_list[i].length
            else:
                new_segments.append(path.segment_list[i])

    path.segment_list = new_segments


# def mutate_path(path: Path, size_x, size_y):
def mutate_path(path: Path, start_point, size_x, size_y):
    mutation_index = random.randint(0, len(path.segment_list) - 1)
    mutation_segment_direction = path.segment_list[mutation_index].direction

    cord_point = path.get_point(start_point, mutation_index)

    mutation_limit = 0
    mutation_value = 0
    direction = ''
    # Split one long segment into two shorter segments
    if random.random() < 0.5:
        split_segment(path, mutation_index)
        if random.random() < 0.5:
            split_segment(path, mutation_index)
            mutation_index += 1
    # Get mutation value based on direction
    if mutation_segment_direction in ['N', 'S']:
        direction = 'E' if random.random() < 0.5 else 'W'
        if direction == 'E':
            mutation_limit = size_x - cord_point.x - 1
        else:
            mutation_limit = cord_point.x
    else:
        direction = 'N' if random.random() < 0.5 else 'S'
        if direction == 'N':
            mutation_limit = cord_point.y
        else:
            mutation_limit = size_y - cord_point.y - 1
    if mutation_limit > 0:
        mutation_value = random.randint(1, mutation_limit)
        path.segment_list.insert(mutation_index, Segment(direction, mutation_value))
        path.segment_list.insert(mutation_index + 2, Segment(get_inverted_direction(direction), mutation_value))
    repair_path(path)


def split_segment(path: Path, index: int):
    value = random.randint(0, path.segment_list[index].length)
    direction = path.segment_list[index].direction
    path.segment_list[index].length -= value
    path.segment_list.insert(index, Segment(direction, value))


def get_inverted_direction(direction):
    if direction == 'W':
        return 'E'
    if direction == 'E':
        return 'W'
    if direction == 'N':
        return 'S'
    return 'N'
