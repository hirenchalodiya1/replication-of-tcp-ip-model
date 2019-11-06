def str2bits(string):
    res = ""
    for x in string:
        bits = ''.join(format(ord(x), 'b'))
        while len(bits) != 8:
            bits = '0' + bits
        res += str(bits)
    return res


def bits2str(string):
    data = ""
    for i in range(0, len(string), 8):
        j = min(i+8, len(string))
        char = chr(int(string[i:j], 2))
        data += char
    return data


def str2bytes(string):
    return string.encode('utf-8')


def bytes2str(string):
    return string.decode('utf-8')
