#This program takes names from a file, gives them the corrcet capitalisation and adds them to a newly created file.
namesFile = open("names.txt", "r")
names = namesFile.readlines() #Files the file with the incorrect names in it
correctedNames = []

for i in range(len(names)):
    name = names[i].title() #Format the names correctly
    correctedNames.append(name) #Add the corrected names to the list


formattedNames = open("names-formatted.txt", "w") #creates "names-formatted.txt" file
formattedNames.writelines(correctedNames) #Adds the corrected names to the new file
formattedNames.close #closes the new file so no errors appear
