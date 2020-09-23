def concatAtSpecifiedIndex(string1, string2):
    len1 = len(string1)
    midindex = int(len1 / 2)
    print("original strings are: ", string1, string2)
    newstring = string1[:midindex:] + string2 + string1[midindex:]
    print(newstring)


concatAtSpecifiedIndex("tesbmw", "la")
concatAtSpecifiedIndex("bwc", "mar")