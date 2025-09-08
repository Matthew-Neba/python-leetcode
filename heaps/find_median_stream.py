from heapq import heappush, heappop, heapify
class MedianFinder:
    # can easily do findMedian() in O(nlogn) time, however can we do better?
    # Since we are dealing with dynamic data and need order statistics,
    # Perhaps use a heap? 
    # If we have an even number of elements, 
    # The median = (biggest of smaller half of sorted elems) + 
    # (smallest of bigger half of sorted elems) / 2 . 
    # or If we have an odd number of elements,
    # median = (biggest of the smaller half of sorted elems) (given we always
    # ensure the size of the smaller half is >= the size of bigger half)
    #
    # Perhaps we can use two heaps to simulate these two halfs of the
    # array?
    #
    # With these update methods, we ensure the invariant of the left heap always having
    # all elements smaller than the right heap after each update step. Can be proved
    # with induction.
    #

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        # compare sizes of heaps
        # compare num to top of heaps
        #
        # O(logn) time complexity , O(n) space complexity
        if self.size == 0:
            # add to left heap
            heappush(self.left_heap, -num)

            self.size += 1
            return

        # dealing with max heaps so need to be careful with negatives
        # cur num is smaller than the max of the mins
        if num < -self.left_heap[0]:
            # add this values to max of mins, adding negative since python only
            # has min heaps
            heappush(self.left_heap, -num)

            # balance heaps if too big of a size difference,
            # remember we are always making left heap bigger than right heap 
            # but only by the maximum of 1
            if len(self.left_heap) > 1 + len(self.right_heap):
                popped_value = -heappop(self.left_heap)

                # now add this to the min of the maxs heap
                heappush(self.right_heap, popped_value)
        
        else:
            # add this value to the min of maxs
            heappush(self.right_heap, num)

            if len(self.right_heap) > len(self.left_heap):
                popped_value = heappop(self.right_heap)

                # now add this to the max of mins heap
                heappush(self.left_heap, -popped_value)

        self.size += 1
        return


    def findMedian(self) -> float:
        # O(1) time complexity, O(1) space complexity
        if self.size % 2 == 0:
            return (-self.left_heap[0] + self.right_heap[0])/2
        else:
            return -self.left_heap[0] 

