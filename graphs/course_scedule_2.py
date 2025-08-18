from collections import deque
from typing import List

# Key to this question is realizing that to match the interpretatino of topological sorting to this problem, we must flip any prerequisite from [u,v]: u --->  to [v,u] : v ---> u. This now means v must be taken before u. The topological sort interpretation will now match this problem's.

#  O(V + E) time complexity, O(V + E) space complexity to store the graph
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # perform the topological sort
        # O(V + E) time complexity, O(V) space for the queue
        def topological_sort(graph, in_degree):

            # we will have a processing queue to process all nodes with indegree 0 and update thier neighbors indegree
            queue = deque([])
            course_order = []

            # get the nodes with indegree 0
            for i, count in enumerate(in_degree):
                if count == 0:
                    print(i)
                    course_order.append(i)
                    queue.append(i)
            
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for neighbor in graph[node]:
                        # decrement indegree of neighbors
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                            course_order.append(neighbor)
                            queue.append(neighbor)
            
            return course_order if len(graph) == len(course_order) else []
       
        # create the adjencency list
        graph = {i:[] for i in range(numCourses)}

        # create in-degree array
        in_degree = [0 for _ in range(numCourses)]

        # we will have an indegree array holding the indegree for every node
        # populate adjacency list and the in_degree
        for edge in prerequisites:
            u,v = edge
            graph[v].append(u)
            in_degree[u] += 1
        
        return topological_sort(graph, in_degree)
        
        
        