from typing import List
class Solution:
    # 
    # Notice that if a partition into two subsets is possible, it must equal be equal to
    # sum(nums)/2. Therefore, we just need to see if there exists some partition of the
    # numbers such that thier sum is equal to sum(nums)/2. 
    #
    # Problem becomes 0/1 knapsack equivalent
    # In 0/1 knapsack, be careful to seperate the DP arrays
    # get  the sum of numbers
    # O(n*target) time complexity and O(target) space complexity
    def canPartition(self, nums: List[int]) -> bool:
 
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
         
        target = total_sum // 2  # still an integer since we did floor division

        dp_old = [False] * (target+1)
        dp_old[0] = True
        for num in reversed(nums):
            # important for tabulation to make sure you are seperating the tables, so
            # one does not influence another
            dp_new = dp_old[:]
            for i in range(len(dp_old)):
                # can now reach all values + num
                if dp_old[i] and i + num <= target:
                    dp_new[i+num] = True
            dp_old = dp_new
            
        return dp_new[target]



            




