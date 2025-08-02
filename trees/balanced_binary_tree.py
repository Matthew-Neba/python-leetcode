from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This problems follows the same recursion pattern as described in the tips.md that is similar to maximum path sum and k'th smallest integer. Key to this problem is realizing that the height of the current tree is dependent on the height of it's left and right subtrees. This allows us to use recursion.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True
        def dfs_height(root):
            nonlocal res
            if root == None:
                return 0
            
            left_height = dfs_height(root.left)
            right_height = dfs_height(root.right)

            if abs(left_height - right_height) > 1:
                res = False

            return 1 + max(left_height, right_height)
        dfs_height(root)
        return res
        