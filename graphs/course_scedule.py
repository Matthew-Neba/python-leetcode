from collections import deque
from typing import List
# we are looking to see if there exists some topological sorting of the courses, can
# use Kahn's algorithm for this (it can also detect cyles)

# Key to this question is realizing that to match the interpretatino of topological sorting to this problem, we must flip any prerequisite from [u,v]: u --->  to [v,u] : v ---> u. This now means v must be taken before u. The topological sort interpretation will now match this problem's.

#  O(V + E) time complexity, O(V + E) space complexity to store the graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # perform the topological sort
        # O(V + E) time complexity, O(V) space for the queue
        def topological_sort(graph, in_degree):

            # we will have a processing queue to process all nodes with indegree 0 and update thier neighbors indegree
            queue = deque([])
            processed = 0

            # get the nodes with indegree 0
            for i, count in enumerate(in_degree):
                if count == 0:
                    processed += 1
                    queue.append(i)
            
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for neighbor in graph[node]:
                        # decrement indegree of neighbors
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                            processed += 1
                            queue.append(neighbor)
            
            return len(graph) == processed
       
        # create the adjencency list
        graph = {i:[] for i in range(numCourses)}

        # create in-degree array
        in_degree = [0 for _ in range(numCourses)]

        # we will have an indegree array holding the indegree for every node
        # populate adjacency list and the in_degree

        # u,v were flipped here to v,u for a reason. This is because topological sort interpretrs,
        # the edge u ---> v as u comes before v. However, this questions has it the other way around
        for edge in prerequisites:
            u,v = edge
            graph[v].append(u)
            in_degree[u] += 1
        
        return topological_sort(graph, in_degree)
        
        
        