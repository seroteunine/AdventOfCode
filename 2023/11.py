G = open('11.txt').read()
G = [[num for num in row] for row in G.split('\n')]

R = len(G)
C = len(G[0])

rExp, cExp = set(), set()
coord = []

for r in range(R):
    for c in range(C):
        if G[r][c] == '#':
            coord.append((r, c))
        elif all(value == '.' for value in G[r]) and all(value == '.' for value in list(zip(*G))[c]):
            rExp.add(r)
            cExp.add(c)

EXPANSION = 1 #Part 1
# EXPANSION = 1000000 - 1 #Part 2
t = 0
for i, v in enumerate(coord):
    for j in coord[i+1:]:
        x = abs(v[1] - j[1])
        y = abs(v[0] - j[0])
        x += sum(EXPANSION * (j[0] < r < v[0] or j[0] > r > v[0]) for r in rExp)
        y += sum(EXPANSION * (j[1] < c < v[1] or j[1] > c > v[1]) for c in cExp)
        t += x + y

print(t)