import random #This allows me to use the random function

maxGuesses = 7 #The amount of guesses a user is allowed
guessesRemaining = maxGuesses #The amount of guesses a user has left

guessList = [''] #Initialising the list of guesses the user will enter

randomNumberMax = 26 #The highest number the user will have to guess
randomNumberMin = 0 #The lowest number a user will have to guess
randomNumber = random.randrange(randomNumberMin, randomNumberMax) #The calculation of the number the user will have to guess using the random.randrange tool
print(randomNumber)
lessThanText = "The number you entered is less than the answer." #Text to be used later
greaterThanText = "The number you entered is greater than the answer." #Text to be used later
usersGuess = input("Please guess a random number between " + str(randomNumberMin) + " and " + str(randomNumberMax-1) + ": ") #Asking the user to guess a random number between two values

while usersGuess != randomNumber: #If the users guess is not equal to the random number, run through this while loop
    
    if (int(usersGuess) < randomNumber): #If the users guess is less than the random number, print lessThanText
        print(lessThanText)
    elif(int(usersGuess) > randomNumber): #If the users guess is greater than the random number, print greaterThanText
        print(greaterThanText) 
    else: #If the user guessed correctly, break the loop
        break
    
    guessesRemaining = guessesRemaining - 1 #The current amount of guesses the player has left
    guessList.append(usersGuess) #Adding the users guess to a list to be displayed later
    if (guessesRemaining > 0): #If the player has correctly guessed the random number, break out of the loop. 
        usersGuess = input("Please guess again: ")
        if int(usersGuess) == randomNumber:
            break
    else: #If they have not guessed the number correctly, but have run out of guesses, break the loop
        break

if int(usersGuess) == randomNumber: #If the player has guessed the number correctly, congratulate them and show them all the numbers that they guessed
    guessList.append(usersGuess)
    print("Congrats, you guessed correctly! Your guesses were: ")
    for guess in range(len(guessList)):
        print(guessList[guess])
else: #If the player has not guessed the number correctly, call them a fool and tell them the correct answer
    print("Ya fool, ya guessed wrong. The answer was " + str(randomNumber))