from typing import List
# Problem imeddiately presents itslef as a backtracking problem. The difficulty is in seeing if a better solution exist. We start by realizing that there is no other way to check if there is a solution but by simulating the process of forming the word on the grid. No check for the frequency of the characters etc. exist that will allow us to determine if a solution exist.
# 
#  Then we realize that even if we don't resuse the previous checks for a square, we will just redo it 3 times at most since each grid square only has 3 adjecent squares. Therefore, DP will only reduce the work by a maximum factor of 3 and this, not affect the time complexity while increasing the space complexity. Backtracking is optimal here

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # up, down, right, left
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        board_rows = len(board)
        board_cols = len(board[0])

        res = False
        def backtrack(path_set, cur_row, cur_col):
            nonlocal res
            if len(path_set) == len(word):
                res = True
                return
            
            # 1) ensure we havent been to this square before
            if (cur_row, cur_col) in path_set:
                return


            # 2) ensure it is in bounds of the map
            if not (0 <= cur_row < board_rows and  0 <= cur_col < board_cols):
                return

            # 3) ensure it is the proper value we are looking for
            if board[cur_row][cur_col] == word[len(path_set)]:
                path_set.add((cur_row, cur_col))

                for d_row,d_col in directions:
                    new_row = cur_row + d_row
                    new_col = cur_col + d_col
                    
                    backtrack(path_set, new_row, new_col)
                
                path_set.remove((cur_row, cur_col))


        # run the backtrack on every grid square
        for row in range(board_rows):
            for col in range(board_cols):
                backtrack(set(), row ,col)
                if res:
                    return True
        
        return False
