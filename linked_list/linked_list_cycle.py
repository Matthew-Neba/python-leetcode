from typing import Optional

# Key to this problem is realizing that  a cycle exists if we encounter a node we have already previously encountered. Therefore, we just need to mark every node we encounter somehow. This is done in this solution by setting thier value to infinity. 

# Custom objects are hashable in python. Ususablly, mutuable objects are not hashable such as list, dicts, sets but custom objects are. But note that the key for the hash for a mutable object is now the id of the object. Therefore, even if we have two different objects with same contents, they will have different hash values. This can be unintuitive. Python helps avoid this confusion by making the other default mutable like lists,dicts and sets as unhashable.

#  __eq__ Class dunder method is used for == comparisons. "is" keyword is used to compare id's of objects. __hash__ is used to define the hash function for a class. Custom classes by default have the __hash__ function return the id(pointer) of the object.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head != None:
            if head.val == float("inf"):
                return True
            else:
                head.val = float("inf")  
                
            head = head.next

        return False
    
# can also use Floyd's cycle detection algorithm here. Key point of this algorithm is realizing that by moving the fast pointer by 2 and the slow pointer by 1, we are effectively substracting the distance between the fast and slow pointer by 1 IF a cycle exists. Therefore, the slow and fast pointer will meet if and only if there is a cycle. Else, the fast pointer will go out of bounds of the container. Important to have some mechanisms to known when out of bounds of the container.Also since the max distance between slow and fast pointers is n, algorithm is O(n) in time. The hidden constant for the time complexity for this FLoyd's cycle detection algorithm is smaller than the previous solution since not modifying values of the nodes.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        
        return False