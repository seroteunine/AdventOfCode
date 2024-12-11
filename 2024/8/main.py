from collections import defaultdict


G = open('input.txt').read().strip().split('\n')
R = len(G)
C = len(G[0])

antennas_dict = defaultdict(list)
for i in range(R):
    for j in range(C):
        ch = G[i][j]
        if ch != '.':
            antennas_dict[ch].append((i, j))

antinodes = set()
for antennas in antennas_dict.values():
    for i in range(len(antennas)):
        r1, c1 = antennas[i]
        for j in range(i + 1, len(antennas)):
            r2, c2 = antennas[j]
            dr, dc = r2 - r1, c2 - c1
            p1 = (r1 - dr, c1 - dc)
            p2 = (r2 + dr, c2 + dc)
            for p in [p1, p2]:
                if 0 <= p[0] < R and 0 <= p[1] < C:
                    antinodes.add(p)

print(len(antinodes))

# Part 2
antinodes = set()
for antennas in antennas_dict.values():
    for i in range(len(antennas)):
        r1, c1 = antennas[i]
        for j in range(i + 1, len(antennas)):
            r2, c2 = antennas[j]
            dr, dc = r2 - r1, c2 - c1
            pr, pc = r1, c1
            while 0 <= pr < R and 0 <= pc < C:
                antinodes.add((pr, pc))
                pr, pc = pr - dr, pc - dc
            pr, pc = r2, c2
            while 0 <= pr < R and 0 <= pc < C:
                antinodes.add((pr, pc))
                pr, pc = pr + dr, pc + dc

print(len(antinodes))