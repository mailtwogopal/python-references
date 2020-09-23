sentence = "dev1234test45"
Letter = ""
numbers = ""
for i in range(0, len(sentence)):
    if sentence[i].isalpha():  # isalpha will check if each value of sentence is alphabet or not
        Letter = Letter + sentence[i]
    else:
        numbers = numbers + sentence[i]
print(len(Letter), Letter)
print(len(numbers), numbers)
