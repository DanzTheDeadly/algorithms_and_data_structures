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
    

class DisjointSetOptimized:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def __repr__(self) -> str:
        return str(self.parent)
    
    def find(self, x):
        to_link = []
        while x != self.parent[x]:
            to_link.append(x)
            x = self.parent[x]
        for idx in to_link:
            self.parent[idx] = x
        return x
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            self.parent[parentY] = parentX
        print(self, (x,y))

    def connected(self, x, y):
        return self.find(x) == self.find(y)