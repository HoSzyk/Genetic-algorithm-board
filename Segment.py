from Point import Point


class Segment:
    def __init__(self, direction='', length=0):
        self.__direction = direction
        self.__length = length

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, new_direction):
        self.__direction = new_direction

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        self.__length = new_length

    def get_end_point(self, point: Point):
        if self.direction == 'S':
            return Point(point.x, point.y + self.length)
        elif self.direction == 'N':
            return Point(point.x, point.y - self.length)
        elif self.direction == 'E':
            return Point(point.x + self.length, point.y)
        elif self.direction == 'W':
            return Point(point.x - self.length, point.y)

    def get_points_between(self, start_point: Point):
        end_point = self.get_end_point(start_point)
        result = []
        min_point = start_point if start_point.x < end_point.x or start_point.y < end_point.y else end_point
        for x in range(min_point.x, min_point.x + abs(end_point.x - start_point.x) + 1):
            for y in range(min_point.y, min_point.y + abs(end_point.y - start_point.y) + 1):
                new_point = Point(x, y)
                if new_point != start_point and new_point != end_point:
                    result.append(Point(x, y))
        return result

    def __repr__(self):
        return f'{self.__direction} {self.__length}'
