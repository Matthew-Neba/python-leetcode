from typing import List

#  Key to this problem was finding out how to check the constraints for the backtracking optimally. We know we can use a set for the rows and cols to check the row and cols constraint in O(1) time. The hard part was checking the diagonal constraints in O(1) time. This can however be done by realizing that each line has an equation. We can then obtain the positive and negative diag line equations for any grid square and store these equations in two sets. Then, we can check the diagonal constraints in constant time.

# O(n!) time complexity (not exactly n! but we are reducing by atleast 2 on each row), O(n^2) space complexity for the board
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # need a row set, need a col set, need a updiag set, need a down diag set
        # to uniquely identify a line, we just need the intercept and slope. we will store thse in
        #  the diag sets
        res = []

        def backtrack(row_set, col_set, pos_diag_set, neg_diag_set, board, row):
            #  we are now considering row + 1
            if row == n:
                # need to return the board in the correct problem format
                ret_board = []
                for row in board:
                    ret_row = "".join(row)
                    ret_board.append(ret_row)
                res.append(ret_board)
                return

            # consider all squares in this row
            for col in range(n):
                # already have a queen in this row
                if row in row_set:
                    continue 

                # already have a queen in this col
                if col in col_set:
                    continue
            
                # calculate the positive intercept, (-row used to orientate grind in first cartesian quadrant)
                pos_y_intercept = col - (-row)
                if pos_y_intercept in pos_diag_set:
                    continue

                # calculate the negative intercept
                neg_y_intercept = col + (-row)
                if neg_y_intercept in neg_diag_set:
                    continue

                # we can place a queen on this square
                board[row][col] = "Q"

                # add the row, set and diags
                row_set.add(row)
                col_set.add(col)
                pos_diag_set.add(pos_y_intercept)
                neg_diag_set.add(neg_y_intercept)

                # continue backtracking unto the next row
                backtrack(row_set, col_set, pos_diag_set, neg_diag_set, board, row+1)

                # undo the step
                board[row][col] = "."

                row_set.remove(row)
                col_set.remove(col)
                pos_diag_set.remove(pos_y_intercept)
                neg_diag_set.remove(neg_y_intercept)
        
        row_set, col_set, pos_diag_set, neg_diag_set = set(), set(), set(), set()
        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(row_set, col_set, pos_diag_set, neg_diag_set, board, 0)
        return res

