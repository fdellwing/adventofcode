def ensure_proximity():
    global last_direction
    if tail[0] == head[0] and tail[1] == head[1]:
        return
    elif abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
        return
    else:
        if direction == "R":
            tail[0] += 1
            if last_direction and last_direction != direction:
                tail[1] = head[1]
                last_direction = direction
        elif direction == "U":
            tail[1] += 1
            if last_direction and last_direction != direction:
                tail[0] = head[0]
                last_direction = direction
        elif direction == "L":
            tail[0] -= 1
            if last_direction and last_direction != direction:
                tail[1] = head[1]
                last_direction = direction
        elif direction == "D":
            tail[1] -= 1
            if last_direction and last_direction != direction:
                tail[0] = head[0]
                last_direction = direction


with open("input.txt") as f:
    tails = set()
    tail = [1, 1]
    head = [1, 1]
    last_direction = None
    for line in f:
        if line != "\n":
            direction, steps = line.strip().split()
            steps = int(steps)
            if direction == "R":
                for i in range(head[0], head[0] + steps):
                    head[0] += 1
                    ensure_proximity()
                    tails.add(tuple(tail))
            elif direction == "U":
                for i in range(head[1], head[1] + steps):
                    head[1] += 1
                    ensure_proximity()
                    tails.add(tuple(tail))
            elif direction == "L":
                for i in range(head[0], head[0] - steps, -1):
                    head[0] -= 1
                    ensure_proximity()
                    tails.add(tuple(tail))
            elif direction == "D":
                for i in range(head[1], head[1] - steps, -1):
                    head[1] -= 1
                    ensure_proximity()
                    tails.add(tuple(tail))
            last_direction = direction

print(len(tails))
