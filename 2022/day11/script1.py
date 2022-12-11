import math
import operator
from pprint import pprint

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}

index = 0
monkeys = []

with open("input.txt") as f:
    for line in f:
        if line.strip() == "":
            index = 0
        elif line.split()[0] == "Monkey":
            monkey = {
                "items": [],
                "op": [],
                "test": {
                    "divisible": 0,
                    True: 0,
                    False: 0,
                },
                "inspected": 0,
            }
            monkeys.append(monkey)
        else:
            monkey = monkeys[-1]
            if index == 0:
                line = line.split(":")[-1]
                for item in line.split(","):
                    item = int(item.strip())
                    monkey["items"].append(item)
            elif index == 1:
                line = line.split("=")[-1].strip()
                monkey["op"] = line.split()
            elif index == 2:
                monkey["test"]["divisible"] = int(line.split()[-1])
            elif index == 3:
                monkey["test"]["true"] = int(line.split()[-1])
            elif index == 4:
                monkey["test"]["false"] = int(line.split()[-1])
            index += 1

for _ in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            old = item
            ops = monkey["op"]
            m = []
            for op in ops:
                if op == "old":
                    m.append(vars()["old"])
                elif op in operators:
                    m.append(operators[op])
                else:
                    m.append(int(op))
            new = math.floor(m[1](m[0], m[2]) / 3)
            if new % monkey["test"]["divisible"] == 0:
                monkeys[monkey["test"]["true"]]["items"].append(new)
            else:
                monkeys[monkey["test"]["false"]]["items"].append(new)
            monkey["inspected"] += 1
        monkey["items"] = []

inspected = list(reversed(sorted([int(x["inspected"]) for x in monkeys])))
print(inspected[0:2][0] * inspected[0:2][1])
