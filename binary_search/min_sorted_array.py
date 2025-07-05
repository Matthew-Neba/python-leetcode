from typing import List

# When doing binary search and the stopping condition is when we converge on a singular value (no early stopping, searching the entire search space), can use candiates and update them instead of changing the origianl binary search algorithm. For example, to find the minimum index in this problem, I use binary search but update the candiatate if the current element in smaller than the previous candidate.
class Solution:
    def findMin(self, nums: List[int]) -> int:
            min_candidate = float("inf")
            
            low, high = 0, len(nums) - 1
            while high >= low:
                mid = (high + low) // 2

                min_candidate = min(min_candidate, nums[mid])
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return min_candidate