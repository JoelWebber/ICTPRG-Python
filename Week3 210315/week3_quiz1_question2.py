requiredAgeToDrink = 18
currentYear = 2021
enteredBirthYear = int(input("Please enter your year of birth "))

if (requiredAgeToDrink <= (currentYear - enteredBirthYear)):
    print("Come on in and have a drink.")
else:
    print("Get lost kiddo.")