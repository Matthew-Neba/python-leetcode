from typing import  List
class Solution:
    # O(n) time complexity (n subproblems, O(1) each) , O(n) space for stack
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # the minimum cost to get to get past the staircase is the minimum of all the costs 
        # places which allow you to get past the staircase. Since we can only take 1 or 2 steps,
        # this is equal to the minium of the costs to get to the second last or last floor.
        # but notice that this pattern also repeats for the second last and last floor --> DP

        #  input : [1,4,2,6]
        #  dp : [1,4,3,9]
        dp = {0:cost[0], 1:cost[1]}
        def min_cost(n):
            # dp base case
            if n in dp:
                return dp[n]

            current_min = float("inf")
            current_min = min(min_cost(n-1), min_cost(n-2)) + cost[n]

            dp[n] = current_min
            return dp[n]
        
        min_cost(len(cost) - 1)
        return min(dp[len(cost) - 1], dp[len(cost) - 2])