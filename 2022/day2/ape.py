# Part 1

with open("input.txt") as f:
    score = 0
    for line in f.readlines():
        if line != "\n":
            a, b = line.split()
            a = ord(a)
            b = ord(b) - 23
            # Draw
            if b == a:
                score += 3
            # Rock vs Paper
            elif a == 65 and b == 66:
                score += 6
            # Paper vs Scissor
            elif a == 66 and b == 67:
                score += 6
            # Scissor vs Rock
            elif a == 67 and b == 65:
                score += 6
            score += b - 64

print(score)

# Part 2

with open("input.txt") as f:
    score = 0
    for line in f.readlines():
        if line != "\n":
            a, b = line.split()
            a = ord(a)
            b = ord(b)
            # Loose
            if b == 88:
                if a != 65:
                    b = a - 1
                else:
                    b = a + 2
            # Draw
            elif b == 89:
                b = a
            # Win
            else:
                if a != 67:
                    b = a + 1
                else:
                    b = a - 2
            # Draw
            if b == a:
                score += 3
            # Rock vs Paper
            elif a == 65 and b == 66:
                score += 6
            # Paper vs Scissor
            elif a == 66 and b == 67:
                score += 6
            # Scissor vs Rock
            elif a == 67 and b == 65:
                score += 6
            score += b - 64

print(score)
