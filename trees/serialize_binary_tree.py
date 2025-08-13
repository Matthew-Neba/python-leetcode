from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  Key to this problem is realizing that we just need to write some non ambiguous instructions for how to construct the tree using as little extra space as possible. Two ways to do this are to naturally turn to the two main traversal algorithms: BFS and DFS. We can traverse the tree using BFS or DFS and write these steps in the serialization string.

# DFS method
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs_serialize(root):
            if not root:
                # important to store the null values so the instructions are unambiguos
                res.append("Null")
                return

            # store the current root node
            res.append(str(root.val))

            # perform dfs and store the results
            dfs_serialize(root.left)
            dfs_serialize(root.right)
        
        dfs_serialize(root)

        # return a string representation of the array
        return ",".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # prepare data
        data_arr = data.split(",")

        cur_index = 0
        def dfs_deserialize(data_arr):
            nonlocal cur_index
            if data_arr[cur_index] == "Null":
                cur_index += 1
                return None
        
            root = TreeNode(int(data_arr[cur_index]))
            cur_index += 1
            root.left = dfs_deserialize(data_arr)
            root.right = dfs_deserialize(data_arr)

            return root

        return dfs_deserialize(data_arr)
