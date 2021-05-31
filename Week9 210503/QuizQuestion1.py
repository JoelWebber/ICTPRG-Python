#This program gets two numbers from a user, adds them together, and outputs them to a file named "maths.txt."
print("In the following, you will be asked to enter two numbers. Please enter two numbers you would like to have added together into the appropriate fields")

num1 = input("Please enter the first number: ")#gets input from the user
num2 = input("Please enter the second number: ")#gets input from the user

print("The numbers are being added...")

addedNums = int(num1) + int(num2) #adds the inputed numbers together

mathsFile = open("maths.txt", "w")

print("The numbers that you inputed have been added together and are inside the file named 'maths.txt.'")
mathsFile.write("The sum of the numbers that you inputed is: " + str(addedNums)) #writes the sum of the numbers to the file
mathsFile.close #closes the file
