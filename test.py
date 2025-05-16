import numpy as np
import pandas as pd

df = pd.read_csv("CardAttributes.csv", header=0)
print(df)

cardIDDict = {}
cardIDDict = dict(np.column_stack((df["Name"], df.index)))
# print(cardIDDict)

card = df.iloc[2]
print(card)
print(card["Name"])

