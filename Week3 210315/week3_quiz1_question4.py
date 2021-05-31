correctUsername1 = "bob"
correctPassword1 = "password1234"
correctUsername2 = "fred"
correctPassword2 = "happyPass122"
correctUsername3 = "lock"
correctPassword3 = "passwithlock44"

enteredUsername = str(input("Please enter your username "))
enteredPassword = str(input("Please enter your password "))

if (enteredUsername == correctUsername1 and enteredPassword == correctPassword1):
    print("You may enter")
elif (enteredUsername == correctUsername2 and enteredPassword == correctPassword2):
     print("You may enter")
elif (enteredUsername == correctUsername3 and enteredPassword == correctPassword3):
     print("You may enter")
else:
    print("You shall not pass")
    