from typing import List
from collections import Counter, defaultdict

# Key to this problem is realizing that we need to have ensure the count of all the letters in our current substring is equal to the count of thier corresponding values in the input string. If so, we can partition this substring and keep trying to keep more. 

# O(n) time complexity. O(m) space complexity where m is the unique characters in the input string
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
        
#         string_letters = Counter(s)
#         window_letters = defaultdict(int)
#         window_length = 0
#         res = []

#         def not_smaller_letters(s1,s2):
#             for letter in s1:
#                 if s1[letter] < s2[letter]:
#                     return False
#             return True

#         for char in s:
#             window_letters[char] += 1
#             window_length += 1
            
#             if not_smaller_letters(window_letters,string_letters):
#                 res.append(window_length)
#                 window_letters =  defaultdict(int)
#                 window_length = 0

#         return res


# Key insight to reduce the runtime complexity of this problem is realizing we actually just need to keep track of the last occurence of each letter. This information can be then used to simplify the problem. This can be done by ensuring that we create a new substring with our sliding window when the last index of every character in our sliding window is contained in the sliding window.

#  O(n) time complexity. O(m) space complexity where m is the unique characters in the input string
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = [0] * 26

        for index,char in enumerate(s):
            last_index[ord(char) - ord("a")] = index
        
        res = []
        current_length = 0
        partition_end = 0
        for index, char in s:
            current_length += 1
            partition_end = max(partition_end, last_index[ord(char) - ord("a")])

            if index == partition_end:
                res.append(current_length)
                current_length = 0  
                
        return res


            


