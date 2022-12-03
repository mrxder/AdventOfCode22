

current = 0
max = 0

with open("input.txt", 'r') as f:
    for line in f:
        if line == '\n':
            if current > max:
                max = current
            current = 0
        else:
            val = int(line)
            current += val

print(max)