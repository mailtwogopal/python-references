def newstring(string1, string2):
    firstchar = string1[0]
    lastchar = string1[len(string1) - 1]
    midchar = string1[int(len(string1) / 2)]
    firstchar2 = string2[0]
    lastchar2 = string2[len(string2) - 1]
    midchar2 = string2[int(len(string2) / 2)]
    constring = firstchar + firstchar2 + midchar + midchar2 + lastchar + lastchar2
    print(constring)


newstring("america", "japan")
newstring("johny", "india")
