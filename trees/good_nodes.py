from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  Key to this problem is realizing that we just need to traverse the tree using DFS or BFS while maintaining the maximum value encountered along each path. If the current node is greater than the maximum, increment good nodes.

# O(n) time complexity. O(n) space complexity
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # run dfs while keeping track of the maximum element across each path
        good_nodes = 0
        # passing in path_max as a param since need to keep track of it for each individual
        # path and not for the whole traversal as a whole
        def dfs(root, path_max):
            nonlocal good_nodes

            if not root:
                return
            
            path_max = max(path_max, root.val)

            if root.val == path_max:
                good_nodes += 1
            
            dfs(root.left, path_max)
            dfs(root.right, path_max)
        
        dfs(root,root.val)
        return good_nodes
