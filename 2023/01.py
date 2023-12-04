lines = open('01.txt').readlines()

def getNumFromLine(line):
    first = last = None
    for c in line:
        if c.isdigit():
            if not first:
                first = c
            last = c
    return int(first + last) 

total = sum([getNumFromLine(line) for line in lines])
print(total)

#P2
numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,'eight': 8, 'nine': 9}

def getNumFromLine2(line):
    first = last = None
    for i, c in enumerate(line):
        for num in numbers.keys():
            if line[i:].startswith(num):
                if not first:
                    first = str(numbers[num])
                last = str(numbers[num])
    return int(first + last)

total = sum([getNumFromLine2(line) for line in lines])
print(total)
