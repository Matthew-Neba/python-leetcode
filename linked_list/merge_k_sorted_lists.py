from typing import Optional, List   
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Originally, wanted to recursively merge all lists together. We know can be done in O(n1 + n2) time, where n1 and n2 are the sizes of the first and second list respectfully. Therefore, recursively merging all the lists would actually have a time complexity of O(n*k) but a space complexity of O(1) where n is the number of elements in all the lists. Can be done though in O(n * log(k)) time and O(k) space if we use the top k elements pattern with a heap.
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # start off with a dummy node here
        cur = head = ListNode()
        index = 0
        
        # create the min heap, no need to heapify here
        min_heap = []

        # insert the first element of every list into the min heap, O(k) time
        for node in lists:
            heapq.heappush(min_heap, (node.val, index, node))
            index += 1

        #pop the smallest element from the heap O(log(k)), add it to the final list, add the next element connected to it into the min heap O(log(k)). Repeat until no elements are left in the min heap O(n * log(k)) time, O(k) space for the min heap
        while min_heap:
            *_, popped_node = heapq.heappop(min_heap)
            next_node = popped_node.next
            
            # append popped node to the final list
            cur.next = popped_node
            cur = cur.next

            # add next_node to min heap
            if next_node:
                heapq.heappush(min_heap, (next_node.val, index, next_node))
                index += 1
        
        
        # return the final list (accounting for the dummy node)
        return head.next