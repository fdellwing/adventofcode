# Part 1

with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        if line != "\n":
            a = line[:len(line)//2]
            b = line[len(line)//2:]
            c = ''.join(set(a).intersection(b))
            if c <= "Z":
                total += ord(c) - 38
            else:
                total += ord(c) - 96

print(total)

# Part 2

with open("input.txt") as f:
    total = 0
    i = 0
    lines = []
    for line in f.readlines():
        if line != "\n":
            i = i + 1
            lines.append(line.strip())

            if i == 3:
                c = ''.join(set(lines[0]).intersection(lines[1]))
                c = ''.join(set(c).intersection(lines[2]))
                if c <= "Z":
                    total += ord(c) - 38
                else:
                    total += ord(c) - 96

                i = 0
                lines = []

print(total)
