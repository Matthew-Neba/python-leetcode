from typing import List

# Key to this problem is realizing that dfs/bfs is sufficient for cycle detection in an undirected graph 
# if we keep track of the parent

# O(V + E) time complexity, O(V + E) space complexity
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #  a tree is a connected acycyclic graph
        # need to check for connectivity and no cycles

        #run dfs and see if the visited set at the end has n nodes
        # create the adjacency list
        graph = [set() for _ in range(n)]

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        cycle_exists = False

        def dfs_cycle(caller, node):
            nonlocal cycle_exists
            for neighbor in graph[node]:
                # do not call dfs back on the parent
                if neighbor == caller:
                    continue

                # check if we have a cycle
                if neighbor in visited:
                    cycle_exists = True
                    return

                visited.add(neighbor)
                dfs_cycle(node,neighbor)
        
        visited.add(0)
        dfs_cycle(-1,0)

        return not cycle_exists and len(visited) == n
