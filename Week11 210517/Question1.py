validNumber = False
userInput = 0

while not validNumber:
    userInput = input("Please enter a valid number: ")
    if userInput.isdigit():
        validNumber = True
    else:
        print("The number you entered is not valid. Please enter another number.")

print("The number you entered was: " + userInput + ". Your input was valid.")
