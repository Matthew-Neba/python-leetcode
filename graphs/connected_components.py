from typing import List

# can do bfs or dfs here aswell, but chance to do union find. This
# is essentially a number of islands question
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        class Union:
            def __init__(self, n):
                self.sizes = [1 for _ in range(n)]
                self.parents = [i for i in range(n)]
            
            def find(self, x):
                # path compression
                if self.parents[x] == self.parents[self.parents[x]]:
                    return self.parents[x]
                else:
                    self.parents[x] = self.find(self.parents[x])
                    return self.parents[x]
                    
            def union(self, x,y):
                parent_x, parent_y = self.find(x), self.find(y)

                # already in the same union
                if parent_x == parent_y:
                    return False
                
                # union by size
                if self.sizes[parent_x] < self.sizes[parent_y]:
                    self.parents[parent_x] = parent_y
                    self.sizes[parent_y] += self.sizes[parent_x]
                else:
                    self.parents[parent_y] = parent_x
                    self.sizes[parent_x] += self.sizes[parent_y]

                return True

        components = Union(n)
        cc = n
        for u,v in edges:
            did_union = components.union(u,v)
            cc -= 1 if did_union else 0
        
        return cc


        
