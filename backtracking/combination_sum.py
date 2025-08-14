from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(path, choice_idx, total_sum):
            # base case, considered all values
            if choice_idx >= len(nums):
                return

            # no negative values in nums, the target cannot get smaller, prune the decision tree
            if total_sum > target:
                return 
            
            if total_sum == target:
                res.append(path[:])
                return

            # include the current value in the combination
            path.append(nums[choice_idx])
            backtrack(path, choice_idx, total_sum + nums[choice_idx])

            # do not include the current value in the combination
            path.pop()
            backtrack(path, choice_idx + 1, total_sum)
        
        backtrack([], 0, 0)
        return res




