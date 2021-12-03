txt = open('adventofcode/2021/3/input.txt', 'r').read().split('\n')

#Return a new list filter on bit in given position
def filterList(lst, pos, flag): #if flag is set to true, return a list with most common, other return with least common
    ones, zeroes = [], []
    for num in lst:
        if num[pos] == '1':
            ones.append(num)
        else:
            zeroes.append(num)
    if flag:
        return ones if len(ones) >= len(zeroes) else zeroes
    else:
        return ones if len(ones) < len(zeroes) else zeroes

oxygen = co2 = txt
#Oxygen
i = 0
while len(oxygen) != 1:
    oxygen = filterList(oxygen, i, True)
    i += 1
dec_oxygen = int(oxygen[0], 2)

#CO2
i = 0
while len(co2) != 1:
    co2 = filterList(co2, i, False)
    i += 1
dec_co2 = int(co2[0], 2)

print(dec_co2 * dec_oxygen)