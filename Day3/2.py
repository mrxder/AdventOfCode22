
def getPrioOfItem(inp : str) -> int:
    if ord(inp) >= 65 and ord(inp) <= 90:
        return ord(inp) - 65 + 27
    else:
        return ord(inp) - 97 + 1

totalPrio = 0

with open("input.txt", 'r') as f:
    
    count = 0
    currentGroup = []
    for line in f:
        count += 1
        if count % 3 == 0:
            currentGroup.append(line.strip())
            a = currentGroup[0]
            b = currentGroup[1]
            c = currentGroup[2]

            for i in range(len(a)):
                for j in range(len(b)):
                    for k in range(len(c)):
                        if a[i] == b[j] and b[j] == c[k]:
                            commonItem = a[i]
                            break
            
            prioOfCommonItem = getPrioOfItem(commonItem)
            totalPrio += prioOfCommonItem

            currentGroup = []
        else:
            currentGroup.append(line.strip())
        


    
print(totalPrio)


        
