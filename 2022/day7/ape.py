from typing import Dict

with open("input.txt") as f:
    tree = {"/": {}}
    cwd = tree
    dict_h = []
    for line in f:
        if line != "\n":
            if line[0] == "$":
                if "cd .." in line:
                    cwd = dict_h.pop()
                elif "cd" in line:
                    dict_h.append(cwd)
                    cwd = cwd[line.split()[2]]
            elif "dir" in line:
                cwd.update({line.split()[1]: {}})
            else:
                cwd.update({line.split()[1]: line.split()[0]})


def dict_sum(dir: Dict):
    o = {}

    for key, item in dir.items():
        if isinstance(item, dict):
            result = dict_sum(item)
            o.update({key: result})
            new_size = o.get("size", 0) + result["size"]
        else:
            new_size = o.get("size", 0) + int(item)
        o.update({"size": new_size})

    return o


def solve1(dir: Dict):
    o = 0

    for key, item in dir.items():
        if isinstance(item, dict):
            o += solve1(item)
        else:
            if dir["size"] <= 100_000:
                o += dir["size"]

    return o


def solve2(dir: Dict, to_free: int, o: int = 999_999_999):
    for key, item in dir.items():
        if isinstance(item, dict):
            o = solve2(item, to_free, o)
        else:
            if to_free <= dir["size"] < o:
                o = dir["size"]

    return o


foo = dict_sum(tree)

# Part 1
print(solve1(foo))

# Part 2
free = 70_000_000 - foo["size"]
print(solve2(foo, 30_000_000 - free))
