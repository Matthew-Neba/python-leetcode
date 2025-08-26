class Solution:
    # This question shows need to be careful when breaking down the problem into subproblems.
    # It seems easy but only if the problem is only broken down properly.
    def climbStairs(self, n: int) -> int:
        
        dp = {0:1, 1:1}
        def climb(n):
            # dp base case
            if n in dp:
                return dp[n]

            # recursion base case
            steps = climb(n-1) + climb(n-2)

            dp[n] = steps
            return steps
        
        return climb(n)


        
         
        
        