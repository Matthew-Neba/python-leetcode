from typing import List

# Key to this problem is realizing that the only triplets we can possibly use to reach the target triplet are triplets which values are smaller than thier corresponding values in the target triplet for all the indexes. We can thus check if these possible triplets have the target triplet values. 

# O(n) time complexity and O(1) space complexity
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # merge all triplets where the a,b,c terms are all less than or equal to the correponsding
        # values in the target triplet
        res_triplet = [-1,-1,-1]

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                res_triplet[0] = max(res_triplet[0], triplet[0])
                res_triplet[1] = max(res_triplet[1], triplet[1])
                res_triplet[2] = max(res_triplet[2], triplet[2])

            if res_triplet == target:
                return True
        
        return False
        