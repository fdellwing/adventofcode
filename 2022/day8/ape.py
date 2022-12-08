with open("input.txt") as f:
    puzzle = []
    for line in f:
        if line != "\n":
            line = line.strip()
            row = []
            for tree in line:
                row.append(int(tree))
            puzzle.append(row)

# Transpose puzzle
puzzle_t = [list(x) for x in zip(*puzzle)]

# Part 1

visible = set()
for x, row in enumerate(puzzle):
    highest = -1
    for y, tree in enumerate(row):
        if tree > highest:
            highest = tree
            visible.add((x, y))

for x, row in enumerate(puzzle):
    highest = -1
    for y, tree in reversed(list(enumerate(row))):
        if tree > highest:
            highest = tree
            visible.add((x, y))

for y, row in enumerate(puzzle_t):
    highest = -1
    for x, tree in enumerate(row):
        if tree > highest:
            highest = tree
            visible.add((x, y))

for y, row in enumerate(puzzle_t):
    highest = -1
    for x, tree in reversed(list(enumerate(row))):
        if tree > highest:
            highest = tree
            visible.add((x, y))

print(len(visible))

# Part 2


def check_score(tree, x, y):
    score = 1
    count = 0
    for i in range(y + 1, len(puzzle[x])):
        count += 1
        if puzzle[x][i] >= tree:
            break

    score *= count
    count = 0

    for i in range(y - 1, -1, -1):
        count += 1
        if puzzle[x][i] >= tree:
            break

    score *= count
    count = 0

    for i in range(x + 1, len(puzzle_t[y])):
        count += 1
        if puzzle_t[y][i] >= tree:
            break

    score *= count
    count = 0

    for i in range(x - 1, -1, -1):
        count += 1
        if puzzle_t[y][i] >= tree:
            break

    score *= count

    return score


highest_scenic = 0
for x, row in enumerate(puzzle):
    for y, tree in enumerate(row):
        score = check_score(tree, x, y)
        if score > highest_scenic:
            highest_scenic = score

print(highest_scenic)
