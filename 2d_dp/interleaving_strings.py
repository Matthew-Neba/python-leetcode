class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 
        # 2^n * 2^m * (n+m) time for checking all possible interleavings , This is a ridiculous
        # time complexity, where to cut down on time? Maybe consider another approach?
        #
        # How about instead we make use of the properties of s3 that must be true?
        #
        # We know that all the characters and thier relative ordering from s1 and s2
        # must be preserved. This is a necessary condition. But also notice that this is a sufficient.
        # This is because if this is true, then the gaps in s3 not filled by s1 will be filled by s2
        # and vice versa.
        #
        # The problem now is that s1 and s2 don't have distinct characters. So if we see a character in s3,
        # should we assign it to s1 or s2?
        # 
        # For every character in s3, consider assigning it to s1 or s2. Two choices --> DP
        #
        # (n is length of s1, m is length of s2, k is length of s3)
        # It may seem the complexities are: O(k * n * m) time complexity, O(k * n * m) space complexity
        #
        # But since k = n + m, each (i, j) pair corresponds to exactly one k.
        # Therefore the true complexities are: O( 1 * n * m) time complexity, O(1 * n * m) space complexity
        dp = {}
        def assigner(i,j):
            # dp base case
            if (i,j) in dp:
                return dp[(i,j)]
            
            # recursion base case
            # we have consumed everything
            if i == len(s1) and j == len(s2):
                return True

            cur_k = i + j
            possible = False
            if i < len(s1) and s3[cur_k] == s1[i]:
                possible |= assigner(i+1, j)
            
            if j < len(s2) and s3[cur_k] == s2[j]:
                possible |= assigner(i, j+1)

            dp[(i,j)] = possible
            return dp[(i,j)]
        
        return False if len(s1) + len(s2) != len(s3) else assigner(0,0)
