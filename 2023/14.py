G = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split('\n')
G = open('14.txt').read().split('\n')
G = [[ch for ch in row] for row in G]

R = len(G)
C = len(G[0])

def shiftNord(G):
    for r in range(R):
        for c in range(C):
            if G[r][c] == 'O':
                curr, rr = r, r - 1
                while 0 <= rr and G[rr][c] == '.':
                    G[rr][c] = 'O'
                    G[curr][c] = '.'
                    curr, rr = rr, rr - 1

for _ in range(350):
    for __ in range(4):
        shiftNord(G)
        G = [list(col) for col in zip(*reversed(G))]
    t = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == 'O':
                t += R - r
    print(t)