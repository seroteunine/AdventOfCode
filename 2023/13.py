def findLine(G):
    R = len(G)
    for r in range(R - 1):
        if G[r] == G[r + 1]:
            steps = min(r + 1, R - r - 1)
            if all(G[r - d] == G[r + 1 + d] for d in range(1, steps)):
                return r + 1
    return 0

t = 0
for block in open('13.txt').read().split('\n\n'):
    G = block.split('\n')
    r, c = findLine(G), findLine(list(zip(*G)))
    t += r * 100 + c

print(t)      

def findLineImperfect(G):
    R = len(G)
    for r in range(R - 1):
        mistakes = 0
        steps = min(r + 1, R - r - 1)
        for i in range(0, steps):
            for c in range(len(G[r])):
                if G[r - i][c] != G[r + 1 + i][c]:
                    mistakes += 1
        if mistakes == 1:
            return r + 1
    return 0

t = 0
for block in open('13.txt').read().split('\n\n'):
    G = block.split('\n')
    r, c = findLineImperfect(G), findLineImperfect(list(zip(*G)))
    t += r * 100 + c

print(t)      