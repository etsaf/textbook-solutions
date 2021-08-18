def bitSwap(A, B):
    ans = 0
    c = A ^ B
    while c != 0:
        c = c & (c - 1)
        ans += 1
    return ans