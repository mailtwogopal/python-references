string = "JKrowLiNg"
lowerchars = ""
upperchars = ""
for i in range(0, len(string)):
    if string[i].islower():
        lowerchars = lowerchars + string[i]
    if string[i].isupper():
        upperchars = upperchars + string[i]
print(lowerchars + upperchars)