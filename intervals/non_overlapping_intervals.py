from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # There is a greedy solution with sorting.
        #
        # If two intevals overlap, we know we need to remove one of them. We would like to remove the one
        # with the highest number of overlaps. This will reduce our overall number of overlaps the quickest.
        # This mean we will thus remove the interval with the greatest end point of these two. This is because
        # that end point can cause further overlaps down the line.
        #
        # TODO: In short: Always remove the conflicting interval with the greater end time
        intervals.sort()
        res = 0

        l = 0
        r = 1

        #  O(nlogn) time complexity, O(1) space complexity
        while r < len(intervals):
            # check if there is an overlap
            if intervals[l][1] > intervals[r][0]: 
                # remove the interval with the greater end point
                if intervals[l][1] > intervals[r][1]:
                    l = r
                res += 1
                r += 1
            else:
                # no overlap
                l = r
                r += 1
        
        return res
        
                
