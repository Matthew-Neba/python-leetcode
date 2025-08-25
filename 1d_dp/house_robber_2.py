from typing import List
from collections import defaultdict

#  O(n) space, O(n) time
class Solution:
    def rob(self, nums: List[int]) -> int:
        # can do this in O(n) by using two optimal robbing array
        # One will keep track of the optimal cost if we can rob the last house
        # Other will keep track of the optimal costs if we cannot rob the last house
        # Will use these to calculate maximum of choosing the rob the first house or not 
        # rob the first house
        #
        # ex: [1, 3, 4, 7, 6 ,9]

        def robber(n, stop, dp_arr):
            if n > stop:
                return 0

            if dp_arr[n] > 0:
                return dp_arr[n]
            
            
            rob_cur = nums[n] + robber(n+2, stop, dp_arr)
            no_rob_cur = robber(n+1, stop, dp_arr)
            dp_arr[n] = max(rob_cur, no_rob_cur)

            return dp_arr[n]
        
        # can rob the end
        dp_end = defaultdict(int)
        
        # cannot rob the end
        dp_no_end = defaultdict(int)

        robber(1, len(nums) - 1, dp_end)
        robber(0, len(nums) - 2, dp_no_end)

        return max(nums[0] + dp_no_end[2], dp_end[1])


