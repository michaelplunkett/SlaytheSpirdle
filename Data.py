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
        text = entry[-1]
        cardTraits = []
        debuffs = []
        buffs = []
        if re.search(r'Innate.', text): cardTraits.append("Innate")
        if re.search(r'Exhaust.', text): cardTraits.append("Exhaust")
        if re.search(r'Ethereal.', text): cardTraits.append("Ethereal")
        if re.search(r'Unplayable.', text): cardTraits.append("Unplayable")
        if re.search(r'Retain.', text): cardTraits.append("Retain")
        # if re.search(r'Weaken', text): debuffs.append("Weaken")
        # if re.search(r'Frail', text): debuffs.append("Frail")
        # if re.search(r'Vulnerable', text): debuffs.append("Vulnerable")
        # if re.search(r'Intangible', text): buffs.append("Intangible")
        entry.append(cardTraits)
        entry.append(debuffs)
        entry.append(buffs)
        data.append(entry)
f.close()

df = pd.DataFrame(data, columns=["Name", "Color", "Rarity", "Type", "Cost", "Text", "Card Traits", "Debuffs", "Buffs"])

# Assign Card Traits


# Assign Debuffs

# Assign Buffs


print(df)
# print(df["Name"].tolist())
# print(df.loc[df["Cost"] == "X"]["Name"].tolist())