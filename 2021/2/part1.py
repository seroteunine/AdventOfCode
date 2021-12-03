txt = open('adventofcode/2021/2/input.txt', 'r').read().split('\n')

hor = dep = 0
for i in txt:
    dir, val = i.split()[0], int(i.split()[1])
    if dir == 'forward':
        hor += val
    else:
        dep = dep + val if dir == 'down' else dep - val
print(hor, dep, hor * dep)