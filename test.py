import numpy as np
import pandas as pd
import re
from ast import literal_eval

df = pd.read_csv("CardAttributes.csv", header=0, converters={"Card Traits":literal_eval, "Debuffs":literal_eval, "Buffs":literal_eval})
# df = pd.read_csv("CardAttributes.csv", header=0)
# print(df)

cardIDDict = {}
cardIDDict = dict(np.column_stack((df["Name"], df.index)))
# print(cardIDDict)

# card = df.iloc[177]
# print(card)

# traits = card["Card Traits"]
# debuffs = card["Debuffs"]
# buffs = card["Buffs"]

text = "#Exhaust all non-Attack cards in your hand.\nDeal [16|22] damage."
result = re.search(r'Exhaust.', text)
print(result)