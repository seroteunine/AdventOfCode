import re
from collections import defaultdict
f = open('input.txt').read().strip().split('\n')
robots = [[tuple(map(int, pv[2:].split(','))) for pv in r.split()] for r in f]
X, Y = 101, 103
N = 100

def get_end_pos(x, y, dx, dy):
    x = (x + dx * N) % X
    y = (y + dy * N) % Y
    return x, y

def get_quadrants(positions: list):
    q = defaultdict(int)
    for x, y in positions:
        if x < X // 2:
            if y < Y // 2:
                q[1] += 1
            elif y > Y // 2:
                q[3] += 1
        elif x > X // 2:
            if y < Y // 2:
                q[2] += 1
            elif y > Y // 2:
                q[4] += 1
    return q
            

end_pos = [get_end_pos(*p, *v) for p, v in robots]
print(end_pos)
q = get_quadrants(end_pos)
a = 1
for i in q.values():
    a *= i

print(a)