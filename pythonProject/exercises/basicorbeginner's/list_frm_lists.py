def filterList(list1, list2):
    newList = []
    for i in range(0, len(list1)):
        if list1[i] % 2 != 0:
            newList.append(list1[i])
    for j in range(0, len(list2)):
        if list2[j] % 2 == 0:
            newList.append(list2[j])
    return newList


print(filterList([1, 2, 3, 4, 5, 6, 7, 9], [2, 3, 4, 5, 6, 8]))
