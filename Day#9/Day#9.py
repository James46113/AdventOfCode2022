visited = []
hx = 0
hy = 0
tx = 0
ty = 0
moves = [[character.strip() for character in inst.split(" ")] for inst in open("Day#9input.txt", "r").readlines()]

def move_tail():
    global hx, hy, tx, ty
    near = False
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0):
                if tx + x == hx and ty + y == hy:
                    near = True
                    break
        if near:
            break
    if not near:
        if (hx - tx == -2 and hy - ty == 1) or (hx - tx == -1 and hy - ty == 2):
            tx -= 1
            ty += 1
        elif (hx - tx == 2 and hy - ty == 1) or (hx - tx == 1 and hy - ty == 2):
            tx += 1
            ty += 1
        elif (hx - tx == -2 and hy - ty == -1) or (hx - tx == -1 and hy - ty == -2):
            tx -= 1
            ty -= 1
        elif (hx - tx == 2 and hy - ty == -1) or (hy - ty == 1 and hy - ty == -2):
            tx += 1
            ty -= 1
        elif hx - tx == 2:
            tx += 1
        elif hx - tx == -2:
            tx -= 1
        elif hy - ty == 2:
            ty += 1
        elif hy - ty == -2:
            ty -= 1
    if (tx, ty) not in visited:
        visited.append((tx, ty))
    return [tx, ty]

test_moves = [["R", "4"], ["U", "4"], ["L", "3"], ["D", "1"]]
hx += 2
assert move_tail() == [1, 0]
hy += 2
assert move_tail() == [2, 1]

hx = 0
hy = 0

for move in moves:
    if move[0] == "U":
        for _ in range(int(move[1])):
            hy += 1
            move_tail()
    elif move[0] == "D":
        for _ in range(int(move[1])):
            hy -= 1
            move_tail()
    elif move[0] == "L":
        for _ in range(int(move[1])):
            hx -= 1
            move_tail()
    elif move[0] == "R":
        for _ in range(int(move[1])):
            hx += 1
            move_tail()
    if -1 > hx - tx:
        tx -= 1
    elif hx - tx > 1:
        tx += 1
    print(move, hx, hy, tx, ty)
print(len(visited))
for vis in visited:
    if visited.count(vis) > 1:
        print("bad")
print(visited)