bags = [line.strip() for line in open("Day#3input.txt", "r").readlines()]
loletters = list("qwertyuiopasdfghjklzxcvbnm")
loletters.sort()
upletters = list("QWERTYUIOPASDFGHJKLZXCVBNM")
upletters.sort()
letters = loletters + upletters
score = 0
for ind in range(0, len(bags), 3):
    for letter in bags[ind]:
        if letter in bags[ind+1] and letter in bags[ind+2]:
            score += letters.index(letter) +1
            break
print(score)
