from typing import List
# When doing binary search and the stopping condition is when we converge on a singular value (no early stopping, searching the entire search space), can use candiates and update them instead of changing the origianl binary search algorithm. For example, to find the minimum index in this problem, I use binary search but update the candiatate if the current element in smaller than the previous candidate.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
 
        #To perform the split, need to find the minimum in the sorted array O(logn)
        def find_min_index(nums):
            min_index = float("inf")
            min_candidate = float("inf")
            low, high = 0, len(nums) - 1
            
            while high >= low:
                mid = (high + low) // 2

                if nums[mid] < min_candidate:
                    min_candidate = nums[mid]
                    min_index = mid

                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return min_index
        
        # need to split the array into the two non descending portions. Then perform binary search 
        # on these two portions. O(2logn)
        min_index = find_min_index(nums)
        first_segment = (0, min_index)
        second_segment = (min_index, len(nums) - 1)

        # run binary search on first segment O(logn)
        low, high = first_segment
        while high >= low:
            mid = (high + low) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        # run binary search on second segment O(logn)
        low, high = second_segment
        while high >= low:
            mid = (high + low) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1



# can solve this problem in one log(n) pass (instead of 3 like the previous) by realizing that we can check if the current interval contains the rotated segment by comparing the end points (low,high). Then whether or not the interval contains the segment gives allows some condition checks to determine if the interval could have the target value. The insight that developped this solution was analyzing the two cases for any interval. Either an interval contains the rotatted segment or it doesnt. Then analzing those two cases.
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1
        while high >= low:
            mid = (high + low) // 2

            if target == nums[mid]:
                return mid
            # if target higher than nums[mid], check if mid is higer than high. If so, cancel lower half. else if mid is less than high, check if target is greater than nums[high]. If so, cancel upper bound. else, cancel lower bound. 
            elif target > nums[mid]:

                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    if target > nums[high]:
                        high = mid - 1
                    else:
                        low = mid + 1
            # if target lower than nums[mid], check if mid is lower than low. .If so, cancel upper half. else if mid is higher than low, check if target less than low. if so, cancel lower bound. else, cancel upper bound
            else:
               
                if nums[mid] < nums[low]:
                    high = mid - 1
                else:
                    if target < nums[low]:
                        low = mid + 1
                    else:
                        high = mid - 1

        return -1

       


 

        