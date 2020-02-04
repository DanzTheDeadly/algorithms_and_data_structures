from random import randint, choices
import string

def generate_random_datafile (name, lines=100):
    with open(name, 'w') as outfile:
        for i in range(lines):
            id = randint(0, lines)
            data = ''.join(choices(string.ascii_letters, k=10))
            line = '{}\t{}\n'.format(id, data)
            outfile.write(line)


generate_random_datafile('left.txt', lines=5000)
generate_random_datafile('right.txt', lines=5000)

from algorithms.nested_loop_join import join as njoin
from algorithms.hash_join import join as hjoin

njoin('left.txt', 'right.txt')
hjoin('left.txt', 'right.txt')
