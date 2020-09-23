def genevennum(a, b):
    ls = []
    for i in range(a, b):
        if i > 3 & i %2 == 0:
            ls.append(i)
    return ls


print(genevennum(4, 30))
print(genevennum(2, 35))

# simple method - use built in func range
print(list(range(4, 30, 2)))