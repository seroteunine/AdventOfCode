from collections import defaultdict

inp = open('15.txt').read()

#Part 1
def getHash(string):
    curr = 0
    for ch in string:
        curr += ord(ch)
        curr *= 17
        curr = curr % 256
    return curr

t1 = 0
for string in inp.split(','):
    t1 += getHash(string)

#Part 2
boxes = defaultdict(defaultdict)

for string in inp.split(','):
    if string[-1] == '-':
        lbl, foc = string[:-1], None
    else:
        lbl, foc = string.split('=')
    hash = getHash(lbl)
    if foc:
        boxes[hash][lbl] = foc
    elif lbl in boxes[hash]:
        del boxes[hash][lbl]

t2 = 0
for i, box in boxes.items():
    for j, lens in enumerate(box.values()):
        t2 += (i+1) * (j+1) * int(lens)

print(t1)
print(t2)
