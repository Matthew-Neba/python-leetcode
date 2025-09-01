from typing import List

# Key to this problem is realizing that the XOR(^) operation is similar to inverting a light switch. If it was already on, it turns it off. If it was off, it turns it on. We can view every number as having a binary representation. The positions of the 1's can be seen as the light switches it targets when it is XOR to the total(represents the light switches). If we have an even number of flicks on a light swicth, it will be reset to it's initial position of 0. Since every number is included twice except the one number, they will reset thier light swicthes positions and the only light switches on will be the ones from the single number.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res