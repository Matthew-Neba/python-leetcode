from typing import List, Optional

# Key to this prblem is realizing that using recursive dfs and returning values is unreliable in graphs due to cycles, so we should use marking dfs instead instead. We realize that any "O"'s connected to the border cannot be flipped.  This leads me to realize that rather than checking each cell individually, we can invert the problem. This inversion pattern seems to be common with graphing problems. ex: pacific atlantic ocean, islands and treasure
#   1. Start DFS/BFS from all border 'O's and mark all reachable cells.  
#   2. These marked cells are safe and won’t be flipped.  
#   3. Finally, flip all unmarked 'O's, which are truly surrounded.


# O(m*n) time complexity, O(m*n) space complexity
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row_count, col_count = len(board), len(board[0])
        visited = set()

        def dfs_surrounded(pos):
            row,col = pos

            # check if out of bounds
            if not (-1 < row < row_count and -1 < col < col_count):
                return
            
            #if it has been visited before
            if pos in visited:
                return 

            # only expand on "O"
            if not board[row][col] == "O":
                return
            
            # unvisited "O" now
            visited.add(pos)

            dfs_surrounded((row + 1, col))
            dfs_surrounded((row - 1, col))
            dfs_surrounded((row, col + 1))
            dfs_surrounded((row, col - 1))

        # run dfs on all border "O"
        for row in range(row_count):
            if board[row][0] == 'O':
                dfs_surrounded((row,0))

            if board[row][col_count - 1] == 'O':
                dfs_surrounded((row, col_count - 1))

        for col in range(col_count):
            if board[0][col] == 'O':
                dfs_surrounded((0, col))
                
            if board[row_count - 1][col] == 'O':
                dfs_surrounded((row_count - 1, col))


        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] == 'O' and (row,col) not in visited:
                    board[row][col] = 'X'
        

            

            




