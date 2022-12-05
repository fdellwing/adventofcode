import re

m = re.compile(r".*?(\d+).*?(\d+).*?(\d+)")

# Part 1

with open("input.txt") as f:
    setup = True
    puzzle = {}
    for line in f:
        if setup and "1" not in line:
            i = 0
            for _ in range(len(line)):
                try:
                    if not i // 4 in puzzle:
                        puzzle[i // 4] = []
                    if line[i] == " " and line[i + 1] == " ":
                        i += 4
                    elif line[i] == "[":
                        puzzle[i // 4].append(line[i + 1])
                        i += 4
                    else:
                        i += 1
                except IndexError:
                    pass
        elif "move" in line:
            todo = m.findall(line)[0]
            for _ in range(int(todo[0])):
                popped = puzzle[int(todo[1]) - 1].pop(0)
                puzzle[int(todo[2]) - 1].insert(0, popped)
        else:
            setup = False

try:
    for item in puzzle.values():
        print(item[0], end="")
except IndexError:
    pass

print("")

# Part 2

with open("input.txt") as f:
    setup = True
    puzzle = {}
    for line in f:
        if setup and "1" not in line:
            i = 0
            for _ in range(len(line)):
                try:
                    if not i // 4 in puzzle:
                        puzzle[i // 4] = []
                    if line[i] == " " and line[i + 1] == " ":
                        i += 4
                    elif line[i] == "[":
                        puzzle[i // 4].append(line[i + 1])
                        i += 4
                    else:
                        i += 1
                except IndexError:
                    pass
        elif "move" in line:
            todo = m.findall(line)[0]
            popped = []
            for _ in range(int(todo[0])):
                popped.append(puzzle[int(todo[1]) - 1].pop(0))
            popped.reverse()
            for item in popped:
                puzzle[int(todo[2]) - 1].insert(0, item)
        else:
            setup = False

try:
    for item in puzzle.values():
        print(item[0], end="")
except IndexError:
    pass
