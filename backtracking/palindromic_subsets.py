from typing import List
# Exponential possible partitions, backtracking is obvious here. Just need a way to check the palindrome constraint optimally
#Key to this problem is realizing that 

# O(n * 2^n) time complexity , O(n) space complexity
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def backtrack(path, start_idx, choice_idx):
            # choice idx is the i'th split (0-indexed)
            if choice_idx > len(s) - 1:
                if start_idx > len(s) - 1:
                    # check if last index was inclueded to ensure 
                    # the partition includes the whole string
                    res.append(path[:])
                return
            
            # check if current partition is a palindrome
            is_pal = True
            l, r = start_idx, choice_idx
            while r > l:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    is_pal = False
                    break
            
            # if palindrome, this partition is valid, split at this index
            if is_pal:
                path.append(s[start_idx:choice_idx + 1])
                backtrack(path, choice_idx + 1, choice_idx + 1)
                path.pop()
            
            # do not split at this index, keep going
            backtrack(path, start_idx, choice_idx + 1)
        
        backtrack([], 0, 0)
        return res

            




        
        