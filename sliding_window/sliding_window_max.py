from typing import List
from collections import deque

# Originally, was gonna use a min-heap to do a varaition of the top-k algorithm to get an O(n * log(k)) time and O(k) space algorithm. But a better time complexity with same space complexity exists with a deque. To get this solution, the key observation was that if we find that a value after an index in the window is larger that the ones before, will never need to consider any of those previous indices again.

# The monotonic queue method for obtaining the maximum/minimum in a sliding window takes advantage of the fact
# that both the left and right pointers of the window are moving in the same direction. If they are not, we cannot use this method.

# ! To To help with the implementation of all algorithms, imagine yourself as the computer and what needs to be done on each step. Greatly helps

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < k:
            return [max(nums)]
        
        l = r = 0
        max_elems = []
        window_queue = deque()

        while r < len(nums):
            while ((window_queue) and (nums[r] > window_queue[-1])):
                window_queue.pop()
            
            window_queue.append(nums[r])
            r += 1

            if r < k:
                continue
            
            max_elems.append(window_queue[0])

            if nums[l] == window_queue[0]:
                window_queue.popleft()
            
            l += 1

        return max_elems

            

solution = Solution()

solution.maxSlidingWindow([1,2,1,0,4,2,6], 3)

            










        


        