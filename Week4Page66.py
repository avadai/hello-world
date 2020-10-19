Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = 2
>>> exponent = 3
>>> product = 1
>>> for eachPass in range(exponent):
	product = product * number
	print(product, end = " ")

	
2 4 8 
>>> product
8
>>> for count in range(4):
	print(count, end = " ")

	
0 1 2 3 
>>> product = 1
>>> for count in range(4):
	product = product * (count + 1)

	
>>> product
24
>>> 