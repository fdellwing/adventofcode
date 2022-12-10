# This logic was written by SREagle#2162
def ensure_proximity(xT, yT, xH, yH):
    if abs(xH - xT) > 1 or abs(yH - yT) > 1:
        return [xT + (xH - xT) / max(abs(xH - xT), 1),
                yT + (yH - yT) / max(abs(yH - yT), 1)]
    else:
        return [xT, yT]


with open("input.txt") as f:
    tails = set()
    tail = [[1, 1] for _ in range(9)]
    head = [1, 1]
    for line in f:
        if line != "\n":
            direction, steps = line.strip().split()
            steps = int(steps)
            if direction == "R":
                for _ in range(head[0], head[0] + steps):
                    head[0] += 1
                    tail[0] = ensure_proximity(tail[0][0], tail[0][1], head[0], head[1])
                    for i in range(1, len(tail)):
                        tail[i] = ensure_proximity(tail[i][0], tail[i][1], tail[i - 1][0], tail[i - 1][1])
                    tails.add(tuple(tail[8]))
            elif direction == "U":
                for _ in range(head[1], head[1] + steps):
                    head[1] += 1
                    tail[0] = ensure_proximity(tail[0][0], tail[0][1], head[0], head[1])
                    for i in range(1, len(tail)):
                        tail[i] = ensure_proximity(tail[i][0], tail[i][1], tail[i - 1][0], tail[i - 1][1])
                    tails.add(tuple(tail[8]))
            elif direction == "L":
                for _ in range(head[0], head[0] - steps, -1):
                    head[0] -= 1
                    tail[0] = ensure_proximity(tail[0][0], tail[0][1], head[0], head[1])
                    for i in range(1, len(tail)):
                        tail[i] = ensure_proximity(tail[i][0], tail[i][1], tail[i - 1][0], tail[i - 1][1])
                    tails.add(tuple(tail[8]))
            elif direction == "D":
                for _ in range(head[1], head[1] - steps, -1):
                    head[1] -= 1
                    tail[0] = ensure_proximity(tail[0][0], tail[0][1], head[0], head[1])
                    for i in range(1, len(tail)):
                        tail[i] = ensure_proximity(tail[i][0], tail[i][1], tail[i - 1][0], tail[i - 1][1])
                    tails.add(tuple(tail[8]))

print(len(tails))
