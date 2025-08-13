from typing import List
from collections import Counter

# Key to this pro

#  O(2^n) time complexity (to build decision tree), O(n) space complexity
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        # O(n) time complexity, O(n) space complexity for this counter dictionary
        freq_dict = Counter(candidates)
        unique_elems = list(freq_dict.keys()) 

        def backtrack(path, cur_idx, total_sum):
            if total_sum == target:
                res.append(path[:])
                return

            if cur_idx >= len(unique_elems):
                return 
            
            if total_sum > target:
                return
            
            cur_element = unique_elems[cur_idx]

            # dont include the current element
            backtrack(path, cur_idx + 1, total_sum)

            # include the current element
            if freq_dict[cur_element] > 0:
                freq_dict[cur_element] -= 1
                path.append(cur_element)
                backtrack(path, cur_idx, total_sum + cur_element)

                # important to both undo the path changes and the dictionary changes since all nodes in the decision tree are sharing them
                path.pop()
                freq_dict[cur_element] += 1
           
        backtrack([], 0, 0)
        return res
        