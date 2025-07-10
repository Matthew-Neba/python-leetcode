
import heapq

#O((V+E)log(V)) time complexity, O(V) space complexity

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    min_heap = [(0, start)]  # (distance, node)

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))

    return dist