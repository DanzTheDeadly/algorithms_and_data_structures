from array import array
from random import randint
from algorithms import quicksort, insertion_sort
from calgorithms import cquicksort, cinsertion_sort

a = array('i', [randint(0, 1000) for i in range(1000)])

%timeit cinsertion_sort(a, 1000, inplace=False)
%timeit cquicksort(a, 0, 1000, inplace=False)
%timeit insertion_sort(a, inplace=False)
%timeit quicksort(a, 0, 1000, inplace=False)
%timeit sorted(a)

%load_ext cython
%%cython

from linkedlist_cy import benchmark

def pybenchmark ():
    M = []
    for i in range(10000000):
        M.append(i)

%timeit benchmark()
%timeit pybenchmark()
