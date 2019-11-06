def str2bytes(string):
    return ''.join(format(ord(x), 'b') for x in string)
