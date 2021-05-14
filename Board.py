from typing import List, Tuple

from Point import Point


class Board:
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__point_pairs: List[Tuple[Point, Point]] = []

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def point_pairs(self):
        return self.__point_pairs

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @classmethod
    def load_from_file(cls, file_path):
        result = Board()

        with open(file_path) as r:
            line = list(map(int, r.readline().split(';')))
            result.__width, result.__height = line[0], line[1]

            for line in r:
                coordinates = list(map(int, line.split(';')))
                result.__point_pairs.append(
                    (Point(coordinates[0], coordinates[1]), Point(coordinates[2], coordinates[3])))
        return result

    def __repr__(self):
        return 'Width: ' + str(self.__width) + '\nHeight: ' + str(self.__height) +\
               '\nPoints: ' + ' '' '.join(f'{tup[0]}->{tup[1]}' for tup in self.__point_pairs)
