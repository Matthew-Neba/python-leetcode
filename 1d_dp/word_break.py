from typing import List
class Solution:
    # Two ways to do this problem here, can search for the prefixes of the current string
    # up to length m ( m is the maximum string length in the dictionary) , if present in the dictionary
    # time complexity would be O(m^2) time for the string manipulation and O(t) space, 
    # (t is the total number of words in the dictionary) for the set. This is for each search
    #  
    #
    # Or, we could see if each string in the dictionary if a prefix of the current string
    # this is O(m*t) time complexity and O(1) extra space for each search
    #
    # Due to given constraints, t > m . So will do the first method
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dictionary = set(wordDict)

        max_length = 0
        for word in dictionary:
            max_length = max(max_length, len(word))

        dp = {}
        def word_breaker(cur_idx):
            # dp base case
            if cur_idx in dp:
                return dp[cur_idx]
            
            # recursion base case
            if cur_idx >= len(s):
                return True

            cur_string = ""
            can_break = False
            for i in range(cur_idx, cur_idx + max_length):
                if i >= len(s):
                    break
                    
                cur_string += s[i]
                if cur_string in dictionary:
                    # check if we can break the rest of the string
                    can_break |= word_breaker(i + 1)
                        
            dp[cur_idx] = can_break
            return dp[cur_idx]

        word_breaker(0)
        return dp[0]







        