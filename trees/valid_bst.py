from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key to this problem is realizing that we can reuse calculations from validating the subtree's of a node. This can be done by recording the max and min of the subtree and returning it to the parent. The parent then just has to ensure that the max of the validated left subtree is less than it's current value. It also checks if the min of the validated right subtree's node is greater than it's current value. The parent can then return the max and min of it's curret node using the max and min of it's subtree nodes.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        # O(n) time , O(h) space
        def dfs_is_valid_bst(root):
            nonlocal res
            if not root:
                tree_max = float("-inf") 
                tree_min = float("inf")
                
                return tree_max, tree_min
            
            # suppose the left subtree is a valid bst. Then, just need to record the max value
            # in the left subtree. Ensure the current nodes value is greater than it
            left_tree_max, left_tree_min = dfs_is_valid_bst(root.left)
            if not left_tree_max < root.val:
                res = False
            

            # suppose the right subtree is a valid bst. Then, just need to record the minimum value
            # in the right subtree. Ensure the current nodes value is less than it
            right_tree_max, right_tree_min = dfs_is_valid_bst(root.right)
            if not right_tree_min > root.val:
                res = False
            
            # return max and min of this tree
            return max(root.val, right_tree_max), min(root.val, left_tree_min)
        
        dfs_is_valid_bst(root)
        return res

            