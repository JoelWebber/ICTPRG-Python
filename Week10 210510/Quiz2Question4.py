userInput = input("Please input a sentence and the program will output how many times 'a' and 'e' are repeated: ")
aCount = userInput.count('a')
eCount = userInput.count('e')

print("The letter a is repeated", aCount, "times.")
print("The letter e is repeated", eCount, "times.")