from collections import Counter

lines = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split('\n')

lines = open('07.txt').read().split('\n')

#Part 1
values = {'2':2, '3': 3, '4':4, '5':5, '6':6, '7': 7, '8': 8, '9': 9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def getSetValue(hand):
    c = sorted(Counter(hand).values())
    if c == [5]:
        return 6
    if c == [1,4]:
        return 5
    if c == [2, 3]:
        return 4
    if c == [1,1,3]:
        return 3
    if c == [1,2,2]:
        return 2
    if c == [1,1,1,2]:
        return 1
    return 0

def isOrdered(l1, l2):
    h1, h2 = l1.split()[0], l2.split()[0]
    v1, v2 = getSetValue(h1), getSetValue(h2)
    if v1 != v2:
        return v1 < v2
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            return values[h1[i]] < values[h2[i]]
        
for i in range(len(lines)):
    for j in range(0, len(lines)-i-1):
        if not isOrdered(lines[j], lines[j + 1]):
            lines[j], lines[j + 1] = lines[j + 1], lines[j]

sum = 0
counter = 1
for line in lines:
    sum += counter * int(line.split()[1])
    counter += 1

print(sum)

#Part 2
values = {'J':1, '2':2, '3': 3, '4':4, '5':5, '6':6, '7': 7, '8': 8, '9': 9, 'T':10, 'Q':11, 'K':12, 'A':13}
        
def tryJoker(hand):
    if hand.count('J') == 5:
        return 'AAAAA'
    mostcommon = Counter(hand).most_common(1)[0][0]
    if mostcommon != 'J':
        return hand.replace('J', mostcommon) 
    return hand.replace('J', Counter(hand).most_common(2)[1][0])

def isOrdered(l1, l2):
    h1, h2 = l1.split()[0], l2.split()[0]
    h1Jokered, h2Jokered = tryJoker(h1), tryJoker(h2)
    v1, v2 = getSetValue(h1Jokered), getSetValue(h2Jokered)
    if v1 != v2:
        return v1 < v2
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            return values[h1[i]] < values[h2[i]]

#Order       
for i in range(len(lines)):
    for j in range(0, len(lines)-i-1):
        if not isOrdered(lines[j], lines[j + 1]):
            lines[j], lines[j + 1] = lines[j + 1], lines[j]

sum = 0
counter = 1
for line in lines:
    sum += counter * int(line.split()[1])
    counter += 1

print(sum)