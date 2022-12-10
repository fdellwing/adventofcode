with open("input.txt") as f:
    input = f.readlines()

to_add = 0
register = 1
wait = False
strengths = []

for cycle in range(1000):
    if cycle in [20, 60, 100, 140, 180, 220]:
        strengths.append(cycle * register)
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

print(sum(strengths))
