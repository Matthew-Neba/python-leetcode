# If we have a fixed range of values, then can always obtain maximum or minimum in constant time. Can be done with a hashmap storing frequncies of each value. Can also get top k maximum elements with bucket sort variation (can be done for any k if we have only non negative values/can be modified as such by some function. Can also finally use a heap for nlogk if we want top K elements and don't have a fixed range can also use quick select instead of heap.

# key to this problem is realizing that we can ensure the sliding window is valid by ensuring the k <= len(window) - most_frequent_char, this check ensures we properly calculate the minimum number of replacements done for a window

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_freq = [0] * 26

        l = r = 0
        cur_len = max_len = 0

        while r < len(s):
            window_freq[ord(s[r]) - ord("A")] += 1
            cur_len += 1
            r += 1

            # shrink window if invalid
            if (cur_len - max(window_freq) > k):
                window_freq[ord(s[l]) - ord("A")] -= 1
                cur_len -= 1
                l += 1  

            max_len = max(max_len, cur_len)

        return max_len