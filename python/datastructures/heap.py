class MinHeap:
    def __init__(self):
        self.data = [0]
    

    def insert(self, val: int):
        self.data.append(val)
        self.data[0] += 1
        curr = self.data[0]
        while curr > 1 and self.data[curr] < self.data[curr // 2]:
            self.data[curr], self.data[curr // 2] = self.data[curr // 2], self.data[curr]
            curr = curr // 2


    def getMin(self) -> int:
        return self.data[1]
    

    def size(self) -> int:
        return self.data[0]


    def pop(self):
        pass
