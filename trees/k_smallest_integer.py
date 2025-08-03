from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key to this problem is realizing that this problems boils down to checking if there are k-1 elements in the left subtree of the current node. If there are less, then check the right subtree for a node with (k - 1) - (left subtree size + 1) nodes less than it. If there are more, search the left subtree for a node with k-1 elements less than it again. We realize that we can simultaneously check for the size of the subtree and if the k'th smallest node exist in the subtree. This avoids recomputation.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = None
        def dfs_kth_smallest(root,k):
            nonlocal res
            if not root:
                return 0

            left_subtree_size = dfs_kth_smallest(root.left,k)
            right_subtree_size = dfs_kth_smallest(root.right,k - left_subtree_size - 1)

            cur_tree_size = 1 + left_subtree_size + right_subtree_size

            if left_subtree_size == k - 1:
                res = root.val

            return cur_tree_size
        
        dfs_kth_smallest(root,k)
        return res
            