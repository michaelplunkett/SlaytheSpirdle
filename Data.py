import json
import re
import numpy as np

data = []
entry = []
i = 0

f = open('CardData.txt', 'r')
for line in f.readlines():
    valueMatch = re.search(r'\"(.*)\"', line)
    if valueMatch:
        value = valueMatch.group(1)
    if re.search(r'^{$', line):
        entry = []
    elif re.search(r'Name = ', line):
        entry.append(["Name", value])
    elif re.search(r'Color = ', line):
        entry.append(["Color", value])
    elif re.search(r'Rarity = ', line):
        entry.append(["Rarity", value])
    elif re.search(r'Cost = ', line):
        entry.append(["Cost", line[7:-2]])
    elif re.search(r'Text = ', line):
        entry.append(["Text", value])
    elif re.search(r'^},$', line):
        data.append(entry)
f.close()

for x in data:
    print("Card:")
    for y in x:
        print(y)
