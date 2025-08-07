from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Key to this problem is realizing that the missing information from the preorder array is which nodes go in the left vs right subtree of the current node. However, we can get this information from the inorder traversal array if we just search for the current node in that array and split the array from that information. We can also use a hashmap in order to perform this search for the current node in the inorder array more efficient

# O(n) in time complexity, O(n) in space complexity.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # O(n) space complexity
        inorder_dict = {}

        # record the index of every node in the inorder list, will later be used to 
        # split the left and right trees
        for i,node in enumerate(inorder):
            inorder_dict[node] = i
        
        def construct_tree(pre_idx, in_l, in_r):
            # check if any nodes exist in the current tree
            if in_r < in_l:
                # no node here
                return None
            
            # build the current node
            root = TreeNode(preorder[pre_idx])

            # find the index of root in the inorder arr
            root_in_idx = inorder_dict[root.val]
            
            # calculate the left subtree size, will be used to extract the root for the
            # right subtree later from the preorder arr
            left_sub_tree_size = root_in_idx - in_l

            root.left = construct_tree(pre_idx + 1, in_l,root_in_idx - 1)
            root.right = construct_tree(pre_idx + 1 + left_sub_tree_size, root_in_idx + 1,in_r)

            return root
        
        res = construct_tree(0,0, len(inorder) - 1)
        return res