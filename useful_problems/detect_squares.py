from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: 0)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        # ensure points lie on two distinct x and y coordinates to ensure they are aligned with the axis
        # ensure all points are distinct so that the rectangle has four corners
        res = 0
        cur_x, cur_y = point[0], point[1]
        for new_x, new_y in list(self.points):
            
            # instead of fixing sides, fix the diagonal, less conditions to worry about
            # take new point to be the diagonal point

            # ensure actually diagonal
            if cur_x == new_x or cur_y == new_y:
                continue

            # ensure diagonal is for a square and not just for a rectangle
            if not abs(cur_x - new_x) == abs(cur_y - new_y):
                continue

            res += self.points[(new_x, new_y)] * self.points[(cur_x, new_y)] * self.points[(new_x, cur_y)]
        
        return res
            

