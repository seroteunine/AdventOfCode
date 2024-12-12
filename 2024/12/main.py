import re
from collections import defaultdict
f = open('input.txt').read().strip().split('\n')
G = [[i for i in line] for line in f]
R, C = len(G), len(G[0])

def get_region(r, c, region):
    if (r, c) in region:
        return
    region.add((r, c))
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if rr in range(R) and cc in range(C) and G[r][c] == G[rr][cc]:
            get_region(rr, cc, region)
    return region

regions = set()
for r in range(R):
    for c in range(C):
        region = get_region(r, c, set())
        regions.add(frozenset(region))

def get_perimeter(region):
    edges = []
    for r, c in region:
        for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
            rr, cc = r + dr, c + dc
            if (rr, cc) not in region:
                edges.append((rr, cc))
    return edges

def get_price_p1(region):
    return len(region) * len(get_perimeter(region))

# Part 1
t = sum(get_price_p1(region) for region in regions)
print(t)

# Part 2
def get_sides(region):
    edges = get_perimeter(region)
    new = set()
    for r, c in region:
        keep = True
        for dr, dc in [(1, 0), (0, 1)]:
            rr, cc = r + dr, c + dc
            if (rr, cc) in edges:
                keep = False
        if keep:
            new.add((r, c))
    print(new)
    return new

def get_price_p2(region):
    return len(region) * len(get_sides(region))

t = sum(get_price_p2(region) for region in regions)
print(t)