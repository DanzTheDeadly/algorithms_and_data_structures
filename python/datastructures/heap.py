class MinHeap:
    def __init__(self):
        self.data = [0]
    

    def insert(self, val: int):
        self.data.append(val)
        self.data[0] += 1
        idx = self.data[0]
        while idx > 1 and self.data[idx] < self.data[idx // 2]:
            self.data[idx], self.data[idx // 2] = self.data[idx // 2], self.data[idx]
            idx = idx // 2


    def getMin(self) -> int:
        return self.data[1]
    

    def size(self) -> int:
        return self.data[0]


    def pop(self):
        self.data[1] = self.data.pop()
        self.data[0] -= 1
        idx = 1
        smallest_child = idx * 2 if self.data[idx * 2] <= self.data[idx * 2 + 1] else idx * 2 + 1
        while idx <= self.data[0] and self.data[idx] > self.data[smallest_child]:
            self.data[idx], self.data[smallest_child] = self.data[smallest_child], self.data[idx]
            idx = smallest_child
            smallest_child = idx * 2 if self.data[idx * 2] <= self.data[idx * 2 + 1] else idx * 2 + 1