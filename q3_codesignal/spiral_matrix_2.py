class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        res = [[0 for i in range(n)] for i in range(n)]
        cur_n = 1

        rows = cols = n
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while cur_n <= n**2:
            # get top row
            if top <= bottom:
                for i in range(left, right + 1):
                    res[top][i] = cur_n
                    cur_n += 1
                top += 1
            
            # get right column
            if right >= left:
                for i in range(top, bottom + 1):
                    res[i][right] = cur_n
                    cur_n += 1
                right -= 1
            
            # get bottom row
            if bottom >= top:
                for i in range(right, left - 1, -1):
                    res[bottom][i] = cur_n
                    cur_n += 1
                bottom -= 1
            
            # get left column
            if left <= right:
                for i in range(bottom, top -1, -1):
                    res[i][left] = cur_n
                    cur_n += 1
                left += 1
    
        return res





            


solution = Solution()
print(solution.generateMatrix(3))