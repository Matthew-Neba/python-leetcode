from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key to this problem was realizing that the diameter of a tree that must pass through a node is the sum of the depth of it's right and left substrees + 2. We can then recursively compute this depth using dfs but along the way, update our maximum diameter if the current node in the recursive stack has a greater max diameter than what was recorded.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth_dfs(root):
            nonlocal max_diameter 

            if not root:
                return 0

            # get the right and left subtree "depth" (depth here is defined as the number of nodes in the 
            # longest path to a root node)
            left_depth = depth_dfs(root.left)
            right_depth = depth_dfs(root.right)

            # check if the diameter of this current tree is the maximum diameter
            max_diameter = max(max_diameter, left_depth + right_depth)

            # return depth of this tree
            return 1 + max(left_depth,right_depth)
        
        depth_dfs(root)
        return max_diameter
