import statistics

nums = [1, 3, 3, 3, 5, 5, 7, 9, 9]


def mean(x):
    return sum(x) / len(x)


def median(x):
    return statistics.median(x)


def mode(x):
    return statistics.mode(x)


def main():
    print("The mean is", mean(nums))
    print("The median is", median(nums))
    print("The mode is", mode(nums))


main()
