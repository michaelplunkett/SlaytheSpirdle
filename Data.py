import re
import numpy as np
import pandas as pd

data = []
entry = []

f = open('CardData.txt', 'r')
for line in f.readlines():
    valueMatch = re.search(r'\"(.*)\"', line)
    if valueMatch:
        value = valueMatch.group(1)
    if re.search(r'^{$', line):
        entry = []
    elif re.search(r'Name = ', line):
        # entry.append(["Name", value])
        entry.append(value)
    elif re.search(r'Color = ', line):
        # entry.append(["Color", value])
        entry.append(value)
    elif re.search(r'Rarity = ', line):
        # entry.append(["Rarity", value])
        entry.append(value)
    elif re.search(r'Type = ', line):
        # entry.append(["Type", value])
        entry.append(value)
    elif re.search(r'Cost = ', line):
        # entry.append(["Cost", line[7:-2]])
        entry.append(line[7:-2])
    elif re.search(r'Text = ', line):
        # entry.append(["Text", value])
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
print(df["Name"])