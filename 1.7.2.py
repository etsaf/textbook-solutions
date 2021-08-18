n = int(input())
a = []
b = ''
for i in range(n):
    a.append(list(input()))
for layer in range(n):
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
        offset = i - first
        b = a[first][offset + first]
        # left -> top
        a[first][offset + first] = a[last - offset][first]
        # bottom -> left
        a[last - offset][first] = a[last][last - offset]
        # right -> bottom
        a[last][last - offset] = a[first + offset][last]
        # top -> right
        a[first + offset][last] = b
for i in a:
    print(''.join(i))