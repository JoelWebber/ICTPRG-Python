# Write the function between the START and END tags
# START


def IsPalindrome(string):
    lowerString = string.lower()
    formattedString = lowerString.replace(" ", "")
    return formattedString == formattedString[::-1]


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))