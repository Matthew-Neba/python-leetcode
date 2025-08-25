from heapq import heappop, heappush, heapify
from typing import List

#  Key to this problem is realizing  
#  1) exactly one path between each pair of points ---> means no cycles can exist --> need to find a tree
#  2) minimum cost to connect all points together --> Minimum Spanning
#  3)  1 and 2 together ---> MST, can use Prim's algorithm


# O(Elog(E)) time complexity,  O(E) space complexity . There is a trick to reduce the time complexity to (E) though in fully dense graphs. This can be done why by keeping and updating a distance array. Then we can connect any unvisited point in any order to the current MST (order of connection does not matter for Prim's).
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
       
        num_points = len(points)

        def prims(points):
            # choose any point as the start point
            start = (points[0][0], points[0][1])
            total_cost = 0

            available = {(point[0], point[1]) for point in points}
            p_queue = [(0, start)]

            while p_queue:
                cost, cur_point = heappop(p_queue)

                # already in MST
                if cur_point not in available:
                    continue
                
                # we have found minimum cost for this point/node
                total_cost += cost
                available.remove(cur_point)
                for new_x,new_y in available:
                    man_dist = (abs(cur_point[0] - new_x) + abs(cur_point[1] - new_y)) 
                    heappush(p_queue, (man_dist , (new_x , new_y)))
            

            return total_cost

        return prims(points)
            




