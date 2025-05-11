f = open("CardTest.txt", 'r')
for line in f.readlines():
    print(line == "{\n")
f.close()