from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Pay attention to the contraints of the problems, can give hints. Ex: for this question, every number in the array could be between [1,size(array) -1]. These constraints suggets we may need to manipulate index's of the array corresponding to the values in the array.

# One way to do it by modifying original array
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             index = abs(nums[i])
#             if nums[index] < 0:
#                 return index
#             else:
#                 nums[index] = -nums[index] 


# Can do this without modifying the array using Floyd's cycle detection algorithm. Firstly, we realize that due to the problem constraints, each index can be viewed as the node of a linked list. The values can also be viewed as a pointer to another node(index). Thus, since there are duplicate numbers, a node is visited more than once and thus a cycle is guaranteed. Now we want to find the beginning of this cyce. Can be done using Floyd's cycle detection algorithm. The foundation for this algorithm is realizing that using math and simulation (key point is simuation and not exactly algebra), we can solve this problem 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1 = fast1 = 0

        # First part of Floyd's cycle detection algorithm
        while True:
            slow1 = nums[slow1]
            fast1 = nums[nums[fast1]]

            if slow1 == fast1:
                break

        # Second part to get the start of the cycle
        slow2 = 0
        while slow2 != slow1:
            slow2 = nums[slow2]
            slow1 = nums[slow1]
        
        return slow2



solution = Solution()
print(solution.findDuplicate([1,2,3,4,4]))