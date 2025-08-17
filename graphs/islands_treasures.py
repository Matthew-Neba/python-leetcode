from collections import deque
from typing import List

# O(m*n) time complexity, O(m + n) space complexity. The queue can hold a maximum amount of nodes equal to the perimeter of the grid. We are not using a visited set here. Good idea to only add valid items to queue when doing bfs and dfs.

class Solution:
    # shortest unweighted paths, consider bfs. Can do multistart bfs from each treasure. Cannot
    # do it from each land since we cannot easily update the lands with the queue approach once
    # the treasure is found. For multistart bfs, process all nodes in the queue a
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # use a multistart bfs approach. We will start bfs from all treasures
        # simultaneously. If we get to a land cell first, then we have the shortest path 
        # from a treasure to that land cell.

        # no need for visited set, we can just check if cell value is not inf, this means
        # it was previously updated

        def bfs_treasure_hunt(start_positions):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            queue = deque([])

            # initialize the queue
            for pos in start_positions:
                queue.append((0, pos))

            while queue:
                # this part is important for multi start bfs
                for _ in range(len(queue)):
                    path_length, pos = queue.popleft()
    
                    # expand the area
                    for dr,dc in directions:
                        row,col = pos[0] + dr, pos[1] + dc

                        # check if we are in bounds
                        if not (-1 < row < len(grid) and -1 < col < len(grid[0])):
                            continue

                        # check if we are at a water cell
                        if grid[row][col] == -1:
                            continue
                        
                        # check if we have visited this before
                        if grid[row][col] != 2147483647:
                            continue

                        # visit the cell and add to queue
                        grid[row][col] = path_length + 1
                        queue.append((path_length + 1 , (row,col)))

                  
        treasure_positions = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    treasure_positions.append((row,col))

        bfs_treasure_hunt(treasure_positions)











