from collections import defaultdict


f = open('input.txt').read().strip()
f = [int(ch) for ch in f]

converted = []
for i, ch in enumerate(f):
    if not i % 2:
        converted.extend([i // 2] * ch)
    else:
        converted.extend(['.'] * ch)

for i in range(len(converted)):
    if i == len(converted):
        break
    while converted[i] == '.':
        converted[i] = converted.pop()

print(sum(i * ch for i, ch in enumerate(converted)))

# Part 2
converted = []
conv_dict = defaultdict(int)
for i, ch in enumerate(f):
    if not i % 2:
        ind = i // 2
        converted.extend([ind] * ch)
        conv_dict[ind] = ch
    else:
        converted.extend(['.'] * ch)

lastindex = converted.index('.')
print(converted)

for ind in sorted(conv_dict.keys(), reverse=True):
    filelen = conv_dict[ind]
    index = converted.index(ind)
    for i in range(lastindex, index - filelen):
        if converted[i:i + filelen] == ['.'] * filelen:
            converted[index:index + filelen] = ['.'] * filelen
            converted[i:i + filelen] = [ind] * filelen
            lastindex = converted.index('.')
            break

print(converted)

t = 0
for i, c in enumerate(converted):
    if c != '.':
        t += i * c

print(t)