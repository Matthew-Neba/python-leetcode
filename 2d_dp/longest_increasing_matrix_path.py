from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 
        # Longest path question so immediately think of DFS.
        # 
        # [5 5 3]
        # [2 3 6] 
        # [1 1 1]
        #
        # For each grid cell, we run dfs and mark the visited grid cells
        # as visited. The DFS will keep track of the length of the path
        # and update all the nodes it visits with thier longest increasing path.
        # We will make sure this dfs is ran on all nodes. If a node visits a visited cell, 
        # it just needs to know it's longest increasing path so memoizing them
        # O(m*n) time complexity, O(m*n) space complexity
        rows, cols = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(cur_row, cur_col):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            # include this cell
            max_path_length = 1

            for dr,dc in directions:
                row, col = cur_row + dr, cur_col + dc

                # recursion base case
                # out of bounds
                if not (-1 < row < rows and -1 < col < cols):
                    continue

                # not greater, don't consider this cell
                if not matrix[row][col] > matrix[cur_row][cur_col]:
                    continue

                # dp base case 
                # we have already visited this cell and obtained it's longest path
                if not dp[row][col] == -1:
                    max_path_length = max(max_path_length, 1 + dp[row][col])
                    continue
                
                # haven't visited cell yet
                nei_longest_path = dfs(row, col)
                max_path_length = max(max_path_length, 1 + nei_longest_path)
            
            dp[cur_row][cur_col] = max_path_length
            return dp[cur_row][cur_col]
        
        max_path = 0
        for i in range(rows):
            for j in range(cols):
                max_path = max(max_path, dfs(i,j))

        return max_path