a = list(input())
b = []
prev = ''
counter = 0
for i in range(len(a)):
    if a[i] == prev:
        counter += 1
    else:    
        if i != 0:
            b.append(prev)
            b.append(str(counter))
        counter = 1
        prev = a[i]
b.append(prev)
b.append(str(counter))
if len(b) < len(a):
    print(''.join(b))
else:
    print(''.join(a))