from math import floor, ceil, inf
from python.datastructures.heap import MinHeap

def insertion_sort (m, inplace=False):
    if not inplace:
        m = m[:]
    for j in range(1, len(m)): # m
        k = m[j] # m-1
        i = j-1 # m-1
        while i >= 0 and m[i] > k: # m(m+1)/2
            m[i+1] = m[i] # m(m+1)/2-1
            i -= 1 # m(m+1)/2-1
        m[i+1] = k # m-1
    return m


def selection_sort (m):
    n = [] # 1
    while m: # m
        k = m[0] # m
        for i in m[1:]: # m(m+1)/2
            if i < k: # m(m+1)/2-1
                k = i # m(m+1)/2-1
        n.append(m[m.index(k)]) # m
    return n


def mergesort (m, start=0, end=0, inplace=False):
    if not end:
        end = len(m)
    if not inplace:
        m = m[:]
    if end-start > 1:
        div = floor((end+start)/2)
        print(start, div, end)
        mergesort(m, start, div)
        mergesort(m, div, end)
        merge(m, start, div, end)
    if not inplace:
        return m


def merge (m, start, div, end):
    A = m[start:div]
    A.append(999999)
    B = m[div:end]
    B.append(999999)
    i, j = 0, 0
    for n in range(start, end):
        if A[i] < B[j]:
            m[n] = A[i]
            i += 1
        else:
            m[n] = B[j]
            j += 1
    print(m)


def quicksort (m, a=0, b=10, inplace=False):
    if not inplace:
        m = m[:]
    if len(m[a:b]) <= 1:
        return m
    div = a
    for i in range(a, b-1):
        if m[i] <= m[b-1]:
            m[div], m[i] = m[i], m[div]
            div += 1
    m[div], m[b-1] = m[b-1], m[div]
    quicksort(m, a, div)
    quicksort( m, div+1, b)
    return m


def counting_sort (m, r):
    less = [0 for i in range(r)]
    esum = 0
    for n in range(r):
        for k in m:
            if k < n:
                esum += 1
        less[n] = esum
        esum = 0
    res = [0 for i in range(len(m))]
    print(less)
    for j in range(len(m)):
        res[less[m[j]]] = m[j]
        less[m[j]] += 1
    return res


def heapsort(l: list[int]) -> list[int]:
    h = MinHeap()
    for val in l:
        h.insert(val)
    res = []
    for i in range(h.size()):
        res.append(h.getMin())
        h.pop()
    return res


def heapsort_inplace(l: list[int]):
    length = len(l)
    if length <= 1:
        return
    else:
        def _get_biggest_idx(idx1):
            biggest_idx = idx1
            left_idx = idx1 * 2 + 1
            right_idx = idx1 * 2 + 2
            if left_idx < length:
                if l[biggest_idx] < l[left_idx]:
                    biggest_idx = left_idx
                if right_idx < length:
                    if l[biggest_idx] < l[right_idx]:
                        biggest_idx = right_idx
            return biggest_idx
        
        for idx in range(1, length):
            parent = (idx - 1) // 2 
            while idx > 0 and l[idx] > l[parent]:
                l[idx], l[parent] = l[parent], l[idx]
                idx = parent
                parent = (idx - 1) // 2

        while length > 1:
            l[length - 1], l[0] = l[0], l[length - 1]
            idx = 0
            length -= 1
            biggest_idx = _get_biggest_idx(idx)
            while idx != biggest_idx:
                l[idx], l[biggest_idx] = l[biggest_idx], l[idx]
                idx = biggest_idx
                biggest_idx = _get_biggest_idx(idx)