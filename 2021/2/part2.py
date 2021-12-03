txt = open('adventofcode/2021/2/input.txt', 'r').read().split('\n')

hor = dep = aim = 0
for i in txt:
    dir, val = i.split()[0], int(i.split()[1])
    if dir == 'forward':
        hor += val
        dep += val * aim
    else:
        aim = aim + val if dir == 'down' else aim - val 

print(hor, dep, hor * dep)