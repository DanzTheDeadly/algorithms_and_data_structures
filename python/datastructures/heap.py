class MinHeap:
    def __init__(self):
        self.data = [0]
    

    def _get_smallest_idx(self, idx):
        smallest_idx = idx
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        if left_idx <= self.data[0]:
            if self.data[smallest_idx] > self.data[left_idx]:
                smallest_idx = left_idx
            if right_idx <= self.data[0]:
                if self.data[smallest_idx] > self.data[right_idx]:
                    smallest_idx = right_idx
        return smallest_idx


    def getMin(self) -> int:
        return self.data[1]


    def insert(self, val: int):
        self.data.append(val)
        self.data[0] += 1
        idx = self.data[0]
        parent = idx // 2
        while idx > 1 and self.data[idx] < self.data[parent]:
            self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
            idx = parent
            parent = idx // 2


    def pop(self):
        if self.data[0] > 1:
            self.data[1] = self.data.pop()
            self.data[0] -= 1
            idx = 1
            smallest_idx = self._get_smallest_idx(idx)
            while idx != smallest_idx:
                self.data[idx], self.data[smallest_idx] = self.data[smallest_idx], self.data[idx]
                idx = smallest_idx
                smallest_idx = self._get_smallest_idx(idx)
        elif self.data[0] == 1:
            self.data.pop()
            self.data[0] -= 1
        else:
            return False
    

    def size(self) -> int:
        return self.data[0]