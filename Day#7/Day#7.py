from os import mkdir, getcwd, listdir, remove
from os.path import join, isfile
import shutil
try:
    shutil.rmtree(join(getcwd(), "filesystem"))
except FileNotFoundError:
    pass
mkdir(join(getcwd(), "filesystem"))
lines = [line.strip() for line in open("Day#7input.txt", "r").readlines()]
currentPath= ""
for line in lines:
    if line[:3] == "dir":
        if currentPath == "//": currentPath = "/"
        mkdir(getcwd() + "/filesystem/" + join(currentPath, line[4:].strip()))
    elif line.split(" ")[1] == "cd":
        if line.split(" ")[-1] == "..":
            currentPath = "/".join(currentPath.split("/")[:-2]) + "/"
        else:
            currentPath += line.split(" ")[-1] + "/"
    elif line.split(" ")[1] == "ls": pass
    else:
        with open(f"{getcwd()}/filesystem{currentPath}{line.split(' ')[0]}", "w"):
            pass

dir_sizes = []
size_of_small_dirs = 0
def get_size(path: str) -> int:
    global size_of_small_dirs, dir_sizes
    size = 0
    contents = listdir(f"{getcwd()}/{path}")
    files = [file for file in contents if isfile(join(f"{getcwd()}/{path}", file))]
    dirs = [directory for directory in contents if not isfile(join(f"{getcwd()}/{path}", directory))]
    for directory in dirs:
        size += get_size(path + "/" + directory)
    for file in files:
        size += int(file)
    if size <= 100000:
        size_of_small_dirs += size
    dir_sizes.append(size)
    return size

unused_space = 70000000 - get_size("filesystem")
print("ANSWER TO PART 1:", size_of_small_dirs)
diff = 70000000
closest = 0
for dir_size in dir_sizes:
    #print(30000000 - unused_space - dir_size)
    temp_dif = (unused_space + dir_size) - 30000000
    if 0 <= temp_dif < diff:
        diff = temp_dif
        closest = dir_size
print("ANSWER TO PART 2:", closest)
