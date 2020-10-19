number = int(input("Enter the numeric grade: "))
if number > 100:
    print("Error: grade must be between 100 and 0")
elif number < 0:
    print("Error: grade must be between 100 and 0")
else:
    if number > 89:
        grade = 'A'
    elif number > 79:
        grade = 'B'
    elif number > 69:
        grade = 'C'
    elif number < 59:
        grade = 'F'
        print("Your grade is", grade)