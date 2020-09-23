# variable cannot start with number - # single line comment
"""multi
line comment"""

print("hello pythonners \nwelcome")

a = 10
b = "string"
print(a, b)  # print 2 values and use comma to separate them

x, y, z = 1, 3, 0  # this is equal to saying x=1, y=3, z=0
print("value of x is ", x)
print(y, " is the value of y")
print("z hold value of ", z)

# complex numbers
j = 8 + 5j
k = 6 - 2j
i = j - k
print(i)

# python do not have char data type like java, it only has String
# python - immutable data types - numbers, string, tuple
# tuple - will not support assignment, like this z[1] = 5
z = (4, 9, 14)
print(z)
print(z[0], z[2])

s, d = 2, 3
print(s * 2)
print(d ** 2)

today = "Friday"
yogaDay = "Saturday"
print(today is yogaDay)  # returns false
print(today is not yogaDay)  # returns true
