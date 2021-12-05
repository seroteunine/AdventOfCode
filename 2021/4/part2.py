import itertools
txt = open('adventofcode/2021/4/input.txt', 'r').read().split('\n')
nums = [num for num in txt[0].split(',')]
boards = [[row.split() for row in txt[i:i+5]] for i in range(2, len(txt), 6)]

def checkWin(numlist, matrix):
    for i in range(len(matrix)):
        if all(elem in numlist for elem in matrix[i]) or all(elem in numlist for elem in [row[i] for row in matrix]):
            return True

length = len(nums)
numlist = nums[:]
found = False
while not found:
    for board in boards:
        if not checkWin(numlist, board):
            print(sum([int(num) for num in set(list(itertools.chain.from_iterable(board))).difference(nums[:length+1])]) * int(nums[length]))
            found = True
    length -= 1
    numlist.pop(length)
