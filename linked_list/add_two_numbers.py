from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Here, can also solve this problem if decide not to create new linked list for the output but just to modify the input linked lists

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        start = iterNode = ListNode()
        carry = 0
        while l1 or l2 or carry:
            newNode = ListNode()
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            newValue = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            newNode.val = newValue
            iterNode.next = newNode
            iterNode = iterNode.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return start.next
            






            
            



        