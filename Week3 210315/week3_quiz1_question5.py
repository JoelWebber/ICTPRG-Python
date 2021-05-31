userGrade = int(input("Please input your grade "))

if (userGrade < 50):
    print("Sorry, you have not passed")
elif (userGrade < 70):
    print("You will receive a Pass")
elif (userGrade < 80):
    print("You will receive a Credit")
elif (userGrade < 90):
    print("You will receive a Distriction")
elif (userGrade >= 90 and userGrade < 101):
    print("You will receive a High Distrinction")