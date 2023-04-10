from libc.stdlib cimport malloc

# quicksort
cdef void qs (int* m, int start, int end) nogil:
    cdef int i, div
    if end-start > 1:
        div = start
        for i in range(start, end-1):
            if m[i] <= m[end-1]:
                m[div], m[i] = m[i], m[div]
                div += 1
        m[div], m[end-1] = m[end-1], m[div]
        qs(m, start, div)
        qs(m, div+1, end)


cpdef int[:] quicksort (int[:] input):
    cdef:
        int length = len(input)
        int* data = <int*>malloc(sizeof(int)*length)
    #copy array
    cdef int i
    for i in range(length):
        data[i] = input[i]
    #sort
    qs(data, 0, length)
    #return
    cdef int[:] res = <int[:length]>data
    return res


# heapsort
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


# insertion sort
cdef void ins (int* m, int N) nogil:
    cdef int j, k, i
    for j in range(1, N): # m
        k = m[j] # m-1
        i = j-1 # m-1
        while i >= 0 and m[i] > k: # m(m+1)/2
            m[i+1] = m[i] # m(m+1)/2-1
            i -= 1 # m(m+1)/2-1
        m[i+1] = k # m-1


cpdef int[:] insertion_sort (int[:] input):
    cdef:
        int length = len(input)
        int* data = <int*>malloc(sizeof(int)*length)
    #copy array
    cdef int i
    for i in range(length):
        data[i] = input[i]
    #sort
    ins(data, length)
    #return
    cdef int[:] res = <int[:length]>data
    return res
