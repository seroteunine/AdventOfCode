f = open('input.txt').read().strip().split('\n')
f = [[list(map(int, x.split())) if i else int(x) for i, x in enumerate(line.split(': '))] for line in f]

# Part 1
def is_valid(exp, inp):
    if len(inp) == 1:
        return exp == inp[0]
    mltp = [inp[0] * inp[1]] + inp[2:]
    pls = [inp[0] + inp[1]] + inp[2:]
    return is_valid(exp, mltp) or is_valid(exp, pls)

t = sum((exp for exp, inp in f if is_valid(exp, inp)))
print(t) 

# Part 2
def is_valid(exp, inp):
    if len(inp) == 1:
        return exp == inp[0]
    mltp = [inp[0] * inp[1]] + inp[2:]
    pls = [inp[0] + inp[1]] + inp[2:]
    concat = [int(str(inp[0]) + str(inp[1]))] + inp[2:]
    return is_valid(exp, mltp) or is_valid(exp, pls) or is_valid(exp, concat)

t = sum((exp for exp, inp in f if is_valid(exp, inp)))
print(t) 