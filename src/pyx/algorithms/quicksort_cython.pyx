from libc.stdlib cimport malloc

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
