from typing import List
class Solution:
    # 1) There doesn't seem to be a greedy choice here. Bursting the greatest/smallest balloon
    # may or may not lead to an optimal gain since it depends on the neighbors as well.
    #
    # 2) Resort to DP then, however, doing the DP by just choosing which ballons to burst
    # is complex since when we burst a ballon it combines the left ballons
    # with the right ballons. This leads to the subproblems become exponential in size
    #
    # 3) How about if we decide to instead choose which ballons not to burst until we have burst
    # the others (i.e: choose which ballons we burst last). The left and right ballon arrays
    # now become independent subproblems. We can now do DP.
    # 
    # 
    # O(n^3) time complexity --> (n^2 total subarrays and n work is done for each one) 
    # O(n^2) space complexity --> (n(n+1)/2 subarray optimal coins we need to store)
    def maxCoins(self, nums: List[int]) -> int:
        nums = nums
        dp = {}

        def burst(l,r):
            # recursive base case
            if l > r:
                return 0

            # dp base case
            if (l,r) in dp:
                return dp[(l,r)]

            max_coins = 0
            for i in range(l, r+1):
                cur_coins = 0
                # we can use l-1'th and r+1'th ballon since they will be getting burst
                # after we burst this balloon
                left_part = nums[l - 1] if l-1 > -1 else 1
                right_part = nums[r + 1] if r+1 < len(nums) else 1

                cur_coins += left_part * nums[i] * right_part

                # now add the costs of bursting the right and left side
                cur_coins += burst(l,i-1)
                cur_coins += burst(i+1, r)

                # we now have the current coins for bursting this ballon last
                max_coins = max(max_coins, cur_coins)

            dp[(l,r)] = max_coins
            return max_coins
        
        burst(0,len(nums) - 1)
        return dp[(0,len(nums) - 1)]
        
