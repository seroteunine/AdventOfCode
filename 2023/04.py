lines = open('04.txt').read().split('\n')
# lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

#P1
total = 0
for line in lines:
    _, numbers = line.split(':')
    win, own = numbers.split(' | ')
    win = [int(num) for num in win.split()]
    own = [int(num) for num in own.split()]
    count = sum(num in own for num in win)
    score = 2 ** (count-1) if count > 0 else 0
    total += score

print(total)

#P2
copies = {}

for i, line in enumerate(lines):
    copies[i] = copies.get(i, 1)
    _, numbers = line.split(':')
    win, own = numbers.split(' | ')
    win = [int(num) for num in win.split()]
    own = [int(num) for num in own.split()]
    score = sum(num in own for num in win)
    for ii in range(score):
        copies[i + ii + 1] = copies.get(i + ii + 1, 1) + copies[i]

print(sum(copies.values()))