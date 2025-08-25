from collections import defaultdict,deque
from typing import List

# Key to this problem is realizinf this problem is essentially finding a Eulerian path. Can do it using hiezholzer's algorithm. Tricky part is ensuring we get the lexographically correct order. This can be greedily done by always choosing the lexographically smaller edge first when multiple choices are possible. We can use a heap for each neighbor list for all the nodes when choosing which neighbor to visit. But since we asre doing this for all the nodes, the time complexity will be (ElogE), can do it a simpler way then by just sorting at the start.

# O(Elog(E)) time complexity, O(E) space complexity for the adjacency list and for the res queue
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      
        res = deque([])
        def hierholzer(cur , adj):
            while adj[cur]:
                cur_node = adj[cur].pop()
                hierholzer(cur_node, adj)

            res.appendleft(cur)

        adj = defaultdict(list)
        # note: reverse is set to true since hiezholder adds edges at the start of the list
        tickets.sort(reverse = True)

        # Now can populate the adjacency list with sorted values
        for u,v in tickets:
            adj[u].append(v)

        hierholzer("JFK", adj)
        return list(res)
            
            












