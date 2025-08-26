class Solution:
    def longestPalindrome(self, s: str) -> str:
        # To determine if a string is a palindrome, we can check if the  first and last characters
        # are the same. If they are, the string is a palindrome if and only if 
        # the remaining string is also a palindrome. 
        # We can thus take advantage of this fact.
        # We know that there are n(n+1)/2 substrings,
        # we can compute whether each of them is a palindrome in constant
        # time if we know if another substring (middle) part is a substring
        # gives us n(n+1)/2 time complexity and n^2 space complexity 
        # 
        # However, this solution repeated computes whether or not some substrings are palindromes
        # too many times. Even if we memoize these, these function calls still takes O(1) time.
        #
        
        # Firstly, we realize that each palindrome has a center. So if we start at each center
        # and expands outwards, we will eventually check all palindromes centers. There are at most
        # 2n centers (1 for even and 1 for odd length palindrome). Checking whether each center gives
        # a palindrome can be done in O(n) time. Therefore, O(n^2) solution but O(1) space
        max_idx = (0,0)
        max_len = 1 
        for i in range(len(s)):
            # odd length palindromes center
            l,r = i,i
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    # check if the current palindrome is longer than the current longest
                    if r - l + 1 > max_len:
                        max_len = r - l + 1
                        max_idx = (l,r)
                    l -= 1
                    r += 1
                else:
                    break
            
            # even length palindromes center
            l,r = i,i+1
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    # check if the current palindrome is longer than the current longest
                    if r - l + 1 > max_len:
                        max_len = r - l + 1
                        max_idx = (l,r)
                    l -= 1
                    r += 1
                else:
                    break
            
        return s[max_idx[0]:max_idx[1] + 1]
