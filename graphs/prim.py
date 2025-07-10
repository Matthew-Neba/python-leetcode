import heapq

# O((V+E)log(V)) time complexity, O(V) space complexity. We use len(visited) < len(graph) in Prim because we need the visited set for the correctness of the algorithm. Might as well benefit from it for early stopping since we are adding all edges to our min heap.

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, node)
    mst_cost = 0
    mst_edges = []

    while min_heap and len(visited) < len(graph):
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        mst_cost += weight

        for v, edge_weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (edge_weight, v))
                mst_edges.append((u, v, edge_weight))

    return mst_cost, mst_edges
