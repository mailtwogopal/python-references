string = "USA is wealthy USA has less population"
for i in string:
    lastindexof = string.rfind("USA")
print(lastindexof)

# split
str1 = "Emma-is-a-data-scientist"
print(str1.split('-'))

# remove empty strings in string
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
newlist = list(filter(None, str_list))
print(newlist)

# remove all symbols from string
import re
str2 = "/*Jon is @developer & musician"
newstr = re.findall('[a-z, A-Z]+', str2)
print(newstr)
# OR
newst = re.sub(r'[^\w\s]','', str2)
print(newst)