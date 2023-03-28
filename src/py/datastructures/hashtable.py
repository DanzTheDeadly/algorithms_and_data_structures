class HashMapBase:
    def __init__(self, maxhash=10000):
        self.maxhash = maxhash
        self.data = [[] for i in range(self.maxhash)]

    def _hash(self, value):
        index = value % self.maxhash
        return index


class HashSet(HashMapBase):
    def add(self, key: int) -> None:
        index = self._hash(key)
        if not key in self.data[index]:
            self.data[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.data[index]:
            self.data[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        if key in self.data[index]:
            return True
        else:
            return False


class HashMap(HashMapBase):
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.data[index]):
            if k == key:
                self.data[index][i] = (key, value)
                return
        self.data[index].append((key, value))
                

    def get(self, key: int) -> int:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.data[index]):
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for i, (k, v) in enumerate(self.data[index]):
            if k == key:
                self.data[index].pop(i)
                return