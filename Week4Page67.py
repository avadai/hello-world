Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> product = 1
>>> for count in range(1, 5):
	product = product * count

	
>>> product
24
>>> for count in range(1, 3 + 1):
	print(count * 3)

	
3
6
9
>>> lower = int(input("Enter the lower bount: "))
Enter the lower bount: 1
>>> upper = int(input("Enter the upper bound: "))
Enter the upper bound: 10
>>> theSum = 0
>>> for number in range(lower, upper + 1):
	theSum = theSum + number

	
>>> theSum
55
>>> 