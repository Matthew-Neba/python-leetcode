from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key to this problem is realizing that this problem degenerates into a subtree problem. For a node to be a LCA, p and q must 1) either belong in two different subtrees of that node. ex: p belongs in the left subtree, q belongs in the right subtree.  2) both p and q belong in a tree where the root is either p or q. i.e: p is a descendant of q or q is a descentdant of p.BST simplifies this problem by quickly allowing us to determine what subtree p and q belogn to of the current node.

# O(h) time complexity, O(h) space complexity. Where h is the size of the tree (BST).
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check if the current node is p or q
        if root.val == p.val or root.val == q.val:
            return root
        
        # check if p and q belong in different substrees
        if p.val < root.val and q.val > root.val:
            return root
        # check if p and q belong in different substrees
        elif p.val > root.val and q.val < root.val:
            return root
        # check if p and q belong in the left subtree
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        # check if p and q belong in the right subtree
        else:
            return self.lowestCommonAncestor(root.right,p,q)

# Don't really need recursion here. We are not using the subproblems (getting the LCA from root.right or getting the LCA from root.left) to solve the current problem (getting LCA from root). We're just navigating down the tree until we find the answer, then returning it back up.
# O(h) time complexity, O(1)) space complexity. Where h is the size of the tree (BST).
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if root.val == p.val or root.val == q.val:
                return root

            if p.val < root.val and q.val > root.val:
                return root
            elif p.val > root.val and q.val < root.val:
                return root
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                root = root.right

            