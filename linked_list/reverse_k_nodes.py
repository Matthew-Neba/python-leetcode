from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Key to this problem was in the implementation details. 1) Using a dummy node to not have to do initialization steps, 2) Carefully visualizing each step of the algorithm  
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = end = head
        # initialize to some dummy values
        new_list_head = prev_head = ListNode()

        while start:
            # have the end pointer ensure there are k avalaible elements to reverse
            for i in range(k):
                if not end:
                    # not enough elements to reverse, return list
                    return new_list_head.next
                end = end.next

            # reverse elements up to end,  while keeping track of the original start and end of the current list (start, cur, prev) in order to adjust heads properly after
            cur = start
            prev = None
            for i in range(k):
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node

            # adjust the heads now
            start.next = cur
            prev_head.next = prev

            # adjust iterators now and set current list head to be the previous list head
            prev_head = start
            start = end
        
        return new_list_head.next
