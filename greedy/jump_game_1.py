from typing import List

# Key to this solution was realizing that it always benefits us to stop at the spot which will allow use to jump further than what we can currently jump. This is because we can always choose to not jump as far if we have the jump power by stoping early. But we can never choose to jump further if we don't have the jump power.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_left = -1

        for i in range(0, len(nums)):
            # we have arrived, no need to jump more
            if i == len(nums) - 1:
                return True

            # we can jump further if we stop here so stop here and recharge jumps
            if nums[i] > jump_left:
                jump_left = nums[i]

            # if we have no more jump power, we cannot keep going to the end
            if jump_left < 1:
                return False
            
            jump_left -= 1
        
           
        