from collections import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        parity = [0] * len(graph)
        def dfs(u, cur_parity):
            for v in graph[u]:
                if not parity[v]:
                    parity[v] = -1 * cur_parity
                    if not dfs(v, parity[v]):
                        return False
                else:
                    if parity[v] != -1 * cur_parity:
                        return False
            
            return True

        for u in range(len(graph)):
            if not parity[u]:
                parity[u] = 1
                if not dfs(u, 1):
                    return False

        return True
            
            

            
                


