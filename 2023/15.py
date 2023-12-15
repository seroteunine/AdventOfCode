from collections import defaultdict

inp = open('15.txt').read()

#Part 1
def getHash(string):
    curr = 0
    for ch in string:
        curr = (curr + ord(ch)) * 17 % 256
    return curr

t1 = sum(getHash(s) for s in inp.split(','))
print(t1)

#Part 2
boxes = defaultdict(dict)

for string in inp.split(','):
    if string.endswith('-'):
        lbl = string[:-1]
        hash = getHash(lbl)
        boxes[hash].pop(lbl, None)
    else:
        lbl, foc = string.split('=')
        hash = getHash(lbl)
        boxes[hash][lbl] = int(foc)

t2 = 0
for i, box in boxes.items():
    t2 += sum((i+1) * (j+1) * lens for j, lens in enumerate(box.values()))

print(t2)
