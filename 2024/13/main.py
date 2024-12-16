import re
from collections import defaultdict
f = [[tuple([int(y[2:]) for y in x.replace(':', ',').split(', ')[1:]]) for x in line.split('\n')] for line in open('input.txt').read().strip().split('\n\n')]

COST_A, COST_B = 1, 3
MAX_PUSHES = 100
MAX_COST = COST_A * MAX_PUSHES + COST_B * MAX_PUSHES

def least_tokens_to_win(A, B, P):
    is_possible = False
    aX, aY = A
    bX, bY, = B
    for a in range(101):
        for b in range(101):
            pos = (a*aX + b*bX, a*aY + b*bY)
            if pos != P:
                continue
            cost = a * 3 + b
            if not is_possible:
                least = cost
            else:
                least = min(least, cost)
            is_possible = True
    return least if is_possible else 0

t = sum(least_tokens_to_win(*game) for game in f)
print(t)