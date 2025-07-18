from typing import List
# Subarray: a contiguos chunk of an array.  ex: for [1,2,3,4,5] , [1,2,3] is a subsequence  
# Subsequnce: non contiguos but the relative order of elements remain the same as in the original array. ex: for [1,2,3,4,5] , [1,4,5] is a subsequence 

#  Solved this using a small variation of Kadane's algorithm. The Key to this problem is realizing that any array can be split up into it's positive segments split up by the negative values. If we want to merge these positive segments, we need to ensure that the positive segments are greater than or equal to the negative values. But we don't know the suum of one of the positive segementrs however, we can still solve the problem by realizing that we just need to make a decision to include of remove one segment at a time.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = float("-inf")
        cur_segment = 0

        for i in range(len(nums) - 1, -1, -1):
            cur_segment += nums[i]
            cur_max = max(cur_max, cur_segment)

            if cur_segment < 0:
                cur_segment = 0
        
        return cur_max
            