# sets - unordered collection of items, within {}, only unique
numbers = {1, 3, 5, 2, 0, 6}
print(numbers)
numbers2 = {2, "hi", 6, 98, 200}
print(numbers | numbers2)  # combining 2 sets and duplicate values are removed
print(numbers2 & numbers)  # gives only common on 2 sets
print(numbers - numbers2)  # gives items that are only in numbers which is not in numbers2 set
print(numbers2 - numbers)  # gives items that are only in numbers2 which is not in numbers set
