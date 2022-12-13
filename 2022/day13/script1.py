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


indices = []
index = 1

with open("input.txt") as f:
    i = 0
    one, two = None, None
    for line in f:
        if line.strip() == "":
            if compare(one, two) == 1:
                indices.append(index)
            i = 0
            index += 1
        else:
            if i == 0:
                one = eval(line.strip())
            elif i == 1:
                two = eval(line.strip())
            i += 1

if compare(one, two) == 1:
    indices.append(index)
print(sum(indices))
