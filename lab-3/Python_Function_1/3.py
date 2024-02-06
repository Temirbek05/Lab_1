# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):


heads = int(input("Enter the number of chickens heads: "))
legs = int(input("Enter the number of rabbits legs: "))

def Heads(heads):
    return heads

def Legs(legs):
    return int(legs / 4)

ch = Heads(heads)
rb = Legs(legs)

print(f"we have {ch} chickens and {rb} rabbits")