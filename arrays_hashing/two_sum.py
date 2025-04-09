from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        cmplement_dict = {}
        
        for i,num in enumerate(nums):
            cmplement = target - num

            if num in cmplement_dict:
                return [cmplement_dict[num], i]
            else:
                cmplement_dict[cmplement] = i
        
        
