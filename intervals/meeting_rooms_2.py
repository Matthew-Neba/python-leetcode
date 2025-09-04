from typing import List
from heapq import heappush, heappop, heapify

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort intervals by start time
        #
        # We know that we can just record the time for each day that corresponds to the time meetings
        # must start after. That is because the intervals are sorted by start date, so a meeting
        # cannot start before one we have already booked.
        #
        # If a meeting happens before the end time for a day, it must be moved to another day. The question
        # becomes what day do we move it to? Key insight is that we can choose any available day. This is because
        # The rest of the start times must come after the current meeting start time. Gaps don't matter.
        # 
        # Problem now becomes, how to determine which day to choose? O(n^2) in worst case since we would
        # have to compare the current meeting to all the previous days, can we do it more efficiently?
        #   
        # Well, we know the meeting cannot happen if the miniimum end time for all days
        # is greater than the current meeting start time. We also know that it can also always
        # just then use that minimum end time day. Since we are dealing with repeated minimums and maximums,
        # we can use a heap
        #
        # TODO: In short, always scedule meetings the earliest day they can be sceduled. This is the most
        # efficient way to do the problem even though we can choose any available day.
        
        # sort intervals to ensure we can ignore the gaps between meetings on days
        # (sorting ensures that we do not have to consider the case of booking meetings earlier than any current ones on a day),
        intervals.sort(key = lambda interval: [interval.start, interval.end])

        # will contain the end times of each day
        min_heap = [float("inf")]

        for interval in intervals:
            # check minimum element
            if min_heap[0] > interval.start:
                # we need to create a new day
                heappush(min_heap,interval.end)
            else:
                # update the end time of the minimum day
                heappop(min_heap)
                heappush(min_heap, interval.end)

        # -1 to handle the infinity we added
        return len(min_heap) - 1




