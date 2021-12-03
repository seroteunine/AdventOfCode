with open('adventofcode/2021/1/input.txt', 'r') as f:
    txt = [int(line) for line in f.readlines()]

increases = 0
for i in range(1, len(txt)):
    if txt[i] > txt[i-1]:
        increases += 1
print(increases)