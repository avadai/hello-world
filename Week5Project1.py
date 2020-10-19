a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the second side of the triangle: "))
c = float(input("Enter the length of the third side of the triangle: "))

equal = (a == b == c)

if equal:
    print("The triangle IS equilateral!")
else:
    print("The triangle IS NOT equilateral!") 