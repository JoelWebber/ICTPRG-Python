emailInput = input("Please input an email address: ")
numberInput = input("Please input a number: ")

number = int(numberInput)
num = 0
while num < number:
    output = (str(num+1) + "_" + emailInput)
    print (output)
    num += 1