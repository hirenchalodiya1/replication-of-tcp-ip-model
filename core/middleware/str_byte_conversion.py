def str2bits(string):
    res = ""
    for x in string:
        bits = ''.join(format(ord(x), 'b'))
        while len(bits) != 8:
            bits = '0' + bits
        res += str(bits)
    return res


def bits2str(string):
    pass


def str2bytes(string):
    return string.encode('utf-8')


def bytes2str(string):
    return string.decode('utf-8')
