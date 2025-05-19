from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # to rotate a matrix by 90 degrees, can just transpose and then reverse it
        rows, cols = len(matrix), len(matrix[0])

        # transpose
        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse rows
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

    
solution = Solution()
print(solution.rotate([
  [1,2],
  [3,4]
]))


       