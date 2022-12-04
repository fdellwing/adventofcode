with open("input.txt") as f:
    elfs = []
    current = 0
    for line in f.readlines():
        if line == "\n":
            elfs.append(current)
            current = 0
        else:
            current += int(line)

# Part 1
print(max(elfs))

# Part 2
print(sum(sorted(elfs, reverse=True)[:3]))
