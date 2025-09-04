from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 
        # Key inefficiencuy is having to compare every new interval to the previous non overlapping 
        # ones O(n^2). Can we reduce it? Perhaps sorting or sweep line algorithm?
        # 
        # Can use a method similar to insert intervals here, we just need to sort them first

        # sort by start points , nlogn, python implicitly sorts by first element, then second element, etc in an iterable
        intervals.sort()
        
        res = []
        merge_interval = intervals[0]
        for i in range(len(intervals)):
            #  check if merge
            if merge_interval[1] >= intervals[i][0]:
                # merge
                merge_interval = [min(intervals[i][0],merge_interval[0]), max(intervals[i][1],merge_interval[1])]
            else:
                # no merge
                res.append(merge_interval)
                merge_interval = intervals[i]

        res.append(merge_interval)
        return res
            







