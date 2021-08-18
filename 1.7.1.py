n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(input()))
for i in range(n):
    for j in range(n - 1, -1, -1):
        b.append(a[j][i])
    print(''.join(b))
    b = []