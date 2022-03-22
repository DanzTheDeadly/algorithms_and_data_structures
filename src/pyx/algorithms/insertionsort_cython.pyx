from libc.stdlib cimport malloc

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
