# Parse input
G, M = open('input.txt').read().strip().split('\n\n')
G = [[ch for ch in line] for line in G.split('\n')]
M = [ch for ch in M if ch != '\n']
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == '@':
            pos = (r, c)
            break

dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def make_step(r, c, rr, cc):
    global pos
    pos = (rr, cc)
    G[rr][cc] = '@'
    G[r][c] = '.'

def boxes_to_move(rr, cc, dr, dc):
    boxes = 1
    possible = False
    rr, cc = rr + dr, cc + dc
    while True:
        if G[rr][cc] == '#':
            return boxes, possible
        if G[rr][cc] == 'O':
            if possible:
                return boxes, possible
            boxes += 1
        if G[rr][cc] == '.':
            possible = True
        rr, cc = rr + dr, cc + dc

def move_boxes(r, c, dr, dc, boxes):
    rr, cc = r + dr, c + dc
    make_step(r, c, rr, cc)
    G[rr+dr*boxes][cc+dc*boxes] = 'O'
    
def make_move(move):
    r, c = pos
    dr, dc = dirs[move]
    rr, cc = r + dr, c + dc
    if G[rr][cc] == '.':
        make_step(r, c, rr, cc)
    if G[rr][cc] == 'O':
        boxes, possible = boxes_to_move(rr, cc, dr, dc)
        if possible:
            move_boxes(r, c, dr, dc, boxes)

for move in M:
    make_move(move)

# Part 1
t = sum(r * 100 + c for r in range(R) for c in range(C) if G[r][c] == 'O')
print(t)