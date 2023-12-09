lines = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

lines = open('05.txt').read()

blocks = [block for block in lines.split('\n\n')]
seeds = [int(num) for num in blocks[0].split(':')[1].split()]
maps = [[[int(num) for num in str.split()] for str in block.split('\n')[1:]] for block in blocks[1:]]

# Part 1
def transform(block, num):
    for range_ in block:
        if range_[1] <= num < range_[1] + range_[2]:
            return num + (range_[0] - range_[1])
    return num

locations = []
for seed in seeds:
    current = seed
    for map in maps:
        current = transform(map, current)
    locations.append(current)

print(min(locations))

# #Part 2
seeds = [int(num) for num in blocks[0].split(':')[1].split()]
ranges = []
s = 0
while s < len(seeds):
    ranges.append([seeds[s], seeds[s+1]])
    s += 2

def transform(block, R):
    result = []
    for mapping in block:
        remainder = []
        while R:
            (start, end) = R.pop()
            dest, src, size = mapping
            before = (start,min(end,src))
            inter = (max(start, src), min(src+size, end))
            after = (max(src + size, start), end)
            if before[1]>before[0]:
                remainder.append(before)
            if inter[1]>inter[0]:
                result.append((inter[0]-src+dest, inter[1]-src+dest))
            if after[1]>after[0]:
                remainder.append(after)
        R = remainder
    return result + R

locations = []
for start, size in ranges:
    R = [(start, start + size)]
    for map in maps:
        R = transform(map, R)
    locations.append(min(pair[0] for pair in R))

print(min(locations))
