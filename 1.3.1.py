a = list(input().strip())
l = len(a)
spaceNum = 0
for i in a:
    if i == ' ':
        spaceNum += 1
totalLen = len(a) + spaceNum * 2
for i in range(totalLen - l):
    a.append(0)
ind = totalLen - 1
for i in range(l - 1, -1, -1):
    if a[i] == ' ':
        a[ind] = '0'
        a[ind - 1] = '2'
        a[ind - 2] = '%'
        ind -= 3
    else:
        a[ind] = a[i]
        ind -= 1
print(''.join(a))