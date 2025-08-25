from collections import deque
from typing import List

# Key to this problem is just to do a regular bfs/dfs but keep track of the curent
# island size

# O(m*n) time , O(m*n) space for the visited set. Can also modify the grid in place to reduce space complexity down to  O(max(m,n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        #  O(m*n) time, O(max(m,n)) space for queue size (perimeter is largest size queue can have)
        def bfs_max(start_pos):
            nonlocal max_area
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            queue = deque()
            queue.append(start_pos)
            island_size = 0

            while queue:
                row, col = queue.popleft()

                # check if in bounds of the grid
                if not (-1 < row < len(grid) and -1 < col < len(grid[0])):
                    continue

                # check if it is a land
                if grid[row][col] != 1:
                    continue

                
                # check if visited
                if (row,col) in visited:
                    continue
                
                visited.add((row,col))
                island_size += 1
                for dr,dc in directions:
                    queue.append((row + dr, col + dc))
            
            max_area = max(max_area, island_size)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                bfs_max((row,col))

        return max_area

        



