from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        #
        #  immediately thinking of binary search
        #
        def find_area(y, square):
            # give area above y and below y
            bottom_x, bottom_y, length = square 

            # area below y
            below_area = min(length, max(0, y - bottom_y)) * length

            total_area = (length) ** 2
            above_area = total_area - below_area
            
            return (below_area, above_area)

        bottom , top = 0 , 10**9
        # instead of looking for an exact answer,
        # we narrow the interval that can contain the answer
        while top - bottom > 10**(-5):
            mid = (bottom + top) / 2

            total_above , total_below = 0 , 0
            for square in squares:
                area_below, area_above = find_area(mid, square)
                total_below += area_below
                total_above += area_above
            
            if total_above > total_below:
                bottom = mid
            else:
                top = mid

        return (bottom + top) // 2
            




