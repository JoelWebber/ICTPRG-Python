#This program compares a users attempted login details to the login details listed in a file
print("Please log into your account by filling in the fields")
attemptedUsername = input("Please enter your username: ") #The users username attempt
attemptedPass = input("Please enter your password: ") #The users password attempt

attemptedLogin = (attemptedUsername + ":" + attemptedPass) #The combination of the users login attempts that would represent their login details, if correct

loginDetails = open("logins.txt", "r") #Opening the sotrage location of login details
lines = loginDetails.readlines() #Reads all of the lines in the file
for i in range(len(lines)): #For each set of login details, compare the users login attempt and see if it is correct. If it is, tell them "Access Granted", otherwise "Access Denied"

    if attemptedLogin == lines[i].rstrip("\n"):
        splitLogin = lines[i].split(":")
        print(attemptedUsername, ":", splitLogin[0], attemptedPass, ":", splitLogin[1], "Access Granted!") #Tells them they have been granted access and shows their login attempt compared to the real login details.
        break
    else:
        print("Access denied")
