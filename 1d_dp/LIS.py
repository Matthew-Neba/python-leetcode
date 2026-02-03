from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #
        # Can optimize the classic DP formulation of this problem. We can take advantage of the fact that
        # we are only interested in the lengths of the subsequences and 
        # then track the top card of each subsequence. We keep track of the best top card for each length
        # of subsequence. These values are naturally sorted so they allow us to do binary search.
        #
        # Classic example of resstating the DP to optimize it.
        #

        def binary_search(arr, val):
            low, high = 0, len(arr) - 1

            candidate = -1
            while low <= high:
                mid = (low + high) // 2

                if arr[mid] > val:
                    candidate = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return candidate

        N = len(nums)
        heads = []
        for i in range(N - 1, -1, -1):
            idx = binary_search(heads, nums[i])
            if idx == len(heads) - 1:
                heads.append(nums[i])
            else:
                heads[idx + 1] = nums[i]
        
        return len(heads)



