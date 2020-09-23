string = "Apple"
countDict = {}
for i in string:
    count = string.count(i)
    countDict[i] = count
print(countDict)