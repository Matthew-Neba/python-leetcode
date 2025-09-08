from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # top k elements pattern, need a heap/bucket sort
        new_stones = [-val for val in stones]
        heapify(new_stones)

        first, second = None, None

        while len(new_stones) > 1:
            first = -heappop(new_stones)
            second = -heappop(new_stones)

            if not first == second:
                heappush(new_stones,-(first - second))
        
        return -new_stones[0] if new_stones else 0


            