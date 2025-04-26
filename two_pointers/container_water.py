from typing import List

# key here is realizing that we first want as wide and as tall as a container as possible. So initialize pointers to start and end of the array.
# Then, we realize that the only way to have greater area is if bars height increase in a way to increase the area.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights) - 1
        max_water = float("-inf")

        while l < r:
            cur_height = max(heights[l], heights[r])
            cur_water = cur_height * (r-l)

            max_water = max(max_water, cur_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water

