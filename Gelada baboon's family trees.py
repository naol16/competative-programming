class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) 
        self.rank = [1] * n 
 
    def find(self, x):
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
 
n = int(input()) 
p = list(map(int, input().split())) 
uf = UnionFind(n)
for i in range(n):
    uf.union(i, p[i] - 1) 
 
distincttrees = len(set(uf.find(i) for i in range(n)))
print(distincttrees)
 
