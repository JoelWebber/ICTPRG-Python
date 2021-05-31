inputValue = 0
total = 0
while(inputValue != 'x'):
    total = total + int(inputValue)
    inputValue = input("Please enter numbers to be added together. If you wish to stop, press x ")

print("The total of the entered numbers is: " + str(total))
