G = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".split('\n')
G = open('16.txt').read().split('\n')

R = len(G)
C = len(G[0])

energized = set()
splitted = set()

dirs = {'N': [-1,0], 'E': [0,1], 'S':[1,0], 'W':[0,-1]}

def followPath(dir, start):
    if (dir, start) in splitted:
        return
    splitted.add((dir, start))
    dr, dc = dirs[dir]
    rr, cc = start[0] + dr, start[1] + dc
    while 0 <= rr < R and 0 <= cc < C:
        energized.add((rr, cc))
        if dir == 'N':
            if G[rr][cc] == "\\":
                dir = 'W'
            elif G[rr][cc] == '/':
                dir = 'E'
            elif G[rr][cc] == '-':
                followPath('E', (rr, cc))
                followPath('W', (rr, cc))
                return
        elif dir == 'E':
            if G[rr][cc] == "\\":
                dir = 'S'
            elif G[rr][cc] == '/':
                dir = 'N'            
            elif G[rr][cc] == '|':
                followPath('N', (rr, cc))
                followPath('S', (rr, cc))
                return
        elif dir == 'S':
            if G[rr][cc] == "\\":
                dir = 'E'
            elif G[rr][cc] == '/':
                dir = 'W'
            elif G[rr][cc] == '-':
                followPath('E', (rr, cc))
                followPath('W', (rr, cc))
                return
        elif dir == 'W':
            if G[rr][cc] == "\\":
                dir = 'N'
            elif G[rr][cc] == '/':
                dir = 'S'
            elif G[rr][cc] == '|':
                followPath('N', (rr, cc))
                followPath('S', (rr, cc))
                return
        dr, dc = dirs[dir]
        rr, cc = rr + dr, cc + dc

followPath('S', (0,0))
print(len(energized) + 1)

m = 0
for i in range(2):
    for c in range(C):
        energized = set()
        splitted = set()
        followPath('N' if i else 'S', (i * R, c))
        m = max(m, len(energized))

for i in range(2):
    for r in range(R):
        energized = set()
        splitted = set()
        followPath('W' if i else 'E', (r, i * C))
        m = max(m, len(energized))

print(m)



