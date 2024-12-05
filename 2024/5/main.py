from functools import cmp_to_key

f1, f2 = open('input.txt').read().strip().split('\n\n')

f1 = [[int(y) for y in x.split('|')] for x in f1.split('\n')]
f2 = [[int(y) for y in x.split(',')] for x in f2.split('\n')]
updates_wrong = []

def check_valid(update):
    for p1, p2 in f1:
        if p1 in update and p2 in update:
            if update.index(p1) > update.index(p2):
                updates_wrong.append(update)
                return False
    return True

#Part 1
print(sum([update[len(update) // 2] for update in f2 if check_valid(update)]))

#Part 2
def compare(i1, i2):
    if [i2, i1] in f1:
        return -1
    if [i1, i2] in f1:
        return 1


print(sum([sorted(update, key=cmp_to_key(compare))[len(update) // 2] for update in updates_wrong]))