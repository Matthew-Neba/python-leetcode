from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        """
        We can use a variant of quicksort called quick select here.

        [6,7,4,1,3]

        [1 3 6 7 4]
        """

        def partition(pivot_index, l, r):
            pivot_value = nums[pivot_index]
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]

            boundary = l
            for i in range(l,r):
                if nums[i] < pivot_value:
                    nums[i], nums[boundary] = nums[boundary], nums[i]
                    boundary += 1

            nums[boundary], nums[r] = nums[r], nums[boundary]
            # boundary position is where the new pivot is
            return boundary


        def quick_select(l,r,k):
            # parition first
            pivot_index = random.randint(l,r)
            pivot_position = partition(pivot_index, l , r)

            greater_elems = r - pivot_position
            if greater_elems == k - 1:
                return nums[pivot_position]
            elif greater_elems > k - 1:
                # too many elements greater
                return quick_select(pivot_position + 1, r, k)
            else:
                # too little elements greater
                return quick_select(l, pivot_position - 1, k - 1 - greater_elems)
        
        return(quick_select(0, len(nums) - 1, k))


