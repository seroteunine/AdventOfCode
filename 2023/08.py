from collections import defaultdict
from itertools import product
from math import lcm

lines = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

lines = open('08.txt').read()

instr, lines = lines.split('\n\n')
lines = lines.split('\n')

nodes = defaultdict(tuple)

for line in lines:
    start, next = line.split(' = ')
    l, r = next.split(', ')
    nodes[start] = (l[1:], r[:-1])

#Part 1
n = 0
current = 'AAA'
i = 0
while current != 'ZZZ':
    options = nodes[current]
    current = options[0] if instr[i] == 'L' else options[1]
    n += 1
    i = i + 1 if i < len(instr) - 1 else 0

print(n)

#Part 2
nodes = defaultdict(tuple)

current = []
for line in lines:
    start, next = line.split(' = ')
    l, r = next.split(', ')
    nodes[start] = (l[1:], r[:-1])
    if start[-1] == 'A':
        current.append(start)

z = []
for j, curr in enumerate(current):
    i = 0
    n = 0
    while not (current[j][-1] == 'Z' and i == 0):
        options = nodes[current[j]]
        current[j] = options[0] if instr[i] == 'L' else options[1]
        n += 1
        i = i + 1 if i < len(instr) - 1 else 0
    z.append(n)

print(lcm(*z))