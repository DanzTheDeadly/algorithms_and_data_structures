from array import array
from random import randint
from algorithms.algorithms_cython import quicksort, insertion_sort
from algorithms.algorithms_py import cquicksort, cinsertion_sort

a = array('i', [randint(0, 1000) for i in range(1000)])

%timeit cinsertion_sort(a, 1000, inplace=False)
%timeit cquicksort(a, 0, 1000, inplace=False)
%timeit insertion_sort(a, inplace=False)
%timeit quicksort(a, 0, 1000, inplace=False)
%timeit sorted(a)


import array
from data_structures.heap_cython import heapsort
from random import randint

ar = array.array('i', [randint(0,1000) for i in range(100000)])

%timeit sorted(ar)
%timeit heapsort(ar)
