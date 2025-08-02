from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key to this problem is realizing that to determine if the current two trees are the same, we must check if thier left and right subtrees are the same, and then just check thier root node values. This is where the recursion occurs.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p:
                return False if q else True
            
            if not q:
                return False if p else True
            
            left_same = self.isSameTree(p.left,q.left)
            right_same = self.isSameTree(p.right,q.right)

            if not left_same or not right_same:
                return False
            
            return p.val == q.val
        