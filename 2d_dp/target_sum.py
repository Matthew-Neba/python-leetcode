from collections import defaultdict
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Seems like a variation of bounded knapsack  
        #
        # There are two ways to do DP when doing tabulation, push and pull DP.
        #
        # Push: Propagate results from down to up in the table. We are "pushing" the previous subproblems 
        # results upwards, from the lower rows to the higher rows
        #
        # Pull: Fetch results from up to down in the dp table. We are "pulling" subproblem solutions
        # from lower rows of the DP table to the upper rows.
        # 
        # When doing tabulation, pull DP doesn't work well. It's better to do push DP since we are naturally pushing the
        # values up when doing tabulation. 
        #
        # O(n*m) time complexity, O(m) space complexity, where n is the length of nums, m is the sum of all the elements in nums
        dp_old = defaultdict(int)
        dp_old[0] = 1

        for num in nums:
            dp_new = defaultdict(int)
            for amount in dp_old:
                dp_new[amount + num] += dp_old[amount]
                dp_new[amount - num]  += dp_old[amount]
            
            dp_old = dp_new
            
        return dp_old[target]
        