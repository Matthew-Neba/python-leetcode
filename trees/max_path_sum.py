from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This problem uses a specific recursion pattern for trees. The pattern is we are looking for the best value/metric that can be calculated for every single node in the tree. However, we can resuse the work from a node to help it's parent node. K'th smallest integer in BST is similar.

# Key to this problem is realizing that to obtain the maximum path sum for the entire tree, we need to obtain the maximum path sum for the trees rooted at every node, i.e every subtree. Then, we can return the maximum of those maximum path sum. But, we notice that when calculating the maximum path sum for a subtree, we can use part of the calculation to help the parent calculate it's maximum path sum. This avoids repeated work and makes the time complexity O(n).
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float("-inf")
        def dfs_max_path(root):
            nonlocal res
            if not root:
                return 0
            
            # do the maximum with 0, to essentially eliminate negative paths since they reduce the maximum
            left_max_path = max(dfs_max_path(root.left), 0)
            right_max_path = max(dfs_max_path(root.right),0)

            res = max(res, root.val + left_max_path + right_max_path)
            return root.val + max(left_max_path, right_max_path)
        
        dfs_max_path(root)
        return res







        
