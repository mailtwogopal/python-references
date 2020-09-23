def substring(string):
    length = len(string)
    if length >= 7 & length % 2 != 0:
        middleindex = int(length / 2)
        substr = string[middleindex-1:middleindex+2:]
    return substr


print(substring("testola"))
print((substring("JhonDipPeta")))
print(substring("machineries"))