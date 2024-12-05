f = open('input.txt').read().strip().split('\n')
g1 = [line.split()[0] for line in f]
g2 = [line.split()[1] for line in f]

t = 0
g1 = sorted(map(int, g1))
g2 = sorted(map(int, g2))
for n1, n2 in zip(g1, g2):
    t += abs(int(n1) - int(n2))

print(t)

#Part 2
g1, g2 = [], []
for line in f:
    g1.append(line.split()[0])
    g2.append(line.split()[1])

t = 0
for i in g1:
    sim = int(i) * g2.count(i)
    t += sim

print(t)