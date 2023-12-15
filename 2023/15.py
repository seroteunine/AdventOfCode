inp = open('15.txt').read()

#Part 1
t = 0
for string in inp.split(','):
    curr = 0
    for ch in string:
        curr += ord(ch)
        curr *= 17
        curr = curr % 256
    t += curr

print(t)

#Part 2