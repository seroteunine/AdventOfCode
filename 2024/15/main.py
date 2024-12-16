import re
from collections import defaultdict

# Parse input
G, M = open('input.txt').read().strip().split('\n\n')
G = [[ch for ch in line] for line in G.split('\n')]
M = [ch for ch in M if ch != '\n']
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == '@':
            pos = (r, c)
            break

# Part 1
def get_dir(move: str):
    if move == '^':
        return (-1, 0)
    if move == '>':
        return (0, 1)
    if move == 'v':
        return (1, 0)
    if move == '<':
        return (0, -1)

for move in M:
    dr, dc = get_dir(move)
    print(dr, dc)