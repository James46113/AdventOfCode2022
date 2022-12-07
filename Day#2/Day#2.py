with open("Day#2input.txt", "r") as f:
    lines = [line.strip().split(" ") for line in f.readlines()]
score = 0
for line in lines:
    if line[1] == "Y":
        score += 3
        if line[0] == "A":
            choice = "X"
        elif line[0] == "B":
            choice = "Y"
        else:
            choice = "Z"
    elif line[1] == "Z":
        score += 6
        if line[0] == "A":
            choice = "Y"
        elif line[0] == "B":
            choice = "Z"
        else:
            choice = "X"
    else:
        if line[0] == "A":
            choice = "Z"
        elif line[0] == "B":
            choice = "X"
        else:
            choice = "Y"
    if choice == "X":
        score += 1
    if choice == "Y":
        score += 2
    if choice == "Z":
        score += 3
        
print(score)
# A = rock
# B = paper
# C = scissors
# X = rock
# Y = paper
# Z = scissors
