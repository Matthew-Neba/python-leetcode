import random
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """        
        K'th largest pattern, can use quick select or heap 
        bucket sort would be inefficient here since the distances range
        are too large
        """        
        def dist(point):
            x,y = point
            return math.sqrt((x**2) + (y ** 2))

        def partition(l,r):
            pivot_idx = random.randint(l,r)
            pivot_dist = dist(points[pivot_idx])
            points[r], points[pivot_idx] = points[pivot_idx], points[r]

            boundary = l
            for i in range(l,r):
                if dist(points[i]) < pivot_dist:
                    points[boundary], points[i] = points[i], points[boundary]
                    boundary += 1
                print(points)

            points[r], points[boundary] = points[boundary], points[r]
            return boundary

        target_idx = k - 1
        def quick_select(l,r):
            pivot_idx = partition(l,r)

            if pivot_idx == target_idx:
                return points[:pivot_idx + 1]
            elif pivot_idx < target_idx:
                return quick_select(pivot_idx + 1, r)
            else:
                return quick_select(l , pivot_idx - 1)
        
        return quick_select(0, len(points) - 1)