from collections import defaultdict

# Key to this problem is realizing that the invariant of the sliding window is ensuring the frequency of every element in the window is less than or equal to the frequncy of the permutation string. Can then just check if the length of the window is equal to the length of the permutation string. If the invariant is true and thier lengths are equal, this implies the sliding window contains an anagram/permutation of the permutation string. 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # check less than or equal and check for presence, if not present, move window to spot, adjust and check endpoints
        # on each window move
        perm_freq = [0] * 26
        cur_freq = [0] * 26

        for ch in s1:
            perm_freq[ord(ch) - ord("a")] += 1

        l = r = 0
        cur_len = 0

        while r < len(s2):
            cur_char = s2[r]

            if cur_freq[ord(cur_char) - ord("a")] < perm_freq[ord(cur_char) - ord("a")]:
                cur_len += 1
                cur_freq[ord(cur_char) - ord("a")] += 1
                r += 1
                if cur_len == len(s1):
                    return True
            else:
                prev_char = s2[l]

                cur_len -= 1
                cur_freq[ord(prev_char) - ord("a")] -= 1
                l += 1
            
        return False
                







        