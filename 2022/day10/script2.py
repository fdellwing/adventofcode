with open("input.txt") as f:
    input = f.readlines()

to_add = 0
register = 1
wait = False
strengths = []
crt = [[] for _ in range(6)]
index = 0
crt_i = 0

for line in crt:
    for _ in range(40):
        line.append(".")

for cycle in range(1000):
    try:
        if crt_i == register or crt_i == register + 1 or crt_i == register + 2:
            crt[index][crt_i - 1] = "#"
    except IndexError:
        pass
    crt_i += 1
    if cycle in [39, 79, 119, 159, 199, 239]:
        index += 1
        crt_i = 0
    if wait:
        wait = False
        continue
    try:
        cmd = input.pop(0).strip()
    except IndexError:
        cmd = "noop"
        pass
    if to_add:
        register += to_add
        to_add = 0

    if cmd == "noop":
        continue
    to_add = int(cmd.split()[1])
    wait = True

for line in crt:
    print("".join(line))
