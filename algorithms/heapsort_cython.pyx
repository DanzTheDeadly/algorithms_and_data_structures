from libc.stdlib cimport malloc

cdef inline void sink (int* data, int root, int end) nogil:
    cdef int child = root*2 + 1
    while child <= end:
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
            child = child*2 + 1
        else:
            break


cdef void hs (int* data, int length) nogil:
    #heapify
    cdef int start = (length-2)//2
    while start >= 0:
        sink(data, start, length-1)
        start -= 1
    #heapsort
    cdef int counter = length-1
    while counter > 0:
        data[0], data[counter] = data[counter], data[0]
        counter -= 1
        sink(data, 0, counter)

cpdef int[:] heapsort (int[:] input):
    cdef:
        int length = len(input)
        int* data = <int*>malloc(sizeof(int)*length)
    #copy array
    cdef int i
    for i in range(length):
        data[i] = input[i]
    #sort
    hs(data, length)
    #return
    cdef int[:] res = <int[:length]>data
    return res
