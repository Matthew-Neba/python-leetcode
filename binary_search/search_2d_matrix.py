from typing import List

# Key to this problem was realizing that we can genarilize the same concepts used in binary search. Just need some extra math to handle the index positions now. Important note: low and high are still functioning as indexes, but we compute some the true indexes for the matrix using matrix math.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #implement binary search
        m = len(matrix)
        n = len(matrix[0])

        low, high = 0, m * n - 1

        while high >= low:
            mid = (high + low) // 2
            #need math to handle finding the value at the index
            row = mid // n
            coulumn = mid % n

            if target == matrix[row][coulumn]:
                return True
            elif target < matrix[row][coulumn]:
                high = mid - 1
            else:
                low = mid + 1

        return False