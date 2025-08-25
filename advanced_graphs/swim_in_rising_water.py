from typing import List
from heapq import heappush, heappop , heapify

# Key to this problem is realizing that dijstras depends on two conditions. 
# 1) All edge weights must be non negative (i.e: distance between nodes can never decrease)  --> (for greedy part to work)
# 2) The distance to the current node must be a function of the distance to
# all it's neigbor nodes and the node's edge weight   ---> (for dp part to work)

# Here can define distance between two nodes as the maximum value along the path from one to the
# other

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        def dijstras(grid):
            num_rows, num_cols = len(grid) , len(grid[0])
            directions = [(0,1), (0, -1), (1,0), (-1,0)]

            distances = [[float("inf")] * num_cols for _ in range(num_rows)]

            start_distance = grid[0][0]
            distances[0][0] = start_distance
            p_queue = [(start_distance, 0, 0)]

            while p_queue:
                cur_distance, cur_row, cur_col = heappop(p_queue)

                # ensure min distance
                if cur_distance > distances[cur_row][cur_col]:
                    continue
                
                # we are at a minimum distance to this current node
                for dr,dc in directions:
                    row , col = cur_row + dr , cur_col + dc

                    # in bounds
                    if not (-1 < row < num_rows and -1 < col < num_cols):
                        continue

                    # check if min distance
                    new_distance = max(cur_distance, grid[row][col])
                    if new_distance < distances[row][col]:
                        # update neighbor distance and push to heap
                        distances[row][col] = new_distance
                        heappush(p_queue, (new_distance, row, col))

            return distances
        
        min_distances = dijstras(grid)
        return min_distances[len(grid) - 1][len(grid[0]) - 1]













