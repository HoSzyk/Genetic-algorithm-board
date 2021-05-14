import time

import matplotlib.pyplot as plt
import numpy as np
from typing import List
from Path import Path
from Board import Board


class Solution:
    def __init__(self):
        self.__path_list: List[Path] = []

    @property
    def path_list(self):
        return self.__path_list

    @path_list.setter
    def path_list(self, new_path_list):
        self.__path_list = new_path_list

    def append_path(self, path):
        self.__path_list.append(path)

    def __repr__(self):
        return f'Paths:\n {list(map(str, self.__path_list))}'

    def show(self, board: Board):
        points = []
        points_cords = []
        plt.cla()
        plt.axis([0, board.width, 0, board.height])
        # Step for axis
        plt.xticks(np.arange(-1, board.width + 1, 1))
        plt.yticks(np.arange(-1, board.height + 1, 1))
        plt.grid()
        plt.gca().invert_yaxis()
        for i in range(len(self.__path_list)):
            cur_position = board.point_pairs[i][0]

            points.append(cur_position.get_tuple())

            for segment in self.__path_list[i].segment_list:
                points += [i.get_tuple() for i in segment.get_points_between(cur_position)]
                cur_position = segment.get_end_point(cur_position)
                points.append(cur_position.get_tuple())

            points = np.array(points)
            x = points[:, 0]
            y = points[:, 1]
            # Mark start and end of the path
            plt.scatter([x[0], x[-1]], [y[0], y[-1]])
            plt.plot(x, y)
            points = []
        plt.show()
