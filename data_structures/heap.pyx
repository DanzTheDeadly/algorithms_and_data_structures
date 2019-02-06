cdef class Heap:
    cdef int[:] data
    def __cinit__ (self, int[:] input):
        self.data = input.copy()
        self.build()


    def __str__ (self):
        return str([val for val in self.data])


    cdef void build (self) nogil:
        cdef int length = len(self.data)
        cdef int start = (length-2)//2

        while start >= 0:
            self.sink(start, length-1)
            start -= 1


    cdef void sink (self, int root, int end) nogil:
        cdef int child = root*2 + 1
        while child <= end:
            if child + 1 <= end and self.data[child] < self.data[child + 1]:
                child += 1
            if self.data[root] < self.data[child]:
                self.data[root], self.data[child] = self.data[child], self.data[root]
                root = child
                child = child*2 + 1
            else:
                break
