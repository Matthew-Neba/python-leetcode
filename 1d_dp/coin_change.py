from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # instead of asking what is the minimum cost of getting to some value giving we
        # have used our greatest available coin, ask instead: What is the minimum amount of coins
        # we need to reach each value from 0 to t?
        #
        # This is a variation of unbounded knapsack
        #
        #
        dp = {0:0}
        def min_cost(target):
            # dp base case
            if target in dp:
                return dp[target]
            
            cur_min = float("inf")
            for coin in coins:
                new_target = target - coin
                if new_target >= 0:
                    cur_min = min(cur_min, 1 + min_cost(new_target))
            
            dp[target] = cur_min
            return dp[target]  
                
        min_cost(amount)
        return dp[amount] if dp[amount] < float("inf") else -1


        
            
           




            
        