minWords = 3
maxWords = 6

inputtedWords = " "

splitInput = inputtedWords.split(" ")

while len(splitInput) > maxWords or len(splitInput) < minWords:
    inputtedWords = input("Please input a random number of words: ")
    lowerInputtedWords = inputtedWords.lower()
    splitInput = lowerInputtedWords.split(" ")

    if len(splitInput) > maxWords or len(splitInput) < minWords:
        print("The amount of words inputted was not within my range.")

if len(splitInput) <= maxWords and len(splitInput) >= minWords:
    print(splitInput)


