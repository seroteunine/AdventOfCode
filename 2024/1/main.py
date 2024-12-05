f = open('input.txt').read().strip().split('\n')
g1 = sorted([int(line.split()[0]) for line in f])
g2 = sorted([int(line.split()[1]) for line in f])

#Part 1
print(sum([abs(n1 - n2) for n1, n2 in zip(g1, g2)]))

#Part 2
print(sum(i * g2.count(i) for i in g1))