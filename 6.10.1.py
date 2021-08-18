#7 days: represent each bottle number in binary (1000 < 2 ^ 10), assign a strip to each place in representation, if one: add drop
def findBottle(bottles, strips):
    addDrops(bottles, strips)
    testStrips(strips)
    ans = []
    for i in strips:
        if i == 'Positive':
            ans.append('1')
        else:
            ans.append('0')
    ans = int(''.join(ans))
    return ans

def makeStrips(bottles, strips):
    for i in range(len(bottles)):
        bit = i
        a = 0
        while bit:
            if (bit & 1) == 1:
                strips[a].addDrop(bottles[i])
            bit >>= 1
            a += 1