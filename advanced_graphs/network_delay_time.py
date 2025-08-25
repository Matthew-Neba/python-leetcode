from typing import List
from collections import defaultdict
from heapq import heappush, heappop, heapify

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Can be visualized as a water flow problem. Where we pour one unit of water out of the source
        # every second. ti represents the amount of water to reach the target node. inefficient, how to do this
        # with a dfs instead?

        # Can keep track of a number, representing water pumps done for bfs approach. 
        #  O(max(signal) * E) time complexity

        # Can run djikstra's instead to find the minimum time it takes to reach all nodes from source. return the largest
        # time that djikstra's found.
        #  (E + V)log(V) ---> Elog(V) ---> O(Elog(E)) time complexity

        # Djikstra's is generally better since the delays are usually way larger than the 
        # vertices in practice. i.e: we are considering ms for netword delay time

        # create adjacency list
        adj = defaultdict(list)

        # O(E)
        for u,v,t in times:
            adj[u - 1].append((t,v - 1))
        
        # O((E+V)log(V)) time, O(E) space
        def dijstras(start, adj):
            # need distance array and heap
            distances = [float("inf")] * n
            distances[start] = 0

            priority_queue = [(0, start)]
            
            while priority_queue:
                cur_distance, cur_node = heappop(priority_queue)

                # a previous edge we could not remove due to python's limitations
                if cur_distance > distances[cur_node]:
                    continue

                # we are now at a minimum distance to the current node
                for dist,v in adj[cur_node]:
                    new_distance = cur_distance + dist
                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        heappush(priority_queue, (new_distance, v))
            
            # return the minimum distances
            return distances
            

        max_distance = max(dijstras(k - 1, adj))
        return max_distance if max_distance < float("inf") else -1
                
                







