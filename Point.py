class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return f'({str(self.__x)};{str(self.__y)})'

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def get_tuple(self):
        return self.__x, self.__y,
