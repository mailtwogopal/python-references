string = "aBc12ef3$567%(0aL"
countupper = 0
countlower = 0
countnum = 0
countsym = 0
for i in range(0, len(string)):
    if string[i].isalpha():
        if string[i].isupper():
            countupper = countupper + 1
        elif string[i].islower():
            countlower = countlower + 1
    elif string[i].isnumeric():
        countnum = countnum + 1
    else:
        countsym = countsym + 1
prtst = "upperchars {0}, lowerchars {1}, numbers {2}, sp.chars {3}"
print(prtst.format(countupper, countlower, countnum, countsym))