from typing import List
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        # 
        # These problems have recently have been following a pattern of optimization
        # by reducing the values we have to search over. Usually by sorting or some sort of heap/storing min
        # or max.
        #
        # Key observations abs(y2 - y1) + abs(x2 - x1) = 
        # max(y2 - y1 + x2 - x1, y2 - y1 + x1 - x2, y1 - y2 + x2 - x1, y1 - y2 + x1 - x2) = 
        # max (y2 + x2 -y1 - x1, 
        #      y2 - x2 - y1 + x1, 
        #      -y2 + x2 + y1 - x1, 
        #      -y2 - x2 + y1 + x1)
        # 
        # This means that given a point, we do not neeed to compare it to all other points to get the max distance.
        # We just need to compare it to the best in each of the categories - - , - + , + - , + +
        # 
        # Now, to handle the second part of the problem, we need to know the max when we remove this max distance.
        # Notice that if we store the top two values in each of these categories, this can be calculated
        #
        plus_plus = [(float("-inf"), None)] * 2
        plus_minus = [(float("-inf"), None)] * 2
        minus_minus = [(float("-inf"), None)] * 2
        minus_plus = [(float("-inf"), None)] * 2

        for i,point in enumerate(points):
            x,y = point
            if x + y > plus_plus[0][0]:
                plus_plus[1] = plus_plus[0]
                plus_plus[0] = (x + y, i)
            elif x + y > plus_plus[1][0]:
                plus_plus[1] = (x + y, i)

            if x - y > plus_minus[0][0]:
                plus_minus[1] = plus_minus[0]
                plus_minus[0] = (x - y, i)
            elif x - y > plus_minus[1][0]:
                plus_minus[1] = (x - y, i)
            
            if -x + y > minus_plus[0][0]:
                minus_plus[1] = minus_plus[0]
                minus_plus[0] = (-x + y, i)
            elif -x + y > minus_plus[1][0]:
                minus_plus[1] = (-x + y, i)

            if -x - y > minus_minus[0][0]:
                minus_minus[1] = minus_minus[0]
                minus_minus[0] = (-x - y, i)
            elif -x - y > minus_minus[1][0]:
                minus_minus[1] = (-x - y, i)
        
        # max distance after deleting some point
        def delete_point_max_dist(i):
            plus_plus_max = plus_plus[0][0]
            if plus_plus[0][1] == i:
                plus_plus_max = plus_plus[1][0]
            
            plus_minus_max = plus_minus[0][0]
            if plus_minus[0][1] == i:
                plus_minus_max = plus_minus[1][0]
            
            minus_plus_max = minus_plus[0][0]
            if minus_plus[0][1] == i:
                minus_plus_max = minus_plus[1][0]

            minus_minus_max = minus_minus[0][0]
            if minus_minus[0][1] == i:
                minus_minus_max = minus_minus[1][0]
            
            return max(plus_plus_max + minus_minus_max, minus_plus_max + plus_minus_max)

        #
        # now, lets get the best if we exclude a point, exclude the best from each category of 
        # + +, + -, - + , - -
        #
        res = float("inf")
        res = min(res, delete_point_max_dist(plus_plus[0][1]))
        res = min(res, delete_point_max_dist(plus_minus[0][1]))
        res = min(res, delete_point_max_dist(minus_plus[0][1]))
        res = min(res, delete_point_max_dist(minus_minus[0][1]))

        return res

