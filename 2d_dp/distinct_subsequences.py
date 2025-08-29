class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #  exponential if we use backtracking
        #
        # This follows the typical LCS/String 2D DP pattern
        # 
        # They key insight is that the backtracking solution has
        # repeated subtrees where we are trying find the number of distinct ways
        # which some remaining part of s contains the remaining part of t
        # as a subsequence.
        #
        # O(m*n) time complexity, O(m*n) space complexity , m is len(s), n is len(t)
        dp = {}
        def distinct_ways(i,j):
            # dp base case
            if (i,j) in dp:
                return dp[(i,j)]

            # we have sucessfully fully matched t
            if j == len(t):
                return 1

            # no more remaining in s while t has some,can never be matched
            if i >= len(s):
                return 0
            
            # recursion
            ways = 0
            print(i,j)
            if s[i] == t[j]:
                # use character
                take_distinct = distinct_ways(i+1, j+1)

                # don't use
                no_take_distinct = distinct_ways(i+1, j)

                ways = take_distinct + no_take_distinct
            else:
                # no match here,only option is to not use the current character
                ways = distinct_ways(i+1, j)

            dp[(i,j)] = ways
            return dp[(i,j)]

        return distinct_ways(0,0)
            
            



