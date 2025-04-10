from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_dict = defaultdict(list)

        for s in strs:
            freq_list = [0] * 26

            for c in s:
                freq_list[ord(c) - ord("a")] += 1
        
            freq_tuple = tuple(freq_list)

            str_dict[freq_tuple].append(s)
        
        return list(str_dict.values())
    

strs = ["act","pots","tops","cat","stop","hat"]

solution = Solution()

print(solution.groupAnagrams(strs))