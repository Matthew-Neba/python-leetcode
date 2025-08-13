from typing import List

#  Solution cannot be better than 2^n since there are 2^n possible subsets for any set, and we need to atleast create those subsets. We would also like a list of lists. This suggests backtracking may be viable here.


# O(n * 2^n) time complexity, 2*n recursive calls since 2^n nodes in a full decision tree, and for each recursive call, we are copying path O(n)
# O(n + n) = O(n) space complexity, n for the recursive stack other n for the space to store path since it is being reused (popping and reusing it) 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # very similar to dfs, path is like the root node here
        def backtrack(path, choices_idx):
            nonlocal res
            if choices_idx == len(nums):
                # reached a leaf node, one set of choices out of all possible ones 
                # remember python passes in by value, need to copy the path before appending it to res
                res.append(path[::])
                return
          
            # explore the decision tree further, only two choices in the decision tree split point, include the current value or not

            # include the current choice
            path.append(nums[choices_idx])
            backtrack(path, choices_idx + 1)

            # pop off the current choice and continue exploring the other decision tree path (without the current value)
            path.pop()
            backtrack(path, choices_idx + 1)

            return

        backtrack([],0)
        return res

        






            


        

        