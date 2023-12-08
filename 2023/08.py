from collections import defaultdict
from math import lcm

lines = open('08.txt').read()
instr, lines = lines.split('\n\n')
lines = lines.split('\n')

#Part 1
nodes = defaultdict(tuple)

for line in lines:
    start, next = line.split(' = ')
    l, r = next.split(', ')
    nodes[start] = (l[1:], r[:-1])

current = 'AAA'
i = 0
while current != 'ZZZ':
    options = nodes[current]
    current = options[0] if instr[i % len(instr)] == 'L' else options[1]
    i += 1

print(i)

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
    while current[j][-1] != 'Z':
        options = nodes[current[j]]
        current[j] = options[0] if instr[i % len(instr)] == 'L' else options[1]
        i += 1
    z.append(i)

print(lcm(*z))