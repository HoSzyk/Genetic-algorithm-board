from typing import List

from Segment import Segment
from Point import Point


class Path:
    def __init__(self, segment_list=None):
        if segment_list is None:
            segment_list = []
        self.__segment_list: List[Segment] = segment_list

    @property
    def segment_list(self):
        return self.__segment_list

    @segment_list.setter
    def segment_list(self, new_segment_list: Segment):
        self.__segment_list = new_segment_list

    def append_segment(self, segment: Segment):
        self.__segment_list.append(segment)

    def get_point(self, start_point: Point, index):
        cur_point = start_point
        for i in range(index + 1):
            cur_point = self.__segment_list[i].get_end_point(cur_point)
        return cur_point

    def __repr__(self):
        return f'Segments: {" ".join(map(str, self.__segment_list))}'
