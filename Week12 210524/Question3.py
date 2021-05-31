# Write the function between the START and END tags
# START


def FibonacciAdder(number):
    count = 0
    fiboNum1 = 0
    fiboNum2 = 1
    fiboResult = 0
    while count < number:
        fiboResult = fiboNum1 + fiboNum2
        fiboNum1 = fiboNum2
        fiboNum2 = fiboResult
        count = count + 1
        fiboResult -= 1
    return fiboResult


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))