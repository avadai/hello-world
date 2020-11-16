def newton(x):
    tolerance = 0.000001
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
    return round(estimate)

print("The estimate of 25 is", newton(25))