def xor(a, b):

    result = ""

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'

    return result
