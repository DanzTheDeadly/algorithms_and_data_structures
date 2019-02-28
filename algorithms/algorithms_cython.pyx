cpdef void cinsertion_sort (int[:] m, int N, bint inplace=False):
    cdef int j, k, i
    if not inplace:
        m = m.copy()
    for j in range(1, N): # m
        k = m[j] # m-1
        i = j-1 # m-1
        while i >= 0 and m[i] > k: # m(m+1)/2
            m[i+1] = m[i] # m(m+1)/2-1
            i -= 1 # m(m+1)/2-1
        m[i+1] = k # m-1
