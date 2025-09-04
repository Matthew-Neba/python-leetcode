from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval:(interval.start, interval.end))

        for i in range(len(intervals) - 1):
            # check if any conflicts
            if intervals[i].end > intervals[i+1].start:
                return False
        
        return True
                