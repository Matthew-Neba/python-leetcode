from typing import List

# key to this problem is using 4 pointers : top, bottom, left, right in order to keep track of which elements we still need to print/append to result

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        rows, cols =  len(matrix), len(matrix[0])
        top,bottom = 0, rows - 1
        left, right = 0, cols - 1

        while len(res) < rows * cols:
            
            # get top row
            if top <= bottom:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top += 1

            # get right column
            if right >= left:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right -= 1

            #get bottom row
            if bottom >= top:
                for i in range(right,left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # get left coulumn
            if left <= right:
                for i in range(bottom, top -1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res


        

