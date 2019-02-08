cdef class Heap:
    cdef int[:] data
    cdef int length

    def __cinit__ (self, int[:] input):
        self.data = input.copy()
        self.length = len(self.data)
        self.build()


    def __str__ (self):
        cdef str s = ''
        cdef int i
        for i in range(self.length):
            s += str(self.data[i])+' '
        return s


    cdef void build (self) nogil:
        cdef int start = (self.length-2)//2
        while start >= 0:
            self.sink(start, self.length-1)
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


    cpdef void sort (self):
        cdef int counter = self.length-1
        while counter > 0:
            self.data[0], self.data[counter] = self.data[counter], self.data[0]
            counter -= 1
            self.sink(0, counter)
