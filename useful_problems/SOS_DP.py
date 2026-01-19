import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 
        # If we have a problem that involes searching over subsets / aggregating information over subsets, we can use 
        # SOS DP.
        #
        # The key idea is to iterate over all posisble sets ( 2^b), b times (where b is the max
        # amount of items in a set). O(b * 2^b) time, O(2^b) space
        #
        # Then for every b, we update the information over all our possible sets (2^b) allowing a difference in the first
        # b items. This essentially accounts for the subsets of each set which differ in the first b items only.
        # 
        # We use the information from b - 1(subsets that differ in only the b -1 first bits) to update
        # the answer for the first b bits over all possible sets.
        #
        bits = max(nums).bit_length()
        dp = [float("-inf")] * (1 << bits)

        # base case (difference in first 0 bits, i.e: exact match)
        for num in nums:
            dp[num] = num
        
        # now, we allow a difference in all bits <= b and build up the dp incrementally
        for bit in range(bits):
            for mask in range(1 << bits):
                # remember that if the bit is not set, it's dp transition is just equal to previous one, no modification
                # so here, we just need to check if the i'th bit was set and handle that dp transition
                if mask & (1 << bit):
                    dp[mask] = max(dp[mask], dp[mask ^ (1 << bit)])

        # now dp[mask] contains the max value for any subset of mask
        res = float("-inf")

        # remember we are taking the complement of the set represented by the number,
        # due to the problem statement
        for num in nums:
            res = max(res, num * dp[~num])

        return res if res > float("-inf") else 0


              










        