lines = open('06.txt').read().split('\n')

times = [int(num) for num in lines[0].split()[1:]]
distances = [int(num) for num in lines[1].split()[1:]]

print(times, distances)

total = 1
for i, time in enumerate(times):
    dist = distances[i]
    faster = 0
    for j in range(1, time):
        result = j * (time - j)
        if result > dist:
            faster += 1
    total *= faster

print(total)

lines = open('06.txt').read().split('\n')

time, distance = '', ''
for i, num in enumerate(lines[0].split()[1:]):
    time += num.strip()
    distance += lines[1].split()[i+1].strip()
time = int(time)
distance = int(distance)

possible = 0
for j in range(1, time):
    result = j * (time -j)
    if result > distance:
        possible += 1

print(possible)