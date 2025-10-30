from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # can use the shoelace formula for finding the area of any polygon

        def shoelace(points):
            N = len(points)
            x_lace = 0
            y_lace = 0
            for i in range(N - 1):
                x,y = points[i]
                next_x, next_y = points[i + 1]
                x_lace += x * next_y
                y_lace += y * next_x

            # handle final loop
            x_lace += points[N - 1][0] * points[0][1]
            y_lace += points[N - 1][1] * points[0][0]

            return 0.5 * abs(x_lace - y_lace)

        N = len(points)
        res = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j + 1, N):
                    args = [points[i], points[j], points[k]]
                    res = max(res, shoelace(args))
    
        return res
                    





                
                
