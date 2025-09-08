from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This problem is just BFS. The tricky part here is to ensure we are only extracting the nodes from the current level when traversing the queue. This can be done by noting the current size of the bfs queue before traversing it.
# O(n) time complexity, O(n) space complexity
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            cur_level = []
            # for loop is to make sure to only explore nodes of the current level
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)
        
            res.append(cur_level)
        
        return res
