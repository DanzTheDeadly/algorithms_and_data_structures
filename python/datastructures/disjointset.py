class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def __repr__(self) -> str:
        return str(self.parent)
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            self.parent[parentY] = parentX
        print(self, (x,y))

    def connected(self, x, y):
        return self.find(x) == self.find(y)