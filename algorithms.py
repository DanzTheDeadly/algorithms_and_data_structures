import src.py.algorithms.sort as py_sort
import src.py.algorithms.join as py_join
from src.py.algorithms.other import split as py_split


def sort(data, algorithm='selection_sort'):
    if algorithm == 'selection_sort':
        return py_sort.selection_sort(data)
    # TODO meta func