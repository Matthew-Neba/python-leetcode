
# original solution was to break down the array into the segments that are not odd. Then these segments would be smartly used to calculate all the nice arrays. However, this solution had a time complexity of O(n) and a space complexity of O(n). Can do better with a three pointer approach to get a time complexity of O(n) and a space complexity of O(1)

# Three pointer sliding window technique is useful when wanting to use a sliding window but need to keep track of some elements that come before the sliding window. Use a left, middle and right pointer

# class Solution(object):
#     def numberOfSubarrays(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         res = 0

#         # get length of not nice segments
#         segments = []
#         count = 0   
#         for i in nums:
#             if i % 2 == 0:
#                 count += 1
#             else:
#                 segments.append(count)
#                 count = 0
#         # get length of final not nice segment
#         segments.append(count)

#         # calculate all not nice subarrays
#         i = 0
#         while i + k < len(segments):                        
#             # add without combinations of start and end segments
#             res += 1 + segments[i] + segments[i + k]
#             # add combination
#             res += segments[i] * segments[i + k]
#             i += 1
        
#         return res
    
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0

        odd_count = 0
        l = m = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                odd_count += 1

            while odd_count > k:
                if nums[l] % 2 == 1:
                    odd_count -= 1
                l += 1
                m = l
        
            if odd_count == k:
                while nums[m] % 2 == 0:
                    m += 1
                res += (m - l) + 1
            
        return res
    

                        









        


        

        

