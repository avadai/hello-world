import math

iterations = int(input("How many iterations would you like to calculate? "))

while iterations > 48:
    print("The number you entered is too large!")
    iterations = int(input("How many iterations would you like to calculate? "))
else:
    print('%.*f' % (iterations, math.pi))
