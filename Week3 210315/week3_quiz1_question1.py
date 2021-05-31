acceptedName1 = "George"
acceptedName2 = "Frank"
enteredName = str(input("Please enter your name "))

if (enteredName == acceptedName1 or enteredName == acceptedName2):
    print("Greetings,", enteredName + ", how are you?")