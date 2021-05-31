# Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019
fullDate = input("Please enter the date in format dd/mm/yyyy: ")
dateSplitter = fullDate.split("/")
# print(dateSplitter)

print("Date:", dateSplitter[0])
print("Month:", dateSplitter[1])
print("Year:", dateSplitter[2])