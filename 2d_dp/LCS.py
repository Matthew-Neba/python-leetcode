
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #  "cadt"
        #  "cchats"
        #
        # The key to this problem is realizing that we can iterate through both strings
        # simultaneously with two pointers. The goal is to figure out which characters belong to the LCS
        # If the characters at both pointers match,
        # then those characters must be part of the lcs. The tricky part happens when they
        # don't match. In this case, it can be seen that a "gap" (skipping a character) must 
        # exist in either string 1 or string 2 or perhaps both. This gap can be seen as excluding
        # a character from the lcs. We can create this gap in each string by incrementing
        # each string pointer respectively. We can use DP to check whether gapping string 1 or string 2
        # gave a better LCS.
        #
        dp = {}
        
        def find_longest(i,j):
            start_i, start_j = i,j

            # dp base case
            if (i,j) in dp:
                return dp[(i,j)]

            # recursion base case
            if i >= len(text1) or j >= len(text2):
                return 0

            res = 0
            while i < len(text1) and j < len(text2) and text1[i] == text2[j]:
                i += 1
                j += 1
                res += 1
            
            # gap string 1
            gap_string_1 = find_longest(i+1,j)

            # gap string 2
            gap_string_2 = find_longest(i,j+1)

            # gap both
            gap_both = find_longest(i+1, j+1)

            res += max(gap_string_1, gap_string_2, gap_both)

            dp[(start_i,start_j)] = res
            return res 
            
        find_longest(0,0)
        return dp[(0,0)]


# tabulation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text1), len(text2)
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        for i in range(rows -1, -1 , -1):
            for j in range(cols -1, -1, -1):
                if text1[i] == text2[j]:
                    print(len(dp), len(dp[0]))
                    print(i,j)
                    dp[i][j] = 1 + dp[i+1][j+1]     
                else:
                    # consider gapping string 1, gapping string 2 or gapping both
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1] , dp[i+1][j+1])

        return dp[0][0]
        