import math


def newton(x):
    tolerance = 0.000001
    estimate = 1.0

    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
    return round(estimate)


def main():
    while True:
        x = float(input("Enter a number to find it's square root, or press 'Enter' to quit: "))
        if x == " ":
            break
        print("The square root of", x, "is", newton(x))
        print("Python's estimate is ", math.sqrt(x))


main()