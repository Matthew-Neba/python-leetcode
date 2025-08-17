from typing import List
from collections import deque

# Key to this problem is realizign that Initially, I would like to do dfs for each node twice and see if we can reach both oceans respectively. However, I see that if I can reach the ocean from a node, then all the nodes along that path can also reach it. Would use recursion here to return if we can reach the ocean from neighboring cells here. But this kind of recursion to return values does not work with dfs or bfs. However, I realize that we can start from the edges(ocean) and mark the cells we can reach form there. This type of marking dfs is viable with graphs 
# O(m*n) time complexity, O(m*n) space complexity
class Solution:
    # 
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row_count, col_count = len(heights), len(heights[0])

        # perform multistart bfs on each list, store the two visited sets globally
        def bfs_ocean(start_positions, visited):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            queue = deque([])
            visited = set(start_positions)

            for pos in start_positions:
                queue.append(pos)
                visited.add(pos)
            
            while queue:
                for _ in range(len(queue)):
                    pos = queue.popleft()

                    for dr,dc in directions:
                        row, col = pos[0] + dr, pos[1] + dc
                        # check if in bounds
                        if not (-1 < row < row_count and -1 < col < col_count):
                            continue

                        # check if it has been visited before
                        if (row,col) in visited:
                            continue

                        # check if we can backflow there from the current cell
                        if heights[row][col] >= heights[pos[0]][pos[1]]:
                            visited.add((row,col))
                            queue.append((row,col))


        # fetch all pacific and atlantic ocean cells and store them in a list
        pacific_start = []
        atlantic_start = []

        # top
        for col in range(col_count):
           pacific_start.append((0,col))

        # left
        for row in range(1,row_count):
            pacific_start.append((row,0))

        # bottom
        for col in range(col_count):
            atlantic_start.append((row_count - 1,col))
        
        # right
        for row in range(row_count - 1):
            atlantic_start.append((row, col_count - 1))


        # iterated over not one set and see if it belongs in the other, add it to the results
        # in this case 
        pacific_visited, atlantic_visited = set(), set()
        bfs_ocean(pacific_start, pacific_visited)
        bfs_ocean(atlantic_start, atlantic_visited)

        res = []
        for pos in pacific_visited:
            if pos in atlantic_visited:
                res.append(list(pos)) 
        
        return res