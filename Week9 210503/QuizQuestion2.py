#This program lists out names in the file 'people.txt' 
print("At the prompt, enter names and they will be added to a file on separate lines. If you wish to stop entering names, leave the field blank.")

inputNames = [] #Initialises the variable
inputName = ' ' #Initialises the variable


while inputName != '':
    inputName = input("Please enter a name: ") #Gets input from the user
    if inputName == "":#If the input is null, break the loop
        break
    inputName = inputName + "\n"#Adds this to the inputed name so that it will be seperated onto the next line in the file
    inputNames.append(inputName)#Adds the inputed names to the list

nameFile = open("people.txt", "w") #Opens the file
nameFile.writelines(inputNames) #Writes the list of names to the file
nameFile.close#Closes the file
