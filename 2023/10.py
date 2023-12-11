G = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""".split('\n')

G = open('10.txt').read().split('\n')

R = len(G)
C = len(G[0])
coords = {'N': [], 'E': [], 'S': [], 'W':[]}

DIR = {'N':(-1,0), 'E': (0,1), 'S': (1,0), 'W':(0,-1)}

def tryMove(path, dir, current, steps):
    path.append(tuple(current))
    steps += 1
    rr = current[0] + DIR[dir][0]
    cc = current[1] + DIR[dir][1]
    if 0 <= rr < R and 0 <= cc < C:
        next = G[rr][cc]
        if next == 'S':
            return (dir, True, steps)
        match dir:
            case 'N':
                if next == '7':
                    dir = 'W'
                elif next == 'F':
                    dir = 'E'
                elif next == '|':
                    dir = 'N'
                else:
                    return (dir, True, 0)
            case 'E':
                if next == '-':
                    dir = 'E'
                elif next == 'J':
                    dir = 'N'
                elif next == '7':
                    dir = 'S'
                else:
                    return (dir, True, 0)
            case 'S':
                if next == '|':
                    dir = 'S'
                elif next == 'J':
                    dir = 'W'
                elif next == 'L':
                    dir = 'E'
                else:
                    return (dir, True, 0)
            case 'W':
                if next == 'L':
                    dir = 'N'
                elif next == 'F':
                    dir = 'S'
                elif next == '-':
                    dir = 'W'
                else:
                    return (dir, True, 0)
        current[0], current[1] = rr, cc
    return (dir, dead, steps)
     
def PolygonArea(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            start = (r, c)
            for dir in ['N', 'E', 'S', 'W']:
                current = [r, c]
                dead = False
                steps = 0
                path = []
                while not dead:
                    dir, dead, steps = tryMove(path, dir, current, steps)
                print(steps // 2)
                if steps:
                    print(PolygonArea(path) + 1 - 0.5 * len(path))


