from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        final_products = [1] * len(nums)
        front_products = [1] * len(nums)
        back_products = [1] * len(nums)


        for i in range(1,len(nums)):
            front_products[i] = front_products[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            back_products[i] = back_products[i+1] * nums[i+1]

        for i in range(len(nums)):
            final_products[i] = front_products[i] * back_products[i]
            
        return final_products

        
# more optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        final_products = [1] * len(nums)

        # calculate front_products in the final_products array
        for i in range(1,len(nums)):
            final_products[i] = final_products[i-1] * nums[i-1]
        
        #calculate the back_products and final_products simultaneously
        back_products = 1
        for i in range(len(nums) - 1, -1, -1):
            final_products[i] *= back_products
            back_products *= nums[i]
            
        return final_products

        