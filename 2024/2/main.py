f = [[int(x) for x in line.split()] for line in open('input.txt').read().strip().split('\n')]

def is_valid_sequence(sequence, incr):
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        if (diff < 0 and incr) or (diff > 0 and not incr) or abs(diff) > 3 or diff == 0:
            return False
    return True

def check_sequence_part1(sequence):
    if sequence[0] == sequence[1]:
        return False
    incr = sequence[0] < sequence[-1]
    return is_valid_sequence(sequence, incr)

def check_sequence_part2(sequence):
    if check_sequence_part1(sequence):
        return True
    for i in range(len(sequence)):
        test_sequence = sequence[:i] + sequence[i+1:]
        incr = test_sequence[0] < test_sequence[-1]
        valid = True
        j = 0
        while j < len(test_sequence) - 1:
            if not is_valid_sequence(test_sequence[j:j+2], incr):
                valid = False
                break
            j += 1
        if valid:
            return True 
    return False

print(sum(check_sequence_part1(seq) for seq in f))
print(sum(check_sequence_part2(seq) for seq in f))
