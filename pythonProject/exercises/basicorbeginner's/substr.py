def countOfString(string, lookup):
    countOf = string.count(lookup)  # returns count of occurences of given lookup string
    return countOf


#  string methods - find(substring), substring in string, count() to return no. of times substr exists
print(countOfString("test thru test of yes", "test"))
print(countOfString("english language widely spoken in english speaking countries", "english"))
