userInput = int(input("Please enter a number between 50 and 70: "))
while (userInput < 50 or userInput > 70):
    userInput = int(input("This number is not between 50 and 70. Please enter a number between 50 and 70: " ))

print("The number is within range")