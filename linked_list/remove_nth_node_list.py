from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Question is simple to do with two passes but this is O(2n), but with linked lists we are more concerned the hidden constant, O(n) solution is usually trivial. Key here to solve in O(1n) is realizing that we can solve this problem in one pass by using two pointers, where the trail pointer keeps track of the n'th element from the end pointer
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prevNode = None
        endNode = curNode = head

        # create a gap of n between current and end
        for _ in range(n-1):
            endNode = endNode.next
        
        # go to the end of the list
        while endNode.next:
            prevNode = curNode
            curNode = curNode.next
            endNode = endNode.next
        
        # remove curNode, which is the n'th node from end
        if prevNode:
            prevNode.next = curNode.next
        else:
            head = head.next

        return head


        

