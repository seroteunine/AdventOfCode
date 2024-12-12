import re
from collections import defaultdict
f = open('input.txt').read().strip().split('\n')
G = [[int(i) for i in x] for x in f]
R = len(G)
C = len(G[0])

def has_n_ends(pos, visited):
    if pos in visited:
        return 0
    # Disable next line for part 2
    visited.add(pos) 

    r, c = pos
    if G[r][c] == 9:
        return 1
    
    valid = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C:
            if G[rr][cc] == G[r][c] + 1:
                valid += has_n_ends((rr, cc), visited)
    return valid

t = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == 0:
            visited = set()
            t += has_n_ends((r, c), visited)

print(t)