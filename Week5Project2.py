a = float(input("Enter the length of the first side of (a) the triangle: "))
b = float(input("Enter the length of the second side (b) of the triangle: "))
c = float(input("Enter the length of the third side (c) of the triangle: "))

if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
    print("The triangle is a right triangle!")
else:
    print("The triangle IS NOT a right triangle!")
