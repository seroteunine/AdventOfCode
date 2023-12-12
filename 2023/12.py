import re

lines = open('12.txt').read().split('\n')

def isValid(chars, nums):
    matches = re.findall('#+', chars)
    if len(matches) != len(nums):
        return False
    for i, v in enumerate(nums):
        if len(matches[i]) != v:
            return False
    return True

def fillIn(chars, nums):
    question_mark_positions = [i for i, ch in enumerate(chars) if ch == '?']
    n = len(question_mark_positions)
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        replacement = binary.replace('0', '.').replace('1', '#')
        result_chars = list(chars)
        for pos, rep_char in zip(question_mark_positions, replacement):
            result_chars[pos] = rep_char
        result = ''.join(result_chars)
        yield isValid(result, nums)
    
t = 0
for line in lines:
    chars, nums = line.split()
    nums = [int(num) for num in nums.split(',')] 
    t += sum(fillIn(chars, nums))

print(t)