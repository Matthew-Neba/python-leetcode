from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  This problem was a bit trickier than expected. I originally taught I could improve the time complexity of the solution by checking whether or not the current node is the same as multiple subtrees in O(1) time. If this was the case, the time complexity of the solution would be O(n). However, this was found to be impossible.

# O(n * min(m,n)) time complexity, O(n + min(m,n)) space complexity
class Solution:  
    # check whether or not two trees are the same O(min(m,n)) time, O(min(m,n)) space
    def is_same(self, root, subRoot):
        if not root:
            return False if subRoot else True
        
        if not subRoot:
            return False if root else True

        if root.val == subRoot.val:
            left_same = self.is_same(root.left, subRoot.left)
            right_same = self.is_same(root.right, subRoot.right)
            return left_same and right_same
        else:
            return False        


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # run dfs for every node and check if thier respective subtrees match the ones for
        # the subRoot O(n * min(m,n)) time, O(n + min(m,n)) space
        found_subtree = False
        def dfs_isSubtree(root):
            nonlocal found_subtree
            if not root:
                return
            
            if self.is_same(root, subRoot):
                found_subtree = True
            
            dfs_isSubtree(root.left)
            dfs_isSubtree(root.right)
        
        dfs_isSubtree(root)
        return found_subtree


