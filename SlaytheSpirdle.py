import numpy as np
import pandas as pd
from random import randrange

win = False
iterCount = 0
maxIter = 4
df = pd.read_csv("CardAttributes.csv", header=0)
cardIDDict = dict(np.column_stack((df["Name"], df.index)))

cardID = randrange(len(df.index))
card = df.iloc[cardID]

print("Slay the Spirdle, V1")
print("Card picked:", card["Name"])
print()
print("Guess a card: ")

while not win:
    userGuess = input()
    if userGuess not in cardIDDict: 
        print("That is not a card. Please try again.")
        continue
    print("You guessed: \n", df.iloc[cardIDDict[userGuess]], "\n")
    if userGuess == card["Name"]:
        print("You won!")
        break

    iterCount = iterCount + 1
    print("Incorrect, try again.", maxIter - iterCount, "guesses left.")
    if iterCount >= maxIter: win = True