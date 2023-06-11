def hash_join (left_file, right_file):
    def build_hashmap (datafile):
        hashmap = {}
        for line in datafile:
            key, *value = line.strip().split(';')
            if not hashmap.get(key):
                hashmap[key] = [''.join(value)]
            else:
                hashmap[key].append(''.join(value))
        return hashmap

    left = open(left_file)
    right = open(right_file)
    out = open('result.txt', 'w')

    l = build_hashmap(left)

    for r_line in right:
        r = tuple(r_line.strip().split(';'))
        l_values = l.get(r[0])
        if l_values:
            for l_value in l_values:
                joined_row = '{};{};{}\n'.format(r[0], l_value, r[1])
                out.write(joined_row)
    right.seek(0)
    left.close()
    right.close()
    out.close()


def nested_loop_join (left_file, right_file):
    left = open(left_file)
    right = open(right_file)
    out = open('result.txt', 'w')

    for l_line in left:
        l = tuple(l_line.strip().split(';'))
        for r_line in right:
            r = tuple(r_line.strip().split(';'))
            if l[0] == r[0]:
                joined_row = '{};{};{}\n'.format(l[0], l[1], r[1])
                out.write(joined_row)
        right.seek(0)
    left.close()
    right.close()
    out.close()
