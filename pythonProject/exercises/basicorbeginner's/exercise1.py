for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )


sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott") # append takes only one argument so error will be shown
print(sampleList)

var = "jamesbond"
print(var[2::-1]) # reverse from index 2 right to left

sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki") # add takes only one argument so error will be shown
print(sampleSet)

x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

valueOne = 5 ** 2 # ** denotes square of : so here 5 power 2 is 25
valueTwo = 5 ** 3
print(valueOne)
print(valueTwo)

for i in range(10, 15, 1):
  print( i, end=', ')

print("\n")
listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]
print(listOne == listTwo) # returns true
print(listOne is listTwo)

salary = 8000


def printSalary():
    salary = 12000
    print("Salary:", salary)


printSalary()
print("Salary:", salary)

vars = "James" * 2  * 3
print(vars)

var1 = 1
var2 = 2
var3 = "3"
print(var + var2 + var3)