a = list(input())
b = list(input())
charSet1 = dict()
charSet2 = dict()
for i in a:
    if i in charSet1:
        charSet1[i] += 1
    else:
        charSet1[i] = 1
for i in b:
    if i in charSet2:
        charSet2[i] += 1
    else:
        charSet2[i] = 1
print(charSet2 == charSet1)