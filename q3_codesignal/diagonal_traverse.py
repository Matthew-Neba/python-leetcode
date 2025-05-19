class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        res = []

        rows = len(mat)
        cols = len(mat[0])
        cur_row, cur_col = 0,0

        while len(res) < rows * cols:
            

            #top pattern
            while cur_row < rows and cur_row >= 0 and cur_col < cols:
                print(f"cur_row = {cur_row}, cur_col = {cur_col}")

                res.append(mat[cur_row][cur_col])
                cur_row -= 1
                cur_col += 1


            # set cur_row and cur_col to proper values for bottom iteration
            cur_row += 1
            cur_col -= 1


            if cur_col + 1 < cols:
                cur_col += 1
            else:
                cur_row += 1
            
            #bottom patern
            while cur_row < rows and cur_col < cols and cur_col >= 0:
                print(f"cur_row = {cur_row}, cur_col = {cur_col}")

                res.append(mat[cur_row][cur_col])
                cur_row += 1
                cur_col -= 1
            
            # set cur_row and cur_col to proper values for bottom iteration
            cur_row -= 1
            cur_col += 1

            if cur_row + 1 < rows:
                cur_row += 1
            else:
                cur_col += 1

            print(f"cur_row = {cur_row}, cur_col = {cur_col}")
            
        return res



solution = Solution()
print(solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))

            


            
