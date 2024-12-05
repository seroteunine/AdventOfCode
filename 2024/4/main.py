G = [[ch for ch in line] for line in open('input.txt').read().split('\n')]
R = len(G)
C = len(G[0])

t = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == 'X':
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    valid = True
                    for i, ch in enumerate(['M', 'A', 'S']):
                        rr, cc = r + dy * (i+1), c + dx * (i+1)
                        if 0 <= rr < R and 0 <= cc < C:
                            if G[rr][cc] == ch:
                                continue
                        valid = False
                    if valid: 
                        t += 1

print(t)


# Part 2
t = 0
for r in range(1, R - 1):
    for c in range(1, C - 1):
        if G[r][c] == 'A':
            for sngs in ['MMSS', 'SSMM', 'MSMS', 'SMSM']:
                t += sngs == G[r-1][c-1] + G[r-1][c+1] + G[r+1][c-1] + G[r+1][c+1]
print(t)
