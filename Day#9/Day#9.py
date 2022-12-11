visited = []
hx = 0
hy = 0
tx = 0
ty = 0
moves = [[character.strip() for character in inst.split(" ")] for inst in open("Day#9input.txt", "r").readlines()]
for move in moves:
    if move[0] == "U":
        hy += int(move[1])
    elif move[0] == "D":
        hy -= int(move[1])
    elif move[0] == "L":
        hx -= int(move[1])
    elif move[0] == "R":
        hx += int(move[1])
    if -1 > hx - tx or hx - tx > 1:
        pass
    print(move, hx, hy)