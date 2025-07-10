from collections import defaultdict, deque

# O(V+E) time complexity, O(V+E) space complexity

def kahn_topological_sort(graph):
    # 1. Initialize in-degree of all nodes to 0
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        in_degree[u] += 0  # Ensure nodes with no outgoing edges are included

    # 2. Start with all nodes that have in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []

    # 3. Process the queue
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # 4. Cycle check: not all nodes were added
    if len(topo_order) != len(in_degree):
        raise ValueError("Graph has a cycle, topological sort not possible")

    return topo_order