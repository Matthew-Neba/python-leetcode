from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        # 
        # Immediately think of dp/stack (or if just one type of bracket, no need for stack)
        #
        # dp + stack
        # O(m*n* (m+n)) time, O(m*n* (m+n)) space
        # 
        # See if given m open brackets, we can finish the string
        #
        # Practice 3D tabulation
        #
        ROWS, COLS = len(grid), len(grid[0])
        max_open = ROWS + COLS - 1

        # dims: rows, cols, cur_open
        dp = [[[False]*COLS for _ in range(ROWS)] for _ in range(max_open+1)]

        # base case, note that this is necessary for the problem to be possible
        if grid[ROWS - 1][COLS - 1] == ")":
            dp[1][ROWS - 1][COLS - 1] = True

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, - 1, - 1):
                for open_brack in range(max_open+1):
                    close = None
                    if grid[r][c] == "(":
                        close = open_brack + 1
                    else:
                        close = open_brack - 1

                    if close < 0 or close > max_open:
                        continue

                    # check if possible by to close by going down
                    if r + 1 < ROWS and dp[close][r+1][c]:
                        dp[open_brack][r][c] = True
                    
                    # check if possible by to close by going right
                    if c + 1 < COLS and dp[close][r][c+1]:
                        dp[open_brack][r][c] = True
        
        return dp[0][0][0]

