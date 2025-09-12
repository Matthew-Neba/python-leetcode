from typing import List
from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # The absolute difference between any two elements in the subarray must be less than 3

        # Efficiently ensure a subarray is continuos
        # Efficient retrieve these subarrays
        #
        # Every continuos subarray can be broken down into more continuos subarrays
        #
        #  sliding window approach is O(n^2) time , O(1) space
        #
        #  But we see that if we can quickly get the minimum and maximum of the sliding windows, this problem
        # can be done in O(n) time and O(n) time. 
        res = 0
        q_min = deque()
        q_max = deque()

        l = 0
        for r in range(len(nums)):
            # add to the sliding window
            while q_min and q_min[-1] > nums[r]:
                q_min.pop()
            q_min.append(nums[r])

            while q_max and q_max[-1] < nums[r]:
                q_max.pop()
            q_max.append(nums[r])

            # get all the continuos subarays that end at this r
            while abs(q_min[0] - q_max[0]) > 2:
                if q_min[0] == nums[l]:
                    q_min.popleft()

                if q_max[0] == nums[l]:
                    q_max.popleft()

                # decrease the sliding window
                l += 1
            
            # we are at a valid window
            res += r - l + 1
        
        return res
                
