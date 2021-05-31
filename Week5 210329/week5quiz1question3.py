values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
i = 0
sum = 0
total = 0
maxNumber = 0
average = 0.0
while (i < len(values)):
    sum += values[i]
    if (values[i] > maxNumber): maxNumber = values[i]
    i += 1
total = sum
average = total / (len(values))
print("The average of all the numbers in the list is: " + str(round(average, 2)))
print("The highest number in the list is: " + str(maxNumber))
print("The sum of all the values in the list is: " + str(sum))
