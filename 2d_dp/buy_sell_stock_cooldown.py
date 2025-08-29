from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy solution doesn't work here because selling on a day can stop use from buying on the next day
        #
        # However, on each day, we have two choices, we can buy or we can sell, we can therefore explore the optimal
        # combination of these choices using DP
        #
        # In each spot in the DP table, we will have two options. The best profit from selling and then buying
        # and selling onwards from here. Or the best price for buying and then selling and buying onwards from here.
        #
        # Also notice that we dont actually need to store the coin prices in the DP table.
        # This is because if we calculate profit in an online fashion by just subtracting the profit
        # when we buy and adding when we sell, we can eliminate needing to store that extra coin information.
        # Reduces time complexity from O(n^2) to O(n) and space complexity from O(n^2) to O(n)
        
        dp = {}

        # O(n)
        def profit(action, i):
            # dp base case
            if (action,i) in dp:
                return dp[(action,i)]
            
            # recursion base case
            if i >= len(prices):
                return 0

            max_profit = 0
            if action == "buy":
                # we have a coin, can only consider selling. Skip two spots ahead since we cannot buy the
                # next coin
                # buy
                buy_profit = -prices[i] + profit("sell", i+1)

                # don't buy
                no_buy_profit = profit("buy", i+1)

                max_profit = max(buy_profit, no_buy_profit)
                
            else:
                # sell
                sell_profit = prices[i] + profit("buy", i + 2) 

                # don't sell
                no_sell_profit = profit("sell", i + 1)


                max_profit = max(sell_profit, no_sell_profit)

            dp[(action, i)] = max_profit
            return dp[(action, i)]

        return profit("buy",0) 