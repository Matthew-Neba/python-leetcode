from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key to this problem is realizing that to do a right side view, we can just use BFS to do a level order traversal and return the far right node in each level.
 
#O(n) time complexity, O(h) space complexity
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                
                cur_node = queue.pop()

                # if i == 0, we are at the right most node at the current level
                # only append the right most node of each level to the result arr
                if i == 0:
                    res.append(cur_node.val)

                # always appendleft the right node to the queue before the left node to ensure
                # far right node is always at the front of the queue for each level
                if cur_node.right:
                    queue.appendleft(cur_node.right)

                if cur_node.left:
                    queue.appendleft(cur_node.left)
        return res
