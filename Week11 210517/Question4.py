passwordInput = ""
passwordCanBeValid = False
passwordIsValid = True

minimumPasswordLength = 7

symbolsString = "!@#$%^&*()_+-=[{]}\|/.,<>?`~"
symbolList = list(symbolsString)

while passwordIsValid == True:
    passwordInput = input("Please enter a password: ")
    splitPassword = list(passwordInput)
    lowerCharacterExists = False
    upperCharacterExists = False
    symbolCharacterExists = False
    numericCharacterexists = False
    correctPasswordCharacterLength = False

    for character in splitPassword:
        if character.islower() == True:
            lowerCharacterExists = True

        if character.isupper() == True:
            upperCharacterExists = True

        if character.isnumeric() == True:
            numericCharacterexists = True


        for symbol in symbolList:
            if character == symbol:
                symbolCharacterExists = True
    if len(splitPassword) >= minimumPasswordLength:
        correctPasswordCharacterLength = True
    
    if lowerCharacterExists and upperCharacterExists and symbolCharacterExists and numericCharacterexists and correctPasswordCharacterLength:
        confirmPassword = input("Please re enter the password to confirm: ")
        while confirmPassword != passwordInput:
            confirmPassword = input("Passwords do not match. Please re enter the password to confirm: ")
        if confirmPassword == passwordInput:
            print("valid password")
            passwordIsValid = False
    else:
        print("Password is not valid, please try again.")
    

