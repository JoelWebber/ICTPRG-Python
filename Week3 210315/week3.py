#if (y == 20):
#    x = 9
#
#if (y > 100):
#    x = 40
#else
#    x = 20


# num1 = int(input("Please enter score 1 out of 100: "))
# num2 = int(input("Please enter score 2 out of 100: "))
# num3 = int(input("Please enter score 3 out of 100: "))
# average = float((num1 + num2 + num3) / 3)

# if (average > 90):
#     {
#     print("Congratulations, your score is" + str(average))
#     }

# validPassword = str("Reka238")
# passwordAttempt = input(str("Please enter a password"))

# if (passwordAttempt == validPassword):
#     {
#     print("You're in")
#     }
# else:
#     {
#     print("Password is incorrect")
#     }


minimumWage = int(50000)
enteredWage = int(input("Please enter your salary "))
minimumTimeInJob = int(3)
enteredTimeInJob = int(input("Please tell us how long you have been working here for "))

if (minimumWage <= enteredWage):
    if (minimumTimeInJob <= enteredTimeInJob):
        print("You have been accepted for a loan")
    else:
        print("You are ineligible for a loan")
else:
        print("You are ineligible for a loan")
