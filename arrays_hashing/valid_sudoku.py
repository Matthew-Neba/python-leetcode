from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Note that this solution prioritizes time, it is O(n) and O(n) in space and time. Can get O(3n) and O(logn), if we instead store space for just one row/col/grid and iterate through all elemets three times to see if duplicate rows/cols/grids

        num_rows = len(board)
        num_cols = len(board[0])

        rows_sets = [set() for i in range(num_rows)]
        cols_sets = [set() for i in range(num_cols)]
        grid_sets = [set() for i in range(num_rows)]
        
        for row, row_items in enumerate(board):
            for col in range(len(row_items)):
                if board[row][col] == ".":
                    continue

                if board[row][col] in rows_sets[row]:
                    return False
                else:
                    rows_sets[row].add(board[row][col])

                if board[row][col] in cols_sets[col]:
                    return False
                else:
                    cols_sets[col].add(board[row][col])


                # time for figuring out the position in the grid
                grid = (row//3 * 3) + (col//3)

                if board[row][col] in grid_sets[grid]:
                    return False
                else:
                    grid_sets[grid].add(board[row][col])
        
        return True
