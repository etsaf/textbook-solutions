import random
def Nfamilies(n):
    girls = 0
    boys = 0
    for i in range(n):
        genders = runFamily()
        girls += genders[0]
        boys += genders[1]
    return girls / (boys + girls)

def runFamily():
    boys = 0
    girls = 0
    while girls == 0:
        rand = random.randit(0, 1)
        if rand:
            girls += 1
        else:
            boys += 1
    genders = {girls, boys}
    return genders