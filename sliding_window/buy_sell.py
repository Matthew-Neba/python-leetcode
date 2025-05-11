from typing import List

# key to this problem is realizing that we can reduce the brute force search through all pairs of prices. This is done by realizing that if there is a lower price further down the array, then, only need to check all pairs further down from that lower value.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        l,r = 0,1
        max_profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                cur_profit = prices[r] - prices[l]
                max_profit = max(max_profit, cur_profit)
                r += 1
        
        return max_profit
