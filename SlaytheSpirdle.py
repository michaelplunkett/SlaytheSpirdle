import numpy as np
import pandas as pd
from ast import literal_eval # Reads lists from csv
from random import randrange

win = False
iterCount = 0
maxIter = 10
df = pd.read_csv("CardAttributes.csv", header=0, converters={"Card Traits":literal_eval, "Debuffs":literal_eval, "Buffs":literal_eval})
cardIDDict = dict(np.column_stack((df["Name"], df.index)))

# solnCardID = randrange(len(df.index))
solnCardID = 73 # Backstab
solnCard = df.iloc[solnCardID]

print("Slay the Spirdle, V1")
print("Card picked:")
print(solnCard)
print()
print("Guess a card: ")

while not win:
    colorMatch = False
    rarityMatch = False
    typeMatch = False
    costMatch = False
    traitMatch = 0      # Partial boolean: 0 == incorrect, 1 == partial match, 2 == correct
    debuffMatch = 0     # Partial boolean: 0 == incorrect, 1 == partial match, 2 == correct
    buffMatch = 0       # Partial boolean: 0 == incorrect, 1 == partial match, 2 == correct

    userGuess = input()
    if userGuess not in cardIDDict: 
        print("That is not a card. Please try again.")
        continue
    userCard = df.iloc[cardIDDict[userGuess]]
    print("You guessed: \n", userCard, "\n")
    if userGuess == solnCard["Name"]:
        win = True
        print("You won!")
        break
    if userCard["Color"] == solnCard["Color"]: colorMatch = 1
    if userCard["Rarity"] == solnCard["Rarity"]: rarityMatch = 1
    if userCard["Type"] == solnCard["Type"]: typeMatch = 1
    if userCard["Cost"] == solnCard["Cost"]: costMatch = 1

    # Check Card Traits
    anyMatchFlag = False
    fullMatchFlag = True
    if len(solnCard["Card Traits"]) == len(userCard["Card Traits"]): 
        # If both are empty, we already have fullMatchFlag = True 
        for elem in userCard["Card Traits"]:
            if elem in solnCard["Card Traits"]: anyMatchFlag = True
            else: fullMatchFlag = False
    else:
        # With mismatch length, we can never have a full match
        fullMatchFlag = False
        # If one is empty and the other non-empty, we already have anyMatchFlag = fullMatchFlag = False
        for elem in userCard["Card Traits"]:
            if elem in solnCard["Card Traits"]: anyMatchFlag = True
    if fullMatchFlag: traitMatch = 2
    elif anyMatchFlag: traitMatch = 1
    else: traitMatch = 0

    # Check Debuffs
    anyMatchFlag = False
    fullMatchFlag = True
    if len(solnCard["Debuffs"]) == len(userCard["Debuffs"]): 
        # If both are empty, we already have fullMatchFlag = True 
        for elem in userCard["Debuffs"]:
            if elem in solnCard["Debuffs"]: anyMatchFlag = True
            else: fullMatchFlag = False
    else:
        # With mismatch length, we can never have a full match
        fullMatchFlag = False
        # If one is empty and the other non-empty, we already have anyMatchFlag = fullMatchFlag = False
        for elem in userCard["Debuffs"]:
            if elem in solnCard["Debuffs"]: anyMatchFlag = True
    if fullMatchFlag: debuffMatch = 2
    elif anyMatchFlag: debuffMatch = 1
    else: debuffMatch = 0

    # Check Buffs
    anyMatchFlag = False
    fullMatchFlag = True
    if len(solnCard["Buffs"]) == len(userCard["Buffs"]): 
        # If both are empty, we already have fullMatchFlag = True 
        for elem in userCard["Buffs"]:
            if elem in solnCard["Buffs"]: anyMatchFlag = True
            else: fullMatchFlag = False
    else:
        # With mismatch length, we can never have a full match
        fullMatchFlag = False
        # If one is empty and the other non-empty, we already have anyMatchFlag = fullMatchFlag = False
        for elem in userCard["Buffs"]:
            if elem in solnCard["Buffs"]: anyMatchFlag = True
    if fullMatchFlag: buffMatch = 2
    elif anyMatchFlag: buffMatch = 1
    else: buffMatch = 0

    # Print results 
    print("Color:\t\t Correct")  if colorMatch  else print("Color:\t\t Incorrect")
    print("Rarity:\t\t Correct") if rarityMatch else print("Rarity:\t\t Incorrect")
    print("Type:\t\t Correct")   if typeMatch   else print("Type:\t\t Incorrect")
    print("Cost:\t\t Correct")   if costMatch   else print("Cost:\t\t Incorrect")
    match traitMatch:
        case 0: print("Card Traits:\t Incorrect")
        case 1: print("Card Traits:\t Partially correct")
        case 2: print("Card Traits:\t Correct")
    match debuffMatch:
        case 0: print("Debuffs:\t Incorrect")
        case 1: print("Debuffs:\t Partially correct")
        case 2: print("Debuffs:\t Correct")
    match buffMatch:
        case 0: print("Buffs:\t\t Incorrect")
        case 1: print("Buffs:\t\t Partially correct")
        case 2: print("Buffs:\t\t Correct")
    print()

    iterCount = iterCount + 1
    print("Incorrect, try again.", maxIter - iterCount, "guesses left.")
    if iterCount >= maxIter: break