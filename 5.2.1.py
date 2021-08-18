def printBinary(x): # x = float()
    if x >= 1 or x <= 0:
        return 'Error'
    binary = []
    binary.append("0")
    binary.append(".")
    while x > 0:
        if len(binary) > 32:
            return 'Error'
        a = x * 2
        if a >= 1:
            binary.append('1')
            x = a - 1
        else:
            binary.append('0')
            x = a
    return ''.join(binary)