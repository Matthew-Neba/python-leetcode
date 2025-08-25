from collections import deque

def hierholzer(adj, u, path):
    """
    Recursive version of Hierholzer's algorithm step 2.
    """
    while adj[u]:                   # follow edges while available
        v = adj[u].pop()            # consume edge u -> v
        hierholzer(adj, v, path)
    path.leftappend(u)                   # add to path after exploring all edges
