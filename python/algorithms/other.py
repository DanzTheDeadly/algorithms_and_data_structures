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


def reverseWord(word, word_len):
    res = []
    for i in range(word_len-1, -1, -1):
        res.append(word[i])
    return ''.join(res)


def reverseWords(s: str) -> str:
    buffer = []
    buffer_len = 0
    res = []
    ptr = 0
    length = len(s)
    while ptr < length:
        if buffer:
            if s[ptr] == ' ':
                res.append(reverseWord(buffer, buffer_len))
                buffer = []
                buffer_len = 0
            else:
                buffer.append(s[ptr])
                buffer_len += 1
        elif not buffer and s[ptr] != ' ':
            buffer.append(s[ptr])
            buffer_len += 1
        ptr += 1
    if buffer:
        res.append(reverseWord(buffer, buffer_len))
    return ' '.join(res)