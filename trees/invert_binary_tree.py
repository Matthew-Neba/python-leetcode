from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key to this problem is realizing that we need to visit every node and flip it's right and left children. Can visit every node with bfs or dfs



# DFS solution, O(V + E) time complexity -> O(n) for a tree, O(n) space
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # don't need visited set for trees since they are UNDAG and no cycles can exist
        if not root:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.left, root.right
        return root



from collections import deque
# BFS version, O(V + E) time complexity -> O(n) for a tree, O(n) space
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        queue = deque([root])
        while queue:
            cur = queue.pop()
            if cur.left:
                queue.append(cur.left)
            
            if cur.right:
                queue.append(cur.right)
                
            cur.left,cur.right = cur.right,cur.left
        
        return root
