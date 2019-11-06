def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        # If both bit are same then XOR will be zero
        if a[i] == b[i]:
            result += '0'
        else:  # If both bit are different then XOR will be one
            result += '1'
    return result
