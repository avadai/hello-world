import functools

# Asks the user for a file, opens it and reads it.
f = input("Enter a filename: ")
file = open(f, 'r')
file = file.read()

# The contents of the file are put into a list
file = file.split()

# Turns the contents of the list into integer values
file = list(map(int, file))

# The lambda function is used to find the average.
print(functools.reduce(lambda x, y: x+y / len(file), file, 0))