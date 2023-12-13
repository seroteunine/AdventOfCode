def findLine(G):
    R = len(G)
    for r in range(R - 1):
        if G[r] == G[r + 1]:
            steps = min(r + 1, R - r - 1)
            if all(G[r - d] == G[r + 1 + d] for d in range(1, steps)):
                return r + 1
    return None

t = 0
for block in open('13.txt').read().split('\n\n'):
    G = block.split('\n')
    l = findLine(G)
    if l:
        t += l * 100
        continue
    t += findLine(list(zip(*G)))

print(t)    

