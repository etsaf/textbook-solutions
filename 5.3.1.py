def flipBit(x):
    if (~x) == 0:
        return len(list(str(x)))
    prevLen = 0
    currLen = 0
    ans = 0
    while x != 0:
        if (x & 1) == 1:
            prevZ = False
            currLen += 1
        else:
            if x % 2 == 0:
                prevLen = 0
            else:
                prevLen = currLen
            currlen = 0
        ans = max(prevLen + currLen + 1, ans)
        x = x >> 1
    return ans