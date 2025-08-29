class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Key to this problem is realizing we can iterate through both strings simultaneously
        # with pointers. The goal is to figure out which indexes in word1 we should leave as they are
        # and which ones we need to change. We can do this by iterating through word1 and word2
        # using thier respective pointers. If thier characters match, then we know we should not make any changes
        # to word1. However, if thier characters  don't match, then we know a change must be made
        # to word1 at that index to make it the same as word2 at that index.
        # There are 3 changes we are permitted to do, update,insert and delete.
        # We make all those changes and we see which one have the smallest edit distance.
        #
        # Since we are thus trying to ensure word1 and word2 indexes have a certain property(they are equal),
        # we can use the LCS DP pattern here.

        rows,cols = len(word1), len(word2)

        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        # base case (handling the edit distance for empty strings)
        for i in range(0, rows):
            dp[i][cols] = len(word1) - i
        
        for j in range(0, cols):
            dp[rows][j] = len(word2) - j


        for i in range(rows - 1, -1, -1):
            for j in range(cols -1, -1 , -1):
                # if they are the same at thier indexes
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    # consider the edit distance cost of inserting, deleting, and updating
                    dp[i][j] = 1 + min(dp[i][j+1] , dp[i+1][j] , dp[i+1][j+1])
        
        return dp[0][0]

