lines = [line.strip() for line in open("Day#7input.txt", "r").readlines()]
"""
currentDir = ""
parentDir = ""
currentPath = ""
inLS = False

class Folder:
    def __init__(self, name) -> None:
        self.folders = []
        self.files = []
        self.name = name
    
    def add_folder(self, child):
        self.folders.append(child)
        #print(self.folders)

    def add_file(self, size, file):
        self.files.append([file, int(size)])

    def get_total_size(self):
        total = 0
        print(self in self.folders)
        #try:
        #    self.folders.remove(self)
        #except ValueError:
        #    pass
        for file in self.files:
            total += file[1]
        print(len(self.folders))
        for folder in self.folders:
            total += folder.get_total_size()
        return total

    def __str__(self):
        folders = ""
        for folder in self.folders:
            folders += (str(folder) + ", ")   
        return "self: " + self.name + "\n" + "folders: " + folders

folders = []

for line in lines:
    if line[0] == "$":
        if line.split(" ")[1] == "cd":
            if line.split(" ")[-1] == "..":
                currentPath = "|".join(currentPath.split("|")[:-2]) + "|"
            else:
                currentPath += line.split(" ")[-1] + "|"
            currentDir = currentPath.split("|")[-2]
            
            if currentDir == "/":
                currentDir = "root"

            if len(currentPath.split("|")) >= 3:
                if currentPath.split("|")[-3] == "/":
                    parentDir = "root"
                else:
                    parentDir = currentPath.split("|")[-3]
            else:
                parentDir = "skip"
            #print("currentDir:", currentDir)
            #print("currentPath:", currentPath)
            #print("parentDir:", parentDir)
            try:if line.split(" ")[1] == "cd":
            if line.split(" ")[-1] == "..":
                currentPath = "|".join(currentPath.split("|")[:-2]) + "|"
            else:
                currentPath += line.split(" ")[-1] + "|"
            currentDir = currentPath.split("|")[-2]
            
            if currentDir == "/":
                currentDir = "root"

            if len(currentPath.split("|")) >= 3:
                if currentPath.split("|")[-3] == "/":
                    parentDir = "root"
                else:
                    parentDir = currentPath.split("|")[-3]
            else:
                parentDir = "skip"
            #print("currentDir:", currentDir)
            #print("currentPath:", currentPath)
            #print("parentDir:", parentDir)
            try:
                exec(f"{currentDir} == False")
            except NameError:
                exec(f"{currentDir} = Folder('{currentDir}')")
                exec(f"folders.append({currentDir})")
                #pr
                exec(f"{currentDir} == False")
            except NameError:
                exec(f"{currentDir} = Folder('{currentDir}')")
                exec(f"folders.append({currentDir})")
                #print(f"set {currentDir}")
            if parentDir != "skip":
                if parentDir != currentDir:
                    exec(f"{parentDir}.add_folder({currentDir})")
            #print(root)
    elif line[:3] != "dir":
        print(line)
        exec(f"{currentDir}.add_file(*line.split(' '))")

count = 0
print(len(folders))
for fold in folders:
    if fold.get_total_size() >= 10000:
        #print(fold.get_total_size())
        count += 1
print(count)
"""
from os import mkdir, getcwd, walk
from os.path import join
import sys
sys.setrecursionlimit(9999)
mkdir(join(getcwd(), "filesystem"))
currentPath= ""
for line in lines:
    print(line)
    if line[:3] == "dir":
        if currentPath == "//": currentPath = "/"
        mkdir(getcwd() + "/filesystem/" + join(currentPath, line[4:].strip()))
    elif line.split(" ")[1] == "cd":
        print("in cd")
        if line.split(" ")[-1] == "..":
            currentPath = "/".join(currentPath.split("/")[:-2]) + "/"
        else:
            currentPath += line.split(" ")[-1] + "/"
    elif line.split(" ")[1] == "ls": pass
    else:
        print(currentPath)
        with open(f"{getcwd()}/filesystem{currentPath}{line.split(' ')[0]}", "w"):
            pass

    #print(currentPath)
dirs = [directory for directory in walk("filesystem")]
big = 0
def get_size(data):
    global big
    total = 0
    path = data[0]
    curr_dirs = data[1]
    curr_files = data[2]
    for curr_dir in curr_dirs:
        total += get_size(path + "/" + curr_dir)
    for file in curr_files:
        total += int(file)
    if total > 10000:
        big += 1
    return total

print(get_size(dirs[0]))