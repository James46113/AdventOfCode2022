temp_total = 0
highest = 0
sec_high = 0
third_high = 0
with open("Day#1input.txt", "r") as f:
    while True:
        try:
            temp= f.readline().strip()
            if temp != "":
                temp_total += int(temp)
            else:
                if third_high < temp_total:
                    if sec_high < temp_total:
                        if highest < temp_total:
                            third_high = sec_high
                            sec_high = highest
                            highest = temp_total
                        else:
                            third_high = sec_high
                            sec_high = temp_total
                    else:
                        third_high = temp_total
                temp_total=0
        except Exception:
            break
print(highest + sec_high + third_high)
