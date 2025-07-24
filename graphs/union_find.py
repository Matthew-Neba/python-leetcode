class UnionFind:
    def __init__(self, n):
        # Initially each node is its own parent
        self.parent = list(range(n))
        # Each set has size 1 initially
        self.size = [1] * n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # compress the path
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return  # already in the same set

        # Union by size: attach the smaller tree under the larger one
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]