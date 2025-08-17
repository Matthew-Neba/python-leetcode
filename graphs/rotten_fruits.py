from collections import deque
from typing import List

#  - Always process all nodes in queue when doing bfs
#  - Always make sure a node is processed before adding it to queue for bfs or dfs, this many mean doing some pre-processing for the start nodes. Like adding them to the visited set before adding them to the queue
#  - If need to know details about path, dfs is almost always better than bfs
#  - Alot of graph problems can be simplifgied with inversion. ex: pacific atlantic ocean, islands and treasure
# common with graphing problems. ex: pacific atlantic ocean, islands and treasure
# - Generally, do not return values when doing recursive dfs on graphs. We cannot use recursive dfs expecting to return something like in trees since cyle exists. You can have A depends on B which depends on C which depends on A. DFS can only be used for marking for graphs


# O(m*n) time, O(m*n) space complexity (O(m + n) space to be more precise)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # - Start bfs with multiple start positions simultaneously
        # - Incremenet timer
        # - Visit all adjacent square
        # - if they are a fresh fruit, infect, increment infected timer and add to queue. if rotten, skip. if empty, skip
        # - check if infected fruit number is equal to total fruit, if so return true
        # - if queue is empty but not all fruits are infected return -1, no spreading possible
        
        def bfs_rotten_fruit(start_positions):

            timer = 0
            rotten_fruits = len(start_positions)

            queue = deque([])
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            
            for pos in start_positions:
                queue.append(pos)
            
            while queue:
                set_rotten = False
                for _ in range(len(queue)):
                    cur_row , cur_col = queue.popleft()

                    for dr,dc in directions:
                        row, col = cur_row + dr, cur_col + dc

                        # check if in bounds
                        if not (-1 < row < len(grid) and -1 < col < len(grid[0])):
                            continue
                        
                        # check if not fresh
                        if not grid[row][col] == 1:
                            continue
                        
                        # we are at a fresh fruit, make it rotten
                        grid[row][col] = 2
                        rotten_fruits += 1
                        set_rotten = True
                        
                        # expand the rotteness from this fruit
                        queue.append((row,col))

                if set_rotten:
                    timer += 1
            
            return (rotten_fruits, timer) 

        start_positions = []
        total_fruits = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    start_positions.append((row, col))
                    total_fruits += 1
                
                if grid[row][col] == 1:
                    total_fruits += 1
   
        rotten_fruits, timer = bfs_rotten_fruit(start_positions)
        return timer if rotten_fruits == total_fruits else -1 
        




            