a = list(input())
d = dict()
difSymb = 0
evenSymb = 0
oddSymb = 0
for i in a:
    if i.isalpha():
        if i.lower() in d:
            d[i.lower()] += 1
        else:
            difSymb += 1
            d[i.lower()] = 1
for i in d.values():
    if i % 2 == 1:
        oddSymb += 1
print(d)
print(oddSymb <= 1)