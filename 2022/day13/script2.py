from functools import cmp_to_key


def compare(left, right):
    for i in range(len(left)):
        try:
            a, b = left[i], right[i]
        except IndexError:
            return -1
        if isinstance(a, int) and isinstance(b, int):
            if a > b:
                return -1
            elif a < b:
                return 1
        elif isinstance(a, list) and isinstance(b, int):
            b = [b]
            result = compare(a, b)
            if result != 0:
                return result
        elif isinstance(a, int) and isinstance(b, list):
            a = [a]
            result = compare(a, b)
            if result != 0:
                return result
        else:
            result = compare(a, b)
            if result != 0:
                return result
    return 0 if len(left) == len(right) else 1


signals = [[[2]], [[6]]]

with open("input.txt") as f:
    for line in f:
        if line.strip() == "":
            pass
        else:
            signals.append(eval(line.strip()))

sorted_signals = list(reversed(sorted(signals, key=cmp_to_key(compare))))

i1 = sorted_signals.index([[2]]) + 1
i2 = sorted_signals.index([[6]]) + 1

print(i1 * i2)
