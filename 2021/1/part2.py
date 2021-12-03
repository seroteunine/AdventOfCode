with open('adventofcode/2021/1/input.txt', 'r') as f:
    txt = [int(line) for line in f.readlines()]

increases = 0
for i in range(1, len(txt)-2):
    if sum(txt[i:i+3]) > sum(txt[i-1:i+2]):
        increases+=1
print(increases)