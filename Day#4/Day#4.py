pairs = [[list(range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1)), list(range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1))] for pair in [line.strip().split(",") for line in open("Day#4input.txt", "r").readlines()]]
#pairs = [line.strip().split(',') for line in open('Dec4input.txt', 'r').readlines()]
num = 0
num2 = 0
cont = False
#print(len(pairs))
#print(pairs)
for pair in pairs:
	a = pair[0]
	b = pair[1]
#	b = [1, 2, 3, 4]
	#a = [2, 3]
	a_in_b = True
	b_in_a = True
	for numa in a:
		if not numa in b:
			a_in_b = False
		else:
			num2 += 1
			cont = True
			break
	if cont:
		continue
	for numb in b:
		if not numb in a:
			b_in_a = False
		else:
			num2 += 1
			break
	
	if b_in_a or a_in_b:
		num += 1
	
	#print(num, pairs.index(pair))		
print(num, num2)
