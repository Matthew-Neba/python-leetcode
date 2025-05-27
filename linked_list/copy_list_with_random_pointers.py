from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Key idea to do this problem in  constant space is to realize that we need some way to acess the copied random pointer nodes in constant time retroactively since they may not yet exist as we are iterating through the list. Can do this O(n) space and O(n) time using a hashmap. However, can make use of the structure of the linked list by linking the copy node to the original node for every node. This gives a way to acess the random copy nodes in constant time by just doing originalRandomNode.next which will give copied random node. Can then seperate this long linked list into the orginal and the copied list. This solution give O(n) time and O(1) space.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        # create paired linked list (double size of original)
        curNode = head
        while curNode:
            temp = curNode.next
            copy = Node(0)
            copy.val = curNode.val
            copy.next = curNode.next
            copy.random = curNode.random
            curNode.next = copy
            copy.next = temp
            curNode = temp
        
        # make the copied nodes have the correct random pointers
        curNode = head
        while curNode:
            # temp holds the next original node (skip copied node)
            temp = curNode.next.next
            copiedNode = curNode.next
            # attach the correct copied random nodes
            if copiedNode.random:
                copiedNode.random = copiedNode.random.next
            curNode = temp
        
        # seperate the original and copy lists
        curNode = head
        copy = curNode.next
        while curNode:
            temp = curNode.next.next
            copiedNode = curNode.next

            curNode.next = curNode.next.next
            if copiedNode.next:
                copiedNode.next = copiedNode.next.next

            curNode = temp

        return copy
