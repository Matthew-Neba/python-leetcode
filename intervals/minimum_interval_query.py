from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #
        # Fundemental problem is we would like to:
        #
        # 1) Efficiently obtain the minimal interval lengths for each query 
        # 2) Efficient map these to the queries
        #
        # Doing 1 then 2 is hard, can we do 2 then 1?. i.e: figure out the intervals that q can belong to and
        # choosing the minimum of those? 
        #
        # We can use a min-heap to manage candidate intervals. For each query, we add any new intervals 
        # that start before or at the query, and remove those that end before the query. This ensures 
        # the heap only contains intervals that actually cover the current query. Since queries are processed 
        # in sorted order, once an interval no longer covers a query, it will never cover any future queries, 
        # so we can safely discard it. The top of the heap then always gives the smallest valid interval length.
        #
        # This problem is essentially about careful heap state management. 
        #
        res = {}
        intervals.sort()
        min_heap = []

        #  i will represent the queries we are still considering
        i = 0
        for q in sorted(queries):
            # add all intervals the current query and future ones can fit into
            while i < len(intervals) and (intervals[i][0] <= q ):
                # valid interval,can add to the heap
                i_length = intervals[i][1] - intervals[i][0] + 1
                i_end = intervals[i][1]
                heappush(min_heap, (i_length, i_end))
                i += 1
            
            # remove all intervals that were added by a previous query
            # but no longer contain this query
            while min_heap and min_heap[0][1] < q:
                heappop(min_heap)
            
            # we now have the minimum of the valid intervals at the top of the heap
            res[q] = min_heap[0][0] if min_heap else -1
        
        # get the corret order for the queries
        return [res[q] for q in queries]
            