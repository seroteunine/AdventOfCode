from functools import cache

stones = [int(i) for i in open('input.txt').readlines()[1].split()]

@cache
def iterate(N, stn):
    if N == 0:
        return 1
    if stn == 0:
        return iterate(N-1, 1)
    stn_str = str(stn)
    lngth = len(stn_str)
    if lngth & 1:
        return iterate(N-1, stn * 2024)
    else:
        half = lngth // 2
        return iterate(N-1,int(stn_str[:half])) + iterate(N-1,int(stn_str[half:]))

# Part 1
N = 25
t = sum((iterate(N, stone) for stone in stones))
print(t)

# Part 2
N = 75
t = sum((iterate(N, stone) for stone in stones))
print(t)