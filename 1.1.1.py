a = list(input())
isUnique = True
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[j] == a[i]:
            isUnique = False
            break
print(isUnique)