def newton(x, estimate=1.0):
    if abs(x - estimate ** 2) <= 0.000001:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)


def main():
    while True:
        x = float(input("Enter a number to be squared, or press 'Enter' to quit: "))
        if x == " ":
            break
        print("The estimate of", x,  "is", round(newton(x, estimate=1.0)))


main()
