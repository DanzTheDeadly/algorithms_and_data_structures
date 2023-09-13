class MinHeap:
    def __init__(self):
        self.data = [0]
    

    def insert(self, val: int):
        self.data.append(val)
        self.data[0] += 1
        idx = self.data[0]
        parent = idx // 2
        while idx > 1 and self.data[idx] < self.data[parent]:
            self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
            idx = parent
            parent = idx // 2


    def getMin(self) -> int:
        return self.data[1]
    

    def size(self) -> int:
        return self.data[0]


    def pop(self):
        if self.data[0] > 1:
            self.data[1] = self.data.pop()
            self.data[0] -= 1
            idx = smallest_idx = 1
            if idx * 2 <= self.data[0]:
                if self.data[idx] > self.data[idx * 2]:
                    smallest_idx = idx * 2
                if idx * 2 + 1 <= self.data[0]:
                    if self.data[idx * 2] > self.data[idx * 2 + 1]:
                        smallest_idx = idx * 2 + 1
            while idx != smallest_idx:
                self.data[idx], self.data[smallest_idx] = self.data[smallest_idx], self.data[idx]
                idx = smallest_idx
                if idx * 2 <= self.data[0]:
                    if self.data[idx] > self.data[idx * 2]:
                        smallest_idx = idx * 2
                    if idx * 2 + 1 <= self.data[0]:
                        if self.data[idx * 2] > self.data[idx * 2 + 1]:
                            smallest_idx = idx * 2 + 1
        elif self.data[0] == 1:
            self.data.pop()
            self.data[0] -= 1
        else:
            return False