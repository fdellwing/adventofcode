puzzle = [["." for _ in range(1000)] for _ in range(200)]

with open("input.txt") as f:
    for line in f:
        row = line.strip().split(" -> ")
        last_coord = ()
        for coord in row:
            x, y = coord.split(",")
            x = int(x)
            y = int(y)
            if last_coord:
                p_x, p_y = last_coord
                if x == p_x:
                    if y < p_y:
                        for i in range(y, p_y + 1):
                            puzzle[i][x] = "#"
                    elif p_y < y:
                        for i in range(p_y, y + 1):
                            puzzle[i][x] = "#"
                elif y == p_y:
                    if x < p_x:
                        for i in range(x, p_x + 1):
                            puzzle[y][i] = "#"
                    elif p_x < x:
                        for i in range(p_x, x + 1):
                            puzzle[y][i] = "#"
            last_coord = (x, y)

highest = 0
for i, row in enumerate(puzzle):
    if "#" in row:
        highest = i

for i, _ in enumerate(puzzle[highest + 2]):
    puzzle[highest + 2][i] = "#"


def simulate_fall():
    y = 500
    for x in range(1, len(puzzle)):
        if puzzle[x][y] == ".":
            puzzle[x][y] = "o"
            puzzle[x - 1][y] = "."
        elif puzzle[x][y] == "o" or puzzle[x][y] == "#":
            if puzzle[x][y - 1] == ".":
                puzzle[x][y - 1] = "o"
                puzzle[x - 1][y] = "."
                y -= 1
            elif puzzle[x][y + 1] == ".":
                puzzle[x][y + 1] = "o"
                puzzle[x - 1][y] = "."
                y += 1
            else:
                break
        else:
            break
    if x == 1:
        return False
    puzzle[0][500] = "+"
    return True


puzzle[0][500] = "+"

for index in range(100_000):
    if not simulate_fall():
        print(index + 1)
        break

for i, row in enumerate(puzzle):
    #print(row)
    pass
