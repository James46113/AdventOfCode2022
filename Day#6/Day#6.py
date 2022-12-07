letters = []
is_same = False
for ind, letter in enumerate(open("Day#6input.txt", "r").read()):
    is_same = False
    letters.append(letter)
    if len(letters) == 15:
        letters.pop(0)
        for let in letters:
            if letters.count(let) == 1:
                continue
            else:
                is_same = True
                print("is same")
                print(letters)
                break
        if not is_same:
            print(letters)
            print(ind+1)
            break