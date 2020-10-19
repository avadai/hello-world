theSum = 0
ListSum = []
num = int(input("how many numbers are there? "))
for n in range(num):
    number = int(input("Enter a number or press 'Enter' to quit: "))
    theSum = theSum + number
    avg = theSum/num
print("The sum is: ", theSum)
print("The average of the numbers is: ", avg)