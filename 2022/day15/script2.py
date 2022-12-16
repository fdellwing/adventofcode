from scipy.spatial import distance
import re

r = re.compile(r'.*?([0-9-]+).*?([0-9-]+).*?([0-9-]+).*?([0-9-]+)')

devices = []
possible_points = set()
max_i = 4_000_000

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


def generate_square_radius(x, y, r):
    j = y
    for i in range(x + r, x - 1, -1):
        if 0 <= i <= max_i and 0 <= j <= max_i:
            possible_points.add((i, j))
        j += 1
    j = y
    for i in range(x + r, x - 1, -1):
        if 0 <= i <= max_i and 0 <= j <= max_i:
            possible_points.add((i, j))
        j -= 1
    j = y
    for i in range(x - r, x + 1):
        if 0 <= i <= max_i and 0 <= j <= max_i:
            possible_points.add((i, j))
        j += 1
    j = y
    for i in range(x - r, x + 1):
        if 0 <= i <= max_i and 0 <= j <= max_i:
            possible_points.add((i, j))
        j -= 1


def check_possible_beacon(x, y):
    for device in devices:
        s_x, s_y = device[0]
        dis = device[2]
        new = distance.cityblock([s_x, s_y, 0], [x, y, 0])
        if new <= dis:
            return False
    return True


for device in devices:
    s_x, s_y = device[0]
    dis = device[2] + 1
    generate_square_radius(s_x, s_y, dis)

for x, y in possible_points:
    if check_possible_beacon(x, y):
        break

print(x, y)
print(x * 4_000_000 + y)