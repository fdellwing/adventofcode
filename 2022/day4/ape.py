with open("input.txt") as f:
    total = 0
    partial = 0
    for line in f:
        if line != "\n":
            a, b = line.strip().split(',')
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")
            a = [x for x in range(int(a1), int(a2) + 1)]
            b = [x for x in range(int(b1), int(b2) + 1)]
            c = set(a).intersection(b)
            # Part 1
            if len(a) == len(c) or len(b) == len(c):
                total += 1
            # Part 2
            if len(c) > 0:
                partial += 1

print(total)
print(partial)
