a = list(input())
charSet = dict()
isUnique = True
for i in a:
    if i in charSet:
        isUnique = False
        break
    else:
        charSet[i] = 1
print(charSet)
print(isUnique)