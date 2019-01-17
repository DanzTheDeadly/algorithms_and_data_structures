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


cpdef void cquicksort (int[:] m, int start=0, int end=10, bint inplace=True):
    cdef int i, div
    if not inplace:
        m = m.copy()
    if end-start > 1:
        div = start
        for i in range(start, end-1):
            if m[i] <= m[end-1]:
                m[div], m[i] = m[i], m[div]
                div += 1
        m[div], m[end-1] = m[end-1], m[div]
        cquicksort(m, start, div)
        cquicksort(m, div+1, end)
