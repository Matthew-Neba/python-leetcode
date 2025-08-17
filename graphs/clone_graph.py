from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Key to this problem is realizing that this is just a bfs/dfs problem. Need the visited set to ensure we don't have cycles, since we can have and edge [1,2] and [2,1] for example in both node 1 and 2's adjacency lists respectively. We also need to ensure that we include all cloned neighbors in each cloned nodes adjacency list.
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visited = {}

        def dfs(node):
            if node.val in visited:
                return visited[node.val]

            # clone node if it has not yet been visited
            clone_Node = Node(node.val)

            # add it to visited
            visited[node.val] = clone_Node

            # clone all the neighbor subgraphs
            for neighbor in node.neighbors:
                # connect the cloned node to all its cloned neighbors
                clone_Node.neighbors.append(dfs(neighbor))
                
            # return the cloned current node
            return clone_Node
        
        return dfs(node)


