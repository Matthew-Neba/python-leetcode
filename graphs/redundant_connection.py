from typing import List

# Key to this problem is realizing that due to graph theory, we just need to remove the first edge that gives a cycle. This is because in any cycle, if we remove any edge, we will still be connected but break the cycle. The first edge that creates a cycle is also the last edge needed to complete the cycle. now, just need a way to check for cycles as we add edges, simple visited setwont work since no way to know if the edges are joining two seperate components, can use union find for this.

# O(E * inv_ackerman(n) + V) time complexity, O(V) space complexity
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 

        # 

        class Union:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.size = [1 for _ in range(n)]

            def find(self,x):
                # path compression
                print(self.parent, x)
                if self.parent[x] == self.parent[self.parent[x]]:
                    return self.parent[x]
                else:
                    self.parent[x] = self.find(self.parent[x])
                    return self.parent[x]
                
            def union(self,x,y):
                parent_x, parent_y = self.find(x), self.find(y)

                if parent_x == parent_y:
                    return False
                
                # union by size
                if self.size[parent_x] < self.size[parent_y]:
                    self.size[parent_y] += self.size[parent_x]
                    self.parent[parent_x] = parent_y
                else:
                    self.size[parent_x] += self.size[parent_y]
                    self.parent[parent_y] = parent_x
                
                return True
            
        
        components = Union(len(edges))
        for u,v in edges:
            did_union = components.union(u-1,v-1)
            if not did_union:
                return [u,v]

        


        

        