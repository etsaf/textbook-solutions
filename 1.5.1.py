a = list(input())
b = list(input())
err = 0
iA = 0
iB = 0
while iA < len(a) and iB < len(b):
    if a[iA] == b[iB]:
        iA += 1
        iB += 1
    elif a[iA + 1] == b[iB + 1]:
        iA += 1
        iB += 1
        err += 1
    elif a[iA] == b[iB + 1]:
        iB += 1
        err += 1
    elif a[iA + 1] == b[iB]:
        iA += 1
        err += 1
    else:
        err += 2
        break
print(err <= 1)