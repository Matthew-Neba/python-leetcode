from collections import deque
from typing import List

# This problem is essentially just DFS/BFS. There is a trick though to eliminate a visited set in this problem and reduce the space complexity to O(min(m,n)) instead. We can just mark our visited cells in the grid itself and thus, we won't need a visited set.

class Solution:
    # O(m*n) time complexity, O(m *n) space complexity
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        # O(m*n) time complexity, O(m * n) space complexity for queue and visited set
        def bfs_explore(start_pos):
            queue = deque([])
            queue.append(start_pos)

            while queue:
                row,col = queue.pop()

                # check if this has already been explored
                if (row,col) in visited:
                    continue
                
                # we are not on land, dont consider expanding the island
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                    continue
                
                # expand the island
                visited.add((row,col))
                for dr, dc in directions:
                    queue.append((row + dr, col + dc))

            
        # perform bfs on all values
        #  O(m*n) time
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and ((row,col) not in visited):
                    bfs_explore((row,col))
                    islands += 1
        
        return islands
        


