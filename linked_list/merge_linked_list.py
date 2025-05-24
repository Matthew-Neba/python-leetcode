
# Always try and make initialization logic consistent with main logic. Optimally,
# don't want to have any initialization logic and have all the logic happen in the for/while loop. This was done here

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        dummyNode = cur = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        # skip the dummy variable here now
        return dummyNode.next
