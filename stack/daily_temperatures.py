from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 
        # Key to this problem is realizing that we can start at the end of the 
        # array and work backwards. We know that if a day is colder than the next 
        # day, we can just say the next warmer day is the next day. However, if it is 
        # warmer than the next day, we know that we don't need to individually check each
        # day past that colder day. We can just skip to the day warmer than that colder day.
        # However, this is still potentially O(n^2), to reduce it to O(n), we realize that
        # once we skip over a day, we can safely never consider that day again. This is because
        # future checks will only be looking for days warmer than it anyways.
        # Each value can be added and removed from the stack exactly once. 
        #
        # O(n) time complexity, O(n) space complexity
        #

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1 , -1):
            day_count = 1
            # look for next warmer day
            while stack and stack[-1][0] <= temperatures[i]:
                colder_day, next_warmer_day = stack.pop()
                day_count += next_warmer_day
            
            # did not find a warmer day
            if not stack:
                day_count = 0

            stack.append((temperatures[i], day_count))
            res[i] = day_count
                 
        return res


