with open("input.txt") as f:
    buffer = f.read()

    # Part 1
    for i in range(3, len(buffer)):
        marker = set(buffer[i-3:i+1])
        if len(marker) == 4:
            print(i+1)
            break

    # Part 2
    for i in range(13, len(buffer)):
        marker = set(buffer[i-13:i+1])
        if len(marker) == 14:
            print(i+1)
            break
