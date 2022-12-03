from enum import Enum

class Symbol(Enum):
    Rock = "A"
    Paper = "B"
    Scissors = "C"

# class Symbol(Enum):
#     Rock = "X"
#     Paper = "Y"
#     Scissors = "Z"

totalPoints = 0
roundCount = 0

with open("input.txt", 'r') as f:
    
    for line in f:
        print("\nRound " + str(roundCount + 1))
        roundCount += 1
        p1 = Symbol(line[0])
        p2 = Symbol(str(chr(ord(line[2]) - 23)))

        choosenSymobolPoints = 0

        if p2 == Symbol.Rock:
            print("P2 chose Rock")
            choosenSymobolPoints = 1
        elif p2 == Symbol.Paper:
            print("P2 chose Paper")
            choosenSymobolPoints = 2
        elif p2 == Symbol.Scissors:
            print("P2 chose Scissors")
            choosenSymobolPoints = 3

        outcomePoints = 0

        if p1 == p2:
            print("Draw")
            outcomePoints = 3
        elif p1 == Symbol.Rock and p2 == Symbol.Scissors:
            print("P1 wins")
            outcomePoints = 0
        elif p1 == Symbol.Paper and p2 == Symbol.Rock:
            print("P1 wins")
            outcomePoints = 0
        elif p1 == Symbol.Scissors and p2 == Symbol.Paper:
            print("P1 wins")
            outcomePoints = 0
        else:
           print("P2 wins")
           outcomePoints = 6

        
        
        totalRoundPoints = choosenSymobolPoints + outcomePoints
        print("Round points: " + str(totalRoundPoints))
        totalPoints += totalRoundPoints



print("Total Points " + str(totalPoints))