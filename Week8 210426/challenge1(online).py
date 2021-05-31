#Create a script that gathers user information and formats it as potential user login details
#Gather this information from the user: first name, last name, age.
#Example details: First Name, Joe. Last Name, Feathers. Age, 32 
#Add the third last digit of *my* student ID to the inputted value "Age"
#Display the output of the user input like: jfeather@Huawow.io|joeF_(currentYear - Age)
#Continue asking the user for input values until the firstName field is left blank. ""
print("This program will display potential login details of Huawow employees based on user input")

currentYear = 2021
thirdLastDigit = 1
firstName = " "
fixedPartOfOutput = "@Huawow.io|"

while (firstName != ""):
    print ("When asked, please type in values and press enter to input them")
    firstName = input("Please enter a first name. If this field is left blank, the program will be exited: ")
    if (firstName == ""):
        break

    lastName = input("Please enter a last name: ")
    age = input("Please enter an age: ")

    firstNameLetters = list(firstName)#Calculating users login
    lastNameLetters = list(lastName)#Calculating users login
    lastNameInitial = str(lastNameLetters[0])

    calculatingUserAddress = (firstNameLetters[0] + lastName)#Calculating users address
    calculatingUserAddress = calculatingUserAddress.strip()#Calculating users address
    userAddress = calculatingUserAddress.lower()#Calculating users address

    calculatingUserPassword = (firstName.lower() + lastNameInitial.upper())#Calculating user password
    passwordNumber = (currentYear - (int(age) + thirdLastDigit))#Calculating user password
    strPasswordNumber = str(passwordNumber)#Calculating user password
    userPassword = calculatingUserPassword + "_" + strPasswordNumber#Calculating user password
    
    outputUserDetails = (userAddress + fixedPartOfOutput + userPassword)#Calculating the final output of the user login details.
    print(outputUserDetails)

print("The algorithm has ended.")
