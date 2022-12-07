class Stack:
    def __init__(self, start_boxes: list):
        self.boxes = start_boxes
    
    def remove(self, count: int):
        self.boxes, ret = self.boxes[:-count], self.boxes[-count:]
        return ret

    def add(self, itemList: list):
        for item in itemList:
            self.boxes.append(item)

    def get_top(self):
        if len(self.boxes) != 0:
            return self.boxes[-1]
        return ""

    def __str__(self):
        return str(self.boxes)
    
def move(count: int, source: Stack, destination: Stack, one_at_a_time: bool):
    if one_at_a_time:
        print(count)
        print(source)
        print(destination)
        for _ in range(count):
            removed = source.remove(1)
            #print("REM:", removed)
            destination.add(removed)
    else:
        destination.add(source.remove(count))

def printStacks():
    for stack in stacks:
        print(stack.boxes)

stacks= [Stack(["H", "B", "V", "W", "N", "M", "L", "P"]), 
         Stack(["M", "Q", "H"]), 
         Stack(["N", "D", "B", "G", "F", "Q", "M", "L"]), 
         Stack(["Z", "T", "F", "Q", "M", "W", "G"]),
         Stack(["M", "T", "H", "P"]),
         Stack(["C", "B", "M", "J", "D", "H", "G", "T"]),
         Stack(["M", "N", "B", "F", "V", "R"]),
         Stack(["P", "L", "H", "M", "R", "G", "S"]),
         Stack(["P", "D", "B", "C", "N"])]

for line in [line.strip() for line in open("Day#5input.txt", "r").readlines()]:
    printStacks()
    split = line.split(" ")
    count = int(split[1])
    source = int(split[3])-1
    destination = int(split[5])-1
    move(count=count, source=stacks[source], destination=stacks[destination], one_at_a_time=False)
    print(count, source, destination)
    printStacks()
    #input()

finalResult = ""
for stack in stacks:
    finalResult += stack.get_top()
print(finalResult)