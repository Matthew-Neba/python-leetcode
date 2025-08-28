from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 
        # Good to start problems by considering simple/brute force solutions first. Then continue
        # the optimizations.
        #
        # Here we see that we want to consider all possible subsequences and choose the longest one.
        # Can be done using backtracking in O(n*2^n), however, we can see that alot of these subsequences
        # will be invalid. Instead, we only need to consider subsequences where:
        # 1) The indexes are in the subsequence are in increasing order
        # 2) The values in the subsequence are in increasing order
        # 
        # Thus, for each index, we can loop over all indexes which come after it and get the longest
        # subsequence for that index
        # O(n^2) time complexity, O(n) space complexity for this solution.
        # 
        # However, we realize that we are calling alot of the subproblems repeatedly. 
        # ex: [1,2,3,4,5,6] , subsequence(5) will be called for every index from 0 to 3.
        # Can we reduce the amount of these calls? --> Yes, since we are only worried about the length of the lis
        # there is a nlogn binary search solution
        #
        dp = {}
        def LIS(cur_idx):
            # dp base case
            if cur_idx in dp:
                return dp[cur_idx]
            
            # recursion base case
            if cur_idx >= len(nums):
                return 0
            
            max_lis = 1
            # See if can connect the current value to any future longest subsequences
            for i in range(cur_idx + 1, len(nums)):
                if nums[cur_idx] < nums[i]:
                    max_lis = max(max_lis, 1 + LIS(i))
            
            dp[cur_idx] =  max_lis
            return dp[cur_idx]
        
        res = 0
        for i in range(len(nums)):
            res = max(res, LIS(i))

        return res