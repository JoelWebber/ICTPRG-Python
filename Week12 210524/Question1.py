# Write the function between the START and END tags
# START


def AddTwoNumbers(num1, num2):
    sum = num1 + num2
    return sum


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))
print("Test 3 Passed: " + str(AddTwoNumbers(9, 0) != 10))