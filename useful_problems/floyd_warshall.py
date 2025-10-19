from collections import defaultdict
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #
        # We would like to find the shortest distance between all points to all other points. APSP problem. Can use 
        # floyd warshall here.
        #
        adj = defaultdict(list)
        for u,v,weight in edges:
            adj[u].append((v,weight))
            adj[v].append((u,weight))
        
        def floyd_warshall(adj):
            dp = [[float("inf") for _ in range(n)] for _ in range(n)]

            # initialize the dp array for paths of lengh 0 (incldues nodes to themselves and nodes to one other node)
            for u in range(n):
                dp[u][u] = 0
                for v,weight in adj[u]:
                    if weight < dp[u][v]:
                        dp[u][v] = weight

            # order of the nodes does not matter
            for cur_k in range(n - 1, -1, -1):
                # considering using any number of intermediary nodes from {0 ... cur_k}
                for u in range(n):
                    for v in range(n):
                        # check if using the extra node cur_k will lead to a better path
                        dp[u][v] = min(dp[u][v] , dp[u][cur_k] + dp[cur_k][v])
            
            return dp

        pairs_shortest = floyd_warshall(adj)
        res = None
        min_cities = float("inf")

        for i in range(n-1, -1,-1):
            cities = sum(1 for val in pairs_shortest[i] if val <= distanceThreshold)

            if cities < min_cities:
                min_cities = cities
                res = i

        return res
    