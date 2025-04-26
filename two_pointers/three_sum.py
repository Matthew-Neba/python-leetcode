from typing import List

# Don't be scared of sorting. Especially if you see that solution is already O(n^2), can lead to better space complexity or easier time coding the solution. Here, the original hashMap solution gives O(n^2) time but O(n) space. If we sort the input array, can use two pointer approach to get O(n^2) time and O(1) space.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []

        # make sure nums is sorted for 1) easy way to check for no duplicate triplets, 2) enable two pointer approach
        nums.sort()

        for i,curnum in enumerate(nums):

            # since sorted, if first element greater than zero, no solution, finished
            if curnum > 0:
                break

            # make sure no duplicate triplets are added to the list
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
                
            l,r = i+1, len(nums)-1

            while l < r :
                threesum = curnum + nums[l] + nums[r]

                if threesum == 0:
                    if (l > i+1) and (nums[l] == nums[l-1]):
                        l += 1
                        continue

                    triplets.append([nums[l], nums[r], curnum])
                    l+= 1
        
                elif threesum < 0:
                    l+= 1
                else:
                    r -= 1
               
        
        return triplets
                







       



my_soluion = Solution()
print(my_soluion.threeSum([-1,0,1,2,-1,-4]))





        
       