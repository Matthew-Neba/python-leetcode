from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # pruning before doing dijstras
        # 1) Dijstars does't work here due to the path exploration constrain. Dijstra's can fail on problems
        # where the path is constrained since the natural exploration of dijstars will fail. 
        
        # 2) Bellman Ford is better suited for some path constrained problems. Bellman Ford guarantees that
        # all shortest path of length k will be found after k relaxations. However, it does not strictly restrict it
        # to only paths of length k. Need to create a copy of the distances array to handle this
        def bellman_ford(edges, src , k):
            distances = [float("inf")] * n
            distances[src] = 0

            for _ in range(k+1):
                # relax all edges, freeze nodes if we update them since if we don't
                # we may potentially create a path to a node greater than length k
                frozen_distances = distances[::]
                for u,v,cost in flights:
                    if frozen_distances[u] + cost < distances[v]:
                        distances[v] = frozen_distances[u] + cost
            
            return distances
    
        distances = bellman_ford(flights, src, k)
        return distances[dst] if distances[dst] < float("inf") else -1

            
