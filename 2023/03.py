from collections import defaultdict
from functools import reduce
import operator
import re

G = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')

G = open('03.txt').read().split('\n')

#Part 1 
total = 0
#Part 2
gears = defaultdict(list)

R = len(G)
C = len(G[0])
for r in range(R):
    for m in re.finditer('\d+', G[r]):
        for rr in range(r - 1, r + 2):          
            for cc in range(m.start() - 1, m.end() + 1):
                if 0 <= rr < R and 0 <= cc < C:
                    if not G[rr][cc].isdigit() and G[rr][cc] != '.':
                        total += int(m.group()) #P1
                        gears[(rr, cc)].append(int(m.group())) #P2

print(total) #P1
print(sum([reduce(operator.mul, gear, 1) for gear in gears.values() if len(gear) > 1])) #P2



