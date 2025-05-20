import numpy as np
import pandas as pd
from ast import literal_eval

df = pd.read_csv("CardAttributes.csv", header=0, converters={"Card Traits":literal_eval, "Debuffs":literal_eval, "Buffs":literal_eval})
# df = pd.read_csv("CardAttributes.csv", header=0)
# print(df)

cardIDDict = {}
cardIDDict = dict(np.column_stack((df["Name"], df.index)))
# print(cardIDDict)

card = df.iloc[81]
print(card)

traits = card["Card Traits"]
debuffs = card["Debuffs"]
buffs = card["Buffs"]
print(traits)
print(debuffs)
print(buffs)
print(not [])
print(not [1])
print(not ["hello"])
print(not buffs)
print(not debuffs)