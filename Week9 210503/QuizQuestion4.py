import math #Imports the math library
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #The list of numbers needs
value = 0 #initialises the value
product = 0#initialises the value
for i in range(len(numberList)): #For ever number inside of number list, the factorial of each number is found
    product = math.factorial(numberList[i])
    print(numberList[i], "->", product) #prints the final values needed
    product = 0




    
    
