from typing import List
from collections import defaultdict

# trick for this problem is realizing can search for next or previous element in a sequence in constant time using a hashset/hashmap.Other trick is realizing that all sequences build on top of each other, ex: if 2,3,4,5 is a sequence then 3,4,5 must also be a sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   

        num_search = set(nums)
        max_length = 0
        
        for num in num_search:
            # check if we are at the start of a sequence
            if num-1 not in num_search:
                length = 1
                # see how long the sequence is
                while num+length in num_search:
                    length += 1
                
                max_length = max(length, max_length)

        return max_length
    
Solution = Solution()

print(Solution.longestConsecutive([1,2,0,1]))