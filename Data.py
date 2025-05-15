import re
import numpy as np
import pandas as pd

data = []
entry = []

# Data Validation
ValidColor = ["Red", "Green", "Blue", "Purple", "Colorless", "Curse"]
ValidRarity = ["Basic", "Common", "Uncommon", "Rare", "Special", "Curse"]
ValidType = ["Attack", "Skill", "Power", "Status", "Curse"]
ValidCost = ["0", "1", "2", "3", "4", "5", "X", "Unplayable"]

# Read data
f = open('CardData.txt', 'r')
for line in f.readlines():
    valueMatch = re.search(r'\"(.*)\"', line)
    if valueMatch:
        value = valueMatch.group(1)
    if re.search(r'^{$', line):
        entry = []
    elif re.search(r'Name = ', line):
        entry.append(value)
    elif re.search(r'Color = ', line):
        if value not in ValidColor:
            print("Error: Invalid color", value)
        entry.append(value)
    elif re.search(r'Rarity = ', line):
        if value not in ValidRarity:
            print("Error: Invalid rarity", value)
        entry.append(value)
    elif re.search(r'Type = ', line):
        if value not in ValidType:
            print("Error: Invalid type", value)
        entry.append(value)
    elif re.search(r'Cost = ', line):
        value = line[7:-2]
        if value not in ValidCost:
            print("Error: Invalid cost", value)
        entry.append(value)
    elif re.search(r'Text = ', line):
        entry.append(value)
    elif re.search(r'^},$', line):
        data.append(entry)
f.close()

# for x in data:
#     print("Card:")
#     for y in x:
#         print(y)

df = pd.DataFrame(data, columns=["Name", "Color", "Rarity", "Type", "Cost", "Text"])
print(df)
print(df.loc[df["Cost"] == "X"])

