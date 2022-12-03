

current = 0
top3 = [0, 0, 0]

with open("input.txt", 'r') as f:
    for line in f:

        if len(top3) != 3:
            print("Error: top3 is not 3 elements long")
            print(top3)
            exit(1)

        if line == '\n':

            top3.sort()
            for i in range(3):
                if current > top3[i]:
                    top3.pop(i)
                    top3.append(current)
                    break

            current = 0
        else:
            val = int(line)
            current += val
print(top3)
finalSum = 0
for i in range(3):
    finalSum += top3[i]

print(finalSum)