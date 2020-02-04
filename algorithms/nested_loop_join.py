def join (left_file, right_file):
    left = open(left_file)
    right = open(right_file)
    out = open('result.txt', 'w')

    for l_line in left:
        l = tuple(l_line.strip().split('\t'))
        for r_line in right:
            r = tuple(r_line.strip().split('\t'))
            if l[0] == r[0]:
                joined_row = '{}\t{}\t{}\n'.format(l[0], l[1], r[1])
                out.write(joined_row)
        right.seek(0)

    left.close()
    right.close()
    out.close()
