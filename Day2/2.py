from enum import Enum

class Symbol(Enum):
    Rock = "A"
    Paper = "B"
    Scissors = "C"

class Outcome(Enum):
    Lose = "X"
    Draw = "Y"
    Win = "Z"


totalPoints = 0
roundCount = 0

with open("input.txt", 'r') as f:
    
    for line in f:
        p1 = Symbol(line[0])
        neededOutcome = Outcome(line[2])

        if neededOutcome == Outcome.Lose and p1 == Symbol.Rock:
            p2 = Symbol.Scissors
        
        elif neededOutcome == Outcome.Lose and p1 == Symbol.Paper:
            p2 = Symbol.Rock
        
        elif neededOutcome == Outcome.Lose and p1 == Symbol.Scissors:
            p2 = Symbol.Paper
        
        elif neededOutcome == Outcome.Win and p1 == Symbol.Rock:
            p2 = Symbol.Paper
        
        elif neededOutcome == Outcome.Win and p1 == Symbol.Paper:
            p2 = Symbol.Scissors
        
        elif neededOutcome == Outcome.Win and p1 == Symbol.Scissors:
            p2 = Symbol.Rock
        
        elif neededOutcome == Outcome.Draw:
            p2 = p1


        choosenSymobolPoints = 0

        if p2 == Symbol.Rock:
            choosenSymobolPoints = 1
        elif p2 == Symbol.Paper:
            choosenSymobolPoints = 2
        elif p2 == Symbol.Scissors:
            choosenSymobolPoints = 3

        outcomePoints = 0

        if p1 == p2:
            outcomePoints = 3
        elif p1 == Symbol.Rock and p2 == Symbol.Scissors:
            outcomePoints = 0
        elif p1 == Symbol.Paper and p2 == Symbol.Rock:
            outcomePoints = 0
        elif p1 == Symbol.Scissors and p2 == Symbol.Paper:
            outcomePoints = 0
        else:
           outcomePoints = 6

        
        
        totalRoundPoints = choosenSymobolPoints + outcomePoints
        totalPoints += totalRoundPoints



print("Total Points " + str(totalPoints))