from dijkstra import *

with open("input.txt") as f:
    lines = f.readlines()
    g = Graph(len(lines) * len(lines[0].strip()))
    dims = (len(lines), len(lines[0].strip()))

puzzle = []
indexes = []
index = 0

# Fill puzzle and index for later use
with open("input.txt") as f:
    for line in f:
        row = []
        index_row = []
        for c in line.strip():
            if c == "S":
                c = "a"
            row.append(c)
            index_row.append(index)
            index += 1
        puzzle.append(row)
        indexes.append(index_row)

index = 0
possible_start = []
end = 0

for x, row in enumerate(puzzle):
    for y, c in enumerate(row):
        # Start and End
        if c == "a":
            possible_start.append(index)
        elif c == "E":
            end = index

        # Neighbours
        neighbours = []
        if x > 0:
            neighbours.append((x - 1, y))
        if y > 0:
            neighbours.append((x, y - 1))
        if x < dims[0] - 1:
            neighbours.append((x + 1, y))
        if y < dims[1] - 1:
            neighbours.append((x, y + 1))

        # Add Edges
        for n in neighbours:
            n_i = indexes[n[0]][n[1]]
            if ord(str(puzzle[n[0]][n[1]])) - ord(str(puzzle[x][y])) <= 1:
                g.add_edge(index, n_i, 1)

        index += 1

possible_paths = []

for start in possible_start:
    print(f"Running {possible_start.index(start) + 1} of {len(possible_start)}")

    D = dijkstra(g, start)

    for vertex in range(len(D)):
        # Adjust offsets and print solution
        if vertex == end - 1:
            possible_paths.append(D[vertex] + 1)

    # Reset Graph for reuse
    g.visited = []

print()
print(min(possible_paths))
