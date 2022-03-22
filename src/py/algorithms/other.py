def split (string, symbol):
    l = []
    start = 0
    i = 0
    for char in string:
        if char == symbol:
            if start < i:
                l.append(string[start:i])
            i += 1
            start = i
        else:
            i += 1
    if start < i:
        l.append(string[start:i])
    return l


if __name__ == '__main__':
    print(split('dsafgad    fdsaf ads dsaf fagda fdfs    ', ' '))
