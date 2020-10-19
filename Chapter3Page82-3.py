number = int(input("Enter the numeric grade: "))
if number >= 0 and number <= 100:
    print("The number you gave, squared, is", number**2)
else:
    print("Error: grade must be between 100 and 0")