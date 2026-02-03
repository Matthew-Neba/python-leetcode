from typing import List
from collections import defaultdict
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        #
        # Key realization is that even though we can teleport anywhere, when we get to 0 teleportations,
        # we can only go right and down and this, we will eventually hit the base case of k = 0 and be
        # in the final grid cell
        #
        # 2nd key insight is that to limit the amount of teleportations we do, 
        # notice that we are only in the min path cost to get to the end given one less teleportation 
        # from all possible teleportation locations.
        # Thus, if we are careful about the order we execute the dp and store the min path costs,
        # then we can choose to teleport to only one location instead of potentially n locations.
        #
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0,1), (1, 0)]
        
        max_val = max(grid[c_row][c_col] for c_col in range(COLS) for c_row in range(ROWS))                   
        best_tp = [float("inf")] * (max_val + 1)

        dp = [[[float("inf")] * (k + 1) for _ in range(COLS)] for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1][0] = 0
        for tp in range(k + 1):
            for c_row in range(ROWS -1, -1, -1):
                for c_col in range(COLS - 1, -1, -1):
                    # do not use any teleportations
                    for dr,dc in DIRS:
                        n_row, n_col = c_row + dr, c_col + dc
                        if -1 < n_row < ROWS and -1 < n_col < COLS:
                            dp[c_row][c_col][tp] = min(
                                dp[c_row][c_col][tp],
                                grid[n_row][n_col] + dp[n_row][n_col][tp]
                            )
                    
                    # use another teleportation (take the best one only)
                    if tp > 0:
                        dp[c_row][c_col][tp] = min(dp[c_row][c_col][tp] , best_tp[grid[c_row][c_col]])
            
            # update best tp now
            for c_row in range(ROWS):
                for c_col in range(COLS):
                    best_tp[grid[c_row][c_col]] = min(best_tp[grid[c_row][c_col]], dp[c_row][c_col][tp])
            
            # we can tp to any value smaller than this grid value, record the best one
            for val in range(1, max_val + 1):
                best_tp[val] = min(best_tp[val - 1], best_tp[val])

        return dp[0][0][k]
