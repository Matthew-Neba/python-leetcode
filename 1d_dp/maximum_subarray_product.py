from typing import List
class Solution:
    #  key this problem is realizing two things
    # 1) We can only consider segments seperate by 0 since the 0 will propagate all future 
    # products to 0
    # 
    # 2) We would like to include the maximum even number of negative numbers within each of these
    # 0 segmented subarrays. This is because an even number of negative numbers will cancel each other out,
    # leading to a higher product. Thus, if we have an odd number of negatives, we can include all but one of them,
    # and since we are only considering contiguos subarrays, 
    # this means we can include the first and exclude the last negative or 
    # exclude the first and include the last negative
    #
    # 
    # O(n) time complexity, O(1) space complexity
    def maxProduct(self, nums: List[int]) -> int:
        # compare the current maximum against the 
        # part of each segment which includes the first negative
        res = float("-inf")
        products = 1
        for num in nums:
            if num == 0:                
                res = max(0,res)
                products = 1
                continue
            else:
                products *= num
                res = max(res, products)

        # compare the current maximum against the 
        # part of each segment which includes the second negative
        products = 1
        for num in reversed(nums):
            if num == 0:
                res = max(0,res)
                products = 1
                continue
            else:
                products *= num
                res = max(res, products) 
        
        return res
            
            
            
            

