from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        #  There is not a greedy strategy here, picking the largest value might eliminate
        # thhe two nearest largest values

        # There doesn't seem to be a math solution aswell, turn to DP

        # We can consider whether or not we rob the current house and pick the maximum of those
        # costs. There is a recursive pattern to this since we can repeat this pattern with any of
        # the remaining houses
        #
        # Instead of asking what order of robbing houses maximizes the money, instead ask will
        # we get more money if we rob or don't rob this house? This reduces the total number of subproblems from n(n+1)/2 to n.
        # The overall time complexity went down from O(n^3) to O(n)
        #
        # Here the order of robbing houses does not matter, this is why we are able to reduce the total number of subproblems # by asking this question. This interval dp pattern is only useful for questions like bursting ballons
        dp = {}

        # O(n) time complexity, O(n) space complexity for dp array and for recursive stack
        def rob_houses(cur_idx):
            # dp base case
            if (cur_idx) in dp:
                return dp[cur_idx]

            # recursive base case
            if cur_idx > len(nums) -1:
                return 0
            
            # we rob this house
            rob_money = nums[cur_idx] + rob_houses(cur_idx + 2)

            # dont rob this house , (note we can choose any available house to rob, but cleverly choosing
            # the next one ensures all houses below the current index have already been considered or were adjacent
            # to a robbed house so they are not available)
            no_rob_money = rob_houses(cur_idx + 1) 

            dp[cur_idx] = max(rob_money, no_rob_money)
            return dp[cur_idx]
        
        return rob_houses(0)
        


            
            
            





