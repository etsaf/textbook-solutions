def oddEven(x):
    # a = 1010 in hexadecimals and 5 = 0101 in binary
    # 0xaaaaaaaa is 1010 taken 8 times to fill a 32-bit number
    mask0 = 0xaaaaaaaa
    masked0 = x & mask0
    mask1 = 0x55555555
    masked1 = x & mask1
    return (masked0 >> 1) | (masked1 << 1)