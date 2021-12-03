txt = open('adventofcode/2021/3/input.txt', 'r').read().split('\n')

gamma = epsilon = ''
for i in range(len(txt[0])):
    zeroes = ones = 0
    for j in range(len(txt)):
        if txt[j][i] == '0':
            zeroes += 1
        else:
            ones += 1
    gamma = gamma + '0' if zeroes > ones else gamma + '1'
    epsilon = epsilon + '0' if zeroes < ones else epsilon + '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)

