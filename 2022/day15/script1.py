from scipy.spatial import distance
import re

r = re.compile(r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+)')

devices = []

with open("input.txt") as f:
    for line in f:
        if line.strip() != "":
            res = r.findall(line)[0]
            s_x = int(res[0])
            s_y = int(res[1])
            b_x = int(res[2])
            b_y = int(res[3])
            device = (
                (s_x, s_y),
                (b_x, b_y),
                distance.cityblock([s_x, s_y, 0], [b_x, b_y, 0])
            )
            devices.append(device)


def check_possible_beacon(x, y):
    for device in devices:
        s_x, s_y = device[0]
        b_x, b_y = device[1]
        if b_x == x and b_y == y:
            return True
        dis = device[2]
        new = distance.cityblock([s_x, s_y, 0], [x, y, 0])
        if new <= dis:
            return False
    return True


blocked = 0

for i in range(-5_000_000, 5_000_000):
    if not check_possible_beacon(i, 2_000_000):
        blocked += 1

print(blocked)