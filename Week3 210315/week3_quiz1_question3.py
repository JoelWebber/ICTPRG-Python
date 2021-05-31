correctUsername = "Cabbage"
correctPassword = "Password-20"

enteredUsername = str(input("Please enter your username "))
enteredPassword = str(input("Please enter your password "))

if (enteredUsername == correctUsername and enteredPassword == correctPassword):
    print("You may enter")
else:
    print("You shall not pass")
    