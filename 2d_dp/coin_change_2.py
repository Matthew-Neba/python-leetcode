from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #  This is just an unbounded knapsack variation. But it seems we need some trick
        # similar to combination sum 2
        #
        # We know that if we know the distinct amount of ways to get from any value
        # to the target amount, then we can just consider all our coins one by one
        # and sum up thier distinct ways to get to the target amount from the coin's value.
        # We can also keep track of our current total so that this pattern can be repeated for all
        # possible amounts
        #
        # Trick here is that doing the classic unbounded knapsack counts all the distinct permutations
        # however, we would only like to count different combinations. Maybe do something similar to 
        # combination sum 2 for this where once we don't use a coin, we never consider it again
        # in the future?
        #
        # O(n*amount) time complexity, O(n * amount) space complexity, where n is the size of coins
        dp = {}
        def coin_changer(cur_total, choice_idx):
            # dp base case
            if (cur_total, choice_idx) in dp:
                return dp[(cur_total, choice_idx)]
            
            # recursion base case
            # we have reached the target
            if cur_total == amount:
                return 1
            
            #recursion base case
            # we haven't reached the target but have no more coins
            if choice_idx >= len(coins):
                return 0

            distinct_ways = 0
            
            # use the coin, so we can continue using it again in the future (like in combination sum2)
            if cur_total + coins[choice_idx] <= amount:
                distinct_ways += coin_changer(cur_total + coins[choice_idx], choice_idx)

            # don't use the coin, so we cannot use it again in the future (like in combination sum2)
            distinct_ways += coin_changer(cur_total, choice_idx + 1)

            dp[(cur_total, choice_idx)] = distinct_ways
            return dp[(cur_total, choice_idx)]
        
        return coin_changer(0,0)



