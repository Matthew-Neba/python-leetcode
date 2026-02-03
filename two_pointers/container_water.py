from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #
        # For this problem, we are maintaining the invariant that the two bars making up the maximum are in the 
        # range [l , r]. Where l is our left pointer and r is our right pointer.
        #
        # Notice that given that the optimal two bars are in the range [l, r], if height[l] < height[r], then,
        # we never need to consider l again. This is because the width of the range is always decreasing,
        # and since the height of any container made with l is bounded by height of l, the area of that container 
        # is guaranteed to be smaller than container (l,r). This same argument can be applied to r.
        #
        N = len(height)
        l = 0
        r = N - 1
        
        res = float("-inf")
        while l < r:
            cur_area = min(height[l], height[r]) * (r - l)
            res = max(res, cur_area)

            if height[l] < height[r]:
                l += 1
            elif height[l] == height[r]:
                # if equal, we have found best for both l and r, we can decrease them both
                l += 1
                r -= 1
            else:
                r -= 1
        
        return res
