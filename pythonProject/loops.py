# while
count = 0
while count < 10:
    print(count)
    count += 1
print("came out of while loop")
print("\n")

# for loop
fruits = ["apple", "citrus", "berries"]
for fruit in fruits:
    print(fruit)

# for loop to find factorial
num = 6
factorial = num
for i in range(num, 1, -1): # this is similar to for(i=num, i>1, i--) in java or js
    factorial = factorial * (i - 1)
print("factorial of ", num, "is ", factorial)


