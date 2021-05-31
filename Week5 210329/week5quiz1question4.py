fullName = input("Please enter you full name: ")
splitFullName = fullName.split(" ")
print(splitFullName)
i = 0
initials = ""
while (i < len(splitFullName)):
    initials += splitFullName[i][0]
    i += 1
    

print(initials)
