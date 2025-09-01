from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n) time complexity, O(1) space complexity

        # Can use dp here. We can extract the last digit and then shift the number
        # to the right by one position. This will eliminate the one digit
        # we extracted. Now we just need to get the number of one's in this remaining 
        # smaller digit. We are guaranteed to have calculated the number of ones in this
        # smaller digit already since  we are building the dp array from 0 upwards.
        # Recursive problem, we can memoize the results with DP.

        dp = [0] * (n+1) 
        for cur_num in range(1,n+1):
            ones = 0
            # check if the least significant bit is a one
            if cur_num & 1 == 1:
                ones += 1
            
            # perform the right shift
            shifted_num = cur_num >> 1
            
            # get the remaining ones
            ones += dp[shifted_num]

            dp[cur_num] = ones

        return dp

