
def getPrioOfItem(inp : str) -> int:
    if ord(inp) >= 65 and ord(inp) <= 90:
        return ord(inp) - 65 + 27
    else:
        return ord(inp) - 97 + 1

totalPrio = 0

with open("input.txt", 'r') as f:
    
    for line in f:
        centerOfLine = int(len(line) / 2)
        compart1 = line[0:centerOfLine]
        compart2 = line[centerOfLine:len(line)]

        doubleItem = ""

        for i in range(len(compart1)):
            for j in range(len(compart2)):
                if compart1[i] == compart2[j]:
                    doubleItem = compart1[i]
                    break
        
        prioOfDouebelItem = getPrioOfItem(doubleItem)
        totalPrio += prioOfDouebelItem
    
print(totalPrio)


        
