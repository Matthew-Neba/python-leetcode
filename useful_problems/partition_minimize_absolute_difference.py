from collections import defaultdict
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Greedy fails with counter example, do backtracking / dp 

        we can get O(maxSum(num)) time and space but that can be ridiculously expensive since num[i] in 
        range 10^7. 

        That algorithm is pseudopolynomial like the knapsack DP solution, however, maxSum is not small 
        like the target in the knapsack problem. We need to bound the problem purely on n.

        Goal is to find the subsequence of length n (n is len(nums)/2) 
        that gets as close to sum(nums)/2 as possible. 

        Can use meet in the middle technique here to improve the runtime complexity,
        this problem is really tight on those constraints.
        
        Remember, if we can solve a problem for halve of k (where k is any parameter) and then combine them
        to solve the original problem, then we can use the meet in the middle technique
        """
        def subseq_sum(cur, cur_sum, elems_used, split_dict, end):
            if cur > end:
                split_dict[elems_used].append(cur_sum)
                return
            # don't include current value
            subseq_sum(cur + 1, cur_sum, elems_used, split_dict, end)

            # include current value
            subseq_sum(cur + 1, cur_sum + nums[cur], elems_used + 1, split_dict, end)
            return
        
        # calculate the sums of the left and right array subsequences
        left_split = defaultdict(list)
        right_split = defaultdict(list)

        subseq_sum(0, 0, 0, left_split, len(nums)//2 - 1)
        subseq_sum(len(nums)//2, 0, 0, right_split, len(nums) - 1)

        res = float("inf")
        total_sum = sum(nums)
        target_sum = total_sum // 2

        # can now do the binary search for every subsequence in the left subarray
        for elem_count in left_split:
            elem_complement = len(nums)//2 - elem_count

            left_sums = left_split[elem_count]
            # sort right_sums for binary search
            right_sums = right_split[elem_complement]
            right_sums.sort()

            for val in left_sums:
                candidate = None
                low, high = 0 , len(right_sums) - 1
                while low <= high:
                    mid = (low + high) // 2

                    if val + right_sums[mid] <= target_sum:
                        candidate = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                    
                # we have found the value that gets this the closest
                if candidate is not None:
                    split_sum = right_sums[candidate] + val
                    other_split_sum = total_sum - split_sum
                    res = min(res, abs(split_sum - other_split_sum))
            
        return res
