from typing import List

# key to this problem is realizing that we can get total area of water by summing area of water trapped in every individual location. Second major key is realizing we can use two pointers and keep track of left and right minimuns to obtain this water in linear time
class Solution:
    def trap(self, height: List[int]) -> int:

        l,r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        cur_water = 0   

        while l < r:
            if lMax <= rMax:
                cur_water += lMax - height[l]
                l += 1
                lMax = max(lMax, height[l])
            else:
                cur_water += rMax - height[r]
                r -= 1
                rMax = max(rMax, height[r])
                

        return cur_water


solution = Solution()
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))
