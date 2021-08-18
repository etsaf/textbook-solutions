def getNext(x): #find the rightmost zero that has a one next, put the remaining ones as right as possible
    a = x
    i = 0
    found = False
    num1 = 0
    while a != 0:
        if a & 1 == 1:
            num1 += 1
        if a & 1 == 1 and (a - 1) & 2 == 0:
            break
        a = a >> 1
        i += 1
    if not found:
        return -1
    pos = i + 1
    x = x | (1 << pos) #replace found bit
    x = x & ~((1 << pos) - 1)#clear all bits to the right
    x = x | ((1 << num1)  - 1)#put in the number of ones
    return x

def getPrev(x):
    a = x #find the rightmost one that has a zero to the right
    i = 0
    found = False
    num1 = 0
    while a != 0:
        if a & 1 == 0:
            num0 += 1
        if a & 1 == 0 and a & 2 == 2:
            break
        a = a >> 1
        i += 1
    if not found:
        return -1
    pos = i + 1
    x = x & (~ (1 << pos)) #replace found bit
    x = x & ~((1 << pos) - 1) #clear all bits to the right
    mask = ((1 << pos) - 1) & (~((1 << num1) - 1))
    x = x | mask #put in the number of zeros
    return x