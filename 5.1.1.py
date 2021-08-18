def insert(N, M, i, j):
    rmask = (~ 0) << (j + 1)
    lmask = (2 << i) - 1
    mask = rmask | lmask
    clear = N & mask
    new = M << (j + 1)
    return clear | new