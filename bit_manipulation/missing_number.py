from typing import List
class Solution:
    #
    # Hash set solution is obvious here but that is O(n) in space. Is it possible to do quicker?
    # Perhaps using  some array marking technique or math or perhaps bits?
    #
    # O(n) time complexity, O(1) space complexity
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        supposed_sum = (n)*(n+1)//2
        actual_sum = sum(nums)

        return supposed_sum - actual_sum

        

        
        