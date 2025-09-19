from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # perfect sliding window
        # O(n) time, O(n) space
        #
        #  What is the sliding window area of interest? count of interesting elements
        #
        #  Need a way to efficiently maintain and retrieve count of interesting elements
        #  Can use a prefix sum to efficiently retreive them
        #
        #  (prefix[r + 1] - prefix[l]) % modulo == k     ===> (for some integer t)
        #  prefix[r + 1]  == prefix[l] + k + modulo * t  ===> (apply mod on both sides)
        #  (prefix[r + 1]) % modulo  == (prefix[l] + k) % modulo
        #
        # Can use a hashmap to store all the l values of (prefix[l] + k) % modulo , then, we can 
        # just find these for the current r in constant time. We are finding the modulo complements
        # for each r. Similar to the idea in two sum.
        prefix_sums = [0]
        res = 0
        
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                prefix_sums.append(prefix_sums[-1] + 1)
            else:
                prefix_sums.append(prefix_sums[-1])

        complement_count = defaultdict(int)
        
        for r in range(len(nums)):
            # add this current r as a choice to the sliding window
            complement_count[(prefix_sums[r] + k) % modulo] += 1

            # find the complement
            complement = prefix_sums[r + 1] % modulo
            res += complement_count[complement]

        return res





            


