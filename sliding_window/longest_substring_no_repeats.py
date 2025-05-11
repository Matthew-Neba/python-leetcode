# combining hash set with sliding window approach here, hashset to keep ensure the sliding window has no duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        max_length = 0
        cur_length = 0
        l = r = 0

        dup_set = set()
        
        while r < len(s):
            if (s[r] not in dup_set):
                cur_length += 1
                max_length = max(max_length, cur_length)
                dup_set.add(s[r])
                r += 1
            else:
                dup_set.remove(s[l])
                cur_length -= 1
                l += 1

        return max_length

   
            