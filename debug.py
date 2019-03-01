#import array
#from random import randint
#from algorithms.heapsort_cython import heapsort as pure_heapsort
#from algorithms.quicksort_cython import quicksort
#from algorithms.insertionsort_cython import insertion_sort
#from timeit import timeit
#встроенный питоновский алгоритм сортировки
#%timeit sorted(ar)
#алгоритм сортировки кучи на основе cdef класса cython
#%timeit class_heapsort(ar)
#алгоритм сортировки кучи в чистом виде на cython
#%timeit pure_heapsort(ar)
#быстрая сортировка
#%timeit quicksort(ar)

#ranges = [10, 25, 50, 75, 100, 150, 400, 1000, 5000, 10000, 50000, 100000, 250000, 500000]
#times_h = []
#times_q = []
#for rng in ranges:
#    ar = array.array('i', [randint(0,1000) for i in range(rng)])
#    times_h.append(timeit(lambda: pure_heapsort(ar), number=500))
#    times_q.append(timeit(lambda: quicksort(ar), number=500))
#
#import pandas as p
#from math import log10
#
#df = p.DataFrame({'length': ranges, 'heapsort': times_h, 'quicksort': times_q})
#df.plot(x='length', figsize=(15,10))

from data_structures.queue_cython import Queue
import cProfile

def test ():
    a = Queue()
    for i in range(1, 10000000):
        a.enqueue(i)
        while 1:
            j = a.dequeue()
            if not j:
                break

cProfile.run('test()')
