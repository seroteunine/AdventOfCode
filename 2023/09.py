lines = open('09.txt').read().split('\n')

def diff(l):
    return [l[i+1] - l[i] for i in range(len(l) - 1)]

#Part 1
def addToLast(l):
    if all([l[0] == n for n in l]):
        return l[-1]
    return l[-1] + addToLast(diff(l))

#Part 2
def addToFirst(l):
    if all([l[0] == n for n in l]):
        return l[0]
    return l[0] - addToFirst(diff(l))
    
t1 = t2 = 0
for line in lines:
    line = [int(num) for num in line.split()]
    t1 += addToLast(line)
    t2 += addToFirst(line)
   
print(t1)
print(t2)