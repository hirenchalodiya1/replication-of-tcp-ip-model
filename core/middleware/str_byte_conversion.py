def str2bits(string):
    return ''.join(format(ord(x), 'b') for x in string)


def bits2str(string):
    pass


def str2bytes(string):
    return string.encode('utf-8')


def bytes2str(string):
    return string.decode('utf-8')
