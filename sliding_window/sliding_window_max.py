from typing import List
from collections import deque

# Originally, was gonna use a min-heap to do a varaition of the top-k algorithm to get an O(n * log(k)) time and O(k) space algorithm. But a better time complexity with same space complexity exists with a deque. To get this solution, the key observation was that if we find that a value after an index in the window is larger that the ones before, will never need to consider any of those previous indices again.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # instead , add elements one at a time


            










        


        