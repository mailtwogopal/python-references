# 1
nums = {1, 3, 2, 6, 5, 4, 4, 6}
print(len(nums))  # removes duplicates and returns length since set returns unique elements
# 2
d = {"name": "john", "age": 38}
print(d.keys())  # returns keys
print(d.items())  # returns key value pairs as tuple
print(list(d.keys()))  # returns keys as list
# 3

# 4
a = [4, 7, 3, 2, 5, 9]
for item in a:
    print(a.index(item), item)  # index() returns the position of element in the list
# 5

# 6
# string = str(input("enter the string: "))
string = "year2020"
print("reverse of string entered is ", string[::-1])
# 7

# 8
a = [1, 3, 6, 78, 35, 55, 120]
b = [12, 24, 35, 24, 88, 120, 155]
a1 = set(a) & set(b)  # converting list to set to find intersection
print(list(a1))  # converting back to list as per question
