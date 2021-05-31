correctEmail = False
hasFullStop = False
hasAtSymbol = False
isCorrectLength = False

while correctEmail == False:
    inputEmail = input("Please input a correctly formatted email address: ")
    splitEmail = inputEmail.split("@")
    if len(splitEmail) == 2:
        hasAtSymbol = True
        for character in splitEmail[1]:
            if character == ".":
                hasFullStop = True            
        if len(splitEmail[0]) > 2 and len(splitEmail[0]) < 33:
            if len(splitEmail[1]) > 2 and len(splitEmail[1]) < 33:
                isCorrectLength = True
        if hasFullStop and hasAtSymbol and isCorrectLength:
            correctEmail = True
            print(inputEmail)
    if correctEmail == False:
        print("Email was not formatted correctly. Please try again.")
    hasFullStop = False
    hasAtSymbol = False
    isCorrectLength = False

