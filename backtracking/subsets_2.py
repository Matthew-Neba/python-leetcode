from typing import List

# can use idea similar to combination sum 2. However, we did the sorting method instead of the hashmap method

#  O(n * 2^n) time complexity (the n is for the time it takes to copy the path), O(n) space complexity
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the input list
        nums.sort()
        res = []

        # perform the backtracking now
        def backtrack(path, cur_idx):
            # we have considered all elements
            if cur_idx == len(nums):
                # O(n) time complexity to copy path
                res.append(path[::])
                return
            
            # include the current element
            path.append(nums[cur_idx])
            backtrack(path, cur_idx + 1)
            path.pop()

            # never consider the current element again
            while cur_idx + 1 < len(nums) and nums[cur_idx] == nums[cur_idx + 1]:
                cur_idx += 1

            backtrack(path, cur_idx + 1)  

        backtrack([], 0)
        return res
        