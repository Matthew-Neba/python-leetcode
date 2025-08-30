class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #
        # Key to this problem is realizing that we know what to do when we encounter an
        # alph character or a ".". We can just increment the positions we are comparing in our
        # s and t strings. The issue arises with "*". In this scenario, we have the decision
        # to take any number of characters. 0,1,...,rest of string s. But we don't know which choice
        # will end up matching our s string. We need to check each one and see
        # which matces. Also, there will be repeated function calls as well. 
        # So we can use the string DP pattern here.
        # 
        # Key insight to this problem was realizing instead of checking every possible
        # value that * can consume, we could just say it consumes 0 or atleast 1. O(n)
        # to O(1). Another key insight was to look ahead to see if * was present before making
        # decisions on each char.

        dp = {}
        def matcher(i,j):
            # dp base case
            if (i,j) in dp:
                return dp[(i,j)]
            
            # Recursion base cases
            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            match_found = False
            # look ahead, see if * ahead in p before consuming the char in s,
            # keep in mind that for these conditions, s could be fully consumed
            if j+1 < len(p) and p[j+1] == "*":
                # take 0 char in s
                match_found |= matcher(i, j+2)

                # take atleast one char in s if s has any
                if i < len(s) and (s[i] == p[j] or p[j] == "."):
                    match_found |= matcher(i+1, j)
            else:
                # take one character in both is s has any
                if i < len(s) and (s[i] == p[j] or p[j] == "."):
                    match_found |= matcher(i+1, j+1)

            dp[(i,j)] = match_found
            return dp[(i,j)]

        return matcher(0,0)


            




