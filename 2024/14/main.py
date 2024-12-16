import re
from collections import defaultdict
from functools import reduce
f = open('input.txt').read().strip().split('\n')
robots = [[tuple(map(int, pv[2:].split(','))) for pv in r.split()] for r in f]
X, Y = 101, 103
N = 100

def get_end_pos(x, y, dx, dy, N):
    x = (x + dx * N) % X
    y = (y + dy * N) % Y
    return x, y

def get_quadrants(positions: list):
    q = defaultdict(int)
    for x, y in positions:
        mx, my = X // 2, Y // 2
        if x == mx and y == my:
            continue
        if x < mx and y < my:
            q[1] += 1
        elif x > mx and y < my:
            q[2] += 1
        elif x < mx and y > my:
            q[3] += 1
        elif x > mx and y > my:
            q[4] += 1
    return q
            
end_pos = [get_end_pos(*p, *v, N) for p, v in robots]
q = get_quadrants(end_pos)
a = reduce((lambda x, y: x * y), q.values(), 1)
print(a)

# Part 2 - Just brute force and inspect output
def print_grid(positions):
    for y in range(Y):
        row = ''
        for x in range(X):
            if (x, y) in positions:
                row += 'X'
                continue
            row += ' '
        print(row)

for n in range(62, 10000, 101):
    end_pos = [get_end_pos(*p, *v, n) for p, v in robots]
    print_grid(end_pos)
    print(n)
