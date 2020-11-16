# The list used for the test
isSorted = [1, 4, 5, 8, 10]

# printing the list for the user to see
print("Here is the list of numbers: " + str(isSorted))

# This checks to see whether the list is sorted or not
Yes = 0
if isSorted == sorted(isSorted):
    Yes = 1

# If the list is sorted, it prints the top.
# However, if the list is not sorted, it prints the else statement.
if Yes:
    print("True. (The list is sorted)")
else:
    print("False. (the list is not sorted)")