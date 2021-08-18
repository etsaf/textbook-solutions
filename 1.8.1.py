n = int(input())
m = int(input())
a = []
b = ''
for i in range(n):
    a.append(list(input()))
rowz = []
colz = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            rowz.append(i)
            colz.append(j)
for k in range(n):
    for t in range(m):
        if k in rowz:
            a[k][t] = '0'
        if t in colz:
            a[k][t] = '0'
for i in a:
    print(''.join(i))