from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Notice that the array stores a maximum of n distinct numbers. Therefore, the first missing positive
        must be in the range 1 to n+1. We know that if the array then
        does not contain all the numbers in range 1 to n+1, then we can return the smallest number
        that it does not contain in that range 1 to n+1. 

        i.e: we are interested in sorting the numbers in the array that are
        in the range 1 to n.

        Cyclic sort is the perfect method to sort elements in range 0 to n, in O(n) time and O(1)
        space.
        """
        n = len(nums)

        cur_idx = 0
        while cur_idx < n:
            correct_idx = nums[cur_idx] - 1
            # 1) number in the right range
            # 2) number in correct position already and duplicate check in one 
            if  0 <= correct_idx < n and nums[correct_idx] != correct_idx + 1:
                nums[cur_idx], nums[correct_idx] = nums[correct_idx], nums[cur_idx]
            else:
                cur_idx += 1   

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
                
            
       





