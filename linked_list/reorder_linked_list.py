from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Key here is realizing problem can be broken down into three steps. 1) Split linked list in half, 2) reverse second half, 3) merge them together. Another key idea here is the use fast and slow pointers to get the middle of the linked list in O(n/2) time

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # get middle in O(n/2) time
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        # reverse elements after the middle of the linked list
        prevNode = None
        while middle:
            nextNode = middle.next
            middle.next = prevNode
            prevNode = middle
            middle = nextNode
        
        firstHalf, secondHalf = head, prevNode

        # merge together
        while secondHalf:
            tmp1, tmp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = tmp1
            firstHalf, secondHalf = tmp1, tmp2
        

        

        