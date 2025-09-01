class Solution:
    # O(1) time complexity, O(1) space complexity
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            cur = n >> i
            # check if the least significant bit is a one
            if cur & 1 == 1:
                count += 1
        
        return count