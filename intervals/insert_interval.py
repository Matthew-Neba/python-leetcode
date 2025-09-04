from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # figure out where to insert the value
        #
        # Initallly wanted to do binary search but may still have to merge all intervals
        # in the worst case. No benefit to the O(logn) in that case
        #
        
        # so every interval may or may not be merged
        res = []
        new_interval = newInterval
        for i in range(len(intervals)):
            cur_interval = intervals[i]
            # First two conditions are the only situations where the intevals don't overlap
            if new_interval[0] > cur_interval[1]:
                res.append(cur_interval)
            elif new_interval[1] < cur_interval[0]:
                # since the intevals are sorted, we know we can stop if the end point is less that 
                # some other intevals start point
                res.append(new_interval)
                return res + intervals[i:]
            else:
                # the intevals must overlap, merge them
                new_interval = [min(cur_interval[0], new_interval[0]), max(cur_interval[1], new_interval[1])]

        # we have not found a place yet for the new_inteval, it belongs at the end
        res.append(new_interval)

        return res





