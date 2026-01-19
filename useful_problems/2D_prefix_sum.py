from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        #
        # need a way to quickly get the sum for a square
        # 
        # Originate each sqare/rectangle from the origin pos: (0, 0), can quickly then get the sums for each
        # rectangle/square using an idea similar to the 2D Difference array etc.
        #
        ROWS, COLS = len(mat), len(mat[0])

        # prefix[i][j] is the sum of all grid cells from (0,0) to (i, j)
        prefix = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                prefix[i][j] = mat[i][j] + (
                (prefix[i - 1][j] if i > 0 else 0) + 
                (prefix[i][j - 1] if j > 0 else 0) -
                (prefix[i - 1][j - 1] if (i > 0 and j > 0) else 0)
                )

        # now iterate over all squares 
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                k = 0
                while i + k < ROWS and j + k < COLS:
                    end_row = i + k
                    end_col = j + k

                    square_sum = prefix[end_row][end_col] + (
                    -(prefix[i - 1][end_col] if i > 0 else 0)
                    -(prefix[end_row][j - 1] if j > 0 else 0)
                    +(prefix[i - 1][j - 1] if (i > 0 and j > 0) else 0)
                    )

                    if square_sum <= threshold:
                        res = max(res, k + 1)

                    k += 1

        return res        

                    

        
        
        
        