from functools import cache
import math
class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        # 
        # dp or math , go ahead with the dp
        #
        # (n,k) --> (number of ways to get different concerts)
        #
        # (dont forget to put 0 people on this stage), do seperately
        # dp[(n, k)] =  sum i from 1 to n: n choose i * y * dp(n - i, k + 1)
        #
        # Notice that taking that dp recurrence needs a sum over n which
        # would give us a time complexity of O(n^3).
        #
        # Instead, we can look to restate the recurrence relation. We can do something similar to the Stirling
        # Numbers Of The Second Kind recurrence relation for this problem. 
        # In general, whenever we are dealing 
        # with partitioning a set into groups, consider using the Stirling Numbers. 
        #
        # The Stirling Style Recurrence Relation for this problem:
        # dp[(n,k)] = n * dp[(n - 1, k)] + (x - (k - 1) * dp[(n - 1, k - 1)]
        #
        MOD = 10**9 + 7
        @cache
        # note that we want non empty stages, reason for the base cases being set like that
        def s(n, k):
            # some pruning
            if k > x:
                return 0

            # we have no performers and no stages left, we have sucessfully filled out stages and people
            if k == 0 and n == 0:
                return 1

            # 1) every performer must be on a stage
            # 2) every stage must have people (we will handle no people on stages case later)
            if k == 0 or n == 0:
                return 0

            return (k * s(n - 1, k)) + ((x - k + 1) * s(n - 1, k - 1))
        
        # now handle the case where we dont put people on stages and also handle the scoring
        res = 0
        for stages_used in range(1, min(x,n) + 1):
            res += (pow(y, stages_used, MOD) * s(n, stages_used)) % MOD

        s.cache_clear()
        return res % MOD
            

            

