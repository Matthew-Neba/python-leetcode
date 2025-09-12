from heapq import heappush, heappop, heapify
from typing import List

# O(nlogk) time, O(k space)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            heappush(self.min_heap, num)

            if len(self.min_heap) > k:
                heappop(self.min_heap)


    def add(self, val: int) -> int:
        heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]


        
