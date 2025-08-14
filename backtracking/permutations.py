from typing import List

# we need some way to extract all the elements we still need to consider for the permutation, we can do this by removing and swapping elements as we build the permutations. The cur_pos keeps tracks of the rest of the elements we still need to consider for the permutation.

# O(n * n!) time complexity, O(n) space complexity
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(path, cur_pos):
            if cur_pos >= len(nums):
                # O(n) time
                res.append(path[:])
                return
            
            # keeps track of the current element added to path, we do not want to include it in the further permutation options
            cur_num = nums[cur_pos]
            for i in range(cur_pos,len(nums)):
                # swap out the element
                nums[i], cur_num = cur_num, nums[i]
                path.append(cur_num)
                backtrack(path, cur_pos + 1)
                path.pop()

                # swap it back into the same position so we don't disrupt the other backtracks
                nums[i], cur_num = cur_num, nums[i]
        
        backtrack([], 0)
        return res
